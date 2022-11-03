+++
title = "Section 2.2: Kinematics of Rotation"
date = "2022-11-02T03:01:37Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++







## 2.2 Kinematics of Rotation



* The motion of a rigid body about a center of rotation (a body-fixed reference point) is characterized at each point in time by an axis of rotation and a rate of rotation

* According to [Euler's theorem of rotations](https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem), we can go from one orientation of a rigid body to another in a single rotation
    - Rotations are not commutative in general, i.e., the order of rotations matter
    - However the combination of any number of rotations in some order can be represented by a single rotation

* Orientations are specified by the rotations it takes to reach that orientation from some reference orientation.

Let $q$ by the path describing the motion of the body and $M(q(t))$ be the rotation that takes the body from a reference orientation to the orientation specified by $q(t)$. Let $\vec{\xi_\alpha}(t)$ be some vector in the body-frame (to some constituent particle) in orientation given by $q(t)$, and $\vec{\xi'_\alpha}$ be the same body-frame vector in the reference orientation, then:


{% mathjax() %}
$$
\vec{\xi}_\alpha(t) = \mathscr{M}(q(t)) \vec{\xi'}_\alpha\tag{2.11}
$$
{% end %}




To find the kinetic energy, we need to combine the contributions of all the constituent particles, aka, the velocities of the particles.


{% mathjax() %}
$$
\vec{\xi}_\alpha(t) = \mathscr{M}(q(t)) \vec{\xi'}_\alpha = M(t)\vec{\xi'}_\alpha\tag{2.12}
$$
{% end %}




where  $M = \mathscr{M} \circ q$. Taking the time derivative:


{% mathjax() %}
$$
D\vec{\xi}_\alpha(t) = DM(t)\vec{\xi'}_\alpha\tag{2.13}
$$
{% end %}




By inverting Eq. 2.12, we can write $\vec{\xi'}_{\alpha}$ in terms of $\vec{\xi}\_{\alpha}$,


{% mathjax() %}
$$
D\vec{\xi}_\alpha(t) = DM(t)(M(t))^{-1}\vec{\xi}_\alpha(t)\tag{2.13}
$$
{% end %}




Since $M(t)$ is a rotation represented by an orthogonal matrix $\mathbf{M}(t)$, with the property, $(\mathbf{M}(t))^{-1}$ = $(\mathbf{M}(t))^{\intercal}$. Therefore, $\mathbf{M}(t)(\mathbf{M}(t))^{\intercal}$ = $\mathbf{I}$ and hence $D(\mathbf{M}\mathbf{M}^\intercal) = \mathbf{0}$.


{% mathjax() %}
$$
\mathbf{0} = D(\mathbf{M}\mathbf{M}^\intercal) = D(\mathbf{M})\mathbf{M}^\intercal + \mathbf{M}D \mathbf{M}^\intercal\tag{2.15}
$$
{% end %}




> Note: $(AB)^\intercal = B^\intercal A^\intercal => (D\mathbf{M}\mathbf{M}^\intercal)^\intercal = (\mathbf{M}^\intercal)^\intercal D\mathbf{M}^\intercal = \mathbf{M}D \mathbf{M}^\intercal$


{% mathjax() %}
$$
D(\mathbf{M})\mathbf{M}^\intercal = -\mathbf{M}D \mathbf{M}^\intercal = -(D\mathbf{M}\mathbf{M}^\intercal)^\intercal\tag{2.16}
$$
{% end %}




This shows that $D(\mathbf{M})\mathbf{M}^\intercal$ is anti-symmetric. If $\mathbf{u}$ has the components $(x, y, z)
$, all anti-symmetric 3x3 matrices have the following form:


{% mathjax() %}
$$
\mathscr{A}(\mathbf{u}) = \begin{pmatrix}0 &-z& y\\ z &0 &-x\\-y &x &0\end{pmatrix}\\
$$
{% end %}




Multuplying this matrix by a vector is equivalent to a cross-product by the vector $\vec{u}$ (and $\mathbf{u}$ is the matrix representation of $\vec{u}$. The inverse of the function $\mathscr{A}$ is one that extracts the components of $\mathbf{u}$ from a given skew-symmetric matrix. 

> Note: $\mathscr{A}^{-1}$ is *not* the inverse of the skew-symmetric matrix. Rather, this is a function that by definition, extracts the components of $\vec{u}$ from a skew-symmetric matrix.

So the matrix multiplication $D\mathbf{M}\mathbf{M}^\intercal$ can be interpreted as a cross-product with a vector that we can call $\vec{\omega}$ which is the angular velocity vector. Therefore,


{% mathjax() %}
$$
\boldsymbol{\omega} = \mathscr{A}^{-1}(D \mathbf{M} \mathbf{M}^\intercal) \tag{2.18}
$$
{% end %}




Therefore the differential equations of the constituent particles can be written as:


{% mathjax() %}
$$
D \vec{\xi}_\alpha(t) = \vec{\omega}(t) \times \vec{\xi}_\alpha(t)\tag{2.19}
$$
{% end %}




This shows that the velocity o the constituent particles are perpendicular to their position vectors and proportional to the rate of rotation and distance from the instantaneous center:

{% mathjax() %}
$$
\dot{\vec{\xi}}_\alpha = \vec{\omega} \times \vec{\xi}_\alpha\tag{2.20}
$$
{% end %}




The components, $\boldsymbol{\omega}'$ of the angular velocity vector in the body frame are $\boldsymbol{\omega}' = \mathbf{M}^\intercal \boldsymbol{\omega}$, or

{% mathjax() %}
$$
\boldsymbol{\omega}' = \mathbf{M}^\intercal  \mathscr{A}^{-1}(D \mathbf{M} \mathbf{M}^\intercal) \tag{2.21}
$$
{% end %}




**Note: Need to figure out why it is $\mathbf{M}^\intercal$ and not $\mathbf{M}$ in Eq. 2.21. Is this not a "rotation" of the vector? Question posted at: [https://physics.stackexchange.com/questions/734684/angular-velocity-in-body-frame-vs-inertial-frame](https://physics.stackexchange.com/questions/734684/angular-velocity-in-body-frame-vs-inertial-frame)**


This is a kinematic relationship that is valid for any path and can be used to obtain the components of angular velocity given the configuration and velocity at any time.



### Implementation of angular velocity functions

```clojure
(defn M-of-q->omega-of-t [M-of-q]
    (fn [q]
        (fn [t]
          (let [M-on-path (compose M-of-q q)
                omega-cross t]
             (* ((D M-on-path) t)
               (transpose (M-on-path t)))
          (rigid/antisymmetric->column-matrix (omega-cross t)))
)))

;; `omega-cross` produces the matrix representation of cross product "omega x"
;; antisymmetric->column-matrix corresponds to A^{-1} and extracts vector components from
;; a skew symmetric matrix


;; This function gives components of omega in body-fixed axes
(defn M-of-q->omega-body-of-t [M-of-q]
    (fn [q]
        (fn [t]
          (* (transpose (M-of-q (q t)))
             (((M-of-q->omega-of-t M-of-q) q) t)))))


;; We use Gamma-bar to convert these functions of path to functions of local tuple

(defn M->omega [M-of-q]
  (Gamma-bar
    (M-of-q->omega-of-t M-of-q)))

(defn M->omega-body [M-of-q]
  (Gamma-bar
    (M-of-q->omega-body-of-t M-of-q)))
 
:ok
```


    :ok





These procedures will return angular velocities as a function of state (aka local tuple)
