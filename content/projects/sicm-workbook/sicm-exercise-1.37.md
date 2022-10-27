+++
title = "Exercise 1.37: Velocity transformation"
date = "2022-10-27T05:15:14Z"
draft = false

[extra]
latex = true
+++



### Exercise 1.38: Velocity transformation

Use the procedure Gamma-bar to construct a procedure that transforms velocities given a coordinate transformation. Apply this procedure to the procedure `p->r` to deduce (again) equation (1.67) on page 42.


{% mathjax() %}
$$
\begin{align*}
v_x &= \dot{r} \cos{\varphi} − r \dot{\varphi} \sin{\varphi} \\
v_y &= \dot{r} \sin{\varphi} + r \dot{\varphi} \cos{\varphi}\tag{1.67}
\end{align*}
$$
{% end %}









We need to define a function `F->C_v` that takes a local tuple coordinate transformation function $F$ and returns a new local tuple function $C_v$. $C_v$ when evaluated on a local tuple, returns the expression for velocity in terms of the new coordinates.

If the fucntion $F$ is defined as $x = F(t, x')$, then $v = C_v(t, x', v')$.

We start with a path-dependent function $\bar{C_v}$ with path $q'$ as its input, defined as: 


{% mathjax() %}
$$
\bar{C_v}[q'] :=  \dot{Q} \circ \Gamma \left[ F \circ \Gamma[q'] \right]
$$
{% end %}



where $\dot{Q}$ is a selector function that extracts the velocity component of a local tuple. We get $C_v$ by applying the `Gamma-bar` function on $\bar{C_v}$


{% mathjax() %}
$$
C_v = \bar{\Gamma}[ \bar{C_v} ]
$$
{% end %}



```clojure
(defn F->C_v
    [F]
    (fn C_v [local]
        (let [f-bar (fn [q-prime]
                        (let [q (compose F (Gamma q-prime))] ;; q = F . Gamma[q']
                        (compose velocity (Gamma q))         ;; 
                    ))
              ]
        ((Gamma-bar f-bar) local))
))

(rendertex ((F->C_v p->r)
           (up 't (up 'r 'varphi) (up 'rdot 'varphidot)))
           )
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{- r\,\dot {\varphi}\,\sin\left(\varphi\right) + \dot r\,\cos\left(\varphi\right)} \cr \cr \displaystyle{r\,\dot {\varphi}\,\cos\left(\varphi\right) + \dot r\,\sin\left(\varphi\right)}\end{pmatrix}
$$
{% end %}





^ The above answer matches Eq. 1.67
