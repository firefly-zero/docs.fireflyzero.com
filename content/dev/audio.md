---
title: 🔊 Audio
weight: 25
params:
  art: /audio.png
---

## 🧱 Basics

Sound in Firefly Zero is constructed as a tree of nodes. There is already one node present, called `OUT`. Everything connected to it will play on the speakers (or headphones) of the device. Some nodes, called *sources*, can produce a sound by generating it using math or by reading it from memory or file system. For example, to play note A in 4th octave (440 Hz) using a sine wave:

{{< hint warning >}}
**Loud sounds ahead!**

Turn your volume down. Loud sounds may damage your hearing. Also, when you experiment with the sound by yourself, keep in mind that you won't hear too low or too high frequences but they still can harm your hearing if played too loud.
{{< /hint >}}

{{< tabs >}}
{{< tab "Rust" >}}

```rust
#![no_std]
#![no_main]
use firefly_rust::audio;

#[no_mangle]
extern fn boot() {
    audio::OUT.add_sine(audio::Freq::A4, 0.);
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
package main

import (
    "github.com/firefly-zero/firefly-go/firefly"
    "github.com/firefly-zero/firefly-go/firefly/audio"
)

func init() {
    firefly.Boot = boot
}

func boot() {
    audio.Out.AddSine(audio.A4, 0.)
}
```

{{< /tab >}}
{{< /tabs >}}

<audio controls src="/sine.mp3" preload="metadata"></audio>

{{< hint info >}}
If you want to visualize audio, try [Friture](https://friture.org/), a free and open-source cross-platform program that can show frequencies of any audio you play. Playing the example above should show a sharp spike at 440 Hz on the "FFT Spectrum" panel.
{{< /hint >}}

You can connect up to 4 child nodes to a single node, including `OUT`. For example, to play the chord C (notes C, E, and G):

{{< tabs >}}
{{< tab "Rust" >}}

```rust
audio::OUT.add_sine(audio::Freq::C4, 0.);
audio::OUT.add_sine(audio::Freq::E4, 0.);
audio::OUT.add_sine(audio::Freq::G4, 0.);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
audio.Out.AddSine(audio.A4, 0.)
audio.Out.AddSine(audio.E4, 0.)
audio.Out.AddSine(audio.G4, 0.)
```

{{< /tab >}}
{{< /tabs >}}

<audio controls src="/chord.mp3" preload="metadata"></audio>

In between the source nodes and the output, you can add *effect* nodes that modify the sound that comes through them. For example, the `Gain` node can be used to increase or decrease the gain (volume) of the sound:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let gain = audio::OUT.add_gain(0.5);
gain.add_sine(audio::Freq::A4, 0.);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
gain := audio.Out.AddGain(0.5)
gain.AddSine(audio.A4, 0.)
```

{{< /tab >}}
{{< /tabs >}}

<audio controls src="/gain.mp3" preload="metadata"></audio>

Finally, you can change parameters of nodes over time using *modulators*. For example, use `LinearModulator` to linearly raise gain value from 0 to 1 in a span of 2 seconds:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let gain = audio::OUT.add_gain(0.);
gain.modulate(audio::LinearModulator {
    start: 0.,
    end: 1.,
    start_at: audio::Time::ZERO,
    end_at: audio::Time::seconds(2),
});
gain.add_sine(audio::Freq::A4, 0.);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
gain := audio.Out.AddGain(0.)
gain.Modulate(audio.LinearModulator {
    Start: 0.,
    End: 1.,
    StartAt: audio.Seconds(0),
    EndAt: audio.Seconds(2),
});
gain.AddSine(audio.A4, 0.)
```

{{< /tab >}}
{{< /tabs >}}

<audio controls src="/mod-linear-gain.mp3" preload="metadata"></audio>

## 🧰 Available nodes

Sources:

* `empty`: empty audio source that is always stopped.
* `zero`: audio source producing silence.
* `sine`: sine wave generator.

  <audio controls src="/sine.mp3" preload="metadata"></audio>

* `square`: square wave generator.

  <audio controls src="/square.mp3" preload="metadata"></audio>

* `sawtooth`: sawtooth wave generator.

  <audio controls src="/sawtooth.mp3" preload="metadata"></audio>

* `triangle`: triangle wave generator.

  <audio controls src="/triangle.mp3" preload="metadata"></audio>

* `noise`: white noise generator.

  <audio controls src="/noise.mp3" preload="metadata"></audio>

{{< hint info >}}
The sine, square, triangle, sawtooth, and white noise are the most basic sounds. You can learn more about them and about how sound works in an amazing interactive tutorial [Let's learn about waveforms](https://pudding.cool/2018/02/waveforms/).
{{< /hint >}}

Playback control:

* `mute`: consumes the input nodes but produces silence.
* `pause`: can be paused using modultaion.
* `loop`: resets the input if it stops.

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

* `clip`: [clipping](https://en.wikipedia.org/wiki/Clipping_(audio)). Clamps the input amplitude. Can be used for hard [distortion](https://en.wikipedia.org/wiki/Distortion_(music)).
* `gain`: increases or decreases gain by the given multiplier.
* `track_position`: can be used to track how much time has passed since this node was added (or reset).
* `high_pass`: [high-pass filter](https://en.wikipedia.org/wiki/High-pass_filter).
* `low_pass`: [low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter).

## 🎛 Available modulators

LFOs:

* `SineModulator`: sine wave low-frequency oscillator. It looks like this: `∿`. Parameters are oscillation frequency `freq`, lowest produced value `low`, and highest produced value `high`.

  <audio controls src="/mod-sine-gain.mp3" preload="metadata"></audio>

Envelopes:

* `LinearModulator`: linear (ramp up or down) envelope. It looks like this: `⎽╱⎺` or `⎺╲⎽`. The value before `start_at` is `start`, the value after `end_at` is `end`, and the value between `start_at` and `end_at` changes linearly from `start` to `end`.

  <audio controls src="/mod-linear-gain.mp3" preload="metadata"></audio>

* `HoldModulator`: hold envelope. It looks like this: `⎽│⎺` or `⎺│⎽`. The value before `time` is `before` and the value after `time` is `after`. Equivalent to `LinearModulator` with `start_at` being equal to `end_at`.
