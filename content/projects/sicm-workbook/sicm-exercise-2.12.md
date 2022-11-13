+++
title = "Exercise 2.12: Derivation of Euler Angle Kinematics"
date = "2022-11-13T07:06:08Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



### Exercise 2.12: Derivation of Euler Angle Kinematics

**Fill in the details of the derivation of equation (2.73). You may want to use the computer to help with the algebra.**


{% mathjax() %}
$$
\begin{pmatrix}D\theta \\ D\varphi \\ D\psi \end{pmatrix} = \frac{1}{\sin\theta} \begin{pmatrix} 
\cos\psi \sin\theta & -\sin\psi\sin\theta & 0 \\
\sin\psi & \cos\psi & 0 \\
-\sin\psi \cos\theta & -\cos\psi\cos\theta & \sin\theta \\
\end{pmatrix}\begin{pmatrix}\omega^a \\ \omega^b \\ \omega^c\end{pmatrix}\tag{2.73}
$$
{% end %}




**Note how the order of $\theta$, $\varphi$ and $\psi$ are different in the vector**





$$\require{cancel}$$

With 3-1-3 Euler angles, $\mathbf{M}$ is defined as:


{% mathjax() %}
$$
\mathbf{M} = \mathbf{R}_z(\varphi)\cdot\mathbf{R}_x(\theta)\cdot\mathbf{R}_z(\psi)\\
$$
{% end %}



