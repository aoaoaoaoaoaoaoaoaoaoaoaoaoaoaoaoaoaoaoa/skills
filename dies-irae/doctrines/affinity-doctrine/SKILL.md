---
name: affinity-doctrine
description: Apply the machine-wide CPU placement and shared Slurm pool law when launching sustained work, submitting experiments, provisioning the machine, or editing CPU/resource controls and launchers.
---

# Affinity Doctrine

This is the sole CPU-placement authority. `~/.config/affinity-lanes` is its
executable machine projection; no other file may encode its CPU sets or the
pool size.

## Territory

The projection partitions every CPU into three sets of whole physical cores;
SMT siblings never straddle sets.

- **Priority lanes** (`PRIORITY_CPUSET`): the Slurm benchmark pool.
- **Desktop reserve** (`DESKTOP_CPUSET`): interactive headroom; bulk work never
  runs here.
- **Bulk lanes** (`BULK_CPUSET`): the only CPUs bulk work may use.

Desktop, user-session, VM and container processes may use the desktop reserve
and the bulk lanes, never the priority lanes, even when the queue is empty.

Slurm is the sole allocation authority for the priority lanes. No PID file,
manual lease, second queue, or claim scope represents ownership; `cpu-claim` is
retired. Inspect native Slurm jobs and their live cgroups; the persistent
`slurmstepd.scope` alone does not imply a running job.

## Machine Requirements

- **Projection** `~/.config/affinity-lanes`: shell-sourceable `KEY=VALUE` lines
  `PRIORITY_CPUSET`, `DESKTOP_CPUSET`, `BULK_CPUSET`,
  `PRIORITY_CORE_MEMORY_MIB` (per pool core: an 8 GiB worker plus a 256 MiB
  custodian share), `BULK_NICE`, `BULK_CPU_WEIGHT`, `CPU_SCHEDULER=slurm`.
- **Slurm**: `munge`, `slurmctld` and `slurmd` enabled for one local node and
  one `benchmark` partition; `select/cons_tres` with `CR_Core_Memory`;
  `task/cgroup,task/affinity` on `cgroup/v2` constraining cores, RAM (100%) and
  swap (0) under `CgroupSlice=benchmark.slice`; `JobRequeue=0`. The node's
  `CpuSpecList` names the Slurm abstract CPUs (hwloc logical PU indexes) outside
  the priority lanes, `RealMemory` equals the pool slice, and `MemSpecLimit`
  reserves the daemons' share of it.
- **Admission** (`job_submit.lua`): UID 1000 only; one to pool-size workers, each
  one physical core with one executing sibling; job memory by `--mem`, at most
  pool cores × `PRIORITY_CORE_MEMORY_MIB`; no exclusivity, spare cores, core
  specialization, requeue or running reprioritization; finite time up to 24 h.
- **Containment** (required SPANK plugin): per-job PID cap; single-CPU cpuset and
  one-CPU quota per worker task; `oom_score_adj` -900 for every task.
- **systemd**: `benchmark.slice` hosts `slurmd` with `AllowedCPUs` = the priority
  lanes, `MemoryMin` = `MemoryMax` = `RealMemory`, `MemorySwapMax=0`; the `user`,
  `machine` and `capsule` slices are confined to the desktop reserve plus bulk
  lanes, bulk-only services such as `xmrig` to the bulk lanes, and `system.slice`
  stays off the priority lanes.
- **Wrappers**: `~/.local/libexec/cpu-lanes` binds a process tree to
  `BULK_CPUSET` at `BULK_NICE` and `BULK_CPU_WEIGHT` in a user scope; the PATH
  `cargo` wrapper enters it; `cpu-queue` submits and contains experiments.

`/home/main/programming/projects/mcps/cpu_claim` installs all of this: its
`assets/affinity-lanes` is the projection's source, and `scripts/install-slurm.sh`
followed by `scripts/reserve-slurm.sh` render and apply every other mask and
budget from it.

## Experiments

Submit ready commands through `cpu-queue` or native Slurm. Request one physical
core per actual concurrent worker (`--ntasks`, one CPU per task), at most the
whole pool; both siblings are reserved against other jobs. The default worker
uses one sibling. A paired block receives one finite gang allocation and keeps
its scientific barriers.

No job may reserve unused neighboring cores, request LLC isolation, demand
whole-pool exclusivity, or silence the desktop. Dedicated cores do not isolate
DRAM, IO, package power or kernel activity; record concurrent work and apply
the experiment's validity checks without commandeering others' resources.

Reorder pending jobs only. Dispatch priority is not Linux nice/CPUWeight.
Do not suspend, migrate, throttle or restart a valid burn for queue convenience.
No implicit statistical replay: interrupted/uncertain attempts remain failed
or unknown. An explicit new submission creates a new attempt identity.

Memory, no-swap, PID and finite outer-time limits cover the complete job
subtree. Queue wait is not solver time. Startup, finalization/checking and
teardown retain the allocation and belong in its outer time budget.

## Bulk Work

Builds, linking, code generation, compression and ordinary test suites run on
the bulk lanes at reduced scheduling priority, never on the desktop reserve.
Low nice priority and cgroup CPU weight are work-conserving; do not add a CPU
quota or arbitrary small parallelism cap merely to lower utilization.

Invoke maintained launchers directly. `command -v cargo` must resolve to
`~/bin/cargo`, never `~/.cargo/bin/cargo` or a rustup toolchain path. The wrapper
derives repository-specific disk-backed target custody before entering the
bulk scope; rustc, build scripts, nextest and test binaries inherit it. Do not
override its target selection for ordinary work, or add an outer `taskset`,
`nice` or `systemd-run`.

`~/.local/libexec/cpu-lanes` is the stable internal launcher when no maintained
wrapper exists. A missing or malformed machine manifest is a stop condition.
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
reruns the installer as a drained handover: close admission, let running jobs
finish, and never leave two allocators active. Verify actual effective cgroup
masks and SMT sibling separation, not only requested settings. Run
`scripts/audit-agent-instructions` after modifying agent instructions.
