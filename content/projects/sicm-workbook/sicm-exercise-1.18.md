+++
title = "Exercise 1.18: Bead on a triaxial surface"
date = "2022-10-31T01:02:48Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++



### Exercise 1.18: Bead on a triaxial surface

**A bead of mass $m$ moves without friction on a triaxial ellipsoidal surface. In rectangular coordinates the surface satisfies**

{% mathjax() %}
$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
$$
{% end %}

**for some constants $a$, $b$, and $c$. Identify suitable generalized coordinates, formulate a Lagrangian, and find Lagrange's equations.**







The parameteric equations for an ellipsoid are:

{% mathjax() %}
$$
\begin{align*}
x &= a\sin{\theta}\cos{\varphi} \\
y &= b\sin{\theta}\sin{\varphi} \\
z &= c\cos{\theta}
\end{align*}
$$
{% end %}



```clojure
(defn L-free-particle [mass]
    (fn [[_ _ v]]
        (* 1/2 mass (dot-product v v)))   
)

(defn elliptical->rect [a b c]
    (fn [[_ [theta phi] _]]
        (up (* a (sin theta) (cos phi))
        (* b (sin theta) (sin phi))
        (* c (cos theta)))))

;; ;; L' = L . C
(defn L-ellipsoid [m a b c]
    (fn [q-prime]
          ((compose (L-free-particle m) (F->C (elliptical->rect a b c)))
           q-prime)))

(def eom-ellipsoid  
 (let [L (L-ellipsoid 'm 'a 'b 'c)]
    (Lagrange-equations L)
))

(rendertexvec
 (let [state (up (literal-function 'theta) (literal-function 'varphi))]
     ((eom-ellipsoid state) 't)))
```

{% mathjax() %}
\begin{pmatrix}\displaystyle{- {a}^{2}\,m\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,\sin\left(\theta\left(t\right)\right) - {a}^{2}\,m\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2} -2\,{a}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,{\cos}^{2}\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,D\varphi\left(t\right)\,\sin\left(\varphi\left(t\right)\right) + 2\,{b}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,{\cos}^{2}\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,D\varphi\left(t\right)\,\sin\left(\varphi\left(t\right)\right) - {b}^{2}\,m\,\cos\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,\sin\left(\theta\left(t\right)\right)\,{\sin}^{2}\left(\varphi\left(t\right)\right) - {b}^{2}\,m\,\cos\left(\theta\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\varphi\left(t\right)\right) + {a}^{2}\,m\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,{\cos}^{2}\left(\theta\left(t\right)\right)\,{D}^{2}\theta\left(t\right) - {a}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}\varphi\left(t\right) + {b}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}\varphi\left(t\right) + {b}^{2}\,m\,{\cos}^{2}\left(\theta\left(t\right)\right)\,{\sin}^{2}\left(\varphi\left(t\right)\right)\,{D}^{2}\theta\left(t\right) + {c}^{2}\,m\,\cos\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,\sin\left(\theta\left(t\right)\right) + {c}^{2}\,m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{D}^{2}\theta\left(t\right)} \cr \cr \displaystyle{{a}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\theta\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right) + {a}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,\sin\left(\varphi\left(t\right)\right) + 2\,{a}^{2}\,m\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,D\varphi\left(t\right)\,{\sin}^{2}\left(\varphi\left(t\right)\right) + 2\,{b}^{2}\,m\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,D\varphi\left(t\right) - {b}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,{\sin}^{2}\left(\theta\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right) - {b}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,\sin\left(\varphi\left(t\right)\right) - {a}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}\theta\left(t\right) + {a}^{2}\,m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\sin}^{2}\left(\varphi\left(t\right)\right)\,{D}^{2}\varphi\left(t\right) + {b}^{2}\,m\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{D}^{2}\varphi\left(t\right) + {b}^{2}\,m\,\cos\left(\varphi\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,{D}^{2}\theta\left(t\right)}\end{pmatrix}
{% end %}
