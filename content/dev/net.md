---
title: Multiplayer
weight: 22
params:
  art: /multiplayer.png
  icon: fa-solid fa-wifi
  emoji: 🔃
---

Firefly Zero has a very unique approach to multiplayer: every game (or app) can be played together! The only question is how the app handles multiple inputs. And this section covers how you can do that. And don't worry, it's very simple.

## ⚙️ How it works

If you take two or more calculators and punch into all of them the same expression, you'll get the same result. However if you make a typo in any of them, the result might be very different.

And that's exactly how Firefly Zero works: all connected devices agree on the same environment for the startup and each update. They synchronize their random values, system time, all the inputs, when to render each frame, etc. The only things that your app need to worry about is what inputs you use and what files you read.

## 🎮 Handling inputs

There are two ways to handle user input: you can either read the combined input from all devices in one go or read each input separately.

The easiest option is to read the combined input from all devices. This is the best strategy for the apps designed to be played alone. If there is only one device (aka peer), the result will be the input from that device. And if there are multiple devices connected, the result will be the combined input from all devices: if anyone presses a button, it is reported as pressed.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let pad = read_pad(Peer::COMBINED);
let buttons = read_buttons(Peer::COMBINED);
```

{{< /tab >}}
{{< tab "Go" >}}

```go
pad, pressed := firefly.ReadPad(firefly.Combined)
buttons := firefly.ReadButtons(firefly.Combined)
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const maybePad = ff.readPad(ff.Peer.combined);
const buttons = ff.readButtons(ff.Peer.combined);
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Pad pad = read_pad(COMBINED);
Buttons buttons = read_buttons(COMBINED);
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
using @firefly {type Peer}
let pad = @firefly.read_pad(Peer::combined())
let buttons = @firefly.read_buttons(Peer::combined())
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
pad = firefly.read_pad(firefly.COMBINED);
buttons = firefly.read_buttons(firefly.COMBINED);
```

{{< /tab >}}
{{< /tabs >}}

The second option is to read and handle each input individually. This is the best option for when you want to provide a custom logic for multiplayer.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let peers = get_peers();
for peer in peers {
    let pad = read_pad(peer);
    let buttons = read_buttons(peer);
    todo!();
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
peers := firefly.GetPeers()
for _, peer := range peers.Slice() {
    pad, pressed := firefly.ReadPad(peer)
    buttons := firefly.ReadButtons(peer)
    // ...
}
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
var peers = ff.getPeers().iter();
while (peers.next()) |peer| {
    const maybePad = ff.readPad(peer);
    const buttons = ff.readButtons(peer);
    // ...
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peers peers = get_peers()
Peer peer;
for (peer = 0; peer < 32; peer++) {
    if (is_online(peer)) {
        Pad pad = read_pad(peer);
        Buttons buttons = read_buttons(peer);
        // ...
    }
}
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
using @firefly {type Peer}
let peers = @firefly.get_peers().to_array()
for peer in peers {
    let pad = @firefly.read_pad(peer)
    let buttons = @firefly.read_buttons(peer)
    ...
}
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
peers = firefly.get_peers()
for i = 1,#peers do
    peer = peers[i]
    pad = firefly.read_pad(peer);
    buttons = firefly.read_buttons(peer);
end
```

{{< /tab >}}
{{< /tabs >}}

## 💾 Handling files

Since all devices run the same app, all files in the ROM are the same, so reading them on every device will give the same result.

Files created using `dump_file` are not accesible in multiplayer. Calling `load_file` for these in multiplayer will emit an error in logs and return nothing. Create files only in single player mode.

If you want to preserve state between app runs and make it available to all peers in multiplayer, use Stash. Stash is a binary file that can be written using `save_stash` and read using `load_stash`:

{{< tabs >}}
{{< tab "Rust" >}}

