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

A **claim** is the live exclusive kernel lock owned through the `cpu-claim` MCP.
The lock, not its metadata file, is authoritative. Process exit releases it,
including crashes and `SIGKILL`.

## Bulk Work

Compilation, linking, code generation, compression, ordinary test suites, and
other sustained throughput work run at reduced scheduler priority. Prefer
higher-numbered CPUs for such work where a maintained launcher supplies that
preference.

While the priority lanes are free, this preference is not an exclusion. Do not
pin compilation to a narrow CPU set, impose a small job cap, or leave priority
CPUs idle merely because a future experiment may need them.

While a live claim exists, bulk work must exclude every priority-lane CPU and
run only on the remainder. Source the machine manifest and bind the complete
process tree, including helpers. A missing or malformed manifest is a stop
condition only when the claim requires exclusion.

An increased nice value and low cgroup CPU weight are work-conserving: bulk
work may fill otherwise idle CPUs but yields them under contention. Do not add
a permanent CPU quota merely to avoid a 100% utilization reading; a quota
necessarily idles runnable capacity. Thermal or power ceilings require a
separate explicit product contract.

Brief interactive and administrative commands are not bulk work and need no
placement ceremony.

## Claims

Claim the priority lanes only for work whose protocol requires them. State the
purpose, inspect an existing claim rather than overriding it, and release the
claim when the protected work ends. Claiming coordinates ownership only; the
experiment protocol remains responsible for topology, quiescence, controls,
and interpretation.

The MCP, command-line probe, and maintained launchers must consult the same
kernel-lock backing store. Do not mirror claim state into environment variables,
PID files, timestamps, daemons, or a second registry.

## Maintain The Law

When topology changes, update this doctrine and the machine manifest together,
then audit maintained launchers for stale masks or unconditional throttles.
Run `scripts/audit-agent-instructions` after changing agent instructions.
