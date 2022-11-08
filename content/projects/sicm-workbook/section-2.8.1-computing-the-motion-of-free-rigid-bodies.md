+++
title = "Section 2.8.1: Computing the Motion of Free Rigid Bodies (incomplete)"
date = "2022-11-08T05:05:00Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++






## 2.8.1 Computing the Motion of Free Rigid Bodies



> Lagrange's equations for the motion of a free rigid body in terms of Euler angles are quite disgusting, so we will not show them here.

Some configurations may have coordinate singularities when using Euler angles (e.g. [gimbal lock](https://en.wikipedia.org/wiki/Gimbal_lock)). In the explicit Lagrange equations, the singularity arises when we try to find the expression for generalized accelerations. The expression for this involves the inverse of $\partial_2 \partial_2 L$. The determinant of this quantity may become zero when the Euler angle $\theta$ is zero (for 3-1-3 Euler angles).

```clojure
(def Euler-state
  (up 't
      (up 'theta 'varphi 'psi)
      (up 'thetadot 'varphidot 'psidot)))

(rendermd (determinant
    (((square (partial 2)) (rigid/T-rigid-body 'A 'B 'C)) ;; rigid/T-rigid-body = T-body-Euler from book
     Euler-state)))
```


{% mathjax() %}$$
A\,B\,C\,{\sin}^{2}\left(\theta\right)
$$
{% end %}





So we cannot solve for the second derivatives when $\theta = 0$ and the Euler angles may change drastically when $\theta$ is small. This does not mean the actual motion of the rigid body is anything but well-behaved. The problem lies entirely in the representation of the motion using Euler angles. We may use another set of Euler angles when necessary to avoid this problem, but this tends to be cumbersome. In this section, we will be limiting our focus to trajectories that will not contain singularities for the chosen Euler angle set. 


To obtain trjectories, we numerically integrate the Lagrange equations. The system derivative can be obtained directly from the Lagrangian using `Lagrangian->state-derivative`


TBD: Figure out plotting in Clojupyter

```clojure
(defn rigid-sysder [A B C]
  (Lagrangian->state-derivative (rigid/T-rigid-body A B C)))

(defn monitor-errors [win A B C L0 E0]
    (fn [state]
  (let [t (time state)
        L ((rigid/Euler-state->L-body A B C) state)
        E ((rigid/T-rigid-body A B C) state)]
    (plot-point win t (relative-error (ref L 0) (ref L0 0)))
    (plot-point win t (relative-error (ref L 1) (ref L0 1)))
    (plot-point win t (relative-error (ref L 2) (ref L0 2)))
    (plot-point win t (relative-error E E0)))))
```
    Syntax error compiling at (REPL:9:5).
    Unable to resolve symbol: plot-point in this context

      Util.java:   221 clojure.lang.Util/runtimeException
       core.clj:  3214 clojure.core$eval/invokeStatic
       core.clj:  3210 clojure.core$eval/invoke
       main.clj:   437 clojure.main$repl$read_eval_print__9086$fn__9089/invoke
       main.clj:   458 clojure.main$repl$fn__9095/invoke
       main.clj:   368 clojure.main$repl/doInvoke
    RestFn.java:  1523 clojure.lang.RestFn/invoke
       AFn.java:    22 clojure.lang.AFn/run
       AFn.java:    22 clojure.lang.AFn/run
    Thread.java:  1589 java.lang.Thread/run

