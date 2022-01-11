---
title: "Orbiter Addon Development in Rust"
date: 2022-01-10T23:49:12-06:00
draft: false
---

This short article will explore how to create a spacecraft addon for the [Orbiter](http://orbit.medphys.ucl.ac.uk/) spaceflight simulator in the [Rust](https://rust-lang.org/) programming language. I previously took a stab at this back in 2020 with [limited success](https://github.com/thomasantony/RustMFD). I was much less knowledgeable about Rust at the time and the tooling around C++ bindings were not as mature then. This post is a companion to [this new repository](https://github.com/thomasantony/orbiter-rs) that contains a proof-of-concept for building a spacecraft addon for Orbiter in Rust.

## Why Rust?

Rust is a relatively new high level systems programming language with a focus on safety. Orbiter is written in C++ and therefore its addons are also typically written in C++. Rust development for Orbiter is facilitated using the [cxx](https://cxx.rs) crate.

## Design

The repository in its current form produces a DLL file as its build artifact that can be loaded into Orbiter as an addon module. Anyone wanting to create a Rust addon will clone/fork the repository and build it along with the the Rust code for their addon. There are a limited number of Orbiter SDK functions currently available as Rust bindings in this prototype. This will expand in the future to hopefully encompass the majority of the API. The repository includes a demo addon that models NASA's [Surveyor](https://en.wikipedia.org/wiki/Surveyor_program) probe. This follows from the C++ tutorial at [OrbiterWiki](https://www.orbiterwiki.org/wiki/Vessel_Tutorial_1) and implements retro-thruster staging and differential thrust attitude control.

Eventually, I hope to change this so that this repository is a crate that can be imported by an addon module. This will possibly require creation of procedural macros for automatic code generation.

## Developing custom spacecraft addons

All the spacecraft-specific code in the repository lives in its own file (`src/shuttle_pb.rs` for example). The file should include a struct that implements the `OrbiterVessel` trait and calls the `make_orbiter_vessel` macro with an instance of the struct. This macro generates the `create_rust_spacecraft` function that is used to link the code to the OrbiterSDK. For example:

```rust
use crate::{
    ODebug, make_orbiter_vessel, OrbiterVessel, VesselContext, _V,
};

#[derive(Default, Debug)]
pub struct ShuttlePB {
    some_param: i32
}

impl OrbiterVessel for ShuttlePB {
    fn set_class_caps(&mut self, context: &VesselContext) {
        context.SetSize(1.0);
        context.SetPMI(_V!(0.50, 0.50, 0.50));
        context.AddMesh("ShuttlePB");
    }
    fn pre_step(&mut self, context: &VesselContext, _sim_t: f64, _sim_dt: f64, _mjd: f64) {
    }
    fn consume_buffered_key(
        &mut self,
        context: &VesselContext,
        key: crate::ffi::DWORD,
        down: bool,
        kstate: [u8; crate::consts::LKEY_COUNT],
    ) -> i32 {
        0
    }

}

make_orbiter_vessel!(ShuttlePB::default());
```

This file is then included in `lib.rs` as follows:


```rust
mod shuttlepb;
pub use shuttlepb::create_rust_spacecraft;
````

The addon may use any of the wrapped functions currently available. Any other Orbiter SDK functions will require wrappers to be generated for them. An automated tool like [autocxx](https://github.com/google/autocxx) may be worth investigating for this purpose.

## Building and Installing

The addon can be built using `cargo build` assuming that Visual Studio 2019 is available. Other C++ compilers may or may not work. Deploying the addon also requires a config file and any meshes and other dependencies. An example can be seen in `Config/Surveyor.cfg`. Once you build the addon, the DLL will be available in the `target/i686-pc-windows-msvc/Debug` folder. This will need to be renamed to match whatever module name you haev in the configuration file.

## Summary

This proof-of-concept gives a basic framework for building Orbiter addons in Rust. It is not a complete system by any metric and will require significant amounts of work before it can be considered that.
