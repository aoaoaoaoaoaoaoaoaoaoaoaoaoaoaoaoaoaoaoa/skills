---
name: shazam
description: Identify the music audible in a linked webpage, social post, audio, video, or stream, then provide a verified full-length free-to-stream link. Use when the user supplies a link and wants the song, composition, remix, or ordered tracks playing there, including music embedded in longer media.
---

# Shazam

Infer the intended music from the link and conversational context. The user
should not have to specify a timestamp, media type, or extraction method when
the target is reasonably apparent.

Inspect the linked object's own evidence and obtain playable media as needed.
Let its structure, audible changes, credits, captions, comments, and visible
cues determine whether the target is one dominant piece or several tracks in
order. Seek clean representative spans; when one does not match, try materially
different evidence before concluding. `yt-dlp` and `ffmpeg` are available for
media acquisition and isolation. For acoustic recognition of one or more local
clips, run:

```sh
skill=$(readlink -f "${CODEX_HOME:-$HOME/.codex}/skills/shazam")
"$skill/scripts/recognize.py" /path/to/clip ...
```

Treat an acoustic match as evidence rather than an oracle, especially for
covers, samples, live versions, edits, and remixes. Reconcile it with the
linked context.

After identification, find a lawful full-length stream available without a
paid subscription. Prefer an artist, label, distributor, or platform-generated
catalog upload, then a first-party song page on an ad-supported service. Verify
the artist, title, version, and duration; previews, excerpts, Shorts, reaction
videos, compilations, downloaders, and unauthorized rips do not qualify. Link
the playback page rather than an ephemeral media URL. If no qualifying stream
can be verified, say so and link the best authoritative catalog page instead.

Report the exact artist and title with the listening link, adding version,
composer, or timestamps when they distinguish the answer. If uncertainty
remains, state it tersely with the best candidates. Return the identification,
not a process narrative.
