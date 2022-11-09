+++
title = "Section 2.9: Euler's Equations"
date = "2022-11-09T07:13:05Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++







## 2.9 Euler's Equations



> For a free rigid body we have seen that the components of the angular momentum on the principal axes comprise a self-contained dynamical system: the variation of the principal axis components depends only on the principal axis components. Here we derive equations that govern the evolution of these components.

The components of angular momentum (in column matrix form) on the principal axes are:


{% mathjax() %}
$$
\overline{\mathbf{L}}' = \mathbf{I}'\boldsymbol{\omega}'\\
$$
{% end %}




where $\boldsymbol{\omega}'$ are the angular velocity components on the principal axes and $\mathbf{I}'$ is the diagonal inertia tensor in the principal axes basis:


{% mathjax() %}
$$
\mathbf{I}' = \begin{bmatrix}A & 0 & 0 \\ 0 & B & 0 \\ 0 & 0 & C\end{bmatrix}
$$
{% end %}




If $\mathbf{M}$ is the rotation that rotates all vectorsand the body from the fixed reference frame to the actual orientation, then the components of angualr momentum in the inertial frame $\hat{e}_i$ are:


{% mathjax() %}
$$
\mathbf{L} = \mathbf{M} \mathbf{\overline{L}}
$$
{% end %}




For a free rigid vody, the vector angular momentum and therefore its components in the inertial frame are conserved. Therefore:


