---
name: ask-for-sudo
description: Request and execute a privileged local command through a reason-bearing graphical sudo dialog. Use whenever Codex needs sudo, root access, CAP_NET_ADMIN, a write outside user-owned paths, or another administrator-only operation on the owner's graphical Linux workstation.
---

# Ask For Sudo

Use the stable façade:

```sh
/home/main/.local/bin/codex-sudo \
    --reason 'Read the live WireGuard peer state to diagnose pwg; no state will change.' \
    -- /usr/bin/wg show pwg
```

State the concrete purpose, scope, and whether the command reads or mutates state.
Pass the executable and every argument after `--`; prefer an absolute executable
path. The dialog displays both the reason and the exact command before accepting
the password.

Run the façade with the execution tool's escalated sandbox permission. The
global prefix rule allows that elevation without a second Codex approval; a
default sandbox sets `NoNewPrivs` and necessarily prevents `sudo` from working.

Use one invocation for one coherent privileged operation. If shell syntax is
irreducible, pass an exact reviewed program to `/bin/bash -c`; do not conceal a
broad or unrelated operation behind a vague reason.

Never request the password in chat, pass it with `sudo -S`, invoke the bundled
askpass helper directly, store it, or print it. Cancellation is refusal: stop or
choose an unprivileged path.
