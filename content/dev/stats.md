---
title: 🏆 Badges and scores
weight: 50
params:
  art: /multiplayer.png
---

## 🏅 Badges

Badges are achievements that the game rewards to the player for doing some actions. Fore example, collecting a certain number of collectables, finding a rare item, doing a hard combo, etc. You can add badges to your game to encourage players to experiment with features they might not normally use, or to approach your game with entirely different play styles.

Badges are defined in `firefly.toml`:

```toml
[badges]
1 = { name = "m i tasti", descr = "bite yourself" }
2 = { name = "u r tasti", descr = "bite someone else" }
3 = { name = "apel tasti", descr = "eat 100 apples", steps = 100 }
```

The key of each badge is the ID used to refer to it in the game. It must start at 1, go sequentially up, and never change between releases. For now, there can be at most 20 badges in a single game.

Each badge has the following properties:

* `name`: a human-readable badge name. The only required field.
* `descr`: a human-readable badge description. Typically, a hint on how to earn it.
* `position`: the order in which badge should be displayed in the UI, ascending. Defaults to the badge's ID. Earned badges bubble up.
* `steps`: how many steps there are to earn the badge. Defaults to 1: the badge is either earned or not, with nothing in between.
* `xp`: how many experience points earning the achievement brings to the player. Defaults to 1. You can set it to any value between 0 (no XP rewareded) to 200.
* `hidden`: the number of steps required for the badge to be shown. If 0 (default), the badge is always shown. If equal to the number of steps required to earn the badge, the badge will be shown only when earned.

Next, define a constant in your code with the badge ID for each badge:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;

const BITE_SELF: Badge = Badge(1);
const BITE_OTHER: Badge = Badge(2);
const EAT_100_APPLES: Badge = Badge(3);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
const (
    BiteSelf     firefly.Badge = 1
    BiteOther    firefly.Badge = 2
    Eat100Apples firefly.Badge = 3
)
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
const Badge BITE_SELF = 1;
const Badge BITE_OTHER = 2;
const Badge EAT_100_APPLES = 3;
```

{{< /tab >}}
{{< /tabs >}}

When a relevant event happens in the game, call `add_progress` with 3 arguments:

1. The Peer that made the progress. Each device will persist between games only their own progress.
1. The badge ID: one of the constants that we defined earlier.
1. The progress value: the number of steps the peer made toward earning the badge. For example, if the badge is "eat 100 apples" and the player eats 3 apples in one go, pass the value 3. You can also pass a negative value to decrease the progress.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let progress = add_progress(peer, EAT_100_APPLES, 1);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
progress := firefly.AddProgress(peer, Eat100Apples, 1)
```

{{< /tab >}}
{{< tab "C/C++" >}}

```rust
Progress progress = add_progress(peer, EAT_100_APPLES, 1);
```

{{< /tab >}}
{{< /tabs >}}

The function returns the progress that the player made towards earning the badge.

## 🥇 Boards

Boards (aka scoreboards or leaderboards) keep track of best scores of the player and their friends. A game can define up to 20 boards based on different game levels and difficulties.

Boards, just like badges, are defined in `firefly.toml`:

```toml
[boards]
1 = { name = "intro" }
2 = { name = "journey begins (easy)" }
3 = { name = "journey begins (hard)" }
```

And just like badges, keys are IDs starting at 1 and going up to 20. Properties are a bit different, though:

* `name`: a human-readable board name.
* `position`: the order in which the board should be displayed in the UI, ascending. Defaults to the board's ID.
* `min`: the smallest score shown in the UI.
* `max`: the biggest score shown in the UI. The scores outside the min-max range will still be stored and might replace other valid scores.
* `time`: if true, the scores will be formatted as time. For example, "05:13:56". It doesn't include units, so it's up to you if it's seconds, minutes, or even in-game time.
* `decimals`: format the scores as a decimal number with that many digits after the decimal separator. For example, `decimals = 2` will format scores as "123.45" and "7.09".

Just like with badges, it's a good idea to define constants with board IDs:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;

const LEVEL_INTRO: Board = Board(1);
const LEVEL_BEGIN: Board = Board(2);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
const (
    LevelIntro firefly.Board = 1
    LevelBegin firefly.Board = 2
)
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
const Board LEVEL_INTRO = 1;
const Board LEVEL_BEGIN = 2;
```

{{< /tab >}}
{{< /tabs >}}

Use `add_score` to put a player's score on the given board:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let best = add_score(peer, LEVEL_INTRO, 100);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
best := firefly.AddScore(peer, LevelIntro, 100)
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Score best = add_score(peer, LEVEL_INTRO, 100);
```

{{< /tab >}}
{{< /tabs >}}

The returned value is the new personal best of the given peer for the given board.

## 👀 Viewing badges and scores

Use `badges` and `boards` subcommands of `firefly_cli` to list all badges and boards respectively defined in the app:

```bash
firefly_cli badges lux.snek
firefly_cli boards lux.snek
```

In the near future, you'll be able to also view badges (with progress) and boards (with scores) in the launcher.

If you want to display during the game a message when the player earns a badge, you'll need to implement it in the game yourself. Compare the old and the new value returned by `add_progress` to see if the badge was earned just now.
