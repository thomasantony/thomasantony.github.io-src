+++
title = "Section 1.8.5: Noether's Theorem"
date = "2022-10-24T01:14:12Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++







## 1.8.5 Noether's Theorem



If a dynamical system has a symmetry, a coordinate system can be chosen so that the Lagrangian does not depend on a coordinate associated with the symmetry. There is also a conserved quantity associated with the symmetry ([Section 1.8](https://tgvaughan.github.io/sicm/chapter001.html#h1-6c
)). However, there are general symmetries that no coordinate systems can fully express. For example, motion around a central potential is spherically symmetric, i.e., the dynamical system is invariant under rotation about any axis. However, the Lagrangian for this system only demonstrates symmetry about a single axis. 

In general, **a Lagrangian is said to have a symmetry if there exists a coordinate transformation that leaves the Lagrangian unchanged**.
In this section we consider the more general case of **continous symmetries**. A **continuous symmetry** is defined as a parametric family of symmetries. **Emmy Noether proved that for any continuous symmetry, there is a conserved quantity**.

Consider a parametric coordinate transformation, $\widetilde{F}$ with parameter $s$. This means that $\widetilde{F}$ represents an infinite number of coordinate transformations, one for each value of $s$. 

An example would be a function that takes an angle, $s$, as the input and spits out a coordinate transformation that rotates the primed coordinate frame, $x'$ about some axis by that angle.

