---
name: affinity-doctrine
description: Apply the machine-wide CPU placement and shared Slurm pool law when launching sustained work, submitting experiments, provisioning the machine, or editing CPU/resource controls and launchers.
---

# Affinity Doctrine

This is the sole CPU-placement authority. `assets/affinity-lanes` in the
installer repository owns its machine projection, installed at
`~/.config/affinity-lanes` for clients and `/etc/slurm-llnl/affinity-lanes` for
root hooks. No independent file may encode its CPU sets or pool size.

## Territory

The projection partitions every CPU into two sets of whole physical cores:
`HOST_FLOOR_CPUSET`, which Slurm cannot allocate, and `SLURM_ELIGIBLE_CPUSET`.
SMT siblings never straddle sets. Ordinary work, including desktop and bulk,
may use all CPUs except the SMT-complete union of fenced job allocations.
There is no separate hard bulk/desktop partition.

Slurm alone allocates benchmark cores. A required root post-fork hook waits
for `cpu-fence` to exclude an allocation from ordinary systemd slices before
Slurm releases its native exec barrier. The allocation stays fenced between
steps; Epilog releases it only after payload teardown. The root handover
ledger is not an allocator. Recovery consults native jobs and live cgroups;
the persistent `slurmstepd.scope` alone does not imply a running job.

`cpu-queue limit N --for 8h` temporarily caps benchmark capacity using native
core reservations. Existing jobs drain by default. The operator may explicitly
choose `--immediate` to cancel entire overlapping jobs without replay.
`cpu-queue limit clear` restores normal capacity early. Do not impose a manual
limit or cancel another project's jobs merely to expedite your own work.

## Machine Requirements

- **Projection** `~/.config/affinity-lanes`: shell-sourceable `KEY=VALUE` lines
  `HOST_FLOOR_CPUSET`, `SLURM_ELIGIBLE_CPUSET`, `BENCHMARK_MEMORY_MIB`,
  `BULK_NICE`, `CPU_SCHEDULER=slurm`. CPU capacity and memory admission are
  independent; more eligible cores do not imply more available RAM.
- **Slurm**: `munge`, `slurmctld` and `slurmd` enabled for one local node;
  `select/cons_tres` with `CR_Core_Memory` for `benchmark` and
  `CR_Socket_Memory` for `timing`. `l3cache_as_socket` exposes cache domains
  as native sockets; timing requires a complete socket and one task per socket.
  `task/cgroup,task/affinity` on `cgroup/v2` constraining cores, RAM (100%) and
  swap (0) under `CgroupSlice=benchmark.slice`; `JobRequeue=0`. The node's
  `CpuSpecList` names the Slurm abstract CPUs (hwloc logical PU indexes) outside
  the eligible pool, `RealMemory` equals the pool slice, and `MemSpecLimit`
  reserves the daemons' share of it.
- **Admission** (`job_submit.lua`): UID 1000 only; benchmark reserves one physical
  core per worker, timing one complete eligible L3 per worker; one executing
  sibling per worker. Worker capacity follows the partition's granularity.
  Job memory by `--mem`, at most `BENCHMARK_MEMORY_MIB`; no whole-node
  exclusivity, spare cores outside timing's cache reservation, core
  specialization, requeue or running reprioritization; finite time up to 24 h.
  Job arrays are admitted, each task bounded like a job.
- **Containment** (required SPANK plugin): per-job PID cap; single-CPU cpuset and
  one-CPU quota per native worker task; batch supervisors coordinate work and
  are exempt from those per-worker CPU limits; `oom_score_adj` -900 for every task.
- **systemd**: `benchmark.slice` hosts Slurm job cgroups on the eligible pool,
  with `MemoryMin` = `MemoryMax` = `RealMemory`, `MemorySwapMax=0`. Slurm's
  management daemons stay on the host floor. Ordinary top-level slices boot
  on the floor and receive dynamic masks from `cpu-fence`. New top-level
  workload slices must participate in this boundary. IRQs and kernel threads
  are not isolated. A minute timer repairs stale handovers conservatively.
- **Wrappers**: `~/.local/libexec/cpu-lanes` places a process tree at
  `BULK_NICE` beneath the system manager's top-level `bulk.slice`, with
  `CPUWeight=idle`. It competes with ordinary system and user slices at their
  common root, not inside the user manager. A socket-activated root helper
  places the connecting launcher in the scope using its peer pidfd; it never
  executes the payload. The launcher execs in place, preserving its identity,
  sandbox and inherited descriptors. The slice follows the dynamic ordinary-work
  fence; PATH Cargo and standalone Rust build-tool wrappers enter it. Rust-analyzer is
  intentionally exempt for interactive MCP/editor analysis. `cpu-queue`
  submits and contains experiments.

