+++
title = "Exercise 1.14: Coordinate-independence of Lagrange Equations"
date = "2022-11-01T01:56:19Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++






### Exercise 1.14: Coordinate-independence of Lagrange equations

**Check that the Lagrange equations for central force motion in polar coordinates and in rectangular coordinates are equivalent.**

**In order to do this, compute the expressions for accelerations $a_x(t)$ and $a_y(t)$ in terms of the polar coordinates and substitute into the lagrange's equations in cartesian coordinates.**

```clojure
(defn L-central-rectangular [m U]
    (fn [[_  [x y] [v_x v_y]]]
        (let [r (sqrt (+ (square x) (square y)))]
            (- (* 1/2 m (+ (square v_x) (square v_y))) (U r)))))


(def eom-central-rectangular (let [L (L-central-rectangular 'm (literal-function 'U))]
                                 (Lagrange-equations L)))


(def eom-central-r2p (let [r (literal-function 'r)
     phi (literal-function 'varphi)
     rt (literal-function 'r)
     x (* r (cos phi))
     y (* r (sin phi))
     v_x (D x)
     v_y (D y)
     a_x (D v_x)
     a_y (D v_y)
     state (up x y)
     eom ((eom-central-rectangular state) 't)
     ]
        (apply up eom)
    ))
(rendertex eom-central-r2p)
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{- m\,\cos\left(\varphi\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,r\left(t\right) -2\,m\,D\varphi\left(t\right)\,\sin\left(\varphi\left(t\right)\right)\,Dr\left(t\right) - m\,r\left(t\right)\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}\varphi\left(t\right) + m\,\cos\left(\varphi\left(t\right)\right)\,{D}^{2}r\left(t\right) + \cos\left(\varphi\left(t\right)\right)\,DU\left(r\left(t\right)\right)} \cr \cr \displaystyle{- m\,{\left(D\varphi\left(t\right)\right)}^{2}\,r\left(t\right)\,\sin\left(\varphi\left(t\right)\right) + 2\,m\,\cos\left(\varphi\left(t\right)\right)\,D\varphi\left(t\right)\,Dr\left(t\right) + m\,\cos\left(\varphi\left(t\right)\right)\,r\left(t\right)\,{D}^{2}\varphi\left(t\right) + m\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}r\left(t\right) + \sin\left(\varphi\left(t\right)\right)\,DU\left(r\left(t\right)\right)}\end{pmatrix}
$$
{% end %}



```clojure
(let [eom eom-central-r2p
      eom1 (ref eom 0)
      eom2 (ref eom 1)]
    (rendertexvec (up (simplify (+ eom1 eom2)))))
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{- m\,\cos\left(\varphi\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,r\left(t\right) - m\,{\left(D\varphi\left(t\right)\right)}^{2}\,r\left(t\right)\,\sin\left(\varphi\left(t\right)\right) + 2\,m\,\cos\left(\varphi\left(t\right)\right)\,D\varphi\left(t\right)\,Dr\left(t\right) + m\,\cos\left(\varphi\left(t\right)\right)\,r\left(t\right)\,{D}^{2}\varphi\left(t\right) -2\,m\,D\varphi\left(t\right)\,\sin\left(\varphi\left(t\right)\right)\,Dr\left(t\right) - m\,r\left(t\right)\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}\varphi\left(t\right) + m\,\cos\left(\varphi\left(t\right)\right)\,{D}^{2}r\left(t\right) + m\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}r\left(t\right) + \cos\left(\varphi\left(t\right)\right)\,DU\left(r\left(t\right)\right) + \sin\left(\varphi\left(t\right)\right)\,DU\left(r\left(t\right)\right)}\end{pmatrix}
$$
{% end %}





Rewriting the above equations, we get


{% mathjax() %}
$$
\begin{align*}
-mr\dot{\varphi}^2 \cos{\varphi} + (mr\ddot{\varphi} + 2m\dot{r}\dot{\varphi})(-\sin{\varphi}) + m\ddot{r}\cos{\varphi} + DU(r)\cos{\varphi} &= 0 \\
-mr\dot{\varphi}^2 \sin{\varphi} + (mr\ddot{\varphi} + 2m\dot{r}\dot{\varphi})\cos{\varphi} + m\ddot{r}\sin{\varphi} + DU(r)\sin{\varphi} &= 0
\end{align*}
$$
{% end %}




Multiply first eqn by $\cos{\varphi}$ and the second by $\sin{\varphi}$ and add


{% mathjax() %}
$$
-mr\dot{\varphi}^2 + m\ddot{r} + DU(r) = 0\\
$$
{% end %}




Multiply first eqn by $\sin{\varphi}$ and the second by $\cos{\varphi}$ and subtract to get


{% mathjax() %}
$$
mr \ddot{\varphi} + 2m\dot{r}\dot{\varphi} = 0\\
$$
{% end %}




These are the same equations of motion that we obtained by directly building the Lagrangian from polar coordinates.
