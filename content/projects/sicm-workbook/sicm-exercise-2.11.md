+++
title = "Exercise 2.11: Conservation of Angular Momentum"
date = "2022-11-12T22:10:11Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



### Exercise 2.11: Conservation of Angular Momentum

**Fill in the details of the argument that Noether's theorem implies that vector angular momentum is conserved by the motion of the free rigid body.**







$$\require{cancel}$$



According to [Noether's theorem](/projects/sicm-workbook/section-1-8-5-noethers-theorem/), for any continuous symmetry in a system (aka a parametric family of symmetries), there is a conserved quantity. 

In the case of rigid bodies, rotations about any axis is a symmetry. This can be proved as shown below:


The Lagrangian in rectangular coordinates for a rigid body with particles indexed by $\alpha$ is:


{% mathjax() %}
$$
L(t; x,y,z; v_x, v_y, v_z) = \frac{1}{2} \sum_\alpha m_\alpha \left( \dot{x}_\alpha^2 + \dot{y}_\alpha^2 + \dot{z}_\alpha^2\right) \tag{1}
$$
{% end %}




Consider a parameteric rotation about the $z$-axis:


{% mathjax() %}
$$
\begin{pmatrix}x_\alpha \\y_\alpha \\z_\alpha \end{pmatrix} = 
R_z(s)\begin{pmatrix}x_\alpha' \\y_\alpha' \\z_\alpha' \end{pmatrix} = \begin{pmatrix}x_\alpha' \cos{s} - y_\alpha'\sin{s}\\x_\alpha' \sin{s} + y_\alpha'\cos{s}\\z_\alpha'\end{pmatrix}\tag{2}
$$
{% end %}




Since a rotation is an orthogonal transformation, it does not change the magnitude of the vector,


{% mathjax() %}
$$
x_\alpha^2 + y_\alpha^2 + z_\alpha^2 = (x_\alpha')^2 + (y_\alpha')^2 + (z_\alpha')^2\\
$$
{% end %}




Similarly, differentiating Eq.2 along a path, we get:


{% mathjax() %}
$$
\begin{pmatrix}\dot{x}_\alpha\\ \dot{y}_\alpha\\ \dot{z}_\alpha\end{pmatrix} =
R_z(s)\begin{pmatrix}\dot{x}_\alpha'\\ \dot{y}_\alpha'\\ \dot{z}_\alpha'\end{pmatrix}
$$
{% end %}




Therefore, 


{% mathjax() %}
$$
\dot{x}_\alpha^2 + \dot{y}_\alpha^2 + \dot{z}_\alpha^2 = \dot{x}_\alpha'^2 + \dot{y}_\alpha'^2 + \dot{z}_\alpha'^2
$$ 


Combining these, we can see that the post-transformation Lagrangian $L'$ is:


{% mathjax() %}
$$
L'(t; x_\alpha',y_\alpha',z_\alpha'; \dot{x}_\alpha',\dot{y}_\alpha',\dot{z}_\alpha') = \frac{1}{2} \sum_\alpha m \left(\dot{x}_\alpha'^2 + \dot{y}_\alpha'^2 + \dot{z}_\alpha'^2 \right)\tag{3}
$$
{% end %}




Therefore $L'$ in Eq.3 is the exact same function as $L$ in Eq. 1 and hence there is a conserved value corresponding to the rotational symmetry about the z-axis. The momenta are defined as:


{% mathjax() %}
$$
\partial_2 L = \left[\sum_\alpha m_\alpha \dot{x}, \sum_\alpha m_\alpha \dot{y}, \sum_\alpha m_\alpha \dot{z}\right]
$$
{% end %}




and 


{% mathjax() %}
$$
D\widetilde{F}(0)(t;x,y,z)=D\widetilde{R}_z(0)(x,y,z) = [ y, -x, 0]\\
$$
{% end %}




Therefore the Noether integral is:


{% mathjax() %}
$$
\begin{align*}
\mathscr{I}(t; x_\alpha,y_\alpha,z_\alpha; \dot{x}_\alpha,\dot{y}_\alpha,\dot{z}_\alpha) &= ((\partial_2 L)(D\widetilde{F}(0))) (t; x_\alpha,y_\alpha,z_\alpha; \dot{x}_\alpha,\dot{y}_\alpha,\dot{z}_\alpha) \\
&= \sum_\alpha \left(m_\alpha \dot{x}_\alpha~y_\alpha -m_\alpha \dot{y}_\alpha~x_\alpha + (m_\alpha \dot{z}_\alpha)(0) \right) \\
&= \sum_\alpha m_\alpha \left(y_\alpha \dot{x}_\alpha - x_\alpha \dot{y}_\alpha \right)
\end{align*}
$$
{% end %}




This is the $z$ component of the angular momentum vector $\sum_\alpha \vec{\xi_\alpha} \times (m_\alpha \dot{\vec{\xi}}_\alpha)$

In the following program, we compute the noether integrals for rotations around all three coordinate axes.

```clojure
(defn RotX [angle]
    (fn [[x, y, z]]
      (let [ca (cos angle)
            sa (sin angle)]
          (up x
              (- (* ca y) (* sa z))
              (+ (* sa y) (* ca z))))))

(defn RotY [angle]
    (fn [[x, y, z]]
      (let [ca (cos angle)
            sa (sin angle)]
          (up (+ (* ca x) (* sa z))
              y
              (+ (- (* sa x)) (* ca z))))))

(defn RotZ [angle]
    (fn [[x, y, z]]
      (let [ca (cos angle)
            sa (sin angle)]
          (up (- (* ca x) (* sa y))
              (+ (* sa x) (* ca y))
              z))))

;; Coordinate transformation with three angular "inputs" for rotations about
;; all three axes
;; Composing with `coordinate`, extracts the second element of the tuple that is passed in as the argument
(defn F-tilde [angle-x angle-y angle-z]
  (compose (RotX angle-x) (RotY angle-y) (RotZ angle-z) coordinate))

;; Lagrangian for motion of single particle in rigid body
(defn L-rigid-body_particle [m]
    (fn [[t q v]]
        (- (* 1/2 m (square v)))))

;; Define the Noether integral
(def the-Noether-integral
  (let [L (L-rigid-body_particle 'm_alpha)]
    (* ((partial 2) L) ((D F-tilde) 0 0 0))))


(rendertex
(the-Noether-integral
  (up 't
      (up 'x_alpha 'y_alpha 'z_alpha)
      (up 'xdot_alpha 'ydot_alpha 'zdot_alpha))))
```

{% mathjax() %}
\begin{bmatrix}\displaystyle{- m_{\alpha}\,y_{\alpha}\,{\dot z}_{\alpha} + m_{\alpha}\,{\dot y}_{\alpha}\,z_{\alpha}} \cr \cr \displaystyle{m_{\alpha}\,x_{\alpha}\,{\dot z}_{\alpha} - m_{\alpha}\,{\dot x}_{\alpha}\,z_{\alpha}} \cr \cr \displaystyle{- m_{\alpha}\,x_{\alpha}\,{\dot y}_{\alpha} + m_{\alpha}\,{\dot x}_{\alpha}\,y_{\alpha}}\end{bmatrix}
{% end %}




The results above correspond to the components of the angular momentum vector for a single particle in a rigid body. Therefore the conserved quantities for a rigid body are:


{% mathjax() %}
$$
\begin{align*}
\sum_\alpha m_\alpha & \left( z_\alpha{\dot{y}_\alpha} - \dot{z}_\alpha y_\alpha \right)\\
\sum_\alpha m_\alpha & \left( x_\alpha{\dot{z}_\alpha} - \dot{x}_\alpha z_\alpha \right)\\
\sum_\alpha m_\alpha & \left( y_\alpha{\dot{x}_\alpha} - \dot{y}_\alpha x_\alpha \right)\\
\end{align*}
$$
{% end %}




This proves that all three components of the angular moementum vector are conserved for a rigid body in free-rotation.
