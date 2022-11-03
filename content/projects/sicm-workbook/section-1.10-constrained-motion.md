+++
title = "Section 1.10 : Constrained Motion"
date = "2022-10-28T01:12:02Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++





## 1.10 Constrained Motion



When using the Lagrangian method, we may choose the coordinate system that is the most convenient - the number of coordinates may match exactly with the number of degrees of freedom of the system, or we may pick a system that has redundant coordinates along with explicit constraints among coordinates. As an example, a pendulum can be modeled using just the angle of the pendulum from the vertical, or as a point mass with a constraint stating that it should stay a constant distance from the pivot point. The constraints described in this section are more general than the ones developed in [Section 1.6.2](https://tgvaughan.github.io/sicm/chapter001.html#h3_1-6-2).

Consider a dynamic system with $n$ degrees of freedom, specified by $n+1$ coordinates, along with a path constraint of the form:

{% mathjax() %}
$$
\varphi(t, q(t), Dq(t)) = 0
$$

In order to formulate the equations of motion, one approach would be to use the constraint equation to eliminate one of the coordinates, and then use the resulting irredundant coordinates to develop Lagrange's Equations. Any equations developed using redundant coordinates with constraints should be equivalent.

In order to do this, consider the method used originally for deriving Lagrange's equations. Realizable paths were those that had a stationary "action" compared to nearby paths. "Stationary" here means that the action does not change for small changes in the path. We considering constrained motion, these varied paths must also satisfy the constraints. This has some effects on the derivation of Lagrange's equations. Regardless of the method used, the condition for stationary action condenses to the following form (Eq. [1.17](https://tgvaughan.github.io/sicm/chapter001.html#disp_1.17) or Eq. [1.34](https://tgvaughan.github.io/sicm/chapter001.html#disp_1.34)):

{% mathjax() %}
$$
0 = \int_{t_0}^{t_f} \{ (\partial_1 L \circ \Gamma[q]) - D\left( \partial_2 L \circ \Gamma[q] \right) \} \eta \tag{1.182}
$$
{% end %}



where $\eta$ is the variation in the path. In the unconstrained case, we may have arbitrary variations and so the only way for Eq.1.182 to be satisfied was for the integrand to be zero. Furthermore, since $\eta$ can be arbitrarily chosen, the term multiplying with $\eta$ must be zero for the action to be stationary, thereby getting to Lagrange's equations. 

Once we add in constraints, $\eta$ can no longer be arbitrarily chosen. While the intgrand must still be zero for Eq. 1.182 to be satisfied, we can no loner conclude that the factor multiplying $\eta$ must be zero. Therefore,

{% mathjax() %}
$$
\{ (\partial_1 L \circ \Gamma[q]) - D\left( \partial_2 L \circ \Gamma[q] \right) \} \eta  = 0 \tag{1.183}
$$
{% end %}


with $\eta$ subject to the constraints of the dynamic system.

A path $q$ satisfies the constraint if $\bar{\varphi}[q] = \varphi \circ \Gamma[q] = 0$. Since we only allow varied paths that satisfy the constraint, the variation of the constraint must be zero:

{% mathjax() %}
$$
\delta_\eta(\bar{\varphi}) = 0 \tag{1.184}
$$
{% end %}



> The variation must be "tangent" to the constraint surface

Expanding Eq. 1.184 with the chain rule (Eq. [1.26](https://tgvaughan.github.io/sicm/chapter001.html#disp_1.26)) and the definition $\delta_\eta \Gamma[q](t) = (0,\eta(t),D\eta(t))$ ([Eq. 1.31](https://tgvaughan.github.io/sicm/chapter001.html#disp_1.31)), the variation is tangent to the constraint surface if:

{% mathjax() %}
$$
\begin{align*}
\delta_\eta(\bar{\varphi}) &= \delta_\eta( \varphi \circ \Gamma[q]) \\
   &= (D\varphi \circ \Gamma[q]) \delta_\eta\Gamma[q] \\
   &= \left(\partial_0 \varphi \circ \Gamma[q], \partial_1 \varphi \circ \Gamma[q], \partial_2 \varphi \circ \Gamma[q]\right) \cdot [0, \eta, D\eta] \\
   &= (\partial_1 \varphi \circ \Gamma[q])\eta + (\partial_2 \varphi \circ \Gamma[q])D\eta = 0\tag{1.185}
\end{align*}
$$
{% end %}



These are functions of time, so the variation at a given time is tangent to the constraint surface at that time.
