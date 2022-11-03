+++
title = "Section 1.6.1: Coordinate Transformations"
date = "2022-11-02T03:45:41Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++





## 1.6.1 Coordinate Transformations



Assume we have a mechanical system whose motion is described by a Lagrangian that depends on time, position and velocities. Assume also that we have a coordinate transformation $x = F(t, x')$ that goes from "primed" to "unprimed" coordinates. The Lagrangian $L$ is expressed in unprimed coordinates. We want to find the Lagrangian expressed in primed coordinates. If $q$ is a configuration path in unprimed coordinates an $q'$ is in primed coordinates, then they must satisfy:


{% mathjax() %}
$$
L' \circ \Gamma[q'] = L \circ \Gamma [q]\\
$$
{% end %}




In general, the requirement that paths in two different coordinate systems be consistent with the coordinate transformation can be used to deduce how all of the components of the local tuple transform. Given a coordinate transformation $F$, let $C$ be the corresponding function that maps local tuples in the primed coordinate system to corresponding local tuples in the unprimed coordinate system:


{% mathjax() %}
$$
C \circ \Gamma[q'] = \Gamma[q]
$$
{% end %}




Therefore,


{% mathjax() %}
$$
L' = L \circ C\\
$$
{% end %}




Substituting q and q' into the coordinate transformation, and taking its derivative w.r.t $t$ and applying the chain rule,


{% mathjax() %}
$$
Dq(t) = \partial_0 F(t, q'(t)) + \partial_1 F(t, q'(t)) Dq'(t) \\
\\
\text{where } \partial_0 F(t, q'(t)) \text{ is the time derivative of } F(t, q'(t)) \\
\text{ and } \partial_1 F(t, q'(t)) \text{ is the Jacobian of F w.r.t q'}
$$
{% end %}




Therefore the generalized velocity transforms as:


{% mathjax() %}
$$
v = \partial_0 F(t, x') + \partial_1 F(t, x') v'\\
$$
{% end %}




If our local tuples have higher-derivative components,


{% mathjax() %}
$$
\begin{align}
(t, x, v, ... ) &= C(t, x', v', ...) \\
                &= (t, F(t' x'), \partial_0 F(t, x') + \partial_1 F(t, x') v', ...)
\end{align}
$$
{% end %}




#### Note

> $L' = L \circ C$ and $C$ converts from **primed** to **unprimed**. Therefore, the coordinate conversion function from  **primed** to **unprimed** is used to create the conversion from **unprimed** to **primed** Lagrangian. There is sort of an opposite thing going on here.
