+++
title = "Section 1.6 : How to Find Lagrangians"
date = "2022-11-02T03:45:51Z"
draft = false

[extra]
latex = true
+++







## 1.6 How to Find Lagrangians



It is possible to work back from Newton's second law and obtain the Lagrangian $L = T - V$. 

### Constant Acceleration

Consider a particle of mass $m$ in a gravitational field with acceleration, $g$. The potential energy is $mgh$ and kinetic energy is $\frac{1}{2} m v^2$. Therefore, a Lagrangian for the system is:


{% mathjax() %}
$$
L(t; x,y; v_x, v_y) = \frac{1}{2} m (v_x^2 + v_y^2) - mgy
$$


The EOMs for this system can be obtained by applying the EL equations as follows:

```clojure
(defn L-const-accel [m g]
    (fn [[_  [x y] [v_x v_y]]]
        (- (* 1/2 m (+ (square v_x) (square v_y))) (* m g y))))

(let [L (L-const-accel 'm 'g)
      state (up (literal-function 'x) (literal-function 'y))]
   (rendertex (((Lagrange-equations L) state) 't)))
```


{% mathjax() %}
$$
\begin{bmatrix}\displaystyle{m\,{D}^{2}x\left(t\right)} \cr \cr \displaystyle{g\,m + m\,{D}^{2}y\left(t\right)}\end{bmatrix}
$$
{% end %}





The above equations describe constant velocity in the $x$ direction and constant acceleration in the $y$ direction.



### Central Force Field

Consider the motion of a particle of mass $m$ through a potential field, $U(r)$ whose value depends only on the distance $r$ to the center of attraction (e.g. gravity). In rectangular coordinates, the Lagrangian is:


{% mathjax() %}
$$
L(t; x,y; v_x, v_y) =  \frac{1}{2} m (v_x^2 + v_y^2) - U(\sqrt{x^2 + y^2})
$$
{% end %}




Applying EL equations, the equations of motion can be derived as:

```clojure
(defn L-central-rectangular [m U]
    (fn [[_  [x y] [v_x v_y]]]
        (let [r (sqrt (+ (square x) (square y)))]
            (- (* 1/2 m (+ (square v_x) (square v_y))) (U r)))))

(def eom-central-rectangular (let [L (L-central-rectangular 'm (literal-function 'U))]
                                 (Lagrange-equations L)))

(let [state (up (literal-function 'x) (literal-function 'y))]
   (rendertex ((eom-central-rectangular state) 't)))
```


{% mathjax() %}
$$
\begin{bmatrix}\displaystyle{\frac{m\,{D}^{2}x\left(t\right)\,\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2}} + x\left(t\right)\,DU\left(\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2}}\right)}{\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2}}}} \cr \cr \displaystyle{\frac{m\,{D}^{2}y\left(t\right)\,\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2}} + y\left(t\right)\,DU\left(\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2}}\right)}{\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2}}}}\end{bmatrix}
$$
{% end %}





These equations can be rewriten as:


{% mathjax() %}
$$
m D^2 x(t) = -\frac{x(t)}{r(t)} DU(r(t)) \\
m D^2 y(t) = -\frac{y(t)}{r(t)} DU(r(t)) \\
\text{where }r(t) = \sqrt{x(t)^2 + y(t)^2}
$$
{% end %}




This is the same form as two components of $F = ma$ where the particle is acted upon by a radial force of magnitude $-D U(r)$. 

If we describe the system in polar coordinates instead, then $x = r \cos{\varphi} \text{ and } y = r \sin{\varphi}$. 

Consider a configuration path that is represented in both rectangular and polar coordinates. Let $\widetilde{x}$ and $\widetilde{y}$ be components of the rectangular coordinate path, and let $\widetilde{r}$ and $\widetilde{\varphi}$ be components of the corresponding polar coordinate path. Applying the above conversion and differentiating, we get:


