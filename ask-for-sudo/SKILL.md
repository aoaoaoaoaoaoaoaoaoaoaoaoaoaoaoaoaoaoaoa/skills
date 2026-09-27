---
name: ask-for-sudo
description: Request and execute a privileged local command through a reason-bearing graphical sudo dialog on the local or SSH-forwarded display. Use whenever Codex needs sudo, root access, CAP_NET_ADMIN, a write outside user-owned paths, or another administrator-only operation on the owner's Linux workstation.
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

The façade routes the dialog through the caller's forwarded X display in an
SSH session. Shared-app-server calls recover a reachable SSH Codex client from
the host process table, preferring clients in the command's working directory.
Several sessions multiplexed through one SSH connection are equivalent. If
several distinct clients remain possible, the façade refuses to guess; pass a
verified display as `--prompt-display DISPLAY` before `--reason`.

Use one invocation for one coherent privileged operation. If shell syntax is
irreducible, pass an exact reviewed program to `/bin/bash -c`; do not conceal a
broad or unrelated operation behind a vague reason.

The password remains inside the graphical authentication path. Never request,
receive, store, print, or pipe it through chat or command input; cancellation
ends the privileged attempt. The prompt names the target host, reason, and exact
command. Elevate only the operation displayed to the user.
