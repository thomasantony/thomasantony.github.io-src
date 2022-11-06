+++
title = "Section 2.6: Vector Angular Momentum"
date = "2022-11-06T07:14:48Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++







## 2.6 Vector Angular Momentum



> The vector angular momentum of a particle is the cross product of its position vector and its linear momentum vector. For a rigid body the vector angular momentum is the sum of the vector angular momentum of each of the constituents.

The vector angular momentum of a rigid body is


{% mathjax() %}
$$
\sum_\alpha \vec{x}_\alpha \times (m_\alpha \dot{\vec{x}}_\alpha)
$$
{% end %}




Similar to rotational kinetic energy, the vector angular momentum of a rigid body can also be decomposed to the angular momentum of the center of mass and the angular momentum about the center of mass. If we represent the position vectors as sum of the position of the center of mass, $\vec{X}$ and the vectors from the center of mass, $\vec{\xi}_\alpha$, we get:


{% mathjax() %}
$$
\begin{align*}
\vec{x}_\alpha &= \vec{X} + \vec{\xi}_\alpha\tag{2.43}\\
\dot{\vec{x}}_\alpha &= \dot{\vec{X}} + \dot{\vec{\xi}}_\alpha\tag{2.44}\\
\text{where }\vec{X} &= \frac{\sum_\alpha m_\alpha \vec{x}_\alpha}{M} \\
 M &= \sum_\alpha m_\alpha
\end{align*}
$$
{% end %}




As a result of $\vec{X}$ being the center of mass, 


{% mathjax() %}
$$
\sum_\alpha m_\alpha \vec{\xi}_\alpha = \sum_\alpha m_\alpha (\vec{x}_\alpha - \vec{X}) = \underbrace{\sum_\alpha m_\alpha \vec{x}_\alpha}_{= M\vec{X}} - \overbrace{\sum_\alpha m_\alpha}^{=M} \vec{X} = 0\\
$$
{% end %}




Similarly, $\sum_\alpha m_\alpha \dot{\vec{\xi}}_\alpha$ is also equal to zero. Substituting these in the angular momentum, we get:


{% mathjax() %}
$$
\begin{align*}
\sum_\alpha & m_\alpha \left(\vec{X} + \vec{\xi}_\alpha \right) \times  \left(\dot{\vec{X}} + \dot{\vec{\xi}}_\alpha\right)\\
          &= \sum_\alpha m_\alpha (\vec{X} \times \dot{\vec{X}} + \vec{X} \times  \dot{\vec{\xi}}_\alpha + \vec{\xi}_\alpha \times  \dot{\vec{X}} + \vec{\xi}_\alpha \times  \dot{\vec{\xi}}_\alpha )\\
          &= \vec{X} \times M\dot{\vec{X}} +  \vec{X} \times \cancelto{0}{\sum_\alpha m_\alpha \dot{\vec{\xi}}_\alpha} + \cancelto{0}{\sum_\alpha m_\alpha \vec{\xi}_\alpha } \times \dot{\vec{X}}   + \sum_\alpha m_\alpha \vec{\xi}_\alpha \times  \dot{\vec{\xi}}_\alpha\\
          &= \vec{X} \times M\dot{\vec{X}} +  \sum_\alpha \vec{\xi}_\alpha \times  (m_\alpha \dot{\vec{\xi}}_\alpha)\tag{2.46}
\end{align*}
$$
{% end %}




The first term of Eq. 2.46, $\vec{X} \times M\dot{\vec{X}}$ is the angular momentum of the center of mass and the rotational angular momentum is $\sum_\alpha \vec{\xi_\alpha} \times  (m_\alpha \dot{\vec{\xi_\alpha}})$. By substituting $\dot{\vec{\xi_\alpha}} = \vec{\omega} \times \vec{\xi_\alpha}$, we get:


{% mathjax() %}
$$
\vec{L} = \sum_\alpha m_\alpha \vec{\xi}_\alpha \times \left(\vec{\omega} \times  \vec{\xi}_\alpha \right)\tag{2.49}
$$
{% end %}




Using the same technique as done for the rotational kinetic energy in [Section 2.3](/projects/sicm-workbook/section-2-3-moments-of-inertia/), we can resolve $\vec{\omega}$ into its components to find the angular momentum in terms of the moments of inertia as:


{% mathjax() %}
$$
L_j = \sum_k I_{jk} \omega^k\tag{2.50}
$$
{% end %}




where $I_{jk}$ are components of the inertia tensor (the same one used to compute rotational kinetic energy). In terms of the principal moments of inertia, the components of $L$ are:


{% mathjax() %}
$$
\begin{align*}
L_a &= A\omega^a\\
L_b &= B\omega^b\\
L_c &= C\omega^c\tag{2.51}\\
\end{align*}
$$
{% end %}




These are also the partial derivatives of kinetic energy $T_R$ w.r.t angular velocities (Eq. 2.41 in [Section 2.5](/projects/sicm-workbook/section-2-5-principal-moments-of-inertia/)). Therefore $\vec{L}$ is written as a down-tuple (or a row-matrix).





If $\mathbf{M}$ is the matrix representation of the rotation that takes an angular-velocity vector  $\boldsymbol{\omega}'$ to a rotated vector $\boldsymbol{\omega}$, the components transform as $\boldsymbol{\omega} = \mathbf{M}\boldsymbol{\omega}$. 
It is also conventient to work with a column matrix of the angular momentum components, $\overline{\mathbf{L}} = \mathbf{L}^{\mathscr{T}}$. 

Applying this transformation along with $\mathbf{I}' = \mathbf{M}\mathbf{I}\mathbf{M}^{\mathscr{T}}$ to angular momentum


{% mathjax() %}
$$
\begin{align*}
\overline{\mathbf{L}} &= \mathbf{I}\boldsymbol{\omega}\\
                      &= \mathbf{M}\mathbf{I}\mathbf{M}^{\mathscr{T}} \mathbf{M}\boldsymbol{\omega}'\\
                      &= \mathbf{M}\mathbf{I}\boldsymbol{\omega}'
                      &= \mathbf{M} \overline{\mathbf{L}}'\tag{2.52}
\end{align*}
$$
{% end %}




Transposing the result in Eq. 2.52, 


{% mathjax() %}
$$
\mathbf{L} = (\overline{\mathbf{L}})^{\mathscr{T}} = (\mathbf{M} \overline{\mathbf{L}}')^{\mathscr{T}} = \mathbf{L}' \mathbf{M}^{\mathscr{T}}
$$
{% end %}




Therefore, the angular momentum components transform as: $\mathbf{L} = \mathbf{L}' \mathbf{M}^{\mathscr{T}}$

```clojure
(defn L-body [A B C]
    (fn [[omega-a omega-b omega-c]]
      (down (* A omega-a)
            (* B omega-b)
            (* C omega-c))))

(defn L-space [M]
    (fn [A B C]
        (fn [omega-body]
          (* ((L-body A B C) omega-body)
             (transpose M)))))


(rendermd ((L-body 'A 'B 'C)
           (up 'omega_a 'omega_b 'omega_c)))
```


{% mathjax() %}$$
\begin{bmatrix}\displaystyle{A\,{\omega}_a}&\displaystyle{B\,{\omega}_b}&\displaystyle{C\,{\omega}_c}\end{bmatrix}
$$
{% end %}