{% mathjax() %}
$$
x = \widetilde{F}(s) (t, x')
$$
{% end %}



There is a corresponding parametreic state transformation $\widetilde{C}$ associated with $\widetilde{F}$ that transforms the velocity $v'$ as well the time (i.e. the local tuple that forms the input to the Lagrangian).

{% mathjax() %}
$$
\begin{align*}
(t, x, v) &= \widetilde{C}(s) (t, x', v') \\
          &= (t, \widetilde{F}(t,x'),  \partial_0 \widetilde{F} + \partial_1 \widetilde{F} v', ...)
\end{align*}
$$
{% end %}



We require that $\widetilde{F}(0)$ represent the identity transformation $x' = \widetilde{F}(0)(t, x')$, with $\widetilde{C}$ as the corresponding identity state transformation. If the Lagrangian $L$ has a continous symmetry corresponding to $\widetilde{F}$, then the Lagrangian should be unchanged when the coordinates are transformed using $\widetilde{F}$. Therefore:

{% mathjax() %}
$$
\widetilde{L}(s) = L\cdot \widetilde{C}(s) = L
$$
for any $s$. Expanding $\widetilde{C}$ in the above expression, we get:

{% mathjax() %}
$$
\widetilde{L}(s) = L\left(t,\quad\widetilde{F}(s)(t, x'),\quad\partial_1\widetilde{F}(s)(t, x')v' \right)\\
$$
{% end %}




Undoing the "chainrule" in the second term and writing it in terms of the total time derivative,

{% mathjax() %}
$$
\widetilde{L}(s) = L\left(t,\quad\widetilde{F}(s)(t, x'),\quad D_t\widetilde{F}(s)(t, x', v') \right)
$$
{% end %}




**Note: One of the assumptions in the following derivation is that $\partial_0 L = \frac{\partial L}{\partial t} = 0$**

That $\widetilde{L}(s) = L$ for any $s$ implies that $D\widetilde{L}(s) = 0$ (where the $D$ operator represents derivative w.r.t $s$). Therefore, applying the chain rule for each of the components of $\widetilde{L}$, the derivative of $\widetilde{L}$ w.r.t $s$ is:


{% mathjax() %}
$$
\begin{align*}
0 &= D\widetilde({L}(s)(t, x', v'))\\
  &= \left(\underbrace{\partial_0 L}_{=\frac{\partial L}{\partial t} = 0} + \partial_1 L(t, x, v)\right) (D\widetilde{F})(s)(t, x') + \underbrace{\partial_2 L(t,x,v) D(D_t\widetilde{F}(s)(t, x')}_{\text{can swap }D_t\text{ and }D\text{, as }D\text{ w.r.t }s\text{ is unstructured}} \\
  &= \partial_1 L(t, x, v) (D\widetilde{F})(s)(t, x') + \partial_2 L(t,x,v) D_t(D\widetilde{F}(s))(t, x') \\ 
  &= (\partial_1 L \circ \Gamma[q]) \left( (D\widetilde{F})(s) \circ \Gamma[q']\right) + (\partial_2 L \circ \Gamma[q])\left( D_t(D\widetilde{F}(s)) \circ \Gamma[q']\right) \tag{1.157}
\end{align*}
$$
{% end %}




According to Lagrange equations, the first term of Eq. 1.157 is: $(\partial_1 L \circ \Gamma[q]) \left( (D\widetilde{F})(s) \circ \Gamma[q']\right) = (D_t\partial_2 L \circ \Gamma[q]) \left((D\widetilde{F})(s) \circ \Gamma[q']\right)$. Substituting this in Eq. 1.157,

{% mathjax() %}
$$
0 = (D_t \partial_2 L \circ \Gamma[q])\left( (D\widetilde{F}(s)) \circ \Gamma[q']\right) +  (\partial_2 L \circ \Gamma[q])\left( D_t(D\widetilde{F}(s)) \circ \Gamma[q']\right) \tag{1.159}
$$
{% end %}




When $s = 0$, since $\widetilde{F}(0)$ is the identity transformation, the paths $q$ and $q'$ are the same. Therefore, $\Gamma[q] = \Gamma[q']$ and Eq. 1.158 becomes

{% mathjax() %}
$$
\begin{align}
0 &= \left ((D_t \partial_2 L)(D\widetilde{F}(0)) +  (\partial_2 L)(D_t(D\widetilde{F}(0)))\right) \circ \Gamma[q] \\
  &= D_t ((\partial_2 L) (D\widetilde{F}(0))) \circ \Gamma[q] \tag{1.160}
\end{align}
$$
{% end %}




Therefore the state function $\mathscr{I}$:

{% mathjax() %}
$$
\mathscr{I} = (\partial_2 L) (D\widetilde{F}(0))
$$
{% end %}



is conserved along all solution trajectories. This quantity is called the ***Noether integral***. It is the product of the momentum $\partial_2 L$ and a vector associated with the symmetry.

### Illustration : Motion in a Central Potential

Consider the motion of a particle in a central potential. The Lagrangian in rectangular coordinates is:

{% mathjax() %}
$$
L(t; x,y,z; v_x, v_y, v_z) = \frac{1}{2} m \left( v_x^2 + v_y^2 + v_z^2\right) - U(\sqrt{x^2 + y^2 + z^2})
$$
{% end %}



Consider a parameteric rotation about the $z$-axis:

{% mathjax() %}
$$
\begin{pmatrix}x\\y\\z\end{pmatrix} = 
R_z(s)(\begin{pmatrix}x'\\y'\\z'\end{pmatrix}) = \begin{pmatrix}x' \cos{s} - y'\sin{s}\\x' \sin{s} + y'\cos{s}\\z'\end{pmatrix}
\tag{1.163}
$$
{% end %}



Since a rotation is an orthogonal transformation, it does not change the magnitude of the vector,

{% mathjax() %}
$$
x^2 + y^2 + z^2 = (x')^2 + (y')^2 + (z')^2
$$

Similarly, differentiating Eq.1.163 along a path, we get:

{% mathjax() %}
$$
\begin{pmatrix}v_x\\v_y\\v_z\end{pmatrix} =
R_z(s)\begin{pmatrix}v_x'\\v_y'\\v_z'\end{pmatrix}
$$
{% end %}



Therefore, $v_x^2 + v_y^2 + v_z^2 = v_x'^2 + v_y'^2 + v_z'^2$. Combining these, we can see that the post-transformation Lagrangian $L'$ is:

{% mathjax() %}
$$
L'(t; x',y,z'; v_x',v_y',v_z') = \frac{1}{2} m \left( (v'_x)^2 + (v'_y)^2 + (v'_z)^2\right) - U(\sqrt{(x')^2 + (y')^2 + (z')^2
})
$$
{% end %}



Therefore $L'$ is the exact same function as $L$ and hence there is a conserved value corresponding to the rotational symmetry about the z-axis. The momenta are defined as:

{% mathjax() %}
$$
\partial_2 L = [m v_x, m v_y, m v_z]
$$
{% end %}



and 

{% mathjax() %}
$$
D\widetilde{F}(0)(t;x,y,z)=D\widetilde{R}_z(0)(x,y,z) = [ y, -x, 0]
$$
{% end %}




---
**Note about the $D$ operator**

The $D$ operator has the highest precedence, and therefore:

{% mathjax() %}
$$
D\widetilde{F}(0)(t; x,y,z) = D\widetilde{F}(s)(x, y, z)|_{s=0} = \left.\begin{bmatrix} -x \sin{s} - y\cos{s}\\x \cos{s} - y\sin{s}\\0\end{bmatrix}\right|_{s=0}
$$
{% end %}



Here we are taking the derivative w.r.t $s$ and consider $x$, $y$ and $z$ to be constants. Also note that the original $\widetilde{F}(s)$ was defined in terms of the primed coordinates while here it was evaluated on the unprimed coordinates.

---


Therefore, the Noether integral is:

{% mathjax() %}
$$
\begin{align*}
\mathscr{I}(t; x,y,z; v_x,v_y,v_z) &= ((\partial_2 L)(D\widetilde{F}(0))) (t; x,y,z; v_x,v_y,v_z) \\
&= mv_xy -mv_yx + (mv_z)(0) \\
&= m(yv_x - xv_y)
\end{align*}
$$
{% end %}



This is the $z$ component of the angular momentum vector, $\vec{x} \times m\vec{v}$

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

;; Lagrangian for motion in central potential
(defn L-central-rectangular [m U]
    (fn [[t q v]]
        (- (* 1/2 m (square v))
           (U (sqrt (square q))))))

;; Define the Noether integral
(def the-Noether-integral
  (let [L (L-central-rectangular 'm (literal-function 'U))]
    (* ((partial 2) L) ((D F-tilde) 0 0 0))))


(rendertex
(the-Noether-integral
  (up 't
      (up 'x 'y 'z)
      (up 'v_x 'v_y 'v_z))))
```

{% mathjax() %}
\begin{bmatrix}\displaystyle{- m\,v_y\,z + m\,v_z\,y}&\displaystyle{m\,v_x\,z - m\,v_z\,x}&\displaystyle{- m\,v_x\,y + m\,v_y\,x}\end{bmatrix}
{% end %}




These are all three components of the angular momentum. Therefore, angular momentum is conserved for a particle in motion in a central potential
