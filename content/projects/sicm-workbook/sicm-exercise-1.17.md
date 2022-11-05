+++
title = "Exercise 1.17: Bead on a helical wire"
date = "2022-10-31T01:02:55Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++







### Exercise 1.17: Bead on a helical wire

**A bead of mass $m$ is constrained to move on a frictionless helical wire. The helix is oriented so that its axis is horizontal. The diameter of the helix is $d$ and its pitch (turns per unit length) is $h$. The system is in a uniform gravitational field with vertical acceleration $g$. Formulate a Lagrangian that describes the system and find the Lagrange equations of motion.**



The system here has a single degree of freedom - the parameter $s$ describing the horizontal position of the bead along the x-axis. Let $r$ be the radius of the helix. The bead advances horizontally by distance $1/h$ for every rotation around the helix. The angle around the helix is equal to $\frac{2\pi}{1/h}s = 2\pi hs$.

So when $s = 0$, $x, y, z = 0, 0, 0$. Halfway up the first loop, 


{% mathjax() %}
$$
s = \frac{1}{2h}\\
x = s = \frac{1}{2h},\\
y = r \cos{\left(2\pi h \frac{1}{2h}\right)} = r\cos{\pi},\\
y = r \sin{\left(2\pi h \frac{1}{2h}\right)} = r\sin{\pi},\\
$$
{% end %}




The coordinates of the bead in rectangular coordinates are:


{% mathjax() %}
$$
\begin{align*}
x(t) &= s(t) \\
y(t) &= \frac{d}{2} \cos{2 \pi h s} \\
y(t) &= \frac{d}{2} \sin{2 \pi h s} \\
\end{align*}
$$
{% end %}




The velocities in rectangular coordinates are:


{% mathjax() %}
$$
\begin{align*}
v_x(t) &= \dot{s}\\
v_y(t) &= -\pi d h \dot{s} \sin{2 \pi h s}  \\
v_z(t) &= \pi d h \dot{s} \cos{2 \pi h s} \\
\end{align*}
$$
{% end %}




The kinetic energy in generalized coordinates is:


{% mathjax() %}
$$
\begin{align*}
T(t,s,\dot{s}) &= \frac{1}{2} m \left({v_x}^2 + {v_y}^2 + {v_z}^2\right) \\
               &= \frac{1}{2} m \left( \dot{s}^2 + \left( \pi^2 d^2 h^2 \dot{s}^2 \right) (\sin^2{2 \pi h s} + \cos^2{2 \pi h s}) \right) \\
               &= \frac{1}{2} m \dot{s}^2 \left( 1 + \pi^2 d^2 h^2 \right)
\end{align*}
$$
{% end %}




The potential energy in generalized coordinates is:

{% mathjax() %}
$$
V(t,s,\dot{s}) = mgy(t) = m g \frac{d}{2} \cos{2 \pi h s}
$$
{% end %}



```clojure
;; Computing EoMs
(defn T-bead-helical [m g d h]
    (fn [[t [s] [sdot]]]
        (* 1/2 m (square sdot) 
           (+ 1 (square 'pi) (square d) (square h))
        )
    )
)

(defn V-bead-helical [m g d h]
    (fn [[t [s] [sdot]]]
        (* m g (/ d 2) (cos (* 2 'pi h s)))
))

(def L-bead-helical (- T-bead-helical V-bead-helical))
    
(render
 (let [local ((Gamma (up (literal-function 's))) 't)
       L (L-bead-helical 'm 'g 'd 'h)
       ]
     (L local)
     ))

;; EOMs for bead on helical wire under gravity
(let [L (L-bead-helical 'm 'g 'd 'h)
      state (up (literal-function 's))]
   (rendertex (((Lagrange-equations L) state) 't)))
```

{% mathjax() %}
\begin{bmatrix}\displaystyle{- d\,g\,h\,m\,\pi\,\sin\left(2\,h\,\pi\,s\left(t\right)\right) + {d}^{2}\,m\,{D}^{2}s\left(t\right) + {h}^{2}\,m\,{D}^{2}s\left(t\right) + m\,{\pi}^{2}\,{D}^{2}s\left(t\right) + m\,{D}^{2}s\left(t\right)}\end{bmatrix}
{% end %}




The equations of motion for the bead on a helical wire is derived as:

{% mathjax() %}
$$
\ddot{s} = \frac{dgh\pi \sin{\left( 2\pi h s \right)}} { d^2  + h^2  +  \pi^2 + 1 }
$$
{% end %}


