+++
title = "Section 1.8.5: Noether's Theorem"
date = 2019-10-22
draft = false

[extra]
latex = true
+++

**Note**:
***I will be cleaning up this section further and adding an example (or two) later***


If a dynamical system has a symmetry, a coordinate system can be chosen so that the Lagrangian does not depend on a coordinate associated with the symmetry. There is also a conserved quantity associated with the symmetry ([Section 1.8](https://tgvaughan.github.io/sicm/chapter001.html#h1-6c
)). However, there are general symmetries that no coordinate systems can fully express. For examplem, motion around a central potential is spherically symmetric, i.e., the dynamical system is invariant under rotation about any axis. However, the Lagrangian for this system only demonstrates symmetry about a single axis. 

In general, **a Lagrangian is said to have a symmetry if there exists a coordinate transformation that leaves the Lagrangian unchanged**.
In this section we consider the more general case of **continous symmetries**. A **continuous symmetry** is defined as a parametric family of symmetries. **Emmy Noether proved that for any continuous symmetry, there is a conserved quantity**.

Consider a parametric coordinate transformation, $\widetilde{F}$ with parameter $s$. This means that $\widetilde{F}$ represents an infinite number of coordinate transformations, one for each value of $s$. 

An example would be a function that takes an angle, $s$, as the input and spits out a coordinate transformation that rotates the primed coordinate frame, $x'$ about some axis by that angle.

{% mathjax() %}
$$
x = \widetilde{F}(s) (t, x')
$$
{% end %}

There is a corresponding parametreic state transformation $\widetilde{C}$ associated with $\widetilde{F}$ that transforms the velocity $v'$ as well the time (i.e. the local tuple that forms the input to the Lagrangian).

{% mathjax() %}
$$
\begin{align*}
(t, x, v) &= \widetilde{C}(s) (t, x', v') \\
          &= (t, \widetilde{F}(t,x'),  \partial_0 \widetilde{F} + \partial_1 \widetilde{F} v', ...)
\end{align*}
$$
{% end %}

We require that $\widetilde{F}(0)$ represent the identity transformation $x' = \widetilde{F}(0)(t, x')$, with $\widetilde{C}$ as the corresponding identity state transformation. If the Lagrangian $L$ has a continous symmetry corresponding to $\widetilde{F}$, then the Lagrangian should be unchanged when the coordinates are transformed using $\widetilde{F}$. Therefore:

{% mathjax() %}
$$
\widetilde{L}(s) = L\cdot \widetilde{C}(s) = L\quad\text{for any }s
$$
{% end %}

Expanding $\widetilde{C}$ in the above expression, we get:

{% mathjax() %}
$$
\widetilde{L}(s) = L\left(t,\quad\widetilde{F}(s)(t, x'),\quad\partial_1\widetilde{F}(s)(t, x')v' \right)\\
$$
{% end %}

Undoing the "chainrule" in the second term and writing it in terms of the total time derivative,
{% mathjax() %}
$$
\widetilde{L}(s) = L\left(t,\quad\widetilde{F}(s)(t, x'),\quad D_t\widetilde{F}(s)(t, x', v') \right) 
$$
{% end %}

**Note: One of the assumptions in the following derivation is that $\partial_0 L = \frac{\partial L}{\partial t} = 0$**

That $\widetilde{L}(s) = L$ for any $s$ implies that $D\widetilde{L}(s) = 0$ (where the $D$ operator represents derivative w.r.t $s$). Therefore, applying the chain rule for each of the components of $\widetilde{L}$, the derivative of $\widetilde{L}$ w.r.t $s$ is:


{% mathjax() %}
$$
\begin{align*}
0 &= D\widetilde({L}(s)(t, x', v'))\\
  &= \underbrace{\partial_0 L}_{=\frac{\partial L}{\partial t} = 0} + \partial_1 L(t, x, v) (D\widetilde{F})(s)(t, x') + \underbrace{\partial_2 L(t,x,v) D(D_t\widetilde{F}(s)(t, x')}_{\text{can swap }D_t\text{ and }D\text{, as }D\text{ w.r.t }s\text{ is unstructured}} \\
  &= \partial_1 L(t, x, v) (D\widetilde{F})(s)(t, x') + \partial_2 L(t,x,v) D_t(D\widetilde{F}(s))(t, x') \\ 
  &= (\partial_1 L \circ \Gamma[q]) \left( (D\widetilde{F})(s) \circ \Gamma[q']\right) + (\partial_2 L \circ \Gamma[q])\left( D_t(D\widetilde{F}(s)) \circ \Gamma[q']\right) \tag{1.157}
\end{align*}
$$
{% end %}

According to Lagrange equations, the first term of Eq. 1.157 is: $(\partial_1 L \circ \Gamma[q]) \left( (D\widetilde{F})(s) \circ \Gamma[q']\right) = (D_t\partial_2 L \circ \Gamma[q]) \left(D\widetilde{F})(s) \circ \Gamma[q']\right)$. Substituting this in Eq. 1.157,

{% mathjax() %}
$$
0 = (D_t \partial_2 L \circ \Gamma[q])\left( (D\widetilde{F}(s)) \circ \Gamma[q']\right) +  (\partial_2 L \circ \Gamma[q])\left( D_t(D\widetilde{F}(s)) \circ \Gamma[q']\right) \tag{1.159}
$$
{% end %}

When $s = 0$, since $\widetilde{F}(0)$ is the identity transformation, the paths $q$ and $q'$ are the same. Therefore, $\Gamma[q] = \Gamma[q']$ and Eq. 1.158 becomes

{% mathjax() %}
$$
\begin{align}
0 &= \left ((D_t \partial_2 L)(D\widetilde{F}(0)) +  (\partial_2 L)(D_t(D\widetilde{F}(0)))\right) \circ \Gamma[q] \\
  &= D_t ((\partial_2 L) (D\widetilde{F}(0))) \circ \Gamma[q] \tag{1.160}
\end{align}
$$
{% end %}

Therefore the state function $\mathscr{I}$:

{% mathjax() %}
$$
\mathscr{I} = (\partial_2 L) (D\widetilde{F}(0))
$$
{% end %}

is conserved along all solution trajectories. This quantity is called the ***Noether integral***. It is the product of the momentum $\partial_2 L$ and a vector associated with the symmetry.
