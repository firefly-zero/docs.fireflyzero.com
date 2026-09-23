---
title: File system
weight: 5
params:
  icon: fa-solid fa-folder-tree
  emoji: 🗃
---

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
  * `launcher`: short metadata of the launcher. This is the first app that is launched when device/emulator starts.
  * `new-app`: short metadata of the latest installed app. If there is no launcher installed in the system, this is the app that will be launched first when device/emulator starts.
  * `name`: the device name. By default, generated to be unique but users may change the device name. For multiplayer, we require all connected devices to have a unique name to avoid confusion. The name has the same validation rules as author and app IDs and can be at most 16 characters long.
  * `battery`: battery info. Contains the voltage values corresponding to 0% and 100% battery charge.
