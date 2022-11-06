+++
title = "Exercise 2.8: Rotational angular momentum"
date = "2022-11-06T08:12:45Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



## Exercise 2.8: Rotational angular momentum





**Verify that expression in Eq. (2.50) for the components of the rotational angular momentum Eq. (2.49) in terms of the inertia tensor is correct.**


{% mathjax() %}
$$
\vec{L} = \sum_\alpha m_\alpha \vec{\xi}_\alpha \times \left(\vec{\omega} \times  \vec{\xi}_\alpha \right)\tag{2.49}
$$
{% end %}




{% mathjax() %}
$$
L_j = \sum_k I_{jk} \omega^k\tag{2.50}
$$
{% end %}





Consider an arbitrary inertial coordinate frame its the origin at the center of rotation and basis vectors $\hat{e}_0$, $\hat{e}_1$ and $\hat{e}_2$, such that $\hat{e}_0 \times \hat{e}_1 = \hat{e}_2$. If the components of $\vec{\omega}$ in this frame are $\omega^0$, $\omega^1$ and $\omega^2$,
 The inertia matrix of a body in this coordinate frame is:



{% mathjax() %}
$$
\begin{align*}
\vec{L} &= \sum_\alpha m_\alpha \vec{\xi}_\alpha \times \left(\vec{\omega} \times  \vec{\xi}_\alpha \right) \\
          L_i = \vec{L}\cdot \hat{e}_i &= \left( \sum_\alpha m_\alpha \vec{\xi}_\alpha \times \left(\vec{\omega} \times  \vec{\xi}_\alpha \right) \right) \cdot \hat{e}_i\\
\end{align*}
$$
{% end %}




Applying the [triple product formula](https://en.wikipedia.org/wiki/Triple_product#Properties), ${\displaystyle (\mathbf {a} \times \mathbf {b} )\cdot \mathbf {c} = \mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} ) }$,


{% mathjax() %}
$$
\begin{align*}
L_j &= \sum_\alpha \left( m_\alpha \overbrace{\vec{\xi}_\alpha}^{"\mathbf{a}"} \times \underbrace{\left(\vec{\omega} \times  \vec{\xi}_\alpha \right)}_{"\mathbf{b}"} \right) \cdot \overbrace{\hat{e}_j}^{"\mathbf{c}"}\\
&= \sum_\alpha m_\alpha \vec{\xi}_\alpha \cdot \left[ \left(\vec{\omega} \times  \vec{\xi}_\alpha \right) \times \hat{e}_j\right]\\
&= \sum_\alpha m_\alpha \vec{\xi}_\alpha \cdot \left[ \left(\sum_k \hat{e}_k \omega^k \times  \vec{\xi}_\alpha \right) \times \hat{e}_j \right]\\
&= \sum_k \omega^k \sum_\alpha m_\alpha \vec{\xi}_\alpha \cdot \left[ \left(\hat{e}_k \times  \vec{\xi}_\alpha \right) \times \hat{e}_j \right]\\
\end{align*}
$$
{% end %}




Applying the [triple product formula](https://en.wikipedia.org/wiki/Triple_product#Properties) again, ${\displaystyle \mathbf {a} \cdot (\mathbf {b} \times \mathbf {c} )=\mathbf {b} \cdot (\mathbf {c} \times \mathbf {a} )}$,


{% mathjax() %}
$$
\begin{align*}
L_j &= \sum_k \omega^k \sum_\alpha m_\alpha \underbrace{\vec{\xi}_\alpha}_{"\mathbf{a}"} \cdot \left[ \overbrace{\left(\hat{e}_k \times  \vec{\xi}_\alpha \right)}^{"\mathbf{b}"} \times \underbrace{\hat{e}_j}_{"\mathbf{c}"} \right]\\
    &= \sum_k \omega^k \sum_\alpha m_\alpha \left(\hat{e}_k \times  \vec{\xi}_\alpha \right) \cdot \left[ \hat{e}_j \times \vec{\xi}_\alpha \right]\\
    &= \sum_k \omega^k \underbrace{\sum_\alpha m_\alpha \left(\hat{e}_j \times  \vec{\xi}_\alpha \right) \cdot \left( \hat{e}_k \times \vec{\xi}_\alpha \right)}_{I_{jk}}\\
    \\
L_j &= \sum_k I_{jk} \omega^k
\end{align*}
$$
{% end %}



where $I_{jk}$ are components of the inertia tensor.
