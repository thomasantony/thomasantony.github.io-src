+++
title = "Section 1.8.4: The Restricted Three Body Problem"
date = "2022-11-02T04:49:30Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++






## 1.8.4 The Restricted Three-Body Problem

Consider two bodies of masses $M_0$ and $M_1$ in circular orbits about their barycenter. Assume that a third particle has a small enough mass $m$ to not have any effect on the orbits of the other two objects. This third particle moves in a field of time-varying gravitational potential energy.

Let $a$ be the constant distance between the two bodies. If the center of mass is at the origin of the coordinate system, then the distances of the two bodies from the origin are given by:


{% mathjax() %}
$$
a_0 = \frac{M_1}{M_0 + M_1}a, \quad a_1 =  \frac{M_0}{M_0 + M_1}a\\
$$
{% end %}




Each body revolves around the barycenter with angular frequency $\Omega$, with radii as defined above. Kepler's Law gives the relation between $\Omega$ and $a$ as:


{% mathjax() %}
$$
\Omega^2a^3 = G(M_0 + M_1)
$$
{% end %}




We choose our axes so that at time $t_0$, mass $M_1$ is on the positive $\hat{x}$-axis and $M_0$ is on the negative $\hat{x}$-axis. The gravitational potential energy function is:


{% mathjax() %}
$$
V(t, r) = - \left(\frac{GM_0m}{r_0} + \frac{GM_1m}{r_1} \right)
$$
{% end %}




where:


{% mathjax() %}
$$
\begin{align}
r_0 &= \sqrt{(x-x_0)^2 + (y-y_0)^2} \\
r_1 &= \sqrt{(x-x_1)^2 + (y-y_1)^2} \\
\\
x_0 &= -a_0\cos(\Omega t) \\
y_0 &= -a_0\sin(\Omega t) \\
x_1 &=  a_1\cos(\Omega t) \\
y_1 &= -a_1\sin(\Omega t) \\
\Omega &= \frac{G(M_0+M_1)}{a^3} 
\end{align}
$$
{% end %}




It is convenient to instead use a coordinate frame that is rotating along with the two bigger bodies, such that the bodies appear fixed. place the axes so that the two bodies are on the new $\hat{x}'$ axis and we can choose rotating and non-rotating axes to be coincident at time, $t=0$. We can transform to the rotating rectangular coordinates as we did in Section 1.6.1 and get the new Lagrangian as


{% mathjax() %}
$$
L(t; x_r, y_r; \dot{x}_r, \dot{y}_r) = \frac{1}{2}m(\dot{x}_r^2 + \dot{y}_r^2) + \frac{1}{2}m\Omega^2(x_r^2 + y_r^2) + m\Omega(x_r \dot{y}_r - \dot{x}_r y_r) + \frac{G M_0 m}{r_0} + \frac{G M_1 m}{r_1} \tag{1.150}
$$
{% end %}




where now $r_0^2 = (x_r - -a_0)^2 + (y_r-0)^2$ and $r_0^2 = (x_r - a_1)^2 + (y_r-0)^2$.

This Lagrangian in rotating coordinates is *independent* of time. Therefore the energy state function defined by this Lagrangian is conserved. Since it is clearest if we express this in terms of $\Omega$, $a_0$ and $a_1$, we should make those explicit parameters to the Lagrangian.

```clojure
(defn L0 [m V]
  (fn [[t, q, v]]
    (- (* 1/2 m (square v)) (V t q))
      ))

(defn V_3BP [a GM0 GM1 m]
    (fn [t [x y]]
      (let [Omega (sqrt (/ (+ GM0 GM1) (expt a 3)))
            a0 (* (/ GM1 (+ GM0 GM1)) a)
            a1 (* (/ GM0 (+ GM0 GM1)) a)
            x0 (* -1 a0 (cos (* Omega t)))
            y0 (* -1 a0 (sin (* Omega t)))
            x1 (* +1 a1 (cos (* Omega t)))
            y1 (* +1 a1 (sin (* Omega t)))
            r0 (sqrt (+ (square (- x x0)) (square (- y y0))))
            r1 (sqrt (+ (square (- x x1)) (square (- y y1))))]
        (- (+ (/ (* GM0 m) r0) (/ (* GM1 m) r1))))))

(defn LR3B [m a0 a1 Omega GM0 GM1]
    (fn [[t, q, qdot]]
  (let [x (ref q 0)
        y (ref q 1)
        r0 (sqrt (+ (square (+ x a0)) (square y)))
        r1 (sqrt (+ (square (- x a1)) (square y)))
        xdot (ref qdot 0)
        ydot (ref qdot 1)]
        (+ (* 1/2 m (square qdot))
           (* 1/2 m (square Omega) (square q))
           (* m Omega (- (* x ydot) (* xdot y)))
           (/ (* GM0 m) r0) (/ (* GM1 m) r1)))))


(rendermd (
(Lagrangian->energy 
  (LR3B 'm 'a_0 'a_1 'Omega 'GM_0 'GM_1)
)
 (up 't (up 'x_r 'y_r) (up 'v_rx 'v_ry)))
)
```


