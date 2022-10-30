+++
title = "Section 2.1: Rotational Kinetic Energy"
date = "2022-10-30T04:42:17Z"
draft = false

[extra]
latex = true
+++







## 2 Rigid Bodies



> The polhode rolls without slipping on the herpolhode lying in the invariable plane.
>
> Herbert Goldstein, *Classical Mechanics*, footnote, p. 207.


* A rotating top - an axisymmetric body subject to gravity, with a point on the axis of symmetry that is fixed in space
    - The axis of the top precesses about the vertical, apparently moving perpendicular to the direction in which gravity is pulling it
  
* Book thrown into the air - has two stable configurations about longest and shortest axes. Starts tumbling when rotated about intermediate axis

* The Moon always points the same face towards the Earth regardless of the interactions with the Sun and other planets

* A rigid body can be thought to consist of a large number of constituent particles with rigid constraints among them. While the dynamics are the same as any other rigidly constrained system, new tools are needed as the number of particles/constraints are very high.

* We need to define the kinetic and potential energies to define the Lagrangian for a system
    - The strategy is to first rewrite the kinetic and potential energies in terms of quantities that characterize essential aspects of the distribution of mass in the body and the state of motion of the body

* For rotational kinetic energy, a small number of parameters completely specify the state of motion and the relevant aspects of the distribution of mass in the body

* For potential energy, some specific problems the potential energy can be represented with a small number of parameters, but in general we have to make approximations to obtain a representation with a manageable number of parameters



## 2.1 Rotational Kinetic Energy



A rigid body can be considered to consist of a large number of particles with mass $m_\alpha$, $\vec{x_\alpha}$, and velocities $\dot{\vec{x}}_\alpha$ with positional constraints between them. The kinetic energy is:


{% mathjax() %}
$$
\sum_{\alpha} \frac{1}{2} m_\alpha\dot{\vec{x}}_\alpha \cdot \dot{\vec{x}}_\alpha\\
$$
{% end %}




The configuration of a rigid body is fully specified by the position of *any* point inthe body and the orientation of the body. Therefore, we define the position vectors based on a reference point on the body $X$. The position of each particle relative to the reference point can be represented by $\xi_\alpha$:


{% mathjax() %}
$$
\vec{x}_\alpha = \vec{X} + \vec{\xi}_\alpha\tag{2.2}
$$
{% end %}




The corresponding velocities are given by:


{% mathjax() %}
$$
\dot{\vec{x}}_\alpha = \dot{\vec{X}} + \dot{\vec{\xi}}_\alpha\tag{2.3}
$$
{% end %}




The kinetic energy of the body can be rewritten as:


{% mathjax() %}
$$
\begin{align*}
\sum_{\alpha} \frac{1}{2} & m_\alpha  (\vec{X} + \vec{\xi}_\alpha) \cdot (\vec{X} + \vec{\xi}_\alpha) \\
        &= \sum_{\alpha} \frac{1}{2} m_\alpha  (\vec{X} \cdot \vec{X} + \vec{X} \cdot \vec{\xi}_\alpha  + \vec{\xi}_\alpha\cdot\vec{\xi}_\alpha)\tag{2.4}
\end{align*}
$$
{% end %}




If we choose the center of mass of the body as the reference point,


{% mathjax() %}
$$
\vec{X} = \frac{1}{M}  \sum_{\alpha} m_\alpha\vec{x}_\alpha\\
$$
{% end %}




where $M = \sum_\alpha m_\alpha$ is the total mass of the body, then


{% mathjax() %}
$$
\sum_{\alpha} m_\alpha\vec{\xi_\alpha} = \sum_\alpha m_\alpha (\vec{x}_\alpha - \vec{X})\tag{2.6}
$$
{% end %}




Taking the derivative of this, we can see that the relative velocities satisfy $\sum_\alpha m_\alpha \dot{\xi}_\alpha = 0$. So the kinetic energy is equal to:


{% mathjax() %}
$$
\begin{align*}
T &= \frac{1}{2} \left(\sum_{\alpha} m_\alpha \dot{\vec{X}} \cdot \dot{\vec{X}} + \sum_{\alpha} m_\alpha \dot{\vec{X}} \cdot \vec{\xi}_\alpha  + \sum_{\alpha} m_\alpha \dot{\vec{\xi}}_\alpha\cdot\dot{\vec{\xi}}_\alpha\right) \\
  &= \frac{1}{2} \left(\sum_{\alpha} m_\alpha \dot{\vec{X}} \cdot \dot{\vec{X}} + \dot{\vec{X}} \sum_{\alpha} \underbrace{m_\alpha \dot{\vec{\xi}}_\alpha}_{= 0} + \sum_{\alpha} m_\alpha \dot{\vec{\xi}}_\alpha\cdot\dot{\vec{\xi}}_\alpha\right)\\
  &= \frac{1}{2} \sum_{\alpha} m_\alpha \dot{\vec{X}} \cdot \dot{\vec{X}} + \frac{1}{2} \sum_{\alpha} m_\alpha \dot{\vec{\xi}}_\alpha \cdot \dot{\vec{\xi}}_\alpha\tag{2.8}
\end{align*}
$$
{% end %}




This shows that kinetic energy of the rigid body can be separated into two pieces. The translational kinetic energy is:


{% mathjax() %}
$$
\frac{1}{2} \sum_{\alpha} m_\alpha \dot{\vec{X}} \cdot \dot{\vec{X}}\tag{2.9}
$$
{% end %}




The rotational kinetic energy is:

{% mathjax() %}
$$
\frac{1}{2} \sum_{\alpha} m_\alpha \dot{\vec{\xi}}_\alpha \cdot \dot{\vec{\xi}}_\alpha\tag{2.10}
$$
{% end %}




When written in appropriate generalized coordinates, the kinetic energy is a Lagrangian for a free rigid body. Choosing generalized coordinates such that the coordinates specifying the position of the center of mass is separate from those specifying the orientation, then the Lagrange equations completely decouple. This makes the dynamics of translation decoupled from that of translation.

However, this is not true in the general case once potential energies are included in the system. So the motion of the center of mass and the rigid body may be coupled through the potential energy. However, in some specific cases, such as for example, a rigid body moving in a uniform gravitational field, the equations may decouple.
