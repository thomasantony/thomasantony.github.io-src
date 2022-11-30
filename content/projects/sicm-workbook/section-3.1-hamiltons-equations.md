+++
title = "Section 3.1 : Hamilton's Equations"
date = "2022-11-30T07:18:48Z"
draft = false

[extra]
latex = true
chapter = "3"
page_type = "note"
+++







# 3 Hamiltonian Mechanics



> Numerical experiments are just what their name implies: experiments. In describing and evaluating them, one should enter the state of mind of the experimental physicist, rather than that of the mathematician. Numerical experiments cannot be used to prove theorems; but, from the physicist's point of view, they do often provide convincing evidence for the existence of a phenomenon. We will therefore follow an informal, descriptive and non-rigorous approach. Briefly stated, our aim will be to understand the fundamental properties of dynamical systems rather than to prove them.
> ~ Michel Hénon, “Numerical Exploration of Hamiltonian Systems,” in Chaotic Behavior of Deterministic Systems [21], p. 57.


* The formulation of mechanics with generalized coordinates and momenta as the dynamic state variables is called the Hamiltonian formulation. This is equivalent to the Lagrangian formulation, but present a differnet point of view. It is especially useful for understanding the evolution of a system, especially when there are symmetries and conserved quantities

* In systems with symmetries, the conjugate momenta of "cyclic coordinates" (which do not appear in the Lagrangian) are conserved. This insight can be used to simplify and solve many problems in dynamics (e.g. spinning top). The Hamiltonian formulation is motivated by the desire to focus attention on the momenta.

* In the Lagrangian formulation, the momenta are "secondary" quantities -- they are functions of state variables and the evolution of these state variables only depend on the state variables themselves and not the momenta. Since the momenta can be inferred form velocities, it is possible to represent the dynamics in terms of coordinates and momenta. In such a formulation, if a momentum is conserved, it is immediately apparent from its dynamic equation.

* Mechanical systems can exhibit simple or complex behavior - periodic motion, chaotic motion etc. Sometimes the periodicity may be driven by an external force. **The Hamiltonian formulation of dynamics provides a convenient framework in which the possible motions may be placed and understood. We will be able to see the range of stable resonance motions and the range of states reached by chaotic trajectories, and discover other unsuspected possible motions.**



## 3.1 Hamilton's Equations

$\require{cancel}$


Restricting our attention to Lagrangians that only depend onf time, coordinates and velocities, the momenta in a system can be represented as functions of coordinates, velocities and time. It is possible to invert these functions to get a local representation of velocity in terms of time, coordinates and momenta. The equations of motion when recast in terms of coordinates and momenta are called **Hamilton's canonical equations**. We will look at three derivations of these equations: 

* The first strategy is an expansion of the one described in the above paragraph - starting with  inverting the momentum state function.

* The second derivation in Section 3.1.1 first abstracts a key part of the first derivation and then applies the more abstract machinery to derive Hamilton's equations. The third (section 3.1.2) uses the action principle.


The equations for the time derivative of a momentum can be found from Lagrange's equations as:


{% mathjax() %}
$$
D{p}(t) = \partial_1 L(t, q(t),D{q}(t))\tag{3.1}
$$
{% end %}




where (by definition of generalized momenta),


{% mathjax() %}
$$
p(t) = \partial_2 L(t, q(t), Dq(t))\tag{3.2}
$$
{% end %}




To eliminate $Dq(t)$ from Eq. 3.1, we need to invert Eq.3.2. To avoid confusion, we will do this by assigning simple variable names to the function arguments and its output. If Eq.3.1 is restated as:


{% mathjax() %}
$$
a = \partial_2 L (b, c, d)\tag{3.3}
$$
{% end %}




Then the equation can be inverted in terms of the third argument to get the new function $\mathscr{V}$ so that:


{% mathjax() %}
$$
d = \mathscr{V}(b, c, a)\tag{3.4}
$$
{% end %}




Substituting $a$ from Eq. 3.3 in 3.4 (and $d$ in Eq. 3.3), 


