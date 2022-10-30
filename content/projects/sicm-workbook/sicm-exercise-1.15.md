+++
title = "Exercise 1.15: Equivalence"
date = "2022-10-31T01:09:08Z"
draft = false

[extra]
latex = true
+++







### Exercise 1.15: Equivalence

**Here we use the `p->r` conversion function to convert the Lagrangian in rectangular coordinates to polar coordinates (and compare to results from notes and exercise 1.14 where it was computed explicitly).**

```clojure
;; The Coordinate conversion function `C`
(defn p2r [[_ [r phi] [rdot phidot]]]
      (let [x (* r (cos phi))
            y (* r (sin phi))]
        (up x y)))

;; F->C is part of sicmutils and is more complex than in the book for this section
(defn F2C [F]
  (fn [local]
      (let [v (ref local 2)
            t (ref local 0)]
       (up t
       (F local)
       (+ (((partial 0) F) local)
          (* (((partial 1) F) local) v))))))

(defn L-central-rectangular [m U]
    (fn L [[_  [x y] [v_x v_y]]]
        (let [r (sqrt (+ (square x) (square y)))]
            (- (* 1/2 'm (+ (square v_x) (square v_y))) (U r)))))

;; L' = L . C
(defn L-central-polar-using-F2C [m U]
    (fn [q-prime]
        ((compose (L-central-rectangular m U) (F2C p2r))  
           q-prime)))

;; Verify LE in polar coordinates match what was expected
(let [L (L-central-polar-using-F2C 'm (literal-function 'U))
      state (up (literal-function 'r) (literal-function 'varphi))]
   (rendertex (((Lagrange-equations L) state) 't)))
```


{% mathjax() %}
$$
\begin{bmatrix}\displaystyle{- m\,r\left(t\right)\,{\left(D\varphi\left(t\right)\right)}^{2} + m\,{D}^{2}r\left(t\right) + DU\left(r\left(t\right)\right)}&\displaystyle{m\,{\left(r\left(t\right)\right)}^{2}\,{D}^{2}\varphi\left(t\right) + 2\,m\,r\left(t\right)\,D\varphi\left(t\right)\,Dr\left(t\right)}\end{bmatrix}
$$
{% end %}


