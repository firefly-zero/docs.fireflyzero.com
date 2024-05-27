---
title: 🐎 Performance
weight: 30
---

1. Only draw on the screen from the `render` callback. It is possible for `update` to be called more often than `render`, and so anything you draw in there won't be rendered until the next update.
1. Loading files is expensive. Read files only once, in the `boot` callback.
1. Prefer using 32 bit float over 64 bit float.
1. Avoid allocations.
1. Carefully choose the allocator and garbage collector.
1. "An ounce of image is worth a pound of performance." Using primitives instead of images might save quite a bit of RAM and performance.
