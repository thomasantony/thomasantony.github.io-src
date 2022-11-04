+++
title = "Section 2.4: Inertia Tensor"
date = "2022-11-04T04:44:49Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++






## 2.4 Inertia Tensor



The representation of kinetic energy in terms of the inertia tensor involved a rectangular coordinate frame with basis vectors, $\hat{e}$. However the kinetic energy must be the same regardless of the coordinate frame use. This fact can be used to derive how the inertia tensor transforms if the body or the coordinate frame are rotated.

#### Active and passive rotations

Rotating the vector $\vec{x}$ by the rotation $R$ produces a new vector $\vec{x'} = R\vec{x}$. $\vec{x}$ may be written in terms of some arbitrary rectangular coordinate system with the basis vectors ($\hat{e_1}$, $\hat{e_2}$, $\hat{e_3}$). Let $\mathbf{x}$ represent the *column vector* components $x^0$, $x^1$ and $x^2$ fo the vector in this coordinate frame. Let $\mathbf{R}$ be the matrix representation of the rotaton $R$ w.r.t the same coordinate frame. With these definitions, the rotation can be written as: $\mathbf{x}' = \mathbf{R}\mathbf{x}$. Since this rotation carries the vectors to new vectors, it is an **active rotation**.

Alternately, we can rotate the basis vectors used to represent the vectors. While the vectors themselves may be unchanged, the components used to represent them are changed because the basis vectors are now in new orientations. If the new, rotated basis vector are represented by $\hat{e}'_i = R\hat{e}_i$. The componenet along the rotated basis vector is the dot product of the vector $\vec{x}$ with the new basis vector, that is: $(x')^i = \vec{x} \cdot \hat{e}'_i = \vec{x} \cdot (R \hat{e}_i)$. 

Since the rotation of two vectors preserves the angle (and hence the dot product), between them, 


{% mathjax() %}
$$
\begin{align*}
\vec{x} \cdot \vec{y} &= (R\vec{x})\cdot(R\vec{y})\\
=> R^{-1} \vec{x} \cdot \vec{y} &= \vec{x} \cdot (R\vec{y})\\
\end{align*}
$$
{% end %}




Therefore, 


{% mathjax() %}
$$
(x')^i = \vec{x} \cdot (\mathbf{R} \hat{e}_i) = R^{-1} \vec{x} \cdot \hat{e}_i \\
=> \mathbf{x}' = \mathbf{R}^{-1} \mathbf{x}
$$
{% end %}




This type of rotation is called a **passive rotation** where the vectors were unchanged and the coordinate frame was rotated. For such a rotation, the components of a fixed vector changes **as if it was actively rotated by the inverse rotation**.


#### Transformation of moments of inertia under rotation

The kinetic energy in terms of the coordinate frame $\hat{e}_i$ is:


{% mathjax() %}
$$
T = \frac{1}{2} \sum\nolimits_{ij} \omega^i \omega^j I_{ij} \tag{2.30}
$$
{% end %}




In matrix notation, this can be written as :


{% mathjax() %}
$$
T = \frac{1}{2} \boldsymbol{\omega}^{\mathscr{T}} \mathbf{I} \boldsymbol{\omega}\tag{2.31}
$$
{% end %}




where $\boldsymbol{\omega}$ is the column vector containing the components of the angular velocity vector $\vec{\omega}$ in the $\hat{e}_i$ coordinate frame. Applying a passive rotation $R$ to the coordinate frame gets us the new coordinate frame basis vectors $\hat{e}'_i = R \hat{e}_i$. The components of $\boldsymbol{\omega}$ in the new frame satisfies the condition:


{% mathjax() %}
$$
\begin{align*}
\boldsymbol{\omega}' &= \mathbf{R}^{-1} \boldsymbol{\omega}\\
=> \boldsymbol{\omega} &= \mathbf{R} \boldsymbol{\omega}'
\end{align*}
$$
{% end %}




Therefore the kinetic energy is:


{% mathjax() %}
$$
\begin{align*}
T &= \frac{1}{2} \boldsymbol{\omega}^{\mathscr{T}} \mathbf{I} \boldsymbol{\omega} \\
  &= \frac{1}{2} (\mathbf{R} \boldsymbol{\omega}')^{\mathscr{T}} \mathbf{I} \mathbf{R} \boldsymbol{\omega}' \\
  &= \frac{1}{2} (\boldsymbol{\omega}')^{\mathscr{T}}\mathbf{R}^{\mathscr{T}} \mathbf{I} \mathbf{R} \boldsymbol{\omega}'\tag{2.33} \\
\end{align*}
$$
{% end %}




However, the kinetic energy in the $\hat{e}'$ frame is:


{% mathjax() %}
$$
T = \frac{1}{2} (\boldsymbol{\omega}')^{\mathscr{T}} \mathbf{I}' \boldsymbol{\omega} \tag{2.34}
$$
{% end %}




where the components are in terms of the $\hat{e}'$ frame. Comparing equations 2.34 and 2.33, we get:


{% mathjax() %}
$$
\mathbf{I}' = \mathbf{R}^{\mathscr{T}} \mathbf{I} \mathbf{R} \tag{2.35}
$$
{% end %}




This type of transformation is called a "similarity transformation" and this is how the inertia tensor transforms under passive rotation.
