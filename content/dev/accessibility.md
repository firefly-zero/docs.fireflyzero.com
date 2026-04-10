---
title: Accessibility
weight: 40
params:
  art: /multiplayer.png
  icon: fa-solid fa-handshake
  emoji: 🤝
---

Accessibility is about making your game accessible to as many people as possible. Everyone is different and have different limits to their abilities. If you can play your game yourself doesn't mean that others can play it too. And this page will help you to fix it.

## 📑 Game Manuals

Writing a manual is the easiest way to explain people how to play your game. Even if you have an in-game tutorial (which is always the best option if done right), it's still a good idea to write a manual just in case.

{{< hint info >}}
**Writing manuals is fun!**

Don't stop at just a simple "How to play" manual, make it fun and personal. Tell the story of game development, thank people that helped you with the project (even indirectly), give hints to secrets and easter eggs. Think of [Tunic](https://en.wikipedia.org/wiki/Tunic_(video_game)), a game that made its manual the central mechanic for exploring the world.
{{< /hint >}}

The game manual directory should be included in [firefly.toml]({{< ref "/dev/config/" >}}):

```toml
[files]
_manual = { path = "manual" }
```

Or it can also be a single file:

```toml
[files]
_manual = { path = "manual.md" }
```

Every manual page is a [Markdown](https://www.markdownguide.org/) file. We support only some Markdown features (more might be added later).

Blocks:

* `# Page Title`. Must be present at the very top of the file. This is the name of the manual page.
* `## Header`. A section header.
* `### Header`. A sub-section header.
* `[QR](https://fireflyzero.com/)`. A QR code pointing to the given URL. The text in square brackets is discarded.

Text effects:

* `**strong**`. Highlight the word with the accent color (green in the default color scheme).
* `*emphasis*`. Currently highlights the word with the secondary color (gray in the default color scheme). This might change in the future.

Example:

```markdown
# How to Play

Be not afraid!

## Controls

Use **touchpad** to move around and **S** to jump.

## More

See video tutorial:

[tutorial](https://example.com/)
```

## ⚙️ Settings

You can access in runtime system settings for the given peer:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust as ff;

let me = ff::get_me();
let settings = ff::get_settings(me);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
me := firefly.GetMe()
settings := firefly.GetSettings(me)
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const ff = @import("firefly");
const me = ff.getMe();
const settings = ff.getSettings(me);
```

{{< /tab >}}
{{< tab "TS" >}}

```ts
const me = ff.getMe();
const settings = ff.getSettings(me);
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peer me = get_me();
Settings settings = get_settings(me);
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let me = @firefly.get_me()
let settings = @firefly.get_settings(me)
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
me = firefly.get_me()
settings = firefly.get_settings(me)
```

{{< /tab >}}
{{< /tabs >}}

{{< hint warning >}}
**Avoid state drift!**

As covered in [multiplayer docs]({{< ref "/dev/net/" >}}), using `get_me` for game logic might lead to state drift. So, when using `get_me` as the peer for `get_settings`, make sure to use settings only in `render` or in render-related logic.
{{< /hint >}}

Settings attributes:

* `theme` (Theme): The preferred color scheme of the player.
* `language` (Language): The configured interface language.
* `rotate_screen` (bool): If true, the screen is rotated 180 degrees. In other words, the player holds the device upside-down. The touchpad is now on the right and the buttons are on the left.
* `reduce_flashing` (bool): The player has photosensitivity. The app should avoid any rapid flashes.
* `contrast` (bool): The player wants increased contrast for colors. If set, the black and white colors in the default palette are adjusted automatically. All other colors in the default palette or all colors in a custom palette should be adjusted by the app.
* `easter_eggs` (bool): If true, the player wants to see easter eggs, holiday effects, and weird jokes.

## 🗃 Catalog

Firefly Zero has the official catalog of apps and games: [catalog.fireflyzero.com](https://catalog.fireflyzero.com/). When adding a new game to the catalog, you must list in it all the categories of accessibility limitations that apply:

* `accessibility/colors`: **Requires color recognition.** Tip: use not only colors but also shapes for different types of entities. For example, in [Eat the Red King](https://catalog.fireflyzero.com/lux.king), every green pawn has a white dot in the middle. When only color can be used, prefer using black and white. Or orange and blue (like portals in Portal) as these are the "far apart" colors that most of the color blind people can still distinguish.
* `accessibility/sound`: **Requires hearing audio.**
* `accessibility/difficulty`: **Game difficulty/speed cannot be adjusted.** Note: non-action PvP multiplayer games often don't have a notion if difficulty (the difficulty comes from how good your opponent is), so in such cases the category doesn't need to be specified. Tip: introduce mechanics that would help players that get stuck. Allow skipping levels. Allow getting a hint after spending too much time on a single puzzle. Allow grinding for dinamite and potions before a difficult boss battle.
* `accessibility/reaction`: **Requires good reaction and timed inputs.** Tip: Some games are designed to put the player's reaction speed to the test, so it's often ok to have a game where this cannot be adjusted. However, non-action games should provide a room for stress-free experience. Remove timers from your game, allow disabling them, or make them count up, without deadline, and use it only for scoreboards.
* `accessibility/two-handed`: **Requires using buttons and touchpad at the same time.** Tip: touchpad is a very powerful input method and it can encode a lot of information. In a racing game, make it accelerate when the touchpad is touched, without requiring the player to hold a button. If the car can also shoot, make it shoot forward non-stop (or when the touchpad is released and touched again).
* `accessibility/multi-button`: **Requires pressing several buttons at the same time.**
* `accessibility/reading`: **Requires reading and understanding text to progress.** Tip: It can be difficult for many people to read long text, even in their native language. Keep the text short. Use icons. Use environmental storytelling. Ask yourself how you can make the gameplay as intuitive as possible. Make a YouTube video teaching people how to play the game.
* `accessibility/flashing`: **Contains flashing lights.** Tip: Epilepsy can be very dangerous. Avoid rapid change in colors and brightness. Make all transitions smooth if possible. Explosions, even epic ones, don't have to flash and shake the whole screen.
* `accessibility/dizziness`: **Contains rapid movement that can cause dizziness.**
