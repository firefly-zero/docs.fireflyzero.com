---
title: 🗃 File system
weight: 5
---

* `roms/`
  * `<AUTHOR_ID>/`
    * `<APP_ID>/`
      * `_bin`: the main executable WASM binary of the app.
      * `_meta`: the app metadata.
      * `_key`: the app author's public key.
      * `_hash`: the [SHA256](https://en.wikipedia.org/wiki/SHA-2) hash of all files in the directory (both their content and their names) except `_sig` and `_hash` itself.
      * `_sig`: the [PKCS 1 v1.5](https://datatracker.ietf.org/doc/html/rfc2313) signature signing the `_hash` with the author's private key. Can be verified using `_key`.
      * May also contain any other files (game assets) that the app needs to run.
* `data/`
  * `<AUTHOR_ID>/`
    * `<APP_ID>/`
      * `etc/`: directory writable by the app. More precisely, the only directory in the whole FS where a non-sudo app can create, modify, list, or delete files. Empty by default. Usually, used to store game saves or assets produced using the app.
      * `shots/`: directory with app screenshots in PNG format.
      * `stats`
* `sys/`
  * `priv/`: directory with private keys.
    * `<AUTHOR_ID>`: the author's private key. Used to sign apps when building with `firefly_cli build`. Private keys are only present on the emulator's virtual file system but never on the device. Use `firefly_cli key` to manage keys.
  * `pub/`: directory with public keys.
    * `<AUTHOR_ID>`: the author's public key. Used to verify signatures of installed ROMs.
  * `launcher`: short metadata of the launcher. This is the first app that is launched when device/emulator starts.
  * `new-app`: short metadata of the latest installed app. If there is no launcher installed in the system, this is the app that will be launched first when device/emulator starts.
  * `name`: the device name. By default, generated to be unique but users may change the device name. For multiplayer, we require all connected devices to have a unique name to avoid confusion. The name has the same validation rules as author and app IDs and can be at most 16 characters long.
