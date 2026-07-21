# Linux And XDG

On Linux, a per-user application must honor the XDG base-directory contract. Treat configured paths as policy, not suggestions. XDG path variables are valid only when absolute; ignore relative values rather than interpreting them against an ambient working directory.

## Place By Meaning

Use an application-specific subdirectory beneath the appropriate root:

| meaning | root | default when unset |
|---|---|---|
| durable application data | `$XDG_DATA_HOME` | `$HOME/.local/share` |
| user-edited configuration | `$XDG_CONFIG_HOME` | `$HOME/.config` |
| durable, machine-local state | `$XDG_STATE_HOME` | `$HOME/.local/state` |
| disposable, rebuildable cache | `$XDG_CACHE_HOME` | `$HOME/.cache` |
| login-session runtime objects | `$XDG_RUNTIME_DIR` | no default |

State includes material worth retaining across restarts but not treating as portable user data or configuration, such as history, logs, recent-use state, window layout, or undo journals. Cache must remain safely disposable. Do not make correctness, ownership, or irreplaceable work depend on it.

Read system data and configuration through `$XDG_DATA_DIRS` and `$XDG_CONFIG_DIRS`, respecting their order and the precedence of the user layer. Their defaults are `/usr/local/share:/usr/share` and `/etc/xdg`. Do not write into search-path entries merely because they were consulted. User-specific executables belong in `$HOME/.local/bin` when the application is responsible for placing them there.

`$XDG_RUNTIME_DIR` is for sockets, pipes, locks, credentials, and other small runtime objects whose lifetime is the login session. Its contents are local, private to the user, and unfit for durable state or bulk storage. If it is absent, either disable the dependent facility or use a private replacement with equivalent ownership, permissions, locality, and lifecycle while warning about the degraded contract; a casual shared `/tmp` path is not equivalent.

Do not spray dotfiles or application directories directly into `$HOME`, write durable state into the current working directory, or use `/tmp` as persistence. Compatibility with an established legacy location may justify reading or migrating it; it does not make continued proliferation lawful.

## Respect User Space

User-facing directories such as Documents, Downloads, Pictures, and Videos are configured, localized product surfaces. Resolve them through `xdg-user-dir` or a faithful platform library; never infer them from English names or capitalization. Put only material the user intentionally creates, exports, or selects there. Internal databases, thumbnails, logs, models, and indexes remain application internals even when they contain valuable information.

Create only the directories actually needed, with private permissions where their contents are private. Use atomic replacement and suitable synchronization for durable writes. Bound and version caches, remove obsolete generations, and clean runtime artifacts on normal exit while remaining robust to the session manager deleting them first.

Installation, updates, and removal must respect the ownership boundary between package manager, system administrator, application, and user. A per-user program must not mutate system-wide locations; a system service must use the platform's system configuration, state, cache, log, and runtime facilities rather than pretending to be a desktop user. Uninstall removes installed machinery. User-owned data survives unless an explicit purge operation names and confines its destruction.

Verify the lifecycle under non-default XDG paths, absent optional directories, restrictive permissions, concurrent instances, interrupted writes, upgrades, and removal. A program is not XDG-compliant merely because its happy-path cache happens to land under `~/.cache`.

## Authorities

- [XDG Base Directory Specification 0.8](https://specifications.freedesktop.org/basedir/0.8/)
- [`xdg-user-dir(1)`](https://man.archlinux.org/man/xdg-user-dir.1.en)
