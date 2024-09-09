---
title: 🔊 Audio
weight: 25
params:
  art: /audio.png
---

(⌛ Coming soon)

## Available nodes

Sources:

* `empty`: an empty audio source that is always stopped.
* `zero`: an audio source producing silence.
* `sine`: a sine wave generator.
* `square`: a square wave generator.

Playback control:

* `mute`: consumes the input nodes but produces silence.
* `pause`:
* `loop`

Left and right channel mixing:

* `pan`
* `take_left`
* `take_right`
* `swap`

Nodes mixing:

* `mix`
* `all_for_one`
* `concat`

Misc:

* `gain`
* `track_position`
* `high_pass`
* `low_pass`

## Available LFOs

* `Switch`
* `Linear`
* `Sine`
