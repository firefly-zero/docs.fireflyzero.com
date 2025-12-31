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

Room section defines the set of tile IDs for every room. It consists of 20 lines with 30 space-separated IDs in each. For example:

```bulb
R start
W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . P . . . C . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . K . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W
```

### Tile

Tiles define how particular squares in the room look and behave. Each line defines one property of the tile. Supported properties:

* `IMAGE`: Defines the image ID to use when rendering the tile.
* `WALL`: Set `WALL 1` to make the tile a wall. The player cannot step on the tile marked as a wall. You want to set it for walls, NPCs, etc.
* `START`: Set `START 1` to mark the tile as the starting tile. When the game starts, the player will be placed on the given tile in the room that contains this tile.
* `ACTION`: Execute the given action when the player steps on the tile. If the tile is a WALL, the action will be executed when the player *tries* to step on the tile.

For example:

```bulb
T W
IMAGE wall
WALL 1
```

### Image

Image is a set of 8x8 space-separated colors. Supported colors ([SWEETIE-16](https://lospec.com/palette-list/sweetie-16) colro palette):

* `.`: transparent
* `1`: <span style="background-color: #1a1c2c; min-width: 40px; height: 1em; display: inline-block"></span> #1A1C2C: black
* `2`: <span style="background-color: #5d275d; min-width: 40px; height: 1em; display: inline-block"></span> #5D275D: purple
* `3`: <span style="background-color: #b13e53; min-width: 40px; height: 1em; display: inline-block"></span> #B13E53: red
* `4`: <span style="background-color: #ef7d57; min-width: 40px; height: 1em; display: inline-block"></span> #EF7D57: orange
* `5`: <span style="background-color: #ffcd75; min-width: 40px; height: 1em; display: inline-block"></span> #FFCD75: yellow
* `6`: <span style="background-color: #a7f070; min-width: 40px; height: 1em; display: inline-block"></span> #A7F070: light green
* `7`: <span style="background-color: #38b764; min-width: 40px; height: 1em; display: inline-block"></span> #38B764: green
* `8`: <span style="background-color: #257179; min-width: 40px; height: 1em; display: inline-block"></span> #257179: dark green
* `9`: <span style="background-color: #29366f; min-width: 40px; height: 1em; display: inline-block"></span> #29366F: dark blue
* `A`: <span style="background-color: #3b5dc9; min-width: 40px; height: 1em; display: inline-block"></span> #3B5DC9: blue
* `B`: <span style="background-color: #41a6f6; min-width: 40px; height: 1em; display: inline-block"></span> #41A6F6: light blue
* `C`: <span style="background-color: #73eff7; min-width: 40px; height: 1em; display: inline-block"></span> #73EFF7: cyan
* `D`: <span style="background-color: #f4f4f4; min-width: 40px; height: 1em; display: inline-block"></span> #F4F4F4: white
* `E`: <span style="background-color: #94b0c2; min-width: 40px; height: 1em; display: inline-block"></span> #94B0C2: light gray
* `F`: <span style="background-color: #566c86; min-width: 40px; height: 1em; display: inline-block"></span> #566C86: gray

For example, an orange cat:

```bulb
I cat
. . . . . . . .
. . . . . . . .
. 4 . 4 . . . 4
. 4 4 4 . . . 4
. 4 4 4 . . 4 .
. 4 4 4 4 4 . .
. . 4 4 4 4 . .
. . 4 . . 4 . .
```

### Player

Player defines the image to be used for the player character. Currently, the only allowed ID is `idle`. For example:

```bulb
P idle
. . . A A . . .
. . . 3 3 . . .
. . . 3 3 . . .
. . 3 3 3 3 . .
. 3 3 3 3 3 3 .
A . 3 3 3 3 . A
. . 3 . . 3 . .
. . A . . A . .
```

### Actions

Actions define list of actions to be executed when the relevant tile is triggered. Supported actions:

* `SAY`: Print the given message on the screen. It can be used for talking to NPCs, reading books, notifying about state of things, etc. Multiple `SAY` can be used in the same set of actions, each one is printed on a separate page. When a message is shown, actions execution will be paused until the player presses any button. Some examples:
  * `SAY Sailor: Hello, adventurer!`
  * `SAY This door is locked.`
  * `SAY You found a key!`
* `END`: Print "THE END" message and exit the game. Doesn't accept any arguments.
* `EXIT`: Teleport the player to the given room in the given location. For example, `EXIT library 3 18` will teleport the player to the room "library" to the 4th column and 19th row (because the coordinates are zero-indexed).
* `PLACE`: Replace the tile in the current room at the given position with the given tile. If coordinates are not provided, will replace the tile on which the player is currently standing. Useful for picking up items. For example:
  * `PLACE cat 3 18`: Place a cat at x=3 and y=18.
  * `PLACE floor`: Replace the tile that the player is standing on with the floor tile.
* `SET`: Set the value of the given variable. All variables are signed integers and zero by default. For example, `SET key 1` will store `1` in the variable `key`.
* `ADD`: add the given value ti the given variable. For example, `ADD stars 1` will add 1 to the variable `stars`. You can also use negative values to substract. For example, `ADD health -5`.
* `JUMP`: Stop executing the current set of actions and start executing the different one instead. This allows to share common steps between multiple action sets. For example, `JUMP pick` will execute `A pick` instead of all remaining action steps.
* `BRANCH`: JUMP to the given set of actions if the given condition is true. For example `BRANCH key == 0 door_closed` will execute `A door_closed` if the `key` variable is equal to zero. Otherwise (if the player has a key), it will continue executing the remaining actions.

Some examples:

```bulb
A cat
SAY Cat: I'm a cat.
SAY Yes, I can talk.

A key
SAY You found a key!
ADD key 1
PLACE floor

A door
BRANCH key == 0   door_closed
EXIT level1 7 13

A door_closed
SAY The door is closed...
```
