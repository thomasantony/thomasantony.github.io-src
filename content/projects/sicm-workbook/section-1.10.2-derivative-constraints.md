+++
title = "Section 1.10.2: Derivative Constraints"
date = "2022-10-29T19:41:05Z"
draft = false

[extra]
latex = true
+++





## 1.10.2 Derivative Constraints



In this section we look at a specific type of velocity-dependent constraints, which are "total-time derivatives" of a velocity independent function. The methods in [Section 1.10.1](/projects/sicm-workbook/sicm-1.10.1-coordinate-constraints) do not apply here as the constraint is velocity-dependent.

Let this constraint $\psi = 0$ be a velocity-dependent constraint. If $\psi$ is a total-time derivative, this means that there exists some *velocity-independent* function, $\varphi$ such that:


{% mathjax() %}
$$
\psi \circ \Gamma[q] = D(\varphi \circ \Gamma[q])
$$
{% end %}




Since $\varphi$ is velocity independant, $\partial_2 \varphi = 0$. The relationship between $\psi$ and $\varphi$ can be restated (as local-tuple functions) as:


{% mathjax() %}
$$
\psi = D_t \varphi = \partial_0 \varphi + \partial_1 \varphi \dot{Q}\tag{1.214}
$$
{% end %}




We can find $\psi$ by solving this PDE. The constraint is defined as $\psi = 0$. This implies that $\varphi = K$ for some constant $K$. Conversely, if we know that $\varphi = K$, then $\psi = 0$ follows. **Thus, the velocity-dependent constraint, $\psi = 0$ is equivalent to the velocity-independent constraint, $\varphi = K$**. 

If $L$ is the unconstrained Lagrangian, the Lagrange equations with the constraint $\varphi = K$ are:


{% mathjax() %}
$$
\mathscr{E}[L] \circ \Gamma[q] + \lambda(\mathscr{E}[\varphi] \circ \Gamma[q]) = 0\\
$$
{% end %}




where $\lambda$ is a function of time that will be eliminated during the solution process. $K$ can be ignored here as $\lambda(\varphi - K)$ and $\lambda(\varphi)$ result in the same Lagrange equations. The function $\varphi$ is independent of velocity and $\partial_2 \varphi = 0$. So we can use the same techniques from Section 1.10.1 to get the Lagrange equations for the system as:


{% mathjax() %}
$$
\mathscr{E}[L] \circ \Gamma[q] - \lambda(\partial_1 \varphi \circ \Gamma[q]) = 0\\
$$
{% end %}




From Eq. 1.214, we can also infer that $\psi$ is the partial of $\varphi$ w.r.t velocity, or $\partial_2 \psi = \partial_1 \varphi$. Therefore, the Lagrange equations with the constraint $\psi = 0$ can also be written as:


{% mathjax() %}
$$
\mathscr{E}[L] \circ \Gamma[q] - \lambda(\partial_2 \psi \circ \Gamma[q]) = 0\tag{1.218}
$$
{% end %}




This is important because it shows that we can write the Lagrangian in terms of $\psi$ without having to compute $\varphi$, *as long as we can show that $\varphi$ exists*. 

We can also get the same result using the Augmetned Lagrangian technique. Consider the augmented Lagrangian below 


{% mathjax() %}
$$
L' = L + \lambda' \psi\\
$$
{% end %}




The Lagrange equations for $L'$ are:


{% mathjax() %}
$$
\mathscr{E}[L'] \circ \Gamma[q] = -D\lambda (\partial_2 \varphi \circ \Gamma[q]) \tag{1.218}
$$
{% end %}




where $D\lambda' = \lambda$. This shows that Eq. 1.218 and Eq. 1.219 are the same equations.

The technique defined in this section can be used for systems with constraints that can be written in terms of the derivative of a *velocity-independent constraint*. Such constraints are called *integrable constraints*. Any system where the constraints are coordinate constraints, or can be put in the form of a coordinate constraint are called **holonomic constraints**.



### Goldstein's Hoop

$$\require{cancel}$$

![Figure 1.10](/images/projects/sicm-workbook/figure-1.10.jpg)

**Figure 1.10: A massive hoop rolling, without slipping, down an inclined plane.**

"Goldstein's hoop" is an example of a dynamic system with an integrable constraint: a hoop of mass $M$ and radius $R$ rolling down a one-dimensional inclined plane (Figure 1.10). This problem can be formulated in terms of two coordinates, $\varphi$, the angular displacement of an arbitrary point on the hoop from some arbitrary reference line, and $x$, the linear progress of the center of the hoop down the plane. The cojnstraint is that the hoop rolls without slipping, or in other words, the change is $\theta$ is directly reflected a change in $x$. The constraint function is:


{% mathjax() %}
$$
\psi(t; x,\theta; \dot{x},\dot{\varphi}) = R\dot{\theta} - \dot{x} = 0\\
$$
{% end %}




This constraint is represented as a relation between generalized velocities, which can be integrated to get $x = R\theta + c$. This integrated constraint is a velocity-independent constraint. The augmented Lagrangian can be formulated in terms of the original constraint or its derivative.

The kinetic energy consists of the energy of rotation of the hoop (described later in Chapter 2 as $\frac{1}{2}MR^2\dot{\theta}^2$) and the energy from the motion of its center of mass. The potential energy of the system decreses as the hoop proceeds down the slope. Thus the augmented Lagrangian is:


{% mathjax() %}
$$
L(t; x,\theta,\lambda; \dot{x},\dot{\theta},\dot{\lambda}) = \frac{1}{2}MR^2\dot{\theta}^2 + \frac{1}{2}M\dot{x}^2 - (-Mg x\sin\varphi) + \lambda(R\dot{\theta} - \dot{x})\tag{1.122}
$$
{% end %}




Lagrange equations for this Lagrangian can be obtained as:

{% mathjax() %}
$$
\begin{align*}
M D^2x - D\lambda &= Mg \sin\varphi \tag{1.223}\\
M R^2 D^2\theta + R D\lambda &= 0 \tag{1.224}\\
R D\theta - Dx &= 0 \tag{1.225}\\
\end{align*}
$$
{% end %}



Differentiating the third equation, we get 

{% mathjax() %}
$$
R D^2\theta = D^2 x\tag{1.226}
$$
{% end %}



Multiplying Eq. 1.223 by R and adding with Rq. 1.224

{% mathjax() %}
$$
\begin{align*}
0 &= M R D^2x - \cancel{RD\lambda} - M R g \sin\varphi
 + M R^2 D^2\theta + \cancel{R D\lambda} \\
 &= \cancel{M} \cancel{R} D^2x - \cancel{M} \cancel{R} g \sin\varphi + \cancel{M} R^\cancel{2} D^2\theta \\
 &= D^2x + R D^2\theta - g \sin\varphi \\
 &= 2 D^2x - g\sin\varphi \\
=> D^2x &= -\frac{1}{2}g\sin\varphi \tag{1.227}
\end{align*}
$$
{% end %}



This acceleration is just half of what the acceleration would have been for a point mass sliding down a frictionless inclied plane. Also notable is that the acceleration is independent of both $M$ and $R$. From the Lagrange equations, $D\lambda$ can be interepreted as the frictional force that is causing the hoop to roll instead of slide. Combining Eq. 1.223 and Eq. 1.227, this force can be found to be:

{% mathjax() %}
$$
D\lambda = \frac{1}{2} Mg \sin\varphi\tag{1.228}
$$
{% end %}



and the angular acceleration $D^2\theta$ is:

{% mathjax() %}
$$
-\frac{1}{2}\frac{g}{R}\sin\varphi\tag{1.229}
$$
{% end %}