{% mathjax() %}
$$
\begin{align*}
D\mathbf{L} = D (\mathbf{M} \mathbf{\overline{L}}') &= D\mathbf{M}\mathbf{\overline{L}}' + \mathbf{M} D\mathbf{\overline{L}'}\\
\implies \mathbf{M} D\mathbf{\overline{L}'} &= -D\mathbf{M}\mathbf{\overline{L}}'\\
D\mathbf{\overline{L}'} &= -\mathbf{M}^{\mathscr{T}} D\mathbf{M}\mathbf{\overline{L}}'\tag{2.65}
\end{align*}
$$
{% end %}




From [section 2.2](/projects/sicm-workbook/section-2-2-kinematics-of-rotation/), we know that the components of the angular velocity can be written as:


{% mathjax() %}
$$
\begin{align*}
\boldsymbol{\omega}' &= \mathbf{M}^\mathscr{T}  \mathscr{A}^{-1}(D \mathbf{M} \mathbf{M}^\mathscr{T}) \tag{2.21}\\
\implies \mathbf{M}\boldsymbol{\omega}' &= \mathscr{A}^{-1}(D \mathbf{M} \mathbf{M}^\mathscr{T}) \tag{2.21a}\\
\implies \mathscr{A}(\mathbf{M}\boldsymbol{\omega}') &= D \mathbf{M} \mathbf{M}^\mathscr{T} \tag{2.21b}\\
\implies \mathscr{A}(\mathbf{M}\boldsymbol{\omega}')\mathbf{M} &= D \mathbf{M} \tag{2.21c}\\
\end{align*}
$$
{% end %}




Substituting Eq.2.21c in Eq.2.65 along with $\mathbf{I}'\boldsymbol{\omega}' = \overline{\mathbf{L}}'$


{% mathjax() %}
$$
\begin{align*}
\mathbf{I}' D\boldsymbol{\omega}' &= -\mathbf{M}^{\mathscr{T}} D\mathbf{M}\mathbf{I}'\boldsymbol{\omega}'\\
    &= -\mathbf{M}^{\mathscr{T}} \mathscr{A}(\mathbf{M}\boldsymbol{\omega}') \mathbf{M}~  \mathbf{I}'\boldsymbol{\omega}' \tag{2.66}
\end{align*}
$$
{% end %}




**Note**: The function $\mathscr{A}$ converts a vector into an anti-symmetric matrix. Multiplying this matrix with a vector is equivalent to taking a cross product of the original vector with this second vector. We also know that rotating the cross product of two vectors gives the same vector as is obtained by taking the cross product of two rotated vectors, or $R(\vec{u} \times \vec{v}) = (R\vec{u} )\times(R\vec{v})$

These two terms can be written in terms of $\mathscr{A}$ as:


{% mathjax() %}
$$
R(\vec{u} \times \vec{v}) = \mathbf{R} \mathscr{A}(\mathbf{u}) \mathbf{v}
$$
{% end %}




{% mathjax() %}
$$
(R\vec{u})\times(R\vec{v}) = \mathscr{A}(\mathbf{R} \mathbf{u}) \mathbf{R}\mathbf{v}\\
$$
{% end %}




{% mathjax() %}
$$
\begin{align*}
\implies \mathbf{R} \mathscr{A}(\mathbf{u}) \mathbf{v} &= \mathscr{A}(\mathbf{R} \mathbf{u}) \mathbf{R} \mathbf{v}\\
\implies \mathbf{R} \mathscr{A}(\mathbf{u}) &=  \mathscr{A}(\mathbf{R} \mathbf{u}) \mathbf{R}\\
\mathscr{A}(\mathbf{u}) &=  \mathbf{R}^{\mathscr{T}} \mathscr{A}(\mathbf{R} \mathbf{u}) \mathbf{R}\tag{2.67}\\
\end{align*}
$$
{% end %}




Substituting Eq. 2.67 in Eq. 2.66:


{% mathjax() %}
$$
\begin{align*}
\mathbf{I}' D\boldsymbol{\omega}' &= - \mathscr{A}(\boldsymbol{\omega}') \mathbf{I}'\boldsymbol{\omega}' \tag{2.68}
\end{align*}
$$
{% end %}




This is the matrix form of **Euler's Equations** that gives the derivative of the body components of angular velocity entirely in terms of the angular velocity components and the principal moments of inertia. If the components of $\boldsymbol{\omega}'$ are $(\omega^a, \omega^b, \omega^c)$, then the equations can be re-written as:


{% mathjax() %}
$$
\begin{align*}
A D\omega^a &= (B - C) \omega^b \omega^c\\
B D\omega^b &= (C - A) \omega^c \omega^a\\
C D\omega^c &= (A - B) \omega^a \omega^b\tag{2.69}\\
\end{align*}
$$
{% end %}




These equations can also be written in terms of the components of angular momentum as:


{% mathjax() %}
$$
\begin{align*}
D L_a &= \left(\frac{1}{C} - \frac{1}{B}\right) L_b L_c\\
D L_b &= \left(\frac{1}{A} - \frac{1}{C}\right) L_c L_a\\
D L_c &= \left(\frac{1}{B} - \frac{1}{A}\right) L_a L_b\tag{2.69}\\
\end{align*}
$$
{% end %}




These equations *only* depend on the principal axes components of $L$. Equations 2.21b and 2.67 can be used to get the derivatives of the orientation of the body in terms of the angular velocity.


{% mathjax() %}
$$
\begin{align*}
D \mathbf{M} &= \mathscr{A}(\mathbf{M}\boldsymbol{\omega}')\mathbf{M}\tag{2.21c}\\
             &= \mathbf{M} \overbrace{\mathbf{M}^{\mathscr{T}}~\mathscr{A}(\mathbf{M}\boldsymbol{\omega}')\mathbf{M}}^{\text{Refer Eq. 2.67}}\\
             &= \mathbf{M} \mathscr{A}(\boldsymbol{\omega}')
\end{align*}
$$
{% end %}




{% mathjax() %}
$$
D\mathbf{M} = \mathbf{M}\mathscr{A}(\boldsymbol{\omega}')\tag{2.71}
$$
{% end %}




When the orientation of the body is represented by a DCM, this gives nine ordinary differential equations. These equations can be integrated witht eh initial conditions determined by the initial configuration matrix to get the evolution of the spatial orientation of the body. Combined with Euler's equations, these equations completely definet the motion of a rigid body.

However, having to integrate nine equations is rather cumbersome when we know that the orientation can be represented by just three states (the Euler angles). In order to reduce this to a system of three equations we can go back to parameterizing the rotation matrix with the Euler angles. We can form the matrix $\mathbf{M}$ by composing $\mathscr{M}$ with an Euler coordinate path (i.e. write it as the product of three rotation matrices, $R_z$, $R_x$ and $R_z$). We can then solve for $D\theta$, $D\phi$ and $D\psi$ as:


{% mathjax() %}
$$
\begin{pmatrix}
D\theta \\ D\phi \\ D\psi
\end{pmatrix} = \frac{1}{\sin\theta}\begin{pmatrix}
\cos\psi\sin\theta & -\sin\psi\sin\theta & 0\\
\sin\psi & \cos\psi & 0 \\
-\sin\psi\cos\theta & -\cos\psi\cos\theta & \sin\theta\end{pmatrix} \begin{pmatrix}\omega^a\\ \omega^b\\ \omega^c \end{pmatrix}
$$
{% end %}




These equations are singular for $\theta = 0$, as expected. To quote the book:

> The singularity in the equations of motion for $\theta = 0$ does not correspond to anything funny in the motion of the rigid body. A practical solution to the singularity problem is to choose another set of Euler-like angles that have a singularity in a different place, and switch from one to the other when the going gets tough.



## Euler's equations for forced rigid bodies



$$\require{cancel}$$


In this section, we derive Euler's equations for a rigid body subject to an external torque. Consider a rigid body subject to some potential energy that is a function of time and configuration ($t$ and $q$). A suitable Lagrangian is $L = T - V$. If we use the 3-1-3 Euler angle set as the coordinates, the last of the three active rotations that define the coordinate is about the $z$ axis by the angle $\phi$. The Lagrange equation for $\phi$ is:

{% mathjax() %}
$$
D \partial_{\dot{\phi}} L = -D \underbrace{p_\phi}_{\text{conjugate momentum of }\phi} = \partial_{1,1} V(t; \theta(t), \phi(t), \psi(t))
$$
{% end %}



where $\partial_{1,1}$ refers to a partial derivative with respect to a component (at index 1 or $\phi$) of the coordinate argument of the potential energy function. If we define the torque component $T_z$, to be minus the derivative of the potential energy with respect to the angle of rotation of the body about the z axis, then,


{% mathjax() %}
$$
T_z(t) = -D p_\phi = \partial_{1,1} V(t; \theta(t), \phi(t), \psi(t))
$$
{% end %}



and so $D p_\phi (t) = T_z$. Since the orientation of the coordinate axes are arbitrary, we may choose and orient them as we want. Thus if we want any component of the vector torque, we may choose the z-axis so that we can compute it in this way. Therefore the vector torque gives the derivative of the vector angular momentum (**why?**):


{% mathjax() %}
$$
D\vec{L} = \vec{T}
$$
{% end %}




This can be substituted in Eq. 2.65 with $\mathbf{T}$ being the torque components in a column vector.


{% mathjax() %}
$$
D\overline{\mathbf{L}} = \overline{\mathbf{T}} = D\mathbf{M}~\overline{\mathbf{L}}' + \mathbf{M}D\overline{\mathbf{L}}'\\
$$
{% end %}




Substituting in $\mathbf{I}'\boldsymbol{\omega}' = \overline{\mathbf{L}}'$, and $D\mathbf{M}$ from Eq. 2.21c,


{% mathjax() %}
$$
\begin{align*}
\overline{\mathbf{T}} &= \left(\mathscr{A}(\mathbf{M}\boldsymbol{\omega}')\mathbf{M}\right)~\mathbf{I}'\boldsymbol{\omega}' + \mathbf{M}\mathbf{I}'D\boldsymbol{\omega}'\\
\implies \mathbf{M}^\mathscr{T} \overline{\mathbf{T}} &= \underbrace{\left(\mathbf{M}^\mathscr{T}  \mathscr{A}(\mathbf{M}\boldsymbol{\omega}')\mathbf{M}\right)}_{\text{see Eq. 2.67}}~\mathbf{I}'\boldsymbol{\omega}' + \mathbf{I}'D\boldsymbol{\omega}'\\
\implies \overbrace{\mathbf{M}^\mathscr{T} \overline{\mathbf{T}}}^{= \overline{\mathbf{T}}'} &= \mathscr{A}(\boldsymbol{\omega}') \mathbf{I}'\boldsymbol{\omega}' + \mathbf{I}' D\boldsymbol{\omega}'\\
\implies \overline{\mathbf{T}}' &= \mathscr{A}(\boldsymbol{\omega}') \mathbf{I}'\boldsymbol{\omega}' + \mathbf{I}' D\boldsymbol{\omega}'\tag{2.82}
\end{align*}
$$
{% end %}




where $\overline{\mathbf{T}}'$ represents the torque vector components on the principal axes and $\mathbf{I}'$ is the inertia tensor in the basis vectors of the principal axes. The angular velocity rates can be determined from Eq. 2.82 as:


{% mathjax() %}
$$
\begin{align*}
A D \boldsymbol{\omega^a} - \left(B - C\right) \omega^b \omega^c &= \mathbf{T}_a\\
B D \boldsymbol{\omega^b} - \left(C - A\right) \omega^c \omega^a &= \mathbf{T}_b\\
C D \boldsymbol{\omega^c} - \left(A - B\right) \omega^a \omega^b &= \mathbf{T}_c\tag{2.83}\\
\end{align*}
$$
{% end %}




The angular velocity components (on the principal axes) can be substituted by the angular momentum components on the principal axes as: $\omega^a = \frac{L_a}{A}, \omega^b = \frac{L_b}{B}, \omega^c = \frac{L_c}{C}$, to get:


{% mathjax() %}
$$
\begin{align*}
\cancel{A} \frac{D L_a}{\cancel{A}} - \left(B - C\right) \frac{L_b L_c}{BC} &= T_a\\
\cancel{B} \frac{D L_b}{\cancel{B}} - \left(C - A\right) \frac{L_c L_a}{CA} &= T_b\\
\cancel{C} \frac{D L_c}{\cancel{C}} - \left(A - B\right) \frac{L_a L_b}{AB} &= T_c\\
\end{align*}
$$
{% end %}




This simplifies into:


{% mathjax() %}
$$
\begin{align*}
T_a &= D L_a - \left(\frac{1}{C} - \frac{1}{B}\right) L_b L_c\\
T_b &= D L_b - \left(\frac{1}{A} - \frac{1}{C}\right) L_c L_a\\
T_c &= D L_c - \left(\frac{1}{B} - \frac{1}{A}\right) L_a L_b\tag{2.80}\\
\end{align*}
$$
{% end %}




where the torque components on the principal axes can be obtained as: $\overline{\mathbf{T}}' = \mathbf{M}^{-1}\overline{\mathbf{T}}$. 

It is to be noted that the torque does not affect the orientation directly, but instead only affects the angular momentum or angular velocity. Therefore Euler's equations define the dynamics of the system while the derivatives of orientation define the kinematics of the system.
