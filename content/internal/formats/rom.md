---
title: ROM
weight: 8
params:
  icon: fa-solid fa-floppy-disk
  emoji: 💾
---

Running `firefly_cli export` creates a single-file distribution for an app's ROM. This ROM can be imported back using `firefly_cli import`.

This file is a regular [zip archive](https://en.wikipedia.org/wiki/ZIP_(file_format)) with [zstd](https://en.wikipedia.org/wiki/Zstd) compression. Because zstd compression support is added into the zip specification only in 2020, your archive program won't be able to open it.
