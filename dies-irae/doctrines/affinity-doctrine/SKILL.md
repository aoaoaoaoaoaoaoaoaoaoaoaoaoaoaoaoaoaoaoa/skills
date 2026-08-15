---
name: affinity-doctrine
description: Apply the machine-wide CPU placement law when launching sustained low-priority work, claiming experimental CPUs, or editing build launchers, systemd CPU controls, affinity configuration, benchmarks, profilers, or other CPU-intensive tooling.
---

# Affinity Doctrine

This is the sole normative source for CPU placement on the owner's workstation.
`~/.config/affinity-lanes` is the executable machine projection. Repositories
may require this doctrine but must not duplicate its CPU sets.

## Two Zones

The **priority lanes** are the physical-core territory reserved on demand for
experiments. The **remainder** is every other logical CPU. The machine manifest
defines both sets; experiment protocols may select subsets of the priority
lanes but do not redefine them.

A **claim** is the live `cpu-priority-claim.scope` cgroup. Its existence is
bound to its process tree: the claim ends when the last process exits, including
after launcher crashes or `SIGKILL`. No manual lease exists.

## Bulk Work

Compilation, linking, code generation, compression, ordinary test suites, and
other sustained throughput work run at reduced scheduler priority. Prefer
higher-numbered CPUs for such work where a maintained launcher supplies that
preference.

While the priority lanes are free, this preference is not an exclusion. Do not
pin compilation to a narrow CPU set, impose a small job cap, or leave priority
CPUs idle merely because a future experiment may need them.

Bulk work launched while a live claim exists must exclude every priority-lane
CPU and run only on the remainder. Source the machine manifest and bind the
complete process tree, including helpers. A missing or malformed manifest is a
stop condition only when the claim requires exclusion.

An increased nice value and low cgroup CPU weight are work-conserving: bulk
work may fill otherwise idle CPUs but yields them under contention. Do not add
a permanent CPU quota merely to avoid a 100% utilization reading; a quota
necessarily idles runnable capacity. Thermal or power ceilings require a
separate explicit product contract.

Brief interactive and administrative commands are not bulk work and need no
placement ceremony.

## Claims

Run work whose protocol requires the priority lanes through `cpu-claim run` and
state its purpose. The command waits without polling, starts the fixed scope,
and applies the manifest's priority CPU set through inherited scheduler
affinity and the scope's cgroup controls where delegated. Its complete live
cgroup is the claim; there is no separate release operation. Claiming
coordinates ownership only. The experiment protocol remains responsible for
topology, quiescence, controls, and interpretation.

`cpu.wait` is an advisory sleep, not a reservation. Use one wait rather than
polling, but prefer `cpu-claim run` when work should begin after acquisition so
the wait and claim remain atomic.

The MCP, command-line probe, and maintained launchers must consult the same
systemd scope. Do not mirror claim state into environment variables, PID files,
timestamps, daemons, manual locks, or a second registry. A short-lived kernel
mutex may serialize scope creation but never represents the claim.

On systemd hosts, delegate the `cpuset` controller to the user manager so
`AllowedCPUs` becomes cgroup-wide containment; verify the live scope's
`EffectiveCPUs` against the manifest. Inherited scheduler affinity remains the
portable enforcement and defense in depth.

## Maintain The Law

When topology changes, update this doctrine and the machine manifest together,
then audit maintained launchers for stale masks or unconditional throttles.
Run `scripts/audit-agent-instructions` after changing agent instructions.
