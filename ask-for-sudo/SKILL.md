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

The reason states the concrete purpose, the scope, and whether the command reads
or changes state. Pass the executable and every argument after `--`, preferring
an absolute executable path.

Run the façade with the execution tool's escalated sandbox permission. The
global prefix rule allows that elevation without a second Codex approval; a
default sandbox sets `NoNewPrivs`, which prevents `sudo` from working.

In an SSH session, the façade shows the dialog on the caller's forwarded X
display. When called from a shared app server, it finds a reachable SSH Codex
client in the host's process table, preferring clients in the command's working
directory; sessions multiplexed through one SSH connection count as one client.
If several distinct clients remain, the façade refuses to guess: pass a verified
display as `--prompt-display DISPLAY` before `--reason`.

Use one invocation for one coherent privileged operation. When the operation
needs shell syntax, pass an exact reviewed program to `/bin/bash -c`; never
conceal a broad or unrelated operation behind a vague reason.

The dialog shows the target host, the reason, and the exact command before it
accepts the password; elevate only the operation it shows. The password stays
inside the graphical authentication path: never request, receive, store, print,
or pipe it through chat or command input. Cancellation ends the privileged
attempt.
