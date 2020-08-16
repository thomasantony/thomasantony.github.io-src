---
title: "Writing Orbiter Addons using Rust : Part 1"
date: 2020-08-15T20:08:15-05:00
draft: true
tags: orbiter, rust, orbitersim, cxx, coding
categories: Orbiter, Rust
---

The venn diagram of [Orbiter](http://orbit.medphys.ucl.ac.uk/) enthusiasts and [Rust](https://www.rust-lang.org/) language fans probably has very little overlap. However, I happen to fall into both camps and to my knowledge, there is currently no example of writing addons for Orbiter in Rust. This series will be focused on using the [cxx](https://github.com/dtolnay/cxx) crate to interface Rust code with the Orbiter-sdk with the end goal of writing a proof-of-concept MFD addon for Orbiter in Rust. 

## Pre-requisites

### Visual Studio toolchain 

Follow my previous [article](/posts/orbiter-sdk-vs-2019) to set up Visual Studio 2019 for Orbiter SDK. However, for this particular use case, only the actual compiler toolchain and windows SDK is required (rather than the IDE).

### Rust for Windows

Install Rust on windows following the instructions at (https://www.rust-lang.org/tools/install)[https://www.rust-lang.org/tools/install]. After it is installed, run the following command to install the Win32 target since Orbiter 2016 does not support 64-bit code. 

```
rustup target add i686-pc-windows-msvc
```


