---
title: 🔊 Audio
weight: 25
params:
  art: /audio.png
---

(⌛ Coming soon)

{{< hint warning >}}
**Loud sounds ahead!**

Turn your volume down. Loud sounds may damage your hearing. Also, when you experiment with the sound by yourself, keep in mind that you won't hear too low or too high frequences but they still can harm your hearing if played too loud.
{{< /hint >}}

{{< hint info >}}
If you want to visualize audio, try [Friture](https://friture.org/), a free and open-source cross-platform program that can show frequencies of any audio you play. Playing the example above should show a sharp spike at 440 Hz on the "FFT Spectrum".
{{< /hint >}}

## Available nodes

Sources:

* `empty`: empty audio source that is always stopped.
* `zero`: audio source producing silence.
* `sine`: sine wave generator.
* `square`: square wave generator.
* `sawtooth`: sawtooth wave generator.
* `triangle`: triangle wave generator.
* `noise`: white noise generator.

{{< hint info >}}
The sine, square, triangle, sawtooth, and white noise are the most basic sounds. You can learn more about them and about how sound works in an amazing interactive tutorial [Let's learn about waveforms](https://pudding.cool/2018/02/waveforms/).
{{< /hint >}}

Playback control:

* `mute`: consumes the input nodes but produces silence.
* `pause`:
* `loop`

Left and right channel mixing:

* `pan`: shift the audio to the left (0.0), right (1.0), or something in between.
* `take_left`: convert stereo to mono by taking the left channel.
* `take_right`: convert stereo to mono by taking the right channel.
* `swap`: swap left and right channels of the stereo input.

Nodes mixing:

* `mix`: mix all the inputs. Stops only if all input sources stop. Most of the other nodes (including the root `OUT` node), if given multiple inputs, will behave the same as `mix`.
* `all_for_one`: same as `mix` but stops when any of the sources stops.
* `concat`: play the inputs one after the other, in the order as they added. An input is played if all previous inputs have stopped.

Misc:

* `clip`:
* `gain`:
* `track_position`:
* `high_pass`:
* `low_pass`:

## Available modulators

LFOs:

* `SineModulator`: sine wave low-frequency oscillator. It looks like this: `∿`. Paramaters are oscillation frequency `freq`, lowest produced value `low`, and highest produced value `high`.

Envelopes:

* `LinearModulator`: linear (ramp up or down) envelope. It looks like this: `⎽╱⎺` or `⎺╲⎽`. The value before `start_at` is `start`, the value after `end_at` is `end`, and the value between `start_at` and `end_at` changes linearly from `start` to `end`.
* `HoldModulator`: hold envelope. It looks like this: `⎽│⎺` or `⎺│⎽`. The value before `time` is `before` and the value after `time` is `after`. Equivalent to `LinearModulator` with `start_at` being equal to `end_at`.
