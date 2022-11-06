+++
title = "Section 1.8.3: Central Forces in Three Dimensions"
date = "2022-11-06T00:16:30Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++







## 1.8.3 Central Forces in Three Dimensions

Consider the motion of a particle in a potential field $V(r)$ in three dimensions using spherical coordinates, $r, \theta, \varphi$, where $\theta$ is the colatitude and $\varphi$ is the longitude. The kinetic energy is:

{% mathjax() %}
$$
T(t; r, \theta, \varphi; \dot{r}, \dot{\theta}, \dot{\varphi} = \frac{1}{2} m \left(\dot{r}^2 + r^2\dot{\theta}^2 + r^2(\sin\theta)^2\dot{\varphi}^2 \right)
$$
{% end %}



```clojure
(defn T3-spherical [m]
    (fn [[_, [r, theta, _], [rdot, thetadot, phidot]]]
      (* 1/2 m
         (+ (square rdot)
            (square (* r thetadot))
            (square (* r (sin theta) phidot))))))

;; Lagrangian = T-V
(defn L3-central [m Vr]
  (defn Vs [[_, [r, _, _], _]]
      (Vr r))
  (- (T3-spherical m) Vs))
```


    #'user/L3-central



```clojure
;; The generalized forces can be computed by taking the partial derivative of the Lagrangian w.r.t the coordinates
(rendertex ( ((partial 1) (L3-central 'm (literal-function 'V)))
             (up 't
                 (up 'r 'theta 'phi)
                 (up 'rdot 'thetadot 'phidot))))

;; Here \varphi is a "cyclic coordinate" as it does not appear in the Lagrangian explicitly 
;; and hence does not have a force associated with it
```

{% mathjax() %}
\begin{bmatrix}\displaystyle{m\,{\dot {\phi}}^{2}\,r\,{\sin}^{2}\left(\theta\right) + m\,r\,{\dot {\theta}}^{2} - DV\left(r\right)} \cr \cr \displaystyle{m\,{\dot {\phi}}^{2}\,{r}^{2}\,\sin\left(\theta\right)\,\cos\left(\theta\right)} \cr \cr \displaystyle{0}\end{bmatrix}
{% end %}


```clojure
;; Compute the momenta by taking partial derivative w.r.t generalized velocities
(rendertex ( ((partial 2) (L3-central 'm (literal-function 'V)))
             (up 't
                 (up 'r 'theta 'phi)
                 (up 'rdot 'thetadot 'phidot))))
```

{% mathjax() %}
\begin{bmatrix}\displaystyle{m\,\dot r} \cr \cr \displaystyle{m\,{r}^{2}\,\dot {\theta}} \cr \cr \displaystyle{m\,\dot {\phi}\,{r}^{2}\,{\sin}^{2}\left(\theta\right)}\end{bmatrix}
{% end %}




The momentum conjugate to $\varphi$ is conserved. We can show that this is actually the $z$ component of the angular momentum vector $r \times (m\vec{v})$, for position $\vec{r}$ and linear momentum $m\vec{v}$ by writing the $z$ component of the angular momentum in spherical coordinates:

```clojure
;; z component of ang momentum
(defn ang-mom-z [m]
    (fn [[_, xyz, v]]
        (ref (cross-product xyz (* m v)) 2)))

;; Coordinate conversion
(defn s->r2 [[_, [r, theta, phi]]]
      (let [x (* r (sin theta) (cos phi))
            y (* r (sin theta) (sin phi))
            z (* r (cos theta))]
        (up x y z)))

(rendermd
 ((compose (ang-mom-z 'm) (F->C s->r))
  (up 't
     (up 'r 'theta 'phi)
     (up 'rdot 'thetadot 'phidot)))) 

;; results in m phidot r² sin²(θ) which is equal to the momentum conjugate of phi
```


{% mathjax() %}$$
m\,\dot {\phi}\,{r}^{2}\,{\sin}^{2}\left(\theta\right)
$$
{% end %}





Since the choice of $z$ axis arbitrary based on the coordinate system, if one component is conserved, then all components are conserved. Therefore, angular momentum is conserved. We can **choose** the $z$ axis such that all the angular momentum is in the $z$ component. 

So for a general position vector $\vec{x}$, since $\vec{x}\cdot L = \vec{x}\cdot(m\vec{x}\times\vec{v}) = \vec{v}\cdot(\vec{x}\times\vec{x}) = 0$ ( from the scalar triple product), the motion is confined to the plane perpendicular to the angular momentum i.e., colatitude $\theta = \pi/2$ and $\dot{\theta} = 0$. This motion was discussed before in Section 1.6

Ref: [https://physics.stackexchange.com/q/731892/47598](https://physics.stackexchange.com/q/731892/47598)

Computing the energy from the Lagrangian, we can see that it does equal $T+V$

```clojure
(rendermd
  ((Lagrangian->energy (L3-central 'm (literal-function 'V)))
   (up 't
       (up 'r 'theta 'phi)
       (up 'rdot 'thetadot 'phidot))))

;; The energy is conserved because the Lagrangian has no explicit time dependence.
```


{% mathjax() %}$$
\frac{1}{2}\,m\,{\dot {\phi}}^{2}\,{r}^{2}\,{\sin}^{2}\left(\theta\right) + \frac{1}{2}\,m\,{r}^{2}\,{\dot {\theta}}^{2} + \frac{1}{2}\,m\,{\dot r}^{2} + V\left(r\right)
$$
{% end %}