{% mathjax() %}
$$
\begin{align}
\widetilde{x}(t) &= \widetilde{r}(t) \cos{ \widetilde{\varphi}(t) } \\
\widetilde{y}(t) &= \widetilde{r}(t) \sin{ \widetilde{\varphi}(t) } \\
=> D \widetilde{x}(t) &= D \widetilde{r}(t) \cos{\widetilde{\varphi}(t)} -  \widetilde{r}(t) \sin{\widetilde{\varphi}(t)} D \widetilde{\varphi}(t) \\
D \widetilde{y}(t) &= D \widetilde{r}(t) \sin{\widetilde{\varphi}(t)} +  \widetilde{r}(t) \cos{\widetilde{\varphi}(t)} D \widetilde{\varphi}(t) \\
=> v_x &= \dot{r}\cos{\varphi} - r\dot{\varphi} \sin{\varphi} \\
v_y &= \dot{r}\sin{\varphi} + r\dot{\varphi} \cos{\varphi}
\end{align}
$$
{% end %}




From the above expressions for generalized velocities, the expression for kinetic energy can be obtained as:


{% mathjax() %}
$$
T = \frac{1}{2} m ( \dot{r}^2 + r^2\dot{\varphi}^2 )
$$
{% end %}




And the Lagrangian as:


{% mathjax() %}
$$
L = \frac{1}{2} m ( \dot{r}^2 + r^2\dot{\varphi}^2 ) - U(r)
$$
{% end %}




Applying Lagrange's Equations, we get:

```clojure
(defn L-central-polar [m U]
    (fn [[_  [r phi] [rdot phidot]]]
            (- (* 1/2 m (+ (square rdot) (* (square r) (square phidot)))) (U r))))

(def eom-central-polar (let [L (L-central-polar 'm (literal-function 'U))]
                                 (Lagrange-equations L)))

(let [state (up (literal-function 'r) (literal-function 'varphi))]
   (rendertex ((eom-central-polar state) 't)))
```


{% mathjax() %}
$$
\begin{bmatrix}\displaystyle{- m\,{\left(D\varphi\left(t\right)\right)}^{2}\,r\left(t\right) + m\,{D}^{2}r\left(t\right) + DU\left(r\left(t\right)\right)} \cr \cr \displaystyle{2\,m\,D\varphi\left(t\right)\,r\left(t\right)\,Dr\left(t\right) + m\,{\left(r\left(t\right)\right)}^{2}\,{D}^{2}\varphi\left(t\right)}\end{bmatrix}
$$
{% end %}



```clojure
;; F->C in book
(defn F2C [F] 
    (fn [q-prime]
        ((Gamma (F q-prime)) 't)
    ))

(defn p2r [[_ [r phi] [rdot phidot]]]
      (let [x (* r (cos phi))
            y (* r (sin phi))]
        (up x y)))

;; Local tuple after coordinate conversion from polar -> rectilinear
(rendertex ((F2C p2r)
            (up 't 
                 (up (literal-function 'r) (literal-function 'phi))
                 (up (literal-function 'rdot) (literal-function 'phidot)))
            ))
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{t} \cr \cr \displaystyle{\begin{pmatrix}\displaystyle{r\left(t\right)\,\cos\left(\phi\left(t\right)\right)} \cr \cr \displaystyle{r\left(t\right)\,\sin\left(\phi\left(t\right)\right)}\end{pmatrix}} \cr \cr \displaystyle{\begin{pmatrix}\displaystyle{- r\left(t\right)\,\sin\left(\phi\left(t\right)\right)\,D\phi\left(t\right) + Dr\left(t\right)\,\cos\left(\phi\left(t\right)\right)} \cr \cr \displaystyle{r\left(t\right)\,\cos\left(\phi\left(t\right)\right)\,D\phi\left(t\right) + Dr\left(t\right)\,\sin\left(\phi\left(t\right)\right)}\end{pmatrix}}\end{pmatrix}
$$
{% end %}





The first equation says that mass times radial acceleration is equal to the sum of the force due to the potential field ($U(r)$) and the centrifugal force $mr\dot{\varphi}^2$. The second equation can be interpreted as $\frac{d}{dt}(mr^2 \dot{\varphi}) = 0$ or that the angular momentum is conserved.
