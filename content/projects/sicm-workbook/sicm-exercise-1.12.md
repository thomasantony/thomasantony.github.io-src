+++
title = "Exercise 1.12: Lagrange's Equations"
date = "2022-11-01T01:59:57Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++







### Exercise 1.12: Lagrange's Equations

**Compute Lagrange's equations for the Lagrangians in exercise 1.9 using the Lagrange-equations procedure.**

---
**a. An ideal planar pendulum consists of a bob of mass m connected to a pivot by a massless rod of length $l$ subject to uniform gravitational acceleration g. A Lagrangian is $L(t, \theta, \dot{\theta}) = \frac{1}{2} m l^2 \dot{\theta}^2 + m g l\cos{\theta}$ . The formal parameters of $L$ are $t$, $\theta$, and $\dot{\theta}$; $\theta$ measures the angle of the pendulum rod to a plumb line and $\dot{\theta}$ is the angular velocity of the rod.**

```clojure
(defn L-pendulum [m g l]
    (fn [[_ [theta] [thetadot]]] 
      (+ (* 1/2 m (square l) (square thetadot))
         (* m g l (cos theta)))))

(def eom-pendulum 
        (Lagrange-equations (L-pendulum 'm 'g 'l)))

(rendertex (let [state (up (literal-function 'theta))]
            ((eom-pendulum state) 't)))
```


{% mathjax() %}
$$
\begin{bmatrix}\displaystyle{g\,l\,m\,\sin\left(\theta\left(t\right)\right) + {l}^{2}\,m\,{D}^{2}\theta\left(t\right)}\end{bmatrix}
$$
{% end %}





--- 
**b. A particle of mass m moves in a two-dimensional potential $V(x, y) = (x^2 + y^2)/2 + x^2y − y^3/3$, where $x$ and $y$ are rectangular coordinates of the particle. A Lagrangian is $L(t;x,y;v_x,v_y)=\frac{1}{2} m (v_x^2+v_y^2) − V(x,y)$.**

```clojure
(defn potential-field [x y] 
    (+ (/ (+ (square x) (square y)) 2)
       (* (square x) y)
       (- (/ (cube y) 3))
    ))
(defn L-particle-potential-field [m V]
    (fn [[_ [x y] [v_x v_y]]] 
      (- (* 1/2 m (+ (square v_x) (square v_y)))
         (V x y))))

(def eom-particle-potential-field 
        (Lagrange-equations (L-particle-potential-field 'm potential-field)))

(rendertexvec (let [state (up (literal-function 'x) (literal-function 'y))]
            ((eom-particle-potential-field state) 't)))
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{m\,{D}^{2}x\left(t\right) + 2\,x\left(t\right)\,y\left(t\right) + x\left(t\right)} \cr \cr \displaystyle{m\,{D}^{2}y\left(t\right) + {\left(x\left(t\right)\right)}^{2} - {\left(y\left(t\right)\right)}^{2} + y\left(t\right)}\end{pmatrix}
$$
{% end %}





--- 
**c. A Lagrangian for a particle of mass m constrained to move on a sphere of radius $R$ is $L(t;\theta,\phi;\alpha,\beta)=\frac{1}{2}mR^2(\alpha^2+(\beta \sin\theta)^2)$. The angle $\theta$ is the colatitude of the particle and $\phi$ is the longitude; the rate of change of the colatitude is $\alpha$ and the rate of change of the longitude is $\beta$.**

```clojure
(defn L-particle-on-sphere [m R]
    (fn [[_ [theta phi] [alpha beta]]] 
        (* 1/2 m (square R) 
                 (+ (square alpha) 
                    (square (* beta (sin theta)))
                  )
        )
))

(def eom-particle-on-sphere
        (Lagrange-equations (L-particle-on-sphere 'm 'R)))

(rendertexvec  (let [state (up (literal-function 'theta) (literal-function 'phi))]
            ((eom-particle-on-sphere state) 't)))
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{- {R}^{2}\,m\,\sin\left(\theta\left(t\right)\right)\,{\left(D\phi\left(t\right)\right)}^{2}\,\cos\left(\theta\left(t\right)\right) + {R}^{2}\,m\,{D}^{2}\theta\left(t\right)} \cr \cr \displaystyle{2\,{R}^{2}\,m\,\sin\left(\theta\left(t\right)\right)\,D\phi\left(t\right)\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right) + {R}^{2}\,m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{D}^{2}\phi\left(t\right)}\end{pmatrix}
$$
{% end %}


