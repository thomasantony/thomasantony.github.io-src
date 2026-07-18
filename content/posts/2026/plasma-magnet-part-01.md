+++
title = "Plasma Magnet 01"
date = "2026-07-18T05:24:01.000Z"
draft = true
+++

The plasma magnet is a proposed mode of space propulsion which harnesses the kinetic energy of the solar wind using a magnetic sail. The magnetic sail is powered by a rotating magnetic field that induces currents in the solar wind electrons preferentially (compared to the protons) and hence generates its own magnetic field which is supposed to inflate until the magnetic pressure matches the dynamic pressure of the solar wind.

This is the first in a series of posts where I am trying to replicate this in numerical simulations using the open source Particle-In-Cell simulation software - [WarpX](https://blast-warpx.github.io/).

Intro

WarpX + GPU?

Modifying WarpX for generating RMF
Naive impl
Divergence form discretization
Divergence-free implementation (cartesian 3D only)

Later ...

Building the infra
- python dispatch
- python worker + scheduler
    - all the problems
    - unstable - dispatch server crashes
    - unable to retrieve artifacts
    - more excpetions from GIL
    - finally porting to JS
    - auto-terminate
    - Manual D1 access
    - Still have the occasional problem

Tangent - ThunderCompute investigation and pinned host memory


Initial attempt - direct solar wind - miserably failed

Phase 0
Vacuum Coil Validation
Single electron rotation and reverse

Non-driven plasma
- filters?

boundary qualification - PML, periodic
wasted time?



Phase 1 results summary

RMF discovery (non-driven vs driven)
- seed repeat

Local Kinetic Fidelity
- finer grid and/or timestep

RMF full run
- results?
- plots?

