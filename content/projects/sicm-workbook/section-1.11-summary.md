+++
title = "Section 1.11: Summary"
date = "2022-10-29T21:22:55Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++



## Summary



This chapter was primarily introducing the Lagrangian method of analyzing mechanical systems. Here are some of the key points:


* To start with, we need to distinguish between realizable motions and other possible motions of the system. This is achieved using the "action function", which is constructed to be stationary only on paths that describe realizable motions, with respect to variations in the path. This is called the *principle of stationary action* or *principle of least action* and is the foundation of classical mechanics (and apparently electrodynamics, quantum mechanics and general relativity). The stationary action principle is a coordinate-independent description of realizable paths. Regardless of if the system has constraints, we may choose any system of coordinates that uniquely determines the configuration of the system.

    - An action is defined as the integral of a function, *the Lagrangian* along a path. For many mechanical systems, the appropriate choice for a Lagrangian is the difference between the kinetic energy and potential energy of the system. This is not unique and there may be many choices of valid Lagrangians for a given system. 

    - By applying the Euler-Lagrange operator to the Lagrangian, we can derive a set of ordinary differential equations called the *Lagrange equations* that describes the motion of the system. Any realizable path saisfies these *equations of motion*. 

    - We can add a "total-time derivative" to a Lagrangian without affecting the Lagrange equations of system

    - The entire time-history of a system can be simulated from a starting point with an initial state (which usually consists of the coordinates and the rate of change of the coordinates at the initial time) using these equations of motion

* If there are continuous symmetries in a system, there are conserved quantities associated with that system ([Noether's theorem](/projects/sicm-workbook/section-1.8.5-noethers-theorem))

    - If the Lagrangian can be formulated such that the symmetries manifest as missing coordinates in the Lagrangian,  then there are conserved momenta that are "conjugate" to these coordinates
    - If the Lagrangian is independent of time then there is a conserved energy.
    
* [Constraints](/projects/sicm-workbook/section-1.10-constrained-motion) in a dynamic system can be either holonomic or non-holonomic
    - The constraints can be added to the systems by augmenting the Lagrangian with the constraint function.
    - With Holonomic constraints, the "Lagrange multiplier" $\lambda$ and redundant coordinates can be eliminated from the system and the dynamic equations formulated in terms of just the coordinates and velocities.
        - Holonomic constraints are those which are either coordinate functions, or can be represented as coordinate functions (called integrable constraints)
    - Non-holonomic constraints have a velocity dependency and systems with these constraints do not currently have a general solution
