+++
title = "Exercise 2.13: Bicycle Wheel (incomplete)"
date = "2022-11-13T20:15:14Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



### Exercise 2.13: Bicycle Wheel

**a. Imagine that you are holding a bicycle wheel by the axle (in both hands) and the wheel is spinning so that the top edge is going away from your face. If you torque the wheel by pushing down with your right hand and pulling up with your left hand the wheel will precess. Which way does it try to turn?**





$$\require{cancel}$$

Assume that the axle of the wheel forms the $z$ axis of the system (positive to the right). Let the $x$ axis point forward, and the $y$ axis point up, forming a right-handed coordinate system. The bicycle wheel starts spinning about the axle with some speed $\omega^c$. Therefore the angular velocity vector is:


{% mathjax() %}
$$
\vec{\omega} = \omega^c \hat{z}
$$
{% end %}




Pushing the axle down on the right side and pulling it up on the left equals a positive torque about the $x$ axis, that is,


{% mathjax() %}
$$
\vec{T} = \mathbf{T}_a \hat{x}
$$
{% end %}





From Eq. 2.83 in the book


{% mathjax() %}
$$
\begin{align*}
A D \omega^a - \left(B - C\right) \omega^b \omega^c &= \mathbf{T}_a\tag{2.83a}\\
B D \omega^b - \left(C - A\right) \omega^c \omega^a &= \mathbf{T}_b\tag{2.83b}\\
C D \omega^c - \left(A - B\right) \omega^a \omega^b &= \mathbf{T}_c\tag{2.83c}\\
\end{align*}
$$
{% end %}




Substituting $A = B$ (as the wheel is symmetric) and $\mathbf{T}_c = 0$ in Eq. 2.83c, we find that $D \boldsymbol{\omega^c} = 0$ which means that $\omega^c$ is a constant. Substituting $\mathbf{T}_b = 0$ and $A = B$ in Eq.2.83b,


{% mathjax() %}
$$
\begin{align*}
\overbrace{B}^{=A} D \omega^b - \left(C - A\right) \omega^c \omega^a &= 0\\
\frac{ A D \omega^b}{\left(C - A\right)\omega^c} &=  \omega^a\\
\frac{A}{K_1} D \omega^b = \omega^a
\end{align*}
$$
{% end %}




where $K_1 = (C - A)\omega^c$. Substituting $\omega^a$ in Eq.2.83a, along with $A = B$,


{% mathjax() %}
$$
\begin{align*}
\mathbf{T}_a &= A D \omega^a - \left(\overbrace{B}^{=A} - C\right) \omega^b \omega^c\\
        &= A D ( \frac{A}{K_1} D \omega^b ) - (A - C) \omega^c \omega^b\\
        &= \frac{A^2}{K_1}  D^2 \omega^b + K_1 \omega^b\\
\mathbf{T}_a &= \frac{ A^2 }{K_1} D^2 \omega^b + K_1 \omega^b\\
K_1 \mathbf{T}_a &= A^2 D^2 \omega^b + K_1^2 \omega^b
\end{align*}
$$
{% end %}




This shows that the $\omega^b$ has a motion governed by a second order differential equation dependent on the magnitude of torque applied about the $x$ axis. So the bicycle wheel will try to precess about the $y$ axis (i.e. turn left/right).



**b. A free bicycle wheel rolls on a horizontal surface. If it starts to tilt, the torque from gravity will cause the wheel to turn. Which way will it turn? The reasoning that applied to part a does not directly apply to the rolling bicycle wheel, which is not a holonomic system. However, it is interesting to think about whether the behavior of the two systems is related.**

```python

```
