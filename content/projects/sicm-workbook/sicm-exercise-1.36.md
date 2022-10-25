+++
title = "Exercise 1.36: Noether integral"
date = "2022-10-25T06:24:52Z"
draft = false

[extra]
latex = true
+++



### Exercise 1.36: Noether integral

Consider motion on an ellipsoidal surface. The surface is specified by $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$

Formulate a Lagrangian for frictionless motion on this surface. Assume that two of the axes of the ellipsoid are equal: b = c.

Using angular coordinates $(\theta, \phi)$, where $\theta$ is colatitude from the $z$-axis, and $\phi$ is longitude measured from the $x$-axis, formulate a Lagrangian that captures the symmetry of this ellipsoid: rotational symmetry around the $x$-axis. Formulate a parametric transformation that represents this symmetry and show that the Lagrangian you formulated is invariant under this transformation. Compute the Noether integral associated with this symmetry.

Note that the choice of coordinates does not build in this symmetry.







With $\theta$ being the colatitude from the $z$-axis, and $\phi$ being the longitude measured from the $x$ axis,
The parameteric equations for an ellipsoid are:

{% mathjax() %}
$$
\begin{align*}
x &= a\sin{\theta}\cos{\phi} \\
y &= b\sin{\theta}\sin{\phi} \\
z &= c\cos{\theta}
\end{align*}
$$
{% end %}



```clojure
;; Coordinate transformation for (theta, phi) to rectilinear coordinates
(defn elliptical->rect [a b c]
    (fn [[_ [theta phi] _]]
        (up (* a (sin theta) (cos phi))
            (* b (sin theta) (sin phi))
            (* c (cos theta)))))

;; Free particle Lagrangian
(defn L-free-particle [mass]
    (fn [[_ _ v]]
        (* 1/2 mass (dot-product v v)))   
    )

;; Lagrangian for motion constrained to the ellipsoid
(defn L-ellipsoid [m a b c]
    (fn [q-prime]
          ((compose (L-free-particle m) (F->C (elliptical->rect a b c)))
           q-prime)))

(rendermd
 (let [state (up (literal-function 'theta) (literal-function 'phi))
       local ((Gamma state) 't)
       ]
     ((L-ellipsoid 'm 'a 'b 'c) local)))
```


{% mathjax() %}$$
\frac{1}{2}\,{a}^{2}\,m\,{\cos}^{2}\left(\phi\left(t\right)\right)\,{\cos}^{2}\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2} - {a}^{2}\,m\,\cos\left(\phi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,\sin\left(\phi\left(t\right)\right)\,D\phi\left(t\right) + \frac{1}{2}\,{a}^{2}\,m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\sin}^{2}\left(\phi\left(t\right)\right)\,{\left(D\phi\left(t\right)\right)}^{2} + \frac{1}{2}\,{b}^{2}\,m\,{\cos}^{2}\left(\phi\left(t\right)\right)\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\phi\left(t\right)\right)}^{2} + {b}^{2}\,m\,\cos\left(\phi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,\sin\left(\phi\left(t\right)\right)\,D\phi\left(t\right) + \frac{1}{2}\,{b}^{2}\,m\,{\cos}^{2}\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\phi\left(t\right)\right) + \frac{1}{2}\,{c}^{2}\,m\,{\left(D\theta\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\theta\left(t\right)\right)
$$
{% end %} 





The above Lagrangian is for the motion of a particle constrained to move on an ellipsoid.

The question asks that we look at a spheroid with $b = c$ and look at the symmetry about the $x$ axis. Without losing generality, we can instead consider the case where $a = b$ and look at the symmetry about the $z$ axis. This rotation gets reduced to a simple addition to $\phi$, i.e.

{% mathjax() %}
$$
\begin{pmatrix}\theta\\\phi\end{pmatrix} = R_x(s)(\begin{pmatrix}\theta'\\\phi'\end{pmatrix}) = \begin{pmatrix}\theta'\\\phi' + s\end{pmatrix}
$$
{% end %}



```clojure
;; Assuming two of the axes are equal, i.e., a = b
(def L-ellipsoid-sym (L-ellipsoid 'm 'a 'a 'c))

(rendermd
 (let [state (up (literal-function 'theta) (literal-function 'phi))
       local ((Gamma state) 't)
       ]
     (L-ellipsoid-sym local)))
```


{% mathjax() %}$$
\frac{1}{2}\,{a}^{2}\,m\,{\cos}^{2}\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2} + \frac{1}{2}\,{a}^{2}\,m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\phi\left(t\right)\right)}^{2} + \frac{1}{2}\,{c}^{2}\,m\,{\left(D\theta\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\theta\left(t\right)\right)
$$
{% end %} 



```clojure
;; Defining a parameteric transformation to rotate about the "z" axis
(defn RotZ [angle]
    (fn [[theta, phi]]
      (up
        theta
        (+ phi angle))))

;; Compose with "coordinate" to extract `q` from local tuple (t, q, qdot)
(defn F-tilde [angle]
  (compose (RotZ angle) coordinate))

(def F-tilde-rotated-by-s (F-tilde 's))

;; Lagrangian after "s" degree rotation about X-axis
(def L-ellipsoid-sym-rotated
    (fn [q-prime]
          ((compose L-ellipsoid-sym (F->C F-tilde-rotated-by-s))
           q-prime)))

(rendermd
 (let [state (up (literal-function 'theta) (literal-function 'phi))
       local ((Gamma state) 't)
       ]
     (L-ellipsoid-sym-rotated local)))
```


{% mathjax() %}$$
\frac{1}{2}\,{a}^{2}\,m\,{\cos}^{2}\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2} + \frac{1}{2}\,{a}^{2}\,m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\phi\left(t\right)\right)}^{2} + \frac{1}{2}\,{c}^{2}\,m\,{\left(D\theta\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\theta\left(t\right)\right)
$$
{% end %} 





The symmetry about $z$ axis is verified as the Lagrangian is unchanged post-rotation as shown above.

```clojure
;; Define the Noether integral
(def the-Noether-integral
    (* ((partial 2) L-ellipsoid-sym) ((D F-tilde) 0 )))

(rendermd
(the-Noether-integral
  (up 't
      (up 'theta 'phi)
      (up 'thetadot 'phidot))))
```


{% mathjax() %}$$
{a}^{2}\,m\,\dot {\phi}\,{\sin}^{2}\left(\theta\right)
$$
{% end %} 





The conserved quantity is $m (a\sin{\theta})^2\dot{\phi}$. Here, $\dot{\phi}$ is the rate of angular movement of the particle about the $z$ axis or the rate of change of longitude, and $a\sin(\theta)$ is the "radius". This quantity is analogous to angular momentum.