```rust
let stash = load_stash_buf::<4>(peer, &mut buf[..]);
if let Some(stash) = stash {
    save_stash(peer, &stash);
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
buf := make([]byte, 4)
stash := firefly.LoadStash(peer, buf)
if stash != nil {
    firefly.SaveStash(peer, stash)
}
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
var maybeStash = ff.loadStash(peer, buf);
if (maybeStash) |stash| {
    ff.saveStash(peer, stash)
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Stash stash = load_stash(peer, buf);
if (stash.size != 0)
{
    save_stash(peer, stash);
}
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let buf = FixedArray::make(4, 0)
let stash = @firefly.load_stash(peer, buf)
if stash.length() != 0 {
    @firefly.save_stash(peer, buf)
}
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
stash = firefly.load_stash(peer)
if length(stash) != 0 then
    firefly.save_stash(peer, stash);
end
```

{{< /tab >}}
{{< /tabs >}}

{{< hint info >}}
**Working with limited space**

Currently, the stash size is limited to 80 bytes. It doesn't seem like much but there are lots of ways how to use it effectively. Let's say, you make a collectible card game. The first byte of the stash might represent the current level of the player (up to 255 levels) and the remaining 632 bits (79 bytes) each can store if the player has a specific card (1 for "yes", 0 for "no").

You can optimize it even more if some card combination are not possible. For example, if card A can beupgraded to card B and then to card C (making the previous iteration inaccessible), you can use 2 bytes to store the state of all 3 cards: 00 for None, 01 for A, 10 for B, and 11 for C. That way, you can fit up to 948 cards.
{{< /hint >}}

## 🎲 Randomness

The random values returned by `get_random` are synchronized between devices and are safe to use in multiplayer.

## 🙋 Local peer

You can call the `get_me` function to get the `Peer` corresponding to the local device. But be careful! Do not let it affect the game logic. Otherwise, the state of the app will be different on every device, and everyone will be playing a different game. Use it only for visual effects, like a marker showing the player which character is their. Or showing them only their score. Or in a hidden agenda game (like Mafia) showing them only their role.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let peers = get_peers();
let me = get_me();
for peer in peers {
    if peer == me {
        todo!()
    }
}
```

{{< /tab >}}
{{< tab "Go" >}}

```go
peers := firefly.GetPeers()
me := firefly.GetMe()
for _, peer := range peers.Slice() {
    if peer == me {
        // ...
    }
}
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
const me = ff.getMe();
var peers = ff.getPeers().iter();
while (peers.next()) |peer| {
    if (peer.eq(me)) {
        // ...
    }
}
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peers peers = get_peers();
Peer me = get_me();
for (peer = 0; peer < 32; peer++) {
    if (is_online(peer) && peer == me) {
        // ...
    }
}
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let peers = @firefly.get_peers()
let me = @firefly.get_me()
for peer in peers {
    if peer == me {
        ...
    }
}
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
peers = firefly.get_peers()
me = firefly.get_me()
for i = 1,#peers do
    local peer = peers[i]
    if peer == me then
        -- ...
    end
end
```

{{< /tab >}}
{{< /tabs >}}

## 🥇 Peers' order

The peers are sorted based on their MAC address. That means, the same devices connected together always go in the same order. That also means, if you always give the same peer (for example, the first one on the list) a game advantage (like going first in chess), the same player will always have that advantage. To make things fair, pick a random starting player for each game session using the `get_random` function.

{{< tabs >}}
{{< tab "Rust" >}}

```rust
use firefly_rust::*;
let peers = get_peers();
let idx = get_random() % peers.len();
let peer = peers.iter().nth(idx).unwrap();
```

{{< /tab >}}
{{< tab "Go" >}}

```go
peers := firefly.GetPeers()
idx := firefly.GetRandom() % peers.Len()
peer := peers.Slice()[idx]
```

{{< /tab >}}
{{< tab "Zig" >}}

```zig
var peers = ff.getPeers();
const idx = ff.getRandom() % peers.len();
// ...
```

{{< /tab >}}
{{< tab "C/C++" >}}

```c
Peer peers = get_peers();
// TODO
```

{{< /tab >}}
{{< tab "MoonBit" >}}

```moonbit
let peers = @firefly.get_peers()
let idx = @firefly.get_random() % peers.length()
let peer = peers.to_array()[idx]
```

{{< /tab >}}
{{< tab "Lua" >}}

```lua
local peers = firefly.get_peers()
local idx = firefly.get_random() % #peers
local peer = peers[idx]
```

{{< /tab >}}
{{< /tabs >}}
