---
name: affinity-doctrine
description: Apply the machine-wide physical-core placement law when launching sustained work, submitting experiments, or editing CPU/resource controls and launchers.
---

# Affinity Doctrine

This is the sole CPU-placement authority. `~/.config/affinity-lanes` is its
executable machine projection; repositories must not copy its CPU masks.

## Permanent Territory

The **priority lanes** are six physical cores permanently reserved for
experiments, including both SMT siblings. The **remainder** contains all other
logical CPUs. Ordinary user/desktop/bulk work stays on the remainder even when
the experiment queue is empty or its controller is unavailable.

Slurm is the sole allocation authority. Systemd owns the outer benchmark
slice and delegates its job subtree to Slurm. No PID file, manual lease,
second queue, or `cpu-priority-claim.scope` represents ownership. `cpu-claim`
is retired. Inspect native Slurm jobs and their live cgroups; the persistent
Slurm scope alone does not imply a running job.

## Experiments

Submit ready commands through `cpu-queue` or native Slurm. Request one physical
core per actual concurrent worker (`--ntasks`, one CPU per task); reserve both
siblings against other jobs. The default worker uses one sibling. A paired
block receives one finite gang allocation and keeps its scientific barriers.

No job may reserve unused neighboring cores, request LLC isolation, demand
whole-pool exclusivity, or silence the desktop. A six-worker job can allocate
six cores; a one-worker job allocates one. Dedicated cores do not isolate
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
the remainder at reduced scheduling priority. Low nice priority and cgroup
CPU weight are work-conserving; do not add a CPU quota or arbitrary small
parallelism cap merely to lower utilization.

Invoke maintained launchers directly. In particular use the normal PATH
`cargo` wrapper: it derives repository-specific target custody before entering
the bulk scope. Do not place `systemd-run` outside Cargo or bypass its wrapper.

`~/.local/libexec/cpu-lanes` is the stable internal launcher when no maintained
wrapper exists. It binds the complete process tree to the remainder. A missing
or malformed machine manifest is a stop condition. Brief administration needs
no extra placement ceremony; the systemd parent already bounds user work.

## Maintenance

Keep topology, the machine projection, Slurm configuration, systemd boundaries
and maintained launchers coherent. Verify actual effective cgroup masks and
SMT sibling separation, not only requested settings. Changes require a drained
handover; never leave two allocators active. Run `scripts/audit-agent-instructions`
after modifying agent instructions.
