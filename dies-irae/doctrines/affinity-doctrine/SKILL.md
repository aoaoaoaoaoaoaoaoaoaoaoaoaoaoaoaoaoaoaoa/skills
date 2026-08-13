---
name: affinity-doctrine
description: Apply the machine-wide CPU-affinity law whenever launching or configuring compilation, linking, builds, code generation, compression, ordinary test suites, benchmarks, profilers, or other sustained CPU work. Use it when editing launchers, build scripts, systemd CPU controls, thread-pool limits, or repository instructions that mention CPUs, cores, SMT, taskset, affinity, timing, or performance isolation.
---

# Affinity Doctrine

This is the sole normative source for CPU placement on the owner's workstation.
Repository instructions may require its use but must not restate masks, lane
semantics, or exceptions. The machine manifest
`~/.config/affinity-lanes` is the sole executable projection of its lane
values; it is configuration, not an independent policy.

## Names

- A **physical core** owns execution resources, L1, and L2.
- A **logical CPU** is one scheduler-visible SMT thread.
- An **SMT sibling** is the other logical CPU on the same physical core. “HT
  core” is imprecise: an SMT sibling is not another core.
- The **Sanctum** is the physical-core and cache territory reserved for timing.
- The **Favela** is the low-priority logical-CPU lane for throughput work.
- **Quiescence** is the absence of competing work required for authoritative
  timing.

The current host is a one-socket, one-NUMA-node Ryzen 9 3900XT with 12 physical
cores, 24 logical CPUs, two logical CPUs per core, and four three-core L3
domains. The machine manifest owns the exact logical-CPU sets. The Favela uses
only sibling threads of physical cores outside the Sanctum and shares no L3
domain with it.

## Classify Work

Treat work as a **build** when it compiles, links, generates code or assets,
compresses packages, builds documentation, or runs an ordinary test suite. If
the classification is ambiguous and the work can sustain CPU load, it is a
build. Package-manager helpers and child processes inherit the same class.

Treat work as a **measurement** only when its result is timing, throughput,
latency, profiling, or hardware-counter evidence. Compiling the measured binary
is still a build. Functional tests are builds, not measurements.

Interactive applications and brief administrative commands are neither. Do not
pin trivial work merely to exhibit compliance.

## Place Builds

Source `~/.config/affinity-lanes`, then bind the complete build process tree to
`$COMPILER_CPUSET` at `$COMPILER_NICE`. Cap every known job and thread pool at
`$COMPILER_JOBS`; affinity limits execution capacity, while explicit pool caps
prevent runnable-task and memory explosions. This includes Make, Ninja, Cargo,
Rayon, test runners, OpenMP, BLAS, linkers, compressors, and helpers.

Use the maintained launchers when one exists. Do not invoke a real compiler by
absolute path, clear containment variables, widen affinity, or create a local
fallback mask. A missing, malformed, or topologically stale machine manifest is
a stop condition.

Favela placement is a throughput bargain, not isolation. Its threads share
physical cores with interactive primary threads and may slow them. Low
priority is intentional; a build may putter rather than commandeer the host.

## Measure

Run timing work only on the Sanctum CPUs selected by the owning benchmark
harness. Never schedule work on their SMT siblings. Preserve the harness's
cache-domain rules; for Libgrid, its frozen wave topology and benchmark
documentation remain authoritative within the Sanctum.

Exploratory timings may coexist with Favela work only when marked contaminated
and used to reject bad ideas, never to accept a result. Authoritative timing
requires Quiescence: finish compilation first and suspend builds, tests,
compression, profiling, and other material host load for the complete control
and treatment interval. CPU affinity does not remove package-power, thermal,
memory-controller, storage, kernel, or interrupt interference.

## Maintain The Law

Do not duplicate this policy in `AGENTS.md`, repository documentation, wrapper
comments, or service units. A local surface may state a workload-specific job
count or benchmark topology only when it is a genuine local experimental
contract, not a paraphrase of this doctrine.

When hardware topology or intended lanes change, update this doctrine and the
machine manifest together, then audit all owned `AGENTS.md` files and executable
launchers for stale masks, affinity commands, bypasses, and fallback defaults.
Do not change one projection and leave the others semantically split.

Run `scripts/audit-agent-instructions` after changing agent instructions. It
fails if the global dispatcher is absent or affinity law reappears in a local
`AGENTS.md`.
