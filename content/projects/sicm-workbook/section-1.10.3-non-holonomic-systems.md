+++
title = "Section 1.10.3: Non-holonomic Constraints"
date = "2022-10-29T20:57:43Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++





## 1.10.3 Non-holonomic Systems



Systems with constraints that are no integrable are called *non-holonomic systems*. A constraint is considered to be non-integrable if it cannot be written in terms of an equivalent coordinate constraint. One example of this is a ball rolling without slipping in a bowl, or any 2D surface. The ball may return to the same spot in the bowl, but its orientation when it gets there is entirely dependent on the path that it took to get there and may be completely different. So the constraint cannot be used to eliminate any coordinates.

There is no general solution for equations of motion governing nonholonomic systems. Her we can look at a restricted set of nonholonomic systems with constraints that are linear in velocities, i.e.

{% mathjax() %}
$$
\psi(t, q, v) = G_1(t,q)v + G_0(t,q)\tag{1.230}
$$
{% end %}



We assume that $\psi$ is not a total time derivative. Based on some of the references in the book, if $L$ is the Lagrangian for the unconstrained system, the equations of motions are asserted to be:

{% mathjax() %}
$$
\mathscr{E}[L] \circ \Gamma[q] = \lambda(G_1 \circ \Gamma[q]) = \lambda(\partial_2 \psi \circ \Gamma[q]) \tag{1.231}
$$
{% end %}



With $\psi = 0$, the system is completely specified and the evolution of its dynamics is defined. While Eq.1.231 is identical to Eq. 1.218 from the [previous section](/projects/sicm-workbook/section-1.10.2-derivative-constraints), the derivation does not apply here since the assumptions made there do not hold. 

Eq. 1.185 in [Section 1.10](/projects/sicm-workbook/section-1.10-constrained-motion) defines the condition that the variation $\eta$ must satisfy in order for it to be consistent with the velocity-dependent constraint function $\psi$. It is restated here:

{% mathjax() %}
$$
(\partial_1 \psi \circ \Gamma[q])\eta + (\partial_2 \psi \circ \Gamma[q])D\eta = 0\tag{1.185}
$$
{% end %}



We can no longer eliminate $\eta$ by the logic used in Section 1.10.1, because $\eta$ is no longer orthogonal to $\partial_1 \psi \circ \Gamma[q]$ and we cannot rewrite the constraint as a coordinate constraint because it is not integrable by assumption.

The following derivation for of the nonholonomic equations is from Arnold et.al[6]. We define a "virtual velocity", $\xi$ to be any velocity satisfying the following condition:

{% mathjax() %}
$$
(\partial_2 \psi \circ \Gamma[q])\xi = 0\tag{1.236}
$$
{% end %}



The "principle of d'Alembert–Lagrange" states that:

{% mathjax() %}
$$
(\mathscr{E}[L] \psi \circ \Gamma[q])\xi = 0\tag{1.237}
$$
{% end %}


for any virtual velocity, $\xi$. This could also be restated as "any virtual velocity $\xi$ is orthogonal to $\mathscr{E}[L] \psi \circ \Gamma[q]$. We picked $\xi$ to be arbitrary except that it be orthogonal to $\partial_2 \psi \circ \Gamma[q]$. Therefore, $\partial_2 \psi \circ \Gamma[q]$ must be parallel to $\mathscr{E}[L] \psi \circ \Gamma[q]$. So,


{% mathjax() %}
$$
\mathscr{E}[L] \circ \Gamma[q] = \lambda(\partial_2 \psi \circ \Gamma[q]) \tag{1.238}
$$
{% end %}



which are the non-holonomic equations. 

The basic idea at the end is that the nonholonomic equations do not follow from the action principle. To quote the book:

> It comes down to this: the nonholonomic equations do not follow from the action principle. They are something else. Whether they are correct or not depends on whether or not they agree with experiment.

In the previous sections, we showed how for systems with coordinate constraints or derivative constraints, the Lagrange equations can be derived from a Lagrangian that is augmented with the constraint. However, if we apply the same technique with non-holonomic constraints, the Lagrange equations obtained are not the same as Eq. 1.238 (or 1.231). For example, consider the following augmented Lagrangian:


{% mathjax() %}
$$
L['(t; q,\lambda; \dot{q},\dot{\lambda})=L(t,q,\dot{q})+\lambda\psi(t,q,\dot{q}) \tag{1.239}
$$
{% end %}



The Lagrange equations associated with the coordinates are found to be:

{% mathjax() %}
$$
\begin{align*}
0 &= \mathscr{E}[L]\circ\Gamma[q] \\
  &\quad + D\lambda(\partial_2 \psi \circ \Gamma[q]) + \lambda D (\partial_2 \psi \circ \Gamma[q]) - \lambda(\partial_1 \psi \circ \Gamma[q]) \tag{1.240}
\end{align*}
$$
{% end %}



The Lagrange equation associated with tthe constraint is the constraint equation: $\psi\circ\Gamma[q] = 0$. The equations here involve both $\lambda$ and $D\lambda$. The usual state variables, $q$ and $Dq$ and the constraint are not enough to completely specify the initial conditions for the dynamic system. We need to specify an initial value for $\lambda$ as well (and possibly integrate it along with the states?). This reminds me of the Euler-Lagrange equations as applied to optimal control problems were we have a "costate" $\lambda$ that is integrated along with the states. 

> In general, for any particular physical system, equations (1.231) and (1.240) are not the same, and in fact they have different solutions. It is not apparent that either set of equations accurately models the physical system.  The first approach to nonholonomic systems is not justified by extension of the arguments for the holonomic case and the other is not fully determined. Perhaps this indicates that the models are inadequate, that more details of how the constraints are maintained need to be specified.



[6] V. I. Arnold, V. V. Kozlov, and A. I. Neishtadt, “Mathematical Aspects of Classical and Celestial Mechanics,” Dynamical Systems III, Springer Verlag, 1988.
