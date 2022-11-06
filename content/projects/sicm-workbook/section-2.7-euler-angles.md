+++
title = "Section 2.7: Euler Angles"
date = "2022-11-07T05:40:17Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++







## 2.7 Euler Angles



*Euler Angles* are a set of generalized coordinates for describing the orientation of a rigid body. To quote the book:

> Though the Euler angles allow us to specify all orientations and thus can be used as generalized coordinates, the definition of Euler angles is pretty arbitrary. In fact no reasoning has led us to them. This is reflected in our presentation of them by just saying “here they are.” Euler angles are well suited for some problems, but cumbersome for others.

We start with the reference orientation so that principal-axis unit vectors $\hat{a}, \hat{b}, \hat{c}$ are coincident with the basis vectors $\hat{e}_i$, labeled here by $\hat{x}, \hat{y}, \hat{z}$. The Euler angles are defined in terms of simple rotations about the coordinate axes. Let $R_x(\psi)$ be a right-handed rotation about $\hat{x}$ by angle $\psi$, and $R_z(\psi)$ be a right-handed rotation about $\hat{z}$ by angle $\psi$. The function $\mathscr{M}$ for Euler angles is written as a composition of three of these simple coordinate axis rotations:


{% mathjax() %}
$$
\mathscr{M}(\theta, \varphi, \psi) = R_z(\varphi) \circ R_x(\theta) \circ R_z(\psi)
$$
{% end %}




for Euler angles $\theta, \varphi, \psi$. While these angles can represent any orientation, any specific orientation may be represented by more than one set of Euler angle. For example, when $\theta = 0$, then the orientation does not uniquely define either $\varphi$ or $\psi$.

There are other sets of Euler angles that can serve as generlized coordinates. For example, we can use the Euler angles defined as:


{% mathjax() %}
$$
\mathscr{M}(\theta, \varphi, \psi) = R_x(\varphi) \circ R_y(\theta) \circ R_z(\psi)
$$
{% end %}




Sometimes these are useful when we want to control where in the configuration space the "singularity" in the coordinates show up. The fundamental rotations themselves can be represented as rotation matrices:


{% mathjax() %}
$$
\begin{align*}
\mathbf{R}_z(\psi) &= \begin{bmatrix}
              \cos\psi & -\sin\psi & 0\\
              \sin\psi & \cos\psi & 0\\
              0 & 0 & 1\\
             \end{bmatrix}\\
\mathbf{R}_x(\psi) &= \begin{bmatrix}
              1 & 0 & 0\\
              0 & \cos\psi & -\sin\psi\\
              0 & \sin\psi & \cos\psi\\
             \end{bmatrix}\\
\end{align*}
$$
{% end %}




The rotation $\mathscr{M}$ can then be written as:


{% mathjax() %}
$$
\mathscr{M}(\theta, \varphi, \psi) = \mathbf{R}_x(\varphi) \mathbf{R}_y(\theta) \mathbf{R}_z(\psi)
$$
{% end %}




The rotation matrices and their products can be computed as shown below. These can then be combined with the procedures ` M-of-q->omega-of-t` and `M-of-q->omega-body-of-t` from [section 2.2](/projects/sicm-workbook/section-2.2-kinematics-of-rotation) to compute the components of the angular velocity vector and the body components of the angular velocity vector. 

The code below computes the components of the angular velocity vector for the given Euler angle set.

```clojure
(defn Rz-matrix [angle]
  (matrix-by-rows
    (list (cos angle) (- (sin angle)) 0)
    (list (sin angle) (cos angle) 0)
    (list 0 0 1)))

(defn Rx-matrix [angle]
  (matrix-by-rows
    (list 1 0 0)
    (list 0 (cos angle) (- (sin angle)))
    (list 0 (sin angle) (cos angle))))

;; Rotation function, M
(defn my-Euler->M [[theta, phi, psi]]
  (* (Rz-matrix phi)
       (Rx-matrix theta)
       (Rz-matrix psi)))

;; Methods from section 2.2 are defined in the "rigid" namespace of sicmutils

;; Body-components of angular velocity for given Euler angles
(rendermd
 (matrix/->structure
  (((rigid/M-of-q->omega-body-of-t my-Euler->M)
    (up (literal-function 'theta)
        (literal-function 'varphi)
        (literal-function 'psi)))
   't)))
```