{% mathjax() %}
$$
\begin{align*}
d = \mathscr{V}(b, c, \partial_2 L(b, c, d))\tag{3.5}\\
a = \partial_2 L(b, c, \mathscr{V}(b, c, a))\tag{3.6}\\
\end{align*}
$$
{% end %}




THis pattern can be applied to Eq. 3.1 to get:


{% mathjax() %}
$$
Dp(t) = \partial_1 L (t, q(t), \mathscr{V}(t, q(t), p(t)))\tag{3.7}
$$
{% end %}




Similarly, Eq. 3.2 can be inverted to get:


{% mathjax() %}
$$
Dq(t) = \mathscr{V}(t, q(t), \partial_1 L(t, q(t), Dq(t))\tag{3.8}
$$
{% end %}




Equations 3.7 and 3.8 give dynamic equations for $q$ and $p$ as functions of time, coordinates and momenta. To represent this better, we can define a new Lagrangian as a function of time, coordinates and momenta.


{% mathjax() %}
$$
\widetilde{L}(t, q, p) = L(t, q, \mathscr{V}(t, q, p))
$$
{% end %}




> Here we are using mnemonic names t, q, p for formal parameters of the function being defined. We could have used names like a, b, c as above, but this would have made the argument harder to read.


To get the equations of motion, we need to compute $\partial_1 L$ (applying the chain rule, assuming that $L$ is not an explicit function of time):


{% mathjax() %}
$$
\begin{align*}
\partial_1 \widetilde{L}(t, q, \mathscr{V}(t, q, p)) &= \partial_1 L (t, q, \mathscr{V}(t, q, p)) + \overbrace{\partial_2 L (t, q, \mathscr{V}(t, q, p))}^{=p~\text{from Eq 3.2}}\partial_1 \mathscr{V}(t, q, p)\\
 &= \partial_1 L (t, q, \mathscr{V}(t, q, p)) + p \partial_1 \mathscr{V}(t, q, p)\tag{3.10}
\end{align*}
$$
{% end %}




We introduce the "momentum selector" function here, $P(t,q,p) = p$ such that $\partial_1 P = 0$ to get,


{% mathjax() %}
$$
\begin{align*}
\partial_1 L (t, q, \mathscr{V}(t, q, p)) &= \partial_1 \widetilde{L}(t, q, p) - p \partial_1 \mathscr{V}(t, q, p)\\
           &= \partial_1 \widetilde{L}(t, q, p) - P(t, q, p)\partial_1 \mathscr{V}(t, q, p)\\
           &= -\partial_1 H(t, q, p)\tag{3.11}
\end{align*}
$$
{% end %}




In Eq. 3.11, $H$ is the *Hamiltonian* defined as:


{% mathjax() %}
$$
H = P\mathscr{V} - \widetilde{L}\tag{3.12}
$$
{% end %}




Substituing Eq. 3.11 in 3.7, we get the dynamic equation for momentum as:


{% mathjax() %}
$$
Dp(t) = -\partial_1 H(t, q(t), p(t))\tag{3.11}
$$
{% end %}




The equation for $Dq(t)$ can also be written in terms of the Hamiltonian as shown below:


{% mathjax() %}
$$
\begin{align*}
\partial_2 H (t, q, p) &= \partial_2 (P\mathscr{V} - \widetilde{L})(t, q, p)\\
           &= \overbrace{\partial_2 P(t, q, p)}^{=1} \mathscr{V}(t, q, p) + \overbrace{P(t, q, p)}^{=p} \partial_2 \mathscr{V}(t, q, p) - \partial_2 \widetilde{L}(t, q, p)\\
           &= \mathscr{V}(t, q, p) + p\partial_2 \mathscr{V}(t, q, p) - \partial_2 \widetilde{L}(t, q, p)\tag{3.14}
\end{align*}
$$
{% end %}




$\partial_2 \widetilde{L}$ can be computed using the chain rule as:


{% mathjax() %}
$$
\begin{align*}
\partial_2 \widetilde{L}(t, q, p) &= \partial_2 \left(L(t, q, \mathscr{V}(t, q, p))\right)\\
    &= \partial_2 L(t, q, \mathscr{V}(t, q, p)) \partial_2 \mathscr{V}(t, q, p)\\
    &= p \partial_2\mathscr{V}(t, q, p)\tag{3.15}
\end{align*}
$$
{% end %}




Eq. 3.14 now reduces to: $\partial_2 H (t, q, \mathscr{V}(t, q, p)) = \mathscr{V}(t, q, p) + \cancel{p\partial_2 \mathscr{V}(t, q, p)} - \cancel{p\partial_2 \mathscr{V}(t, q, p)} = \mathscr{V}(t, q, p)$.  This can be substituted in Eq. 3.8 to get:


{% mathjax() %}
$$
Dq(t) = \partial_2 H (t, q, \mathscr{V}(t, q, p))\tag{3.17}
$$
{% end %}




Equations 3.13 and 3.17 are called *Hamilton's equations*.


{% mathjax() %}
$$
\begin{align*}
Dq(t) &= \partial_2 H (t, q, \mathscr{V}(t, q, p))\\
Dp(t) &= -\partial_1 H(t, q(t), p(t))\tag{3.18}\\
\end{align*}
$$
{% end %}




The first equation in 3.18 is restating the relation between velocity and momenta in terms of the Hamiltonian and applies for all paths regardless of whether they are realizable. The second equation only applies for realizable paths. The Hamiltonian has the same value as the energy function $\mathscr{E}$ from Chapter 1. The only difference is that that the velocities are expressed in terms of time, coordinates, and momenta using $\mathscr{V}$:


{% mathjax() %}
$$
H(t, q, p) = \mathscr{E}(t, q, \mathscr{V}(t,q,p))\tag{3.20}
$$
{% end %}





### Illustration using free particle


The Lagrangian for the motion of a free-particle of mass $m$ is:


{% mathjax() %}
$$
L(t; x,y; v_x,v_y) = \frac{1}{2} m (v_x^2 + v_y^2) - V(x, y)
$$
{% end %}




To compute the Hamiltonian, we first ocmpute the momenta as $p = \partial_2 L; p_x = mv_x; p_y = mv_y$. Solving for velocities, we get,
$v_x = p_x/m, v_y = p_y/m$ (This is the definition of $\mathscr{V}$). The Hamiltonian is $H = pv - L(t,q,v)$ with $v$ expressed in terms of $(t, q, p)$.


{% mathjax() %}
$$
\begin{align*}
H &= p_x\frac{p_x}{m} + p_y\frac{p_y}{m} - L = \frac{p_x^2 + p_y^2}{m} - \frac{1}{2}\frac{p_x^2 + p_y^2}{m} + V(x,y)\\
  &= \frac{p_x^2 + p_y^2}{2m} + V(x, y)
\end{align*}
$$
{% end %}




This is the total energy $T + V$ expressed in terms of the momenta.  Hamilton's equations for $Dq(t)$ are:


{% mathjax() %}
$$
D_x(t) = p_x(t)/m \quad D_y(t) = p_y(t)/m\\
$$
{% end %}




The Hamilton's equations for the momenta are:


{% mathjax() %}
$$
\begin{align*}
Dp_x(t) &= -\partial_{p_x} H = -\partial_0 V(x(t), y(t))\\
Dp_y(t) &= -\partial_{p_y} H = -\partial_1 V(x(t), y(t))
\end{align*}
$$
{% end %}





### Hamiltonian State

Given a coordinate path $q$ and a Lagrangian $L$, the corresponding momentum path $p$ is given by Eq. 3.2. This can also be represented in terms of the Hamiltonian as was shown in the section above. The expression for momntum is valid whether or not the path is realizable, i.e., $p = \partial_2 L(t, q, v)$. In the Lagrangian formulation, $(t, q, v)$ represents the state of the path at a given moment and Lagrange's equations describe a unique path emnating from this state. Similarly, $(t, q, p)$ represents the starte of a path in the Hamiltonian formulation and Hamilton's equations describe a path emnating from this state. The two formulations are equivalent and creates the same path for the a given initial state.

When converting Lagrange equations into first order ODEs (prior to integration), we need to invert $ \partial_2 \partial_2 L$. While Hamilton's equations are already first order ODEs, their construction involves an inversion in the form of the function $\mathscr{V}$. A system that is non-invertible in the Lagrangian formulation remains so in the Hamiltonian formulation as well. 

For any given path, $q$, the Lagrangian and Hamiltonian state paths can be deduced from it. For the Lagrangian formulation, the state path is given by:


{% mathjax() %}
$$
\Gamma[q](t) = (t, q(t), Dq(t))
$$
{% end %}




The construction of the Hamiltonian path requires the definition of a Lagrangian. The Hamiltonian path is given by:


{% mathjax() %}
$$
\Pi_L[q](t) = (t, q(t), \partial_2 L(t, q(t), Dq(t))) = (t, q(t), p(t))
$$
{% end %}




The Hamiltonian state path is not unique for a given path as it is dependent on the Lagrangian that we choose when formulating it. There is no unique choice for the Lagrangian and hence there is no unique Hamiltonian state path for a given path.


> The $2n$-dimensional space whose elements are labeled by the n generalized coordinates $q^i$ and the $n$ generalized momenta $p_i$ is called the *phase space*. The components of the generalized coordinates and momenta are collectively called the *phase-space components*. The dynamical state of the system is completely specified by the phase-space state tuple $(t, q, p)$, given a Lagrangian or Hamiltonian to provide the map between velocities and momenta.



### Computing Hamilton's Equations

```clojure
;; Implementation of Hamilton's Equations
(defn qp->H-state-path [q p]
    (fn [t]
      (up t (q t) (p t))))

(defn my-Hamiltonian->state-derivative [Hamiltonian]
    (fn [H-state]
      (up 1
          (((partial 2) Hamiltonian) H-state)
          (- (((partial 1) Hamiltonian) H-state)))))

(defn my-Hamilton-equations [Hamiltonian]
    (fn [q p]
        (let [state-path (qp->H-state-path q p)]
            (- (D state-path)
               (compose (my-Hamiltonian->state-derivative Hamiltonian)
                state-path)))))
```


    #'user/my-Hamilton-equations



```clojure
;; Free particle Hamtiltonian
(defn H-rectangular [m V]
    (fn [state]
      (let [q (coordinate state)
            p (momentum state)]
            (+ (/ (square p) (* 2 m))
               (V (ref q 0) (ref q 1))))))

(rendermd (let [V (literal-function 'V (-> (X Real Real) Real))
        q (up (literal-function 'x)
               (literal-function 'y))
        p (down (literal-function 'p_x)
                 (literal-function 'p_y))]
    (((Hamilton-equations (H-rectangular 'm V)) q p) 't)))
```


{% mathjax() %}$$
\begin{pmatrix}\displaystyle{0} \cr \cr \displaystyle{\begin{pmatrix}\displaystyle{\frac{m\,Dx\left(t\right) - p_x\left(t\right)}{m}} \cr \cr \displaystyle{\frac{m\,Dy\left(t\right) - p_y\left(t\right)}{m}}\end{pmatrix}} \cr \cr \displaystyle{\begin{bmatrix}\displaystyle{Dp_x\left(t\right) + \partial_0V\left(x\left(t\right), y\left(t\right)\right)} \cr \cr \displaystyle{Dp_y\left(t\right) + \partial_1V\left(x\left(t\right), y\left(t\right)\right)}\end{bmatrix}}\end{pmatrix}
$$
{% end %}





> The zero in the first element of the structure of Hamilton's equation residuals is just the tautology that time advances uniformly: the time function is just the identity, so its derivative is one and the residual is zero. The equations in the second element of the structure relate the coordinate paths and the momentum paths. The equations in the third element give the rate of change of the momenta in terms of the applied forces.
