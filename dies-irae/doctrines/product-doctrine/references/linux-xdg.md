# Linux and XDG

On Linux, a per-user application honors the XDG base-directory contract. Configured paths are policy, not suggestions. An XDG path variable is valid only when absolute; ignore a relative value instead of resolving it against the working directory.

## Place by meaning

Use an application-specific subdirectory beneath the appropriate root:

| meaning | root | default when unset |
|---|---|---|
| durable application data | `$XDG_DATA_HOME` | `$HOME/.local/share` |
| user-edited configuration | `$XDG_CONFIG_HOME` | `$HOME/.config` |
| durable, machine-local state | `$XDG_STATE_HOME` | `$HOME/.local/state` |
| disposable, rebuildable cache | `$XDG_CACHE_HOME` | `$HOME/.cache` |
| login-session runtime objects | `$XDG_RUNTIME_DIR` | no default |

State is material worth keeping across restarts but not portable user data or configuration, such as history, logs, recent-use state, window layout, or undo journals. Cache stays safely disposable: correctness, ownership, and irreplaceable work never depend on it.

Read system data and configuration through `$XDG_DATA_DIRS` and `$XDG_CONFIG_DIRS`, respecting their order and the precedence of the user layer. Their defaults are `/usr/local/share:/usr/share` and `/etc/xdg`. Consulting a search-path entry does not license writing to it. User-specific executables belong in `$HOME/.local/bin` when the application is responsible for placing them.

`$XDG_RUNTIME_DIR` holds sockets, pipes, locks, credentials, and other small objects whose lifetime is the login session. Its contents are local, private to the user, and unfit for durable state or bulk storage. If it is absent, disable the dependent facility, or use a private replacement with the same ownership, permissions, locality, and lifecycle and warn about the degraded contract; a casual shared `/tmp` path is not equivalent. Session-lifetime scratch sits beneath one private root whose outer boundary the session manager owns; ownership inside it follows the universal doctrine.

Do not scatter dotfiles or application directories directly into `$HOME`, write durable state into the working directory, or use `/tmp` for persistence. Compatibility with an established legacy location may justify reading or migrating it; it does not justify creating more.

## Respect user space

User-facing directories such as Documents, Downloads, Pictures, and Videos are configured, localized product surfaces. Resolve them through `xdg-user-dir` or a faithful platform library; never infer them from English names or capitalization. Put there only material the user intentionally creates, exports, or selects. Internal databases, thumbnails, logs, models, and indexes remain application internals even when they hold valuable information.

Create only the directories actually needed, with private permissions where their contents are private. Use atomic replacement and suitable synchronization for durable writes. Bound and version caches, remove obsolete generations, and clean up runtime artifacts on normal exit while staying robust to the session manager deleting them first.

Installation, updates, and removal respect the ownership boundaries between package manager, system administrator, application, and user. A per-user program never mutates system-wide locations; a system service uses the platform's system configuration, state, cache, log, and runtime facilities instead of acting as a desktop user. Uninstall removes installed machinery. User-owned data survives unless an explicit purge operation names and confines its destruction.

Verify the lifecycle under non-default XDG paths, absent optional directories, restrictive permissions, concurrent instances, interrupted writes, upgrades, and removal. A program is not XDG-compliant merely because its happy-path cache happens to land under `~/.cache`.

## Authorities

- [XDG Base Directory Specification 0.8](https://specifications.freedesktop.org/basedir/0.8/)
- [`xdg-user-dir(1)`](https://man.archlinux.org/man/xdg-user-dir.1.en)
