---
title: "Orbiter Addon Development in Rust"
date: 2022-01-10T23:49:12-06:00
draft: false
---

This short article will explore how to create a spacecraft addon for the [Orbiter](http://orbit.medphys.ucl.ac.uk/) spaceflight simulator in the [Rust](https://rust-lang.org/) programming language. I previously took a stab at this back in 2020 with [limited success](https://github.com/thomasantony/RustMFD). I was much less knowledgeable about Rust at the time and the tooling around C++ bindings were not as mature then. This post is a companion to [this new repository](https://github.com/thomasantony/orbiter-rs) that contains a proof-of-concept for building a spacecraft addon for Orbiter in Rust.

## Why Rust?

Rust is a relatively new high level systems programming language with a focus on safety. Orbiter is written in C++ and therefore its addons are also typically written in C++. Rust development for Orbiter is facilitated using the [cxx](https://cxx.rs) crate.

## Design

The repository in its current form produces a DLL file as its build artifact that can be loaded into Orbiter as an addon module. ~~Anyone wanting to create a Rust addon will clone/fork the repository and build it along with the the Rust code for their addon.~~(See update below). 

There are a limited number of Orbiter SDK functions currently available as Rust bindings in this prototype.
This will expand in the future to hopefully encompass the majority of the API. The repository includes a demo addon that models NASA's [Surveyor](https://en.wikipedia.org/wiki/Surveyor_program) probe. This follows from the C++ tutorial at [OrbiterWiki](https://www.orbiterwiki.org/wiki/Vessel_Tutorial_1) and implements retro-thruster staging and differential thrust attitude control.

## Developing custom spacecraft addons

***Update 01/11/2022: This section has been changed to reflect changes to the crate***
~~All the spacecraft-specific code in the repository lives in its own file (`src/shuttle_pb.rs` for example).~~
An addon crate implementing a spacecraft should import the `orbiter_rs` crate. It should then set its crate-type to `cdylib`. 

```toml
[package]
name = "shuttlepb"
version = "0.1.0"
authors = ["Thomas Antony"]
edition = "2018"

[lib]
crate-type = ["cdylib"]

[dependencies]
orbiter_rs = { version = "0.1", path = "/path/to/orbiter-rs" }
```

The crate should then have a `lib.rs` containing a struct that implements the `OrbiterVessel` trait. It should then use the `init_vessel` macro as shown below. This macro generates a stub that is links the Rust code to the OrbiterSDK. For example, in `lib.rs`:

```rust
use orbiter_rs::{
    ODebug, OrbiterVessel, VesselContext, _V, init_vessel, FileHandle
};

#[derive(Default, Debug)]
pub struct ShuttlePB {
    _some_param: i32
}

impl OrbiterVessel for ShuttlePB {
    fn set_class_caps(&mut self, context: &VesselContext, _cfg: FileHandle) {
        context.SetSize(1.0);
        context.SetPMI(_V!(0.50, 0.50, 0.50));
        context.AddMesh("ShuttlePB".to_string());
    }
}

init_vessel!(
    fn init(_h_vessel: OBJHANDLE, _flight_model: i32) -> ShuttlePB
    {
        ShuttlePB::default()
    }
    fn exit() {}
);
```

The addon may use any of the wrapped functions currently available. Any other Orbiter SDK functions will require wrappers to be generated for them. An automated tool like [autocxx](https://github.com/google/autocxx) may be worth investigating for this purpose.

## Building and Installing

The addon can be built using `cargo build` assuming that Visual Studio 2019 is available. Other C++ compilers may or may not work. Deploying the addon also requires a config file and any meshes and other dependencies. An example can be seen in `Config/Surveyor.cfg`. Once you build the addon, the DLL will be available in the `target/i686-pc-windows-msvc/debug` folder. This will need to be renamed to match whatever module name you haev in the configuration file.

## Summary

This proof-of-concept gives a basic framework for building Orbiter addons in Rust. It is not a complete system by any metric and will require significant amounts of work before it can be considered that.
