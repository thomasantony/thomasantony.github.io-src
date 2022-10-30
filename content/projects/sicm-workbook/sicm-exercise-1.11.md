+++
title = "Exercise 1.11: Kepler's Third Law"
date = "2022-10-31T01:33:12Z"
draft = false

[extra]
latex = true
+++





### Exercise 1.11: Kepler's third law

**A Lagrangian suitable for studying the relative motion of two particles, of masses $m_1$ and $m_2$, with potential energy $V$, is:**


{% mathjax() %}
$$
L = \frac{1}{2} m \left(\dot{r}^2 + (r\dot{\phi})^2\right) + V(r)
$$
{% end %}




**The argument $m$ is the reduced mass of the system:**


{% mathjax() %}
$$
m = \frac{m_1 m_2}{m_1 + m_2}
$$
{% end %}




**For gravity, the potential energy function is:**


{% mathjax() %}
$$
V(r) = -\frac{G m_1 m_2}{r}
$$
{% end %}




**Consider the simple situation of the particles in circular orbits around their common center of mass. Construct a circular orbit and plug it into the Lagrange equations. Show that the residual gives Kepler's law:**


{% mathjax() %}
$$
n^2 a^3 = G(m_1 + m_2)
$$
{% end %}




**where $n$ is the angular frequency of the orbit and a is the distance between particles.**

```clojure
;; Define Lagrangian and derive EoMs
(defn L-central-polar [m V]
    (fn [[_ [r phi] [rdot phidot]]] 
      (- (* 1/2 m
            (+ (square rdot) (square (* r phidot))) )
         (V r))
        ))

(def m (/ (* 'm_1 'm_2) (+ 'm_1 'm_2) ))
(def V (fn [r] (- (/ (* 'G 'm_1 'm_2) r))))

(def eom-kepler 
        (Lagrange-equations (L-central-polar m V)))

(rendertexvec (let [state (up (literal-function 'r) (literal-function 'phi))]
            ((eom-kepler state) 't)))
```

```clojure
;; Circular orbit
; r(t) = a
; phi(t) = n * t  
(def circ-solution
  (up (fn [t] 'a) (fn [t] (* 'n t))))
(rendertex (circ-solution 't))
```

```clojure
(rendertexvec ((eom-kepler circ-solution) 't))
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{\frac{- {a}^{3}\,m_1\,m_2\,{n}^{2} + G\,{m_1}^{2}\,m_2 + G\,m_1\,{m_2}^{2}}{{a}^{2}\,m_1 + {a}^{2}\,m_2}} \cr \cr \displaystyle{0}\end{pmatrix}
$$
{% end %}





The above equation simplifies to:


{% mathjax() %}
$$
\begin{align*}
-a^3 m_1 m_2 n^2 + G m_1 m_2 (m_1 + m_2) &= 0 \\
=> G (m_1 + m_2) &= a^3 n^2\\
\end{align*}
$$
{% end %}