`/home/main/programming/projects/mcps/cpu_claim` installs all of this: its
`assets/affinity-lanes` is the projection's source, and `scripts/install-slurm.sh`
followed by acceptance and `scripts/reserve-slurm.sh` render, verify and apply
every other mask and budget from it. Drain running jobs before a policy cutover.

## Experiments

Submit ready commands through `cpu-queue` or native Slurm. In the default
`benchmark` partition, request one physical core per actual concurrent worker
(`--ntasks`, one CPU per task), at most the whole pool; both siblings are reserved
against other jobs. The default worker
uses one sibling. A paired block keeps its arms simultaneous, either as one
finite gang allocation or as one short array task per paired unit, such as a
case holding one core per arm replica. Never throttle an array: the scheduler
fills whatever pool exists, and a drain interrupts only the tasks in flight.

Cache-sensitive work may opt into `--partition timing` through `cpu-queue` or
native Slurm. It reserves one entire eligible L3 per actual worker, including
idle neighboring cores; domains sharing the host floor are unavailable. Native
Slurm chooses placement and arbitrates both partitions. Launch measured workers
from the batch supervisor with `srun --exact --ntasks="$SLURM_NTASKS"
--cpus-per-task=1 --cpu-bind=threads`; do not choose CPU/cache IDs or use the
core-pinned `cpu-queue step` API in timing mode. `CPU_QUEUE_RESERVED_CPUS` and
launch receipts describe reserved capacity, not executing-worker count.

Outside timing's native cache reservation, jobs may not reserve unused neighbors,
demand whole-pool exclusivity or silence the desktop. Neither mode isolates
DRAM, IO, package power or kernel activity; record concurrent work and apply
the experiment's validity checks without commandeering others' resources.

Reorder pending jobs only. Dispatch priority is not Linux nice/CPUWeight.
Do not suspend, migrate, throttle or restart a valid burn for queue convenience.
Only explicit operator authorization permits immediate-cap cancellation.
No implicit statistical replay: interrupted/uncertain attempts remain failed
or unknown. An explicit new submission creates a new attempt identity.

Memory, no-swap, PID and finite outer-time limits cover the complete job
subtree. Queue wait is not solver time. Startup, finalization/checking and
teardown retain the allocation and belong in its outer time budget.

## Bulk Work

Builds, linking, code generation, compression and ordinary test suites run in
the idle-priority bulk slice. They may share the host floor and borrow any
unallocated benchmark core, but never overlap a fenced allocation. Idle CPU
scheduling is work-conserving; do not add a CPU quota or arbitrary small
parallelism cap merely to lower utilization. Idle priority does not isolate
SMT, cache, memory bandwidth or IO.

Invoke maintained launchers directly. `command -v cargo` must resolve to
`~/bin/cargo`, never `~/.cargo/bin/cargo` or a rustup toolchain path. The wrapper
derives repository-specific disk-backed target custody before entering the
bulk scope; rustc, build scripts, nextest and test binaries inherit it. Do not
override its target selection for ordinary work, or add an outer `taskset`,
`nice` or `systemd-run`.

`~/.local/libexec/cpu-lanes` is the stable internal launcher when no maintained
wrapper exists. A missing or malformed machine manifest is a stop condition.
Missing launchers or unavailable system containment are also stop conditions;
never fall back to unconfined execution. Socket placement preserves
no-new-privileges and needs no sudo. Managed profiles permitting Unix-socket
connections require no placement-only escalation. If a profile blocks
`connect` to `/run/cpu-lanes.sock`, use reviewed execution escalation or request
explicit policy support; do not route around the denial. Nested launches reuse
containment only after checking effective cgroup limits, not an environment
flag. Set resource overrides before the outermost bulk launch.
Brief administration needs no extra placement ceremony; the systemd parent
already bounds user work.

### Memory

Each wrapped command has a 32 GiB cgroup memory ceiling. A cgroup OOM kill can
trigger scope teardown and SIGTERM the remaining processes; check the scope's
`memory.events` and journal before attributing unexplained termination.

Reduce test concurrency when aggregate memory exceeds the ceiling, not merely
to lower CPU utilization. Only when a single workload genuinely needs more,
set `BULK_MEMORY_MAX_BYTES` for that command (for example, `BULK_MEMORY_MAX_BYTES=$((48<<30)) cargo nextest run`).
Never bypass the wrapper or raise the global limit to conceal fixture leaks.

## Maintenance

Keep topology, the projection, Slurm configuration, systemd boundaries and
maintained launchers coherent. A pool change edits the projection's source and
reruns the installer as a drained handover: set both partitions DOWN to pause
dispatch while still accepting submissions, let running jobs
finish, and never leave two allocators active. Verify actual effective cgroup
masks and SMT sibling separation, not only requested settings. Run
`~/.codex/skills/affinity-doctrine/scripts/audit-agent-instructions` after
modifying agent instructions. The auditor belongs to this skill, not the
`cpu_claim` installer repository.
