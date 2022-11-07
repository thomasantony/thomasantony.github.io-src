+++
title = "Exercise 2.9: Euler angles"
date = "2022-11-07T08:15:00Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



## Exercise 2.9: Euler Angles





**It is not immediately obvious that all orientations can be represented in terms of the Euler angles. To show that the Euler angles are adequate to represent all orientations, solve for the Euler angles that give an arbitrary rotation $R$. Keep in mind that some orientations do not correspond to a unique representation in terms of Euler angles.**



We will solve this for the "3-1-3" euler angles which involves an initial rotation around the $z$ axis, followed by the $x$ axis and then the $z$ axis again. 

From [Section 2.7](/projects/sicm-workbook/section-2-7-euler-angles/), we know that rotations about $z$ and $x$ axes can be represented as: 

{% mathjax() %}
$$
\begin{align*}
\mathbf{R}_z(\psi) &= \begin{bmatrix}
              \cos\psi & -\sin\psi & 0\\
              \sin\psi & \cos\psi & 0\\
              0 & 0 & 1\\
             \end{bmatrix}\\
\mathbf{R}_x(\psi) &= \begin{bmatrix}
              1 & 0 & 0\\
              0 & \cos\psi & -\sin\psi\\
              0 & \sin\psi & \cos\psi\\
             \end{bmatrix}\\
\end{align*}
$$
{% end %}



The rotation $R$ can then be represented in matrix form as:


{% mathjax() %}
$$
\begin{align*}
\mathbf{R}_{zxz}(\theta, \varphi, \psi) = \mathbf{R}_z(\varphi) \mathbf{R}_x(\theta) \mathbf{R}_z(\psi)
\end{align*}
$$
{% end %}



Expanding this matrix multiplication, we can get the matrix $\mathbf{R}_{zxz}$ as a function of $(\theta, \varphi, \psi)$

```python
t = symbols('t', real=True)
theta, phi, psi = symbols('theta phi psi', real=True)

Rz = Matrix([[cos(t), -sin(t), 0],
             [sin(t), cos(t), 0],
             [0, 0, 1]])

Rx = Matrix([[1, 0, 0],
             [0, cos(t), -sin(t)],
             [0, sin(t), cos(t)]])

R_zxz = Rz.subs(t, phi) * Rx.subs(t, theta) * Rz.subs(t, psi)
R_zxz
```

{% mathjax() %}
$\displaystyle \left[\begin{matrix}- \sin{\left(\phi \right)} \sin{\left(\psi \right)} \cos{\left(\theta \right)} + \cos{\left(\phi \right)} \cos{\left(\psi \right)} & - \sin{\left(\phi \right)} \cos{\left(\psi \right)} \cos{\left(\theta \right)} - \sin{\left(\psi \right)} \cos{\left(\phi \right)} & \sin{\left(\phi \right)} \sin{\left(\theta \right)}\\\sin{\left(\phi \right)} \cos{\left(\psi \right)} + \sin{\left(\psi \right)} \cos{\left(\phi \right)} \cos{\left(\theta \right)} & - \sin{\left(\phi \right)} \sin{\left(\psi \right)} + \cos{\left(\phi \right)} \cos{\left(\psi \right)} \cos{\left(\theta \right)} & - \sin{\left(\theta \right)} \cos{\left(\phi \right)}\\\sin{\left(\psi \right)} \sin{\left(\theta \right)} & \sin{\left(\theta \right)} \cos{\left(\psi \right)} & \cos{\left(\theta \right)}\end{matrix}\right]$
{% end %}




Any proper rotation can be represented by the rotation matrix $\mathbf{R}$ where

{% mathjax() %}
$$
\mathbf{R} = \begin{bmatrix}R_{11} & R_{12} & R_{13}\\
R_{21} & R_{22} & R_{23}\\
R_{31} & R_{32} & R_{33}\\
\end{bmatrix}
$$
{% end %}



Comparing $\mathbf{R}$ and $\mathbf{R}_{zxz}$, we get


{% mathjax() %}
$$
\begin{align*}
\cos{\theta} &= R_{33} \implies \theta = \arccos{(R_{33})}\\
\sin(\phi)\sin(\theta) &= R_{13}\\
-\cos(\phi)\sin(\theta) &= R_{23}\\
\sin{(\theta)}\cos{(\psi)} &= R_{32}\\
\sin{(\theta)}\sin{(\psi)} &= R_{31}\\
\end{align*}
$$
{% end %}




We can therefore compute $(\theta, \phi, \psi)$ for a given arbitrary rotation. The particular set of Euler angles chosen may have coordinate singularities. For example, in the z-x-z Euler angle set chosen above, when $\theta = 0$, $\phi$ and $\psi$ are not defined. However, in this case, another set of Euler angles may be chosen that does not have a singularity in that particular configuration.

We have shown above that any arbitrary rotation, as represented by a direction cosine matrix, can be written in terms of Euler angles. **This proves that Euler angles can represent any arbitrary rotation.**
