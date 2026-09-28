---
name: product-doctrine
description: Apply the house doctrine for software as a product running on a user's system. Use when designing, implementing, or reviewing persistence, configuration, filesystem placement, installation, updates, removal, background work, networking, permissions, resource use, desktop integration, or release behavior. Load the Linux/XDG projection when that platform is relevant.
---

# Product Doctrine

Read [references/universal.md](references/universal.md) whenever product behavior is in scope. For Linux user applications, services, packaging, or filesystem behavior, also read [references/linux-xdg.md](references/linux-xdg.md).

The doctrine is normative unless an explicit product contract or a more local instruction overrides it. Apply it to architecture, implementation, review, and verification; do not reduce it to a ceremonial release checklist.

Product unit tests follow `$unit-test-doctrine`; a product obligation does not mandate one unit test per obligation or change.

This doctrine governs the software's outward conduct. Pair it with `$style-doctrine` when the code's inward construction is also in scope.
