+++
title = "Section 2.8 : Motion of a Free Rigid Body"
date = "2022-11-07T08:17:06Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++







## 2.8 Motion of a Free Rigid Body



The kinetic energy of a rigid body, expressed in suitable generalized coordinates, is a Lagrangian for its motion. In [section 2.2](/projects/sicm-workbook/section-2-2-kinematics-of-rotation/) we showed that the kinetic energy of a rigid body can be separated into translational and rotational kinetic energy. If we use two separate sets of coordinats to represent the translation and rotation, the Lagrangian becomes the sum of a translational Lagrangian and a rotational Lagrangian. In this section, we will look at the rotational motion of a rigid body, modeled using Euler angles as the generalized coordinates.



### Conserved Quantities

Since the Lagrangian of a rigid body has no explicit time-dependence, we can infer that energy (i.e. kinetic energy) is conserved. The Lagrangian also does not depend on the Euler angle $\varphi$ (since the expressions for the $\omega$ vector did not depend on $\varphi$ in [section 2.7](/projects/sicm-workbook/section-2-7-euler-angles/)), and therefore its momentum conjugate (the component of $\partial_2 L$ corresponding to $\phi$) is conserved. An explicit expression for the momentum conjugate of $\varphi$ is computed as:

```clojure
(def Euler-state
  (up 't
      (up 'theta 'varphi 'psi)
      (up 'thetadot 'varphidot 'psidot)))

(def momentum-phi
  (ref (((partial 2) (rigid/T-rigid-body 'A 'B 'C)) Euler-state)
       1))

(rendermd momentum-phi)
```


{% mathjax() %}$$
A\,\dot {\varphi}\,{\sin}^{2}\left(\psi\right)\,{\sin}^{2}\left(\theta\right) + B\,\dot {\varphi}\,{\sin}^{2}\left(\theta\right)\,{\cos}^{2}\left(\psi\right) + A\,\dot {\theta}\,\sin\left(\psi\right)\,\sin\left(\theta\right)\,\cos\left(\psi\right) - B\,\dot {\theta}\,\sin\left(\psi\right)\,\sin\left(\theta\right)\,\cos\left(\psi\right) + C\,\dot {\varphi}\,{\cos}^{2}\left(\theta\right) + C\,\dot {\psi}\,\cos\left(\theta\right)
$$
{% end %}





Due to the symmetries in the Lagrangian, we know that the quantity described above ($p_\varphi$) is conserved during the motion of a rigid body. 

In the absence of external torques, we would also expect the angular momentum to be conserved. This can be verified by the Lagrangian formulation. The quantity computed above, $p_\varphi$, can be shown to be the $z$ component of the angular momentum. This is verified below:

```clojure
(def L_z (ref ((rigid/Euler-state->L-space 'A 'B 'C) Euler-state)
        2))

(rendermd (- L_z momentum-phi))
```


{% mathjax() %}$$
0
$$
{% end %}





Similar to the case of [motion in a central potential](/projects/sicm-workbook/section-1-8-3-central-forces-in-three-dimensions/), since the choice of coordinate frames is arbitrary, if one rectangular component of $L$ is conserved, then all of its components are conserved. Therefore, **the vector angular momentum is conserved for a rigid body**.

This fact can also be shown using [Noether's theorem](/projects/sicm-workbook/section-1-8-5-noethers-theorem/). There exists a continuous family of rotations that can transform any orientation into any other orientation. The orientation of coordinate axes used to define the Euler angles are arbitrary and the kinetic energy (the Lagrangian) is the same regardless of choice of coordinate system. This meets the requirements of Noether's theorem which tells us that there is an associated conserved quantity.


> In particular, the family of rotations around each coordinate axis gives us conservation of the angular momentum component on that axis. We construct the vector angular momentum by combining these contributions.

See Exercise 2.11 for detailed proof of this (tbd .. will update link once completed).
