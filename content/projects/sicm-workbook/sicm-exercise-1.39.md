+++
title = "Exercise 1.39: Combining Lagrangians"
date = "2022-10-30T00:29:36Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++



### Exercise 1.39: Combining Lagrangians

**a. Make another primitive component, compatible with the spring-mass structures described in [this section](/projects/sicm-workbook/section-1.10.1-coordinate-constraints#building-systems-from-parts). For example, make a pendulum that can attach to the spring-mass system. Build a combination and derive the equations of motion. Be careful, the algebra is horrible if you choose bad coordinates.**




```clojure
;; Assume that the springs only move horizontally and are not affected by gravity
(defn LspringmassA [m_1 k_1]
    (fn L1 [[_, [x_1], [xdot_1]]]
        (- (* 1/2 m_1 (square xdot_1)) (* 1/2 k_1 (square x_1)))
    ))

(defn LspringmassB [m_2 k_2]
    (fn L2 [[_, [x_2, xi], [xdot_2, xidot]]]
        (- (* 1/2 m_2 (square (+ xdot_2 xidot))) (* 1/2 k_2 (square x_2)))
    ))

;; pendulum is attached at the end of the second spring-mass
;; x_3 defines the attachment point and is constrained to be equal to
;; X_1 + X_2 + x_1 + x_2
(defn L-pendulum [m l g]
    (fn L3 [[_, [x_3 theta], [x3_dot thetadot]]]
        (+ (* m (+ (* (square l) (square thetadot)) (square x3_dot))) (* m g l (cos theta)))
))

(defn L-system [m_1 m_2 m_3 k_1 k_2 l g]
    (fn L [[t, [x_1, x_2, x_3, xi, theta,lambda_1,lambda_2], [xdot_1, xdot_2, xdot_3, xidot, thetadot, lambdadot1, lambdadot2]]]
        (let [L1 (LspringmassA m_1 k_1)
              L2 (LspringmassB m_2 k_2)
              L3 (L-pendulum m_3 l g)
              phi1 (- xi (+ 'X_1 x_1)) ;; linking two spring-mass systems
              phi2 (- x_3 (+ 'X_1 x_1 'X_2 x_2)) ;; connecting pendulum to second spring-mass
              ]
            (+ (L1 (up t (up x_1) (down xdot_1)))
               (L2 (up t (up x_2 xi) (up xdot_2 xidot)))
               (L3 (up t (up x_3 theta) (up xdot_3 thetadot)))
               (* lambda_1 phi1)
               (* lambda_2 phi2)
            )
        )
))


(rendermd
 (let [state (up (literal-function 'x_1) (literal-function 'x_2) (literal-function 'x_3) 
                 (literal-function 'xi) (literal-function 'theta) 
                 (literal-function 'lambda_1) (literal-function 'lambda_2))
       local ((Gamma state) 't)]
    ((L-system 'm_1 'm_2 'm_3 'k_1 'k_2 'l 'g) local)))
```


{% mathjax() %}$$
{l}^{2}\,m_3\,{\left(D\theta\left(t\right)\right)}^{2} + g\,l\,m_3\,\cos\left(\theta\left(t\right)\right) + \frac{-1}{2}\,k_1\,{\left(x_1\left(t\right)\right)}^{2} + \frac{-1}{2}\,k_2\,{\left(x_2\left(t\right)\right)}^{2} + \frac{1}{2}\,m_1\,{\left(Dx_1\left(t\right)\right)}^{2} + \frac{1}{2}\,m_2\,{\left(Dx_2\left(t\right)\right)}^{2} + m_2\,Dx_2\left(t\right)\,D\xi\left(t\right) + \frac{1}{2}\,m_2\,{\left(D\xi\left(t\right)\right)}^{2} + m_3\,{\left(Dx_3\left(t\right)\right)}^{2} - X_1\,{\lambda}_1\left(t\right) - X_1\,{\lambda}_2\left(t\right) - X_2\,{\lambda}_2\left(t\right) - x_2\left(t\right)\,{\lambda}_2\left(t\right) - x_1\left(t\right)\,{\lambda}_1\left(t\right) - x_1\left(t\right)\,{\lambda}_2\left(t\right) + {\lambda}_1\left(t\right)\,\xi\left(t\right) + {\lambda}_2\left(t\right)\,x_3\left(t\right)
$$
{% end %}



```clojure
(def eom-system 
        (Lagrange-equations (L-system 'm_1 'm_2 'm_3 'k_1 'k_2 'l 'g)))

(rendertexvec (let [state (up (literal-function 'x_1) (literal-function 'x_2) (literal-function 'x_3) 
                         (literal-function 'xi) (literal-function 'theta) 
                         (literal-function 'lambda_1) (literal-function 'lambda_2))]
            ((eom-system state) 't)))
```

{% mathjax() %}
\begin{pmatrix}\displaystyle{k_1\,x_1\left(t\right) + m_1\,{D}^{2}x_1\left(t\right) + {\lambda}_1\left(t\right) + {\lambda}_2\left(t\right)} \cr \cr \displaystyle{k_2\,x_2\left(t\right) + m_2\,{D}^{2}x_2\left(t\right) + m_2\,{D}^{2}\xi\left(t\right) + {\lambda}_2\left(t\right)} \cr \cr \displaystyle{2\,m_3\,{D}^{2}x_3\left(t\right) - {\lambda}_2\left(t\right)} \cr \cr \displaystyle{m_2\,{D}^{2}x_2\left(t\right) + m_2\,{D}^{2}\xi\left(t\right) - {\lambda}_1\left(t\right)} \cr \cr \displaystyle{g\,l\,m_3\,\sin\left(\theta\left(t\right)\right) + 2\,{l}^{2}\,m_3\,{D}^{2}\theta\left(t\right)} \cr \cr \displaystyle{X_1 + x_1\left(t\right) - \xi\left(t\right)} \cr \cr \displaystyle{X_1 + X_2 + x_2\left(t\right) + x_1\left(t\right) - x_3\left(t\right)}\end{pmatrix}
{% end %}