{% mathjax() %}$$
\frac{\frac{-1}{2}\,{\Omega}^{2}\,m\,{x_r}^{2}\,\sqrt {{a_0}^{2}\,{a_1}^{2} -2\,{a_0}^{2}\,a_1\,x_r + {a_0}^{2}\,{x_r}^{2} + {a_0}^{2}\,{y_r}^{2} + 2\,a_0\,{a_1}^{2}\,x_r -4\,a_0\,a_1\,{x_r}^{2} + 2\,a_0\,{x_r}^{3} + 2\,a_0\,x_r\,{y_r}^{2} + {a_1}^{2}\,{x_r}^{2} + {a_1}^{2}\,{y_r}^{2} -2\,a_1\,{x_r}^{3} -2\,a_1\,x_r\,{y_r}^{2} + {x_r}^{4} + 2\,{x_r}^{2}\,{y_r}^{2} + {y_r}^{4}} + \frac{-1}{2}\,{\Omega}^{2}\,m\,{y_r}^{2}\,\sqrt {{a_0}^{2}\,{a_1}^{2} -2\,{a_0}^{2}\,a_1\,x_r + {a_0}^{2}\,{x_r}^{2} + {a_0}^{2}\,{y_r}^{2} + 2\,a_0\,{a_1}^{2}\,x_r -4\,a_0\,a_1\,{x_r}^{2} + 2\,a_0\,{x_r}^{3} + 2\,a_0\,x_r\,{y_r}^{2} + {a_1}^{2}\,{x_r}^{2} + {a_1}^{2}\,{y_r}^{2} -2\,a_1\,{x_r}^{3} -2\,a_1\,x_r\,{y_r}^{2} + {x_r}^{4} + 2\,{x_r}^{2}\,{y_r}^{2} + {y_r}^{4}} + \frac{1}{2}\,m\,{v_{rx}}^{2}\,\sqrt {{a_0}^{2}\,{a_1}^{2} -2\,{a_0}^{2}\,a_1\,x_r + {a_0}^{2}\,{x_r}^{2} + {a_0}^{2}\,{y_r}^{2} + 2\,a_0\,{a_1}^{2}\,x_r -4\,a_0\,a_1\,{x_r}^{2} + 2\,a_0\,{x_r}^{3} + 2\,a_0\,x_r\,{y_r}^{2} + {a_1}^{2}\,{x_r}^{2} + {a_1}^{2}\,{y_r}^{2} -2\,a_1\,{x_r}^{3} -2\,a_1\,x_r\,{y_r}^{2} + {x_r}^{4} + 2\,{x_r}^{2}\,{y_r}^{2} + {y_r}^{4}} + \frac{1}{2}\,m\,{v_{ry}}^{2}\,\sqrt {{a_0}^{2}\,{a_1}^{2} -2\,{a_0}^{2}\,a_1\,x_r + {a_0}^{2}\,{x_r}^{2} + {a_0}^{2}\,{y_r}^{2} + 2\,a_0\,{a_1}^{2}\,x_r -4\,a_0\,a_1\,{x_r}^{2} + 2\,a_0\,{x_r}^{3} + 2\,a_0\,x_r\,{y_r}^{2} + {a_1}^{2}\,{x_r}^{2} + {a_1}^{2}\,{y_r}^{2} -2\,a_1\,{x_r}^{3} -2\,a_1\,x_r\,{y_r}^{2} + {x_r}^{4} + 2\,{x_r}^{2}\,{y_r}^{2} + {y_r}^{4}} - {GM}_0\,m\,\sqrt {{a_1}^{2} -2\,a_1\,x_r + {x_r}^{2} + {y_r}^{2}} - {GM}_1\,m\,\sqrt {{a_0}^{2} + 2\,a_0\,x_r + {x_r}^{2} + {y_r}^{2}}}{\sqrt {{a_0}^{2}\,{a_1}^{2} -2\,{a_0}^{2}\,a_1\,x_r + {a_0}^{2}\,{x_r}^{2} + {a_0}^{2}\,{y_r}^{2} + 2\,a_0\,{a_1}^{2}\,x_r -4\,a_0\,a_1\,{x_r}^{2} + 2\,a_0\,{x_r}^{3} + 2\,a_0\,x_r\,{y_r}^{2} + {a_1}^{2}\,{x_r}^{2} + {a_1}^{2}\,{y_r}^{2} -2\,a_1\,{x_r}^{3} -2\,a_1\,x_r\,{y_r}^{2} + {x_r}^{4} + 2\,{x_r}^{2}\,{y_r}^{2} + {y_r}^{4}}}
$$
{% end %}





With some "hand simplification (tbd)" this turns into:
```
(+ (* 1/2 m (expt v_r^x 2))
   (* 1/2 m (expt v_r^y 2))
   (/ (* -1 GM_0 m)
      (sqrt (+ (expt (+ x_r a_0) 2) (expt y_r 2))))
   (/ (* -1 GM_1 m)
      (sqrt (+ (expt (- x_r a_1) 2) (expt y_r 2))))
   (* -1/2 m (expt Omega 2) (expt x_r 2))
   (* -1/2 m (expt Omega 2) (expt y_r 2)))
```

If we separate this into a velocity-dependent part and a velocity-independent part we get

{% mathjax() %}
$$
\mathscr{E}(t; x_r, y_r; \dot{x}_r, \dot{y}_r) = \frac{1}{2} m (\dot{x}_r^2 + \dot{y}_r^2) + mU_r(x_r, y_r)\\
\text{where}\\
U_r(x_r, y_r) = - \left( \frac{GM_0}{r_0} + \frac{GM_1}{r_1} + \frac{1}{2} \Omega^2 (x_r^2 + y_r^2) \right)
$$
{% end %}




**This constant of motion is called the *Jacobi Constant***. This is traditionally defined as $C_\mathscr{J} = -2\mathscr{E}$. Note that this energy state function does not have terms that are linear in $\dot{x}_r$ or $\dot{y}_r$, although they appear in the Lagrangian.
