---
title: 🎮 Input
weight: 20
---

## Buttons

The `read_buttons` function returns which buttons are currently pressed. The SDKs also provide convenience methods to compare two states to get which buttons were just pressed or just released.

The function requires the `player_id` argument. In a singleplayer game, you can pass into it any value.

## Touch pad

The `read_pad` function returns the coordinates of the finger on the touch pad if user currently presses it. The coordinates are expressed as a pair of X and Y values in the range from -1000 to 1000 (both ends included). SDKs also provide a way to convert it into [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system) using `radius` and `azimuth` methods.

When using the emulator with a gamepad, you have to press the stick down (or press LB) for the input to be recognized. This is because we need a way to distinguish between not touching the touch pad and touching it in the middle.

## Multiplayer

(⌛ Coming soon)