{% mathjax() %}$$
\begin{bmatrix}\displaystyle{\begin{pmatrix}\displaystyle{\sin\left(\psi\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,D\varphi\left(t\right) + \cos\left(\psi\left(t\right)\right)\,D\theta\left(t\right)} \cr \cr \displaystyle{\cos\left(\psi\left(t\right)\right)\,\sin\left(\theta\left(t\right)\right)\,D\varphi\left(t\right) - \sin\left(\psi\left(t\right)\right)\,D\theta\left(t\right)} \cr \cr \displaystyle{\cos\left(\theta\left(t\right)\right)\,D\varphi\left(t\right) + D\psi\left(t\right)}\end{pmatrix}}\end{bmatrix}
$$
{% end %}



```clojure
;; Components of angular velocity vector (inertial?)
(rendermd
 (matrix/->structure
  ((rigid/M->omega-body Euler->M)
   (up 't
       (up 'theta 'varphi 'psi)
       (up 'thetadot 'varphidot 'psidot)))))
```


{% mathjax() %}$$
\begin{bmatrix}\displaystyle{\begin{pmatrix}\displaystyle{\dot {\varphi}\,\sin\left(\psi\right)\,\sin\left(\theta\right) + \dot {\theta}\,\cos\left(\psi\right)} \cr \cr \displaystyle{\dot {\varphi}\,\cos\left(\psi\right)\,\sin\left(\theta\right) - \dot {\theta}\,\sin\left(\psi\right)} \cr \cr \displaystyle{\dot {\varphi}\,\cos\left(\theta\right) + \dot {\psi}}\end{pmatrix}}\end{bmatrix}
$$
{% end %}



```clojure
;; This can be further create a procedure that returns the omega vector for the 3-1-3 (z-x-z) Euler angle set
(defn Euler-state->omega-body [[t, [theta, phi, psi], [thetadot, phidot, psidot]]]
      (let [omega-a (+
                       (* thetadot (cos psi))
                       (* phidot (sin theta) (sin psi)))
            omega-b (+
                       (* -1 thetadot (sin psi))
                       (* phidot (sin theta) (cos psi)))
            omega-c (+
                       (* phidot (cos theta)) psidot)]
        (up omega-a omega-b omega-c)))

(rendermd
  (Euler-state->omega-body
   (up 't
       (up 'theta 'varphi 'psi)
       (up 'thetadot 'varphidot 'psidot))))
```


{% mathjax() %}$$
\begin{pmatrix}\displaystyle{\dot {\varphi}\,\sin\left(\psi\right)\,\sin\left(\theta\right) + \dot {\theta}\,\cos\left(\psi\right)} \cr \cr \displaystyle{\dot {\varphi}\,\cos\left(\psi\right)\,\sin\left(\theta\right) - \dot {\theta}\,\sin\left(\psi\right)} \cr \cr \displaystyle{\dot {\varphi}\,\cos\left(\theta\right) + \dot {\psi}}\end{pmatrix}
$$
{% end %}





The `Euler-state->omega-body` procedure can now be used to write functions to compute kinetic energy and angular momentum

```clojure
;; From section 2.5
(defn T-body [A B C]
    (fn [omega-body]
  (* 1/2
     (+ (* A (square (ref omega-body 0)))
        (* B (square (ref omega-body 1)))
        (* C (square (ref omega-body 2)))))))

;; From section 2.6
(defn L-body [A B C] 
    (fn [omega-body]
      (down (* A (ref omega-body 0))
        (* B (ref omega-body 1))
        (* C (ref omega-body 2)))))


;; Kinetic energy
(defn T-body-Euler [A B C]
    (fn [local]
      ((T-body A B C)
       (Euler-state->omega-body local))))

;; Angular momentum in principal axes coordinates
(defn L-body-Euler [A B C] 
    (fn [local]
      ((L-body A B C)
       (Euler-state->omega-body local))))


;; L in reference-frame
(defn L-space-Euler [A B C]
    (fn [local]
      (let [angles (coordinate local)]
        (* ((L-body-Euler A B C) local)
           (transpose (Euler->M angles))))))

;; These are all local-tuple functions similar to the Lagrangian
```
