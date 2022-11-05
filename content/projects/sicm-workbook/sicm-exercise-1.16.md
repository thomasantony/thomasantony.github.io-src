+++
title = "Exercise 1.16: Central force motion"
date = "2022-10-31T01:09:03Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++







### Exercise 1.16: Central force motion

**Find Lagrangians for central force motion in three dimensions in rectangular coordinates and in spherical coordinates. First, find the Lagrangians analytically, then check the results with the computer by generalizing the programs that we have presented.**

```clojure
;; 3D central force Lagrange's eqns
(defn L-central-rect-3d [m U]
    (fn L [[_  [x y z] [v_x v_y v_z]]]
        (let [r (sqrt (+ (square x) (square y) (square z)))]
            (- (* 1/2 'm (+ (square v_x) (square v_y) (square v_z))) (U r)))))

(def eom-central-rect-3d (Lagrange-equations (L-central-rect-3d 'm (literal-function 'U))))

(rendertexvec
 (let [state (up (literal-function 'x) (literal-function 'y) (literal-function 'z))]
 ((eom-central-rect-3d state) 't)))
```

{% mathjax() %}
\begin{pmatrix}\displaystyle{\frac{m\,{D}^{2}x\left(t\right)\,\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}} + x\left(t\right)\,DU\left(\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}\right)}{\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}}} \cr \cr \displaystyle{\frac{m\,\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}\,{D}^{2}y\left(t\right) + y\left(t\right)\,DU\left(\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}\right)}{\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}}} \cr \cr \displaystyle{\frac{m\,\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}\,{D}^{2}z\left(t\right) + z\left(t\right)\,DU\left(\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}\right)}{\sqrt {{\left(x\left(t\right)\right)}^{2} + {\left(y\left(t\right)\right)}^{2} + {\left(z\left(t\right)\right)}^{2}}}}\end{pmatrix}
{% end %}


```clojure
(defn p2r-3d [[_ [r theta phi] _]]
      (let [x (* r (sin theta) (cos phi))
            y (* r (sin theta) (sin phi))
            z (* r (cos phi))]
        (up x y z)))

(defn L-central-polar-3d-using-F2C [m U]
    (fn [q-prime]
        ((compose (L-central-rect-3d m U) (F->C p2r-3d))
           q-prime)))

(def eom-central-polar-3d-using-F2C (Lagrange-equations (L-central-polar-3d-using-F2C 'm (literal-function 'U))))

(rendertex (let [state (up (literal-function 'r) (literal-function 'theta) (literal-function 'varphi))
        local ((Gamma state) 't)]
        (p2r-3d local)))
(render 
 (let [state (up (literal-function 'r) (literal-function 'theta) (literal-function 'varphi))
        local ((Gamma state) 't)
        L (L-central-polar-3d-using-F2C 'm (literal-function 'U))
       ]
     (L local)))

(rendertexvec
 (let [state (up (literal-function 'r) (literal-function 'theta) (literal-function 'varphi))
       ]
     ((eom-central-polar-3d-using-F2C state)'t)))

;; "exercise for the reader ..."
```

{% mathjax() %}
\begin{pmatrix}\displaystyle{\frac{- m\,r\left(t\right)\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} - m\,r\left(t\right)\,{\sin}^{2}\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} - m\,r\left(t\right)\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} + m\,r\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}\theta\left(t\right) - m\,r\left(t\right)\,\cos\left(\varphi\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}\varphi\left(t\right) + 2\,m\,\sin\left(\theta\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,Dr\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} -2\,m\,\cos\left(\varphi\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,D\varphi\left(t\right)\,Dr\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} + m\,{\sin}^{2}\left(\theta\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}r\left(t\right) + m\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}r\left(t\right) + {\sin}^{2}\left(\theta\left(t\right)\right)\,DU\left(r\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)\,DU\left(r\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\right)}{\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}}} \cr \cr \displaystyle{\frac{- m\,{\left(r\left(t\right)\right)}^{2}\,\sin\left(\theta\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,\cos\left(\theta\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} - m\,{\left(r\left(t\right)\right)}^{2}\,\sin\left(\theta\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,{\left(D\theta\left(t\right)\right)}^{2}\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} + m\,{\left(r\left(t\right)\right)}^{2}\,{\cos}^{2}\left(\theta\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}\theta\left(t\right) + 2\,m\,r\left(t\right)\,{\cos}^{2}\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,Dr\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} + m\,r\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}r\left(t\right) + r\left(t\right)\,\sin\left(\theta\left(t\right)\right)\,\cos\left(\theta\left(t\right)\right)\,DU\left(r\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\right)}{\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}}} \cr \cr \displaystyle{\frac{2\,m\,{\left(r\left(t\right)\right)}^{2}\,\sin\left(\theta\left(t\right)\right)\,D\varphi\left(t\right)\,\cos\left(\theta\left(t\right)\right)\,D\theta\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} + m\,{\left(r\left(t\right)\right)}^{2}\,\cos\left(\varphi\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,{\left(D\varphi\left(t\right)\right)}^{2}\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} - m\,{\left(r\left(t\right)\right)}^{2}\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}\varphi\left(t\right) - m\,{\left(r\left(t\right)\right)}^{2}\,{\cos}^{2}\left(\theta\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}\varphi\left(t\right) -2\,m\,r\left(t\right)\,{\cos}^{2}\left(\varphi\left(t\right)\right)\,D\varphi\left(t\right)\,Dr\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} -2\,m\,r\left(t\right)\,D\varphi\left(t\right)\,{\cos}^{2}\left(\theta\left(t\right)\right)\,Dr\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} - m\,r\left(t\right)\,\cos\left(\varphi\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}r\left(t\right) + 2\,m\,{\left(r\left(t\right)\right)}^{2}\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\,{D}^{2}\varphi\left(t\right) + 4\,m\,r\left(t\right)\,D\varphi\left(t\right)\,Dr\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)} - r\left(t\right)\,\cos\left(\varphi\left(t\right)\right)\,\sin\left(\varphi\left(t\right)\right)\,DU\left(r\left(t\right)\,\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}\right)}{\sqrt {{\sin}^{2}\left(\theta\left(t\right)\right) + {\cos}^{2}\left(\varphi\left(t\right)\right)}}}\end{pmatrix}
{% end %}

