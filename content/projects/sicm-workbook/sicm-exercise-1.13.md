+++
title = "Exercise 1.13: Higher-derivative Lagrangians"
date = "2022-11-01T01:56:16Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++







### Exercise 1.13: Higher-derivative Lagrangians

**a. Write a procedure to compute the Lagrange equations for Lagrangians that depend upon acceleration, as in exercise 1.10. Note that Gamma can take an optional argument giving the length of the initial segment of the local tuple needed. The default length is 3, giving components of the local tuple up to and including the velocities.**



Lagrange's equations for Lagrangians that depend on acceleration was derived as:


{% mathjax() %}
$$
D^2(\partial_3 L \cdot \Gamma[q]) − D(\partial_2 L\cdot \Gamma[q])+\partial_1 L\cdot \Gamma[q]=0\\
$$
{% end %}



```clojure
(defn Lagrange-equations-accel [L]
    (fn [q]
        (let [state-path (Gamma q 4)]
                   (+ (D (D (compose ((partial 3) L) state-path)))
                      (-(D (compose ((partial 2) L) state-path)))
                      (compose ((partial 1) L) state-path))
            )))
```


    #'user/Lagrange-equations-accel





---
**b. Use your procedure to compute the Lagrange equations for the Lagrangian:**


{% mathjax() %}
$$
L(t, x, v, a) = - \frac{1}{2} m x a - \frac{1}{2} k x^2\\
$$
{% end %}



```clojure
(defn L-accel [m k]
    (fn [ [_ [x] [v] [a]] ]
        (- (* -1/2 m x a) (* 1/2 'k (square x)))))

(def eom-L-accel
        (Lagrange-equations-accel (L-accel 'm 'k)))


(rendertexvec  (let [state (up (literal-function 'x))]
            ((eom-L-accel state) 't)))
```

{% mathjax() %}
\begin{pmatrix}\displaystyle{- k\,x\left(t\right) - m\,{D}^{2}x\left(t\right)}\end{pmatrix}
{% end %}




---
**c. For more fun, write the general Lagrange equation procedure that takes a Lagrangian that depends on any number of derivatives, and the number of derivatives, to produce the required equations of motion.**



The Generaized Lagrange's Equation seems like a sum of alternate signed terms based on examination. 


{% mathjax() %}
$$
L = \sum_{i=0}^{n} (-1)^i D^i \left( \partial_{i+1} L \cdot \Gamma[q] \right)
$$
{% end %}


