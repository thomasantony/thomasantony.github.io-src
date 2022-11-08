+++
title = "Exercise 2.10: Uniformly accelerated rigid body"
date = "2022-11-08T02:34:39Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



### Exercise 2.10: Uniformly accelerated rigid body

**Show that a rigid body subject to a uniform acceleration rotates as a free rigid body, while the center of mass has a parabolic trajectory.**






$$\require{cancel}$$

The kinetic energy of the rigid body is equal to the sum of the translational and rotational kinetic energy ($T_R$).


{% mathjax() %}
$$
T = \frac{1}{2} m \left(\dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) + T_R(q_R)
$$
{% end %}




The potential energy of the body is equal to $V = m g y$ where $m$ is the total mass of the body assuming that the acceleration is acting in the negative $y$ direction. The potential energy here is not dependent on the mass distribution of the body (aka the moments of inertia) as it does not vary with distance (as in the case of a central potential).

If the position of the body is represented by rectangular coordinates $(x, y, z)$ and orientation is being represented by some set of generalized coordinates $q_R$, then the Lagrangian is:


{% mathjax() %}
$$
L(t; x,y,z, q_R; \dot{q},\dot{q_R}) = \frac{1}{2} m \left(\dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) - mgy + T_R(q_R) 
$$


The Lagrangian can be decoupled into terms for translation (the first two terms) and rotation ($T_R(q_R)$). Therefore the Lagrange equations for the system also decouple as:


{% mathjax() %}
$$
D(\partial_2 L) - \partial_1 L = D([mx, my, mz]) - [0, mg, 0] = 0\\
$$
{% end %}




Therefore the translational equations of motion are:


{% mathjax() %}
$$
\begin{bmatrix}\ddot{x}\\
\ddot{y}\\
\ddot{z}\end{bmatrix} = \begin{bmatrix} 0\\ -g \\ 0\end{bmatrix}
$$
{% end %}




Integrating these w.r.t time, we get:


{% mathjax() %}
$$
\begin{align*}
\begin{bmatrix}\dot{x}\\ \dot{y} \\ \dot{z}\end{bmatrix} &= \begin{bmatrix}X_1\\-gt + Y_1 \\ Z_1\end{bmatrix}\\
\implies \begin{bmatrix}x\\y \\ z\end{bmatrix} &= \begin{bmatrix}X_1 t + X_2 \\ -\frac{1}{2}gt^2 + Y_1 t + Y_2 \\ Z_1 t + Z_2\end{bmatrix}
\end{align*}
$$
{% end %}




These equations describe a parabola. 


The motion of the rigid body is given by the Lagrangian, $T_R(q_R)$ which produces the dynamic equations for a free rigid body.
