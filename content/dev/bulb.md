---
title: Bulb Script
weight: 80
params:
  icon: fa-solid fa-lightbulb
  emoji: 💡
---

Bulb is a scripting language inspired by [Bitsy](https://bitsy.org/) and [Pulp](https://play.date/pulp/) and designed specifically for Firefly to create simple adventure games.

{{< hint info >}}
**What kind of games?**

Bulb is designed for making adventure games: you can walk around, talk to NPCs, interact with objects, and solve puzzles. Bulb cannot be used to implement reaction-based games, physics, real-time behaviors, complex fighting systems, or multiplayer. If your game needs any of these features, go to the main [Getting started]({{< ref "/dev/getting-started/" >}}) to make a game in a proper programming language.
{{< /hint >}}

In the future, we plan to implement a web editor for Bulb. But for now, there is only manual scripting in a text editor. However, we did our best to make this scripting fun and easy!

It's also possible to write simple adventure games for Firefly Zero using [Bitsy](https://bitsy.org/). It's very similar to Bulb but it also has a simple and friendly online editor: [make.bitsy.org](https://make.bitsy.org/). However, Bitsy is not created for Firefly Zero, so it has fewer features and worse performance. If you decide to use Bitsy, go to the main [Getting started]({{< ref "/dev/getting-started/" >}}) and select "Bitsy" as your programming language.

## Getting started

1. [Install firefly-cli and firefly-emulator]({{< ref "/user/installation/" >}})
1. Create a new Bulb project:

    ```bash
    firefly_cli new --lang=bulb hello-world
    ```

1. Build and install the game:

    ```bash
    firefly_cli build
    ```

1. Run the game in the emulator:

    ```bash
    firefly_emulator
    ```

## Scripting

### Sections

Every script consists of multiple sections separated by at least one empty line. Every section start with one letter indicating the section type followed by the section ID.

Section type can be one of:

* `R` is for room.
* `T` is for tile.
* `I` is for image.
* `P` is for player.
* `A` is for actions.

The ID can be anything except whitespace. You can use letters, words, symbols, and even emojis.

For example:

```bulb
A 🐈
SAY I'm a cat.

A tommy
SAY oh hi cat
```

This defines 2 sets of actions: 🐈 and `tommy`.

### Room

Room section defines the set of tile IDs for every room. It consists of 10 lines with 15 space-separated IDs in each. For example:

```bulb
R start
W W W W W W W W W W W W W W W
W . . . . . . . . . . . . . W
W . . . . . . . . . . . . . W
W . . . P . . . C . . . . . W
W . . . . . . . . . . . . . W
W . . . . . . . . . . . . . W
W . . . K . . . . . . . . . W
W . . . . . . . . . . . . . W
W . . . . . . . . . . . . . W
W W W W W W W W W W W W W W W
```

Or with emojis:

```bulb
R start
🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱
🧱 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ 🚩 ⚪️ ⚪️ ⚪️ 🐈 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ 🔑 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ ⚪️ 🧱
🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱 🧱
```

### Tile

Tiles define how particular squares in the room look and behave. Each line defines one property of the tile. Supported properties:

* `IMAGE id`: Defines the image ID to use when rendering the tile.
* `WALL 1`: Make the tile a wall. The player cannot step on the tile marked as a wall. You want to set it for walls, NPCs, etc.
* `START 1`: Mark the tile as the starting tile. When the game starts, the player will be placed on the given tile in the room that contains this tile.
* `ACTION id`: Execute the given action when the player steps on the tile. If the tile is a WALL, the action will be executed when the player *tries* to step on the tile.

For example:

```bulb
T W
IMAGE wall
WALL 1
```

### Image

Every Bulb game includes one big image called `atlas`. The atlas contains a grid of 16x16 pixel square images in the default color palette ([SWEETIE-16](https://lospec.com/palette-list/sweetie-16)). The `I` sections in the Bulb file say which of these squares to use for the tiles.

Supported properties:

* `POS x y`: zero-indexed position of the square to use from the atlas. For example, `POS 2 0` will use the 3rd square from the 1st row.
* `PLAYER 1 idle`: use the image to represent the player. At least one image must have this property set.
* `FRAMES x`. The number of animation frames. Currently unused.

Example:

```bulb
I idle
POS 0 0
PLAYER 1 idle

I cat
POS 1 0

I cat
POS 3 1
```

To add or change images available in the atlas, edit `atlas.png`. See [Install firefly-cli and firefly-emulator]({{< ref "/dev/graphics/" >}}#-additional-resources) on the Graphics page for the list of pixel editors and asset packs.

### Actions

Actions define list of actions to be executed when the relevant tile is triggered. Supported actions:

* `SAY msg`: Print the given message on the screen. It can be used for talking to NPCs, reading books, notifying about state of things, etc. Multiple `SAY` can be used in the same set of actions, each one is printed on a separate page. When a message is shown, actions execution will be paused until the player presses any button. Some examples:
  * `SAY Sailor: Hello, adventurer!`
  * `SAY This door is locked.`
  * `SAY You found a key!`
* `END`: Print "THE END" message and exit the game. Doesn't accept any arguments.
* `MOVE room x y`: Teleport the player to the given room in the given location. For example, `MOVE library 3 18` will teleport the player to the room "library" to the 4th column and 19th row (because the coordinates are zero-indexed).
* `PLACE tile x y`: Replace the tile in the current room at the given position with the given tile. For example, `PLACE cat 3 18` will place a cat at x=3 and y=18.
* `PLACE tile`: If `PLACE` is specified without coordinates, the currently activated tile will be replaced. For example, `PLACE floor` will replace the tile that the player activated (has touched or is standing on).
* `SET var val`: Set the value of the given variable. All variables are signed integers and zero by default. For example, `SET key 1` will store `1` in the variable `key`.
* `ADD var val`: add the given value ti the given variable. For example, `ADD stars 1` will add 1 to the variable `stars`. You can also use negative values to substract. For example, `ADD health -5`.
* `JUMP action`: Stop executing the current set of actions and start executing the different one instead. This allows to share common steps between multiple action sets. For example, `JUMP pick` will execute `A pick` instead of all remaining action steps.
* `SELECT id1 id2 id3`: Randomly jump to one of the given actions. For example, `SELECT heads tails`.
* `IF var > val JUMP action`: JUMP to the given set of actions if the given condition is true. For example `IF key == 0 JUMP door_closed` will execute `A door_closed` if the `key` variable is equal to zero. Otherwise (if the player has a key), it will continue executing the remaining actions. The comparison operator is one of: `>`, `>=`, `<`, `<=`, `==`, or `!=`.
* `IF var > val BREAK`: Stop executing the current set of actions if the condition is true. The same as `IF` with `JUMP` that leads to an empty action set. For example, `BRANCH key == 0`.

For example:

```bulb
A cat
SAY Cat: I'm a cat.
SAY Yes, I can talk.

A key
SAY You found a key!
ADD key 1
PLACE floor
```

Lastly, if there is only one tile using a set of actions, you can join them together by putting `A` without ID between the instructions:

```bulb
T key
IMAGE key
A
SAY You found a key!
ADD key 1
PLACE floor
```

### Scripting recipes

Actions on the starting tile are executed when the game starts. You can use it to greet the player, initialize variables, etc. Don't forget `PLACE` at the end to make sure the actions won't be activated again when the player goes back to the same tile:

```bulb
T 🚩
IMAGE ⚪️
START 1
A
SET health 3
SAY Welcome, adventurer!
PLACE ⚪️
```

To make a door, make a tile that MOVEs the player:

```bulb
A door
MOVE level1 7 13
```

It's also possible to MOVE the player within the same room, which allows implementing portals.

A door that can be opened only using a key can be implemented by SETting and checking a variable:

```bulb
A key
SET key 1
PLACE floor

A door
IF key == 0 JUMP door_closed
MOVE level1 7 13

A door_closed
SAY The door is closed...
```

If you want an NPC to say something different when interacted again, you can replace the NPC tile with the one that looks the same but has a different action:

```bulb
T 🐈
IMAGE cat
WALL 1
A
SAY I'm a cat.
PLACE cat2

T cat2
IMAGE cat
WALL 1
A
SAY MEOW =^_^=
```

And if you want the lines to repeat, the new action cat loop back to one of the previous ones:

```bulb
T cat2
IMAGE cat
WALL 1
A
SAY MEOW =^_^=
PLACE 🐈
```

Similarly, interactive elements, like switches, can be implemented by PLACE'ing a different version of the tile on interaction:

```bulb
T 💡
IMAGE lamp_on
WALL 1
A
PLACE lamp_off

T lamp_off
IMAGE lamp_off
WALL 1
A
PLACE 💡
```

Damage can be tracked in a variable and the health bar can be implemented as a row of tiles in a room corner:

```bulb
T ♥️
IMAGE ♥️
WALL 1

T 💔
IMAGE 💔
WALL 1

T 🔥
IMAGE 🔥
WALL 1
ACTION take_damage

A take_damage
ADD damage 1
PLACE 💔 29 0
IF damage < 2 BREAK
PLACE 💔 28 0
IF damage < 3 BREAK
PLACE 💔 27 0
IF damage < 4 BREAK
SAY You're dead
END
```

There are no dialog choices. If you want the player to make a choice, make them do so by going somewhere or interacting with something. So, instead of "Would you accept the quest?" your NPC will say "Follow me through that door to accept the quest".

## Next steps

1. Check out [games made with Bitsy](https://itch.io/games/tag-bitsy) and [games made with Pulp](https://devforum.play.date/tags/c/games/6/pulp) to see what games people made with similar engines.
1. Experiment! It doesn't seem like much but you can do a lot with it.
