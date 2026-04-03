---
title: Hacking
weight: 25
params:
  art: /debugging.png
  icon: fa-solid fa-code
  emoji: 😎
---

Firefly Zero is one of the first game consoles in the world designed to be hacked. We want you to have fun, and there is nothing more fun than taking things apart and figuring out how everything works. So, let's hack it!

##

{{< hint info >}}
This tutorial covers hacking apps and runtime. To physically take apart the device, see [Repair]({{< ref "/user/repair" >}}).
{{< /hint >}}

{{< hint warning >}}
**Breaking things may break things!**

When taking apps apart, it's possible to break them or damage some data (like game saves). To prevent losing your progress, we'll be mostly using Firefly Emulator in this tutorial. Before hacking the app on the device, make sure to backup game data. We'll cover the emulator and backups below.
{{< /hint >}}

## Preparation

Follow [the installation guide]({{< ref "/user/installation" >}}) to install Firefly Emulator and Firefly CLI:

* CLI means "Command-Line Interface". That means, it's a tool that you can use from command line. Command line is what cool kids use. Instead of clicking buttons in an interface, you type text commands, just like hackers in movies. For example, type `ff import lux.gates` to install "Through the Gate" in the emulator (more on this below). If you never used anything like this before, hacking Firefly Zero is a fun way to learn it.
* The emulator allows you to run Firefly Zero apps on your computer so that you don't need to send them on the device every time you change something. This is what developers do when the make their apps/games. Run `ff emulator` to run the emulator.

With these tools in place, you need to find out the author and app IDs for the app you want to hack. You can see them in the app menu in launcher or in the catalog in the page URL. For example, [Through the Gate](https://catalog.fireflyzero.com/lux.gates) has author ID `lux` and app ID `gates`.

## Accessing ROM files

You can access the file system of the device by getting out the SD card (make sure to turn off the device first!) and inserting it into your computer. The location of the file system for Fireflty Emulator can be found by running `ff vfs`.

You can read more about the file system in the [internal documentation]({{< ref "/internal/fs" >}}) but in this section we're only interested in the `roms/AUTHOR_ID/APP_ID` directory (for example, `roms/lux/gates`). It contains all the files that the game needs to run: binary code, sprites, music, sound effects, levels, etc. Most of it, however, is encoded as a binary, not text, and hence isn't easy to read or modify.

You can get some information about these files using CLI: `ff inspect AUTHOR_ID.APP_ID` (for example, `ff inspect lux.gates`). It will list some of the file formats and extract some information about them. For example, for images, it will list the image width, height, used colors, etc.

{{< hint info >}}
If you break the app after modifying its ROM, just re-install it and everything should work again.
{{< /hint >}}

## Accessing app data

The `data/AUTHOR_ID/APP_ID` directory contains the app data: save files, game progress, logs, etc. If you want to view or modify your save data, it's usually stored in `stash` file but sometimes some progress can also be stored in `etc` directory. Scores and achievements are stored in `stats` file but reading or modifying it can be tough since it's all binary-encoded.

{{< hint info >}}
You can backup game data (backup your progress) by copying the whole app data directory to your computer. To restore it, remove the app data directory in the device (emulato) file system and copy instead the one that you saved earlier.
{{< /hint >}}

## Cheat codes

Some games provide cheat codes that you can send using CLI. For example, when running [Snek](https://catalog.fireflyzero.com/lux.snek): `ff runtime cheat 2 10`. This will add 10 to the current score. Here `2` is the command code (increase score) and 10 is the value.

How to find supported commands and their codes? If you have the app source code (more on this below), you can find the supported cheat codes in `firefly.toml`. For example, Snek has the following section:

```toml
[cheats]
move-apple = 1 # Move apple into a new random position
inc-score = 2  # Increment the score by the given value
dec-score = 3  # Decrement the score by the given value
```

If there is no source code available (and nobody else published the list of cheats), try different codes and see what they do. Have fun!

{{< hint info >}}
Keep in mind that cheat codes don't work in multiplayer.
{{< /hint >}}

## Modifying app code

Some apps have their source code published for everyone to see, use, and modify. Usually, you can find the link to the source code on the app catalog page. See the [developer guide]({{< ref "/dev/" >}}) on how to modify, build, and install apps from source.

## Modifying Firefly Zero

THe source code for Firefly Zero runtime and all system apps is available at [github.com/firefly-zero](https://github.com/firefly-zero/). You can read it, modify, and install on your device. Depending on what you want to do, it might require you to know [Rust](https://rust-lang.org/) programming language.

Modified system apps can be installed the same way as any other apps (see the previous section).

This section will be later updated with a guide on how to install modified runtime on the device.
