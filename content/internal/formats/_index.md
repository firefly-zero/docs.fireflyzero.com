---
title: File formats
type: docs
weight: 3
bookCollapseSection: true
params:
  icon: fa-solid fa-file
  emoji: 📄
---

For media files, the first byte of the file indicates what type it is:

* `0x11`: mono font v1.
* `0x21`: image v1.
* `0x31`: audio v1.
* `0x41`: screenshot v1.

Firefly uses little endian for everything, including custom file formats.

{{<toc>}}