For 3-1-3 Euler angles, there are three rotations with two intermediate frames starting from the inertial frame. Let the inertial frame be represented by the $\hat{a}$, the frame after first rotation by $\hat{b'}$, and the frame after the second rotation by $\hat{b''}$. Let $\hat{b}$ represent the final "body-frame".

Therefore, ${}^{A}\omega^{B'} = \dot{\varphi} \hat{a}_3 = \dot{\varphi} \hat{b}_3'$, $^{B'}\omega^{B''} = \dot{\theta} \hat{b}_1' = \dot{\theta} \hat{b}_1''$ and $^{B''}\omega^{B} = \dot{\psi} \hat{b}_3'' = \dot{\psi} \hat{b}_3$ .


The total angular velocity is the sum of all three components, that is,


{% mathjax() %}
$$
\begin{align*}
^{A}\vec{\omega}^{B} &=~^{A}\omega^{B'} +~^{B'}\omega^{B''} +~^{B''}\omega^{B} \\
                     &=\dot{\varphi} \hat{b}_3' + \dot{\theta} \hat{b}_1'' + \dot{\psi} \hat{b}_3 \\
\end{align*}
$$
{% end %}




**To get the components in body-frame, we need to convert $\hat{b}_3'$ and $\hat{b}_1''$ to be in terms of $\hat{b}$.**

We know that the $\hat{b}$'' rotated about its $z$ axis, forms the body-frame, $\hat{b}$. Therefore, (need to draw coordinate frame rotations to get this expression)


{% mathjax() %}
$$
\begin{pmatrix}\hat{b}_1''\\ \hat{b}_2'' \\ \hat{b}_3''\end{pmatrix} = \begin{pmatrix}\cos\psi & -\sin\psi & 0\\ \sin\psi & \cos\psi & 0 \\0 & 0 & 1\\ \end{pmatrix} \begin{pmatrix}\hat{b}_1\\ \hat{b}_2 \\ \hat{b}_3\end{pmatrix}
$$
{% end %}




{% mathjax() %}
$$
\begin{align*}
\hat{b}_1'' &= \cos{\psi}~\hat{b}_1 - \sin\psi~\hat{b}_2\\
\hat{b}_2'' &= \sin{\psi}~\hat{b}_1 + \cos\psi~\hat{b}_2\\
\hat{b}_3'' &= \hat{b}_3
\end{align*}
$$
{% end %}




Similarly, for the $\hat{b}'$ frame,


{% mathjax() %}
$$
\begin{pmatrix}\hat{b}_1'\\ \hat{b}_2' \\ \hat{b}_3'\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0\\ 
0 & \cos\theta & -\sin\theta\\
0 & \sin\theta & \cos\theta\\
\end{pmatrix} \begin{pmatrix}\hat{b}''_1\\ \hat{b}''_2 \\ \hat{b}''_3\end{pmatrix}
$$
{% end %}




{% mathjax() %}
$$
\begin{align*}
\hat{b}_3' &= \sin\theta~\hat{b}_2'' + \cos\theta~\hat{b}_3''\\
 &= \sin\theta\left(\sin{\psi}~\hat{b}_1 + \cos\psi~\hat{b}_2\right) + \cos\theta~\hat{b}_3\\
 &= \sin\theta\sin{\psi}~\hat{b}_1 + \sin\theta\cos\psi~\hat{b}_2 + \cos\theta~\hat{b}_3\\
\end{align*}
$$
{% end %}





Assuming that the body-frame is the principal axes frame, the angular velocity vector is:

{% mathjax() %}
$$
\begin{align*}
\vec{\omega} &= \dot{\varphi} \hat{b}_3' + \dot{\theta} \hat{b}_1'' + \dot{\psi} \hat{b}_3 \\
 &= \dot{\varphi} \left(\sin\psi \sin\theta~\hat{b}_1 + \cos\psi\sin\theta~\hat{b}_2 + \cos\theta~\hat{b}_3 \right) + \dot{\theta}\left(\cos{\psi}~\hat{b}_1 - \sin\psi~\hat{b}_2\right) + \dot{\psi}~\hat{b}_3\\
\omega^a \hat{b}_1  + \omega^b \hat{b}_2 + \omega^c \hat{b}_3 &= (\sin\psi \sin\theta\dot{\varphi} + \dot{\theta} \cos{\psi})~\hat{b}_1 + \left( + \cos\psi \sin{\theta}\dot{\varphi} - \dot{\theta}\sin\psi\right)\hat{b}_2 + \left( \dot{\varphi}\cos\theta + \dot{\psi} \right)\hat{b}_3
\end{align*}
$$
{% end %}




This can be written in matrix form as:


{% mathjax() %}
$$
\begin{pmatrix}\omega^a \\ \omega^b \\ \omega^c\end{pmatrix} = \begin{pmatrix}
\sin\psi \sin\theta & \cos{\psi} & 0\\
\cos\psi\sin\theta & -\sin\psi & 0\\
\cos\theta & 0 & 1
\end{pmatrix}
\begin{pmatrix}\dot{\varphi} \\ \dot{\theta} \\ \dot{\psi}\end{pmatrix}
$$
{% end %}



Inverting this equation, we get:

```python
theta, phi, psi = symbols('theta phi psi', real=True)
A = Matrix([ [sin(psi)*sin(theta), cos(psi), 0], [cos(psi)*sin(theta), -sin(psi), 0], [cos(theta), 0, 1] ])
simplify(A.inv())
```

{% mathjax() %}
$\displaystyle \left[\begin{matrix}\frac{\sin{\left(\psi \right)}}{\sin{\left(\theta \right)}} & \frac{\cos{\left(\psi \right)}}{\sin{\left(\theta \right)}} & 0\\\cos{\left(\psi \right)} & - \sin{\left(\psi \right)} & 0\\- \frac{\sin{\left(\psi \right)}}{\tan{\left(\theta \right)}} & - \frac{\cos{\left(\psi \right)}}{\tan{\left(\theta \right)}} & 1\end{matrix}\right]$
{% end %}




Therefore,


{% mathjax() %}
$$
\begin{pmatrix}\dot{\varphi} \\ \dot{\theta} \\ \dot{\psi}\end{pmatrix} = \frac{1}{\sin\theta}\begin{pmatrix}
\sin\psi & \cos{\psi} & 0\\
\cos\psi\sin\theta & -\sin\psi\sin\theta & 0\\
-\sin\psi\cos\theta & -\cos\psi\cos\theta & \sin\theta
\end{pmatrix}\begin{pmatrix}\omega^a \\ \omega^b \\ \omega^c\end{pmatrix}
$$
{% end %}




Swapping the rows 1 and 2 to match the order in the question, we get:


{% mathjax() %}
$$
\begin{pmatrix}D\theta \\ D\varphi \\D\psi\end{pmatrix} = \begin{pmatrix}\dot{\theta} \\ \dot{\varphi} \\\dot{\psi}\end{pmatrix} = \frac{1}{\sin\theta}\begin{pmatrix}
\cos\psi\sin\theta & -\sin\psi\sin\theta & 0\\
\sin\psi & \cos{\psi} & 0\\
-\sin\psi\cos\theta & -\cos\psi\cos\theta & \sin\theta
\end{pmatrix}\begin{pmatrix}\omega^a \\ \omega^b \\ \omega^c\end{pmatrix}
$$
{% end %}





### References

[1] : [https://www.youtube.com/watch?v=af041z8jujU](https://www.youtube.com/watch?v=af041z8jujU)
