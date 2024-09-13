---
title: 🔊 Audio
weight: 25
params:
  art: /audio.png
---

(⌛ Coming soon)

{{< hint info >}}
If you want to visualize audio, try [Friture](https://friture.org/), a free and open-source cross-platform program that can show frequencies of any audio you play. Playing the example above should show a sharp spike at 440 Hz on the "FFT Spectrum".
{{< /hint >}}

## Available nodes

Sources:

* `empty`: an empty audio source that is always stopped.
* `zero`: an audio source producing silence.
* `sine`: a sine wave generator.
* `square`: a square wave generator.
* `sawtooth`: a sawtooth wave generator.
* `triangle`: a triangle wave generator.
* `noise`: a white noise generator.

{{< hint info >}}
The sine, square, triangle, sawtooth, and white noise are the most basic basic sounds. You can learn more about tham and just about how sound works in an amazing interactive tutorial [Let's learn about waveforms](https://pudding.cool/2018/02/waveforms/).
{{< /hint >}}

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

* `clamp`:
* `gain`
* `track_position`
* `high_pass`
* `low_pass`

## Available modulators

LFOs:

* `Sine`

Envelopes:

* `Hold`
* `Linear`
