---
title: 🐞 Common errors
weight: 55
---

## 🐞 Common errors

This page lists some of the common errors (and how to deal with them) related to Firefly Zero that you may encounter with different tools.

> unsupported compression method 93

You're trying to manually extract a ROM from a ZIP archive created using `firefly_cli export`. ROMs use ZSTD compression that isn't supported by your archive manager. You should use `firefly_cli import` for installing ROMs instead.

{{< button relref="./terms.md" >}}➡️ Terms{{< /button >}}
