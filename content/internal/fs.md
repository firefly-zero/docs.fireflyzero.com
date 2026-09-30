---
title: File system
weight: 5
params:
  icon: fa-solid fa-folder-tree
  emoji: 🗃
---

## Files

* `roms/`
  * `<AUTHOR_ID>/`
    * `<APP_ID>/`
      * `_bin`: the main executable WASM binary of the app.
      * `_meta`: the app metadata.
      * `_hash`: the [SHA256](https://en.wikipedia.org/wiki/SHA-2) hash of all files in the directory (both their content and their names) except `_sig` and `_hash` itself.
      * `_stats`: default player stats. Contains runtime info about badges and scores.
* `data/`
  * `<AUTHOR_ID>/`
    * `<APP_ID>/`
      * `etc/`: directory writable by the app. More precisely, the only directory in the whole FS where a non-sudo app can create, modify, list, or delete files. Empty by default. Usually, used to store game saves or assets produced using the app.
      * `shots/`: directory with app screenshots in PNG format.
      * `stats`
* `sys/`
  * `battery`: battery info. Contains the voltage values corresponding to 0% and 100% battery charge.
  * `config`: system settings. Includes options that can be configured via [sys.settings](https://catalog.fireflyzero.com/sys.settings), device name, and total XP earned over all games.
  * `device`: device information. Includes hardware revision, serial number, and the currently used OTA partitions for both main and IO chips. Some of it is set when the device is flashed the first time, some of that changes with re-flashing and system updates.
  * `friends`: list of names of all device this device ever connected to. This list allows to reference friends from scoreboards by their index in that list instead of storing the whole name.

## SD Card

Filesystem requirements for the device:

1. Partition: FAT (16 or 32 bit)
1. Partition type: `W95 FAT32 (LBA)`

Follow [this tutorial](https://askubuntu.com/a/1064316) to prepare a clean storage for use with the Firefly Zero device.
