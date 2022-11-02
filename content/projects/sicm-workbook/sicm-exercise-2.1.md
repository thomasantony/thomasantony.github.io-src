+++
title = "Exercise 2.1: Rotational kinetic energy"
date = "2022-11-02T06:11:12Z"
draft = false

[extra]
latex = true
+++



### Exercise 2.1: Rotational kinetic energy

**Show that the rotational kinetic energy can also be written as:**


{% mathjax() %}
$$
T = \frac{1}{2} I\omega^2\\
$$
{% end %}




**where $I$ is the moment of inertia about the line through the center of mass with direction $\hat{\omega}$ and $\omega$ is the instantaneous rate of rotation.**






$$\require{cancel}$$


Let $\hat{\omega}$ be one of the basis vectors of the coordinate system, $\hat{e_0}$, and with its origin at the center of mass of the body. For a constituent particle in the body, $(\xi_\alpha^1)^2 + (\xi_\alpha^2)^2 = \xi_\alpha^\perp$ will equal to the distance from the particle to the line $\hat{e_0}$ which is the same as the line $\hat{\omega}$. Therefore, the inertia component, $I_{00}$ is:


{% mathjax() %}
$$
\begin{align*}
I_{00} &= \sum_\alpha m_\alpha \left( (\xi_\alpha^1)^2 + (\xi_\alpha^2)^2 \right) \\
       &= \sum_\alpha m_\alpha \left( \xi_\alpha^\perp \right)^2\\
       &= I\\
\end{align*}
$$
{% end %}




where $I$ is the moment of inertia about the line $\hat{\omega}$. Also, by definition, the components of the angular velocity vector, $\vec{\omega}$, are:


{% mathjax() %}
$$
\begin{align*}
\omega^0 &= \omega\\
\omega^1 &= 0\\
\omega^2 &= 0\\
\end{align*}
$$
{% end %}




since we defined $\vec{\omega}$ as being in the direction $\hat{\omega} = \hat{e}_0$. Therefore the kinetic energy is:


{% mathjax() %}
$$
\begin{align*}
T &= \frac{1}{2} \sum_{ij} \omega^i\omega^j I_{ij} \\
  &= \frac{1}{2} \left( \omega^0\omega^0 I_{00} +  \omega^0\cancel{\omega^1} I_{01} + \omega^0 \cancel{\omega^2} I_{02} + ... \right) \\
  &= \frac{1}{2} I_{00} \omega^0 \omega^0
\end{align*}
$$
{% end %}




All the other terms in the expression for $T$ cancel out as the components $\omega^1$ and $\omega^2$ are equal to zero. Therefore,


{% mathjax() %}
$$
T = \frac{1}{2} I (\omega)^2\\
$$
{% end %}


