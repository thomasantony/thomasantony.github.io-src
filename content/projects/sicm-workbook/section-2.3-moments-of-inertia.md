+++
title = "Section 2.3: Moments of Inertia"
date = "2022-11-02T06:01:17Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++






## 2.3 Moments of Inertia



The rotational kinetic energy consists of the sum of the kinetic energies of all the constituent particles. This can in turn be written in terms of the angular velocities and some aggregate properties that describe the mass distribution in the rigid body.


{% mathjax() %}
$$
T = \frac{1}{2}\sum_\alpha m_\alpha \dot{\vec{\xi}}_\alpha \cdot \dot{\vec{\xi}}_\alpha\\
$$
{% end %}




substituting in the relation between $\vec{\omega}$ and $\dot{\vec{\xi}}_{\alpha}$


{% mathjax() %}
$$
\frac{1}{2}\sum_\alpha m_\alpha \dot{\vec{\xi}}_{\alpha} \cdot \dot{\vec{\xi}}_\alpha = 
\frac{1}{2}\sum_\alpha m_\alpha \left( \vec{\omega} \times \vec{\xi}_{\alpha} \right) \cdot \left(  \vec{\omega} \times \vec{\xi}_\alpha \right)\\
$$
{% end %}




Here, we introduce and arbitrary inertial coordiante frame its the origin at the center of rotation and basis vectors $\hat{e}_0$, $\hat{e}_1$ and $\hat{e}_2$, such that $\hat{e}_0 \times \hat{e}_1 = \hat{e}_2$. If the components of $\vec{\omega}$ in this frame are $\omega^0$, $\omega^1$ and $\omega^2$,


{% mathjax() %}
$$
\begin{align*}
\frac{1}{2} & \sum_\alpha m_\alpha \left( \left(\sum_i \hat{e}_i \omega^j \right) \times \vec{\xi}_\alpha \right) \cdot \left(  \left(\sum_j \hat{e}_j \omega^j \right) \times \vec{\xi}_\alpha \right)\\
 &= \frac{1}{2} \sum_{ij} \omega^i\omega^j\sum_\alpha m_\alpha ( \hat{e}_i \times \vec{\xi}_\alpha) \cdot (\hat{e}_j \times \vec{\xi}_\alpha) \\
 &= \frac{1}{2} \sum_{ij} \omega^i\omega^j I_{ij}
\end{align*}
$$
{% end %}




where


{% mathjax() %}
$$
I_{ij} = \sum_\alpha m_\alpha ( \hat{e}_i \times \vec{\xi}_\alpha) \cdot (\hat{e}_j \times \vec{\xi}_\alpha)\tag{2.24}
$$
{% end %}




The nine *time-dependent* (?!) quantities, $I_{ij}$ form the components of the *inertia tensor* w.r.t the chosen coordinate system. 


If the components of $\vec{\xi_\alpha}$ are $\xi_{\alpha}^0$, $\xi_{\alpha}^1$ and $\xi_{\alpha}^2$, we can rewrite  $\vec{\xi}_\alpha$ as a sum over its components and simplify the vector products of the basis vectors. Thus we can get expressions for the components of the inertia tensor. The components of the inertia tensor can be arranged to form the *inertia matrix*.


{% mathjax() %}
$$
\mathbf{I} = \begin{bmatrix}I_{00} & I_{01} & I_{02}\\
I_{10} & I_{11} & I_{12}\\
I_{20} & I_{21} & I_{22}\end{bmatrix}\tag{2.25}
$$
{% end %}




where 


{% mathjax() %}
$$
\begin{align*}
I_{00} &= \sum_\alpha m_\alpha \left( (\xi_\alpha^1)^2 + (\xi_\alpha^2)^2 \right)\\
I_{11} &= \sum_\alpha m_\alpha \left( (\xi_\alpha^2)^2 + (\xi_\alpha^0)^2 \right)\\
I_{22} &= \sum_\alpha m_\alpha \left( (\xi_\alpha^0)^2 + (\xi_\alpha^1)^2 \right)\\
I_{ij} &= - \sum_\alpha m_\alpha \xi_\alpha^i \xi_\alpha^j\quad\text{ for } i \neq j\\
\end{align*}
$$
{% end %}




The components of the inertia tensor are real and symmetric, i.e., $I_{jk} = I_{kj}$. In general, the *moment of inertia* about a line can be defined as $\sum_\alpha m_\alpha (\xi_\alpha^\perp)^2$ where $\xi_\alpha^\perp$ is the distance from the line to the particle with index $\alpha$. The diagonal components of the inertia tensor are the moments of inertia about the lines coinciding with the basis vectors. The off-diagonal components are called the *products of inertia*.


Since the inertia tensor involves only the second order moments of mass, the motion of a free rigid body does not depend on the detailed shape of the body. If two bodies have the same inertia tensor, they have the same kinetic energy regardless of what they look like. The potential energy might have effects based on the shape of the body but for the kinetic energy, the inertia tensor is all that matters.
