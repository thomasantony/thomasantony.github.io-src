+++
title = "Exercise 1.40: Bead on a triaxial surface (incomplete)"
date = "2022-10-31T00:25:47Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "exercise"
+++



### Exercise 1.40: Bead on a triaxial surface

**Consider again the motion of a bead constrained to move on a triaxial surface (exercise 1.18). Reformulate this using rectangular coordinates as the generalized coordinates with an explicit constraint that the bead must stay on the surface. Find a Lagrangian and show that the Lagrange equations are equivalent to those found in [exercise 1.18](https://tgvaughan.github.io/sicm/chapter001.html#Exe_1-18) ([solution](/projects/sicm-workbook/sicm-exercise-1-18/)).**






We model the system as a point mass constrained to stay on a triaxial surface using the following coordinate constraint:

{% mathjax() %}
$$
\varphi(t; x,y,z; \dot{x},\dot{y},\dot{z}) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} - 1 = 0
$$

where $a$, $b$ and $c$ are parameters defining the surface. The augmented Lagrangian is:


{% mathjax() %}
$$
L' = \frac{1}{2} m \dot{x}^2 + \lambda \left(\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} - 1\right)
$$
{% end %}



```clojure
(defn L-free-particle [mass]
    (fn [[_ _ v]]
        (* 1/2 mass (dot-product v v)))   
)

(defn ellipsoid-constraint [a b c]
    (fn [[_ [x y z] _]] 
        (- (+ (/ (square x) (square a)) 
              (/ (square y) (square b))
              (/ (square z) (square c))) 1)
    )
)

(defn Augment-Lagrangian [L lambda phi]
    (+ L (* lambda phi)))

(defn L-bead-on-ellipsoid [m a b c]
    (fn [[t [x y z lambda] [xdot ydot zdot lambdadot]]]
        (let [L (L-free-particle m)
              phi (ellipsoid-constraint a b c)
              q (up t (up x y z) (up xdot ydot zdot))]
        (+ (L q) (* lambda (phi q))))))
```


    #'user/L-bead-on-ellipsoid



```clojure
(def eom-system 
        (Lagrange-equations (L-bead-on-ellipsoid 'm 'a 'b 'c)))

(def eqs-system (let [state (up (literal-function 'x) (literal-function 'y) (literal-function 'z) (literal-function 'lambda))]
            ((eom-system state) 't)))

(rendertexvec eqs-system)
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{\frac{{a}^{2}\,m\,{D}^{2}x\left(t\right) -2\,x\left(t\right)\,\lambda\left(t\right)}{{a}^{2}}} \cr \cr \displaystyle{\frac{{b}^{2}\,m\,{D}^{2}y\left(t\right) -2\,y\left(t\right)\,\lambda\left(t\right)}{{b}^{2}}} \cr \cr \displaystyle{\frac{{c}^{2}\,m\,{D}^{2}z\left(t\right) -2\,z\left(t\right)\,\lambda\left(t\right)}{{c}^{2}}} \cr \cr \displaystyle{\frac{{a}^{2}\,{b}^{2}\,{c}^{2} - {a}^{2}\,{b}^{2}\,{\left(z\left(t\right)\right)}^{2} - {a}^{2}\,{c}^{2}\,{\left(y\left(t\right)\right)}^{2} - {b}^{2}\,{c}^{2}\,{\left(x\left(t\right)\right)}^{2}}{{a}^{2}\,{b}^{2}\,{c}^{2}}}\end{pmatrix}
$$
{% end %}





We can eliminate one of the coordinate as the system only has two degrees of freedom. First lets define some terminology:

$$\require{cancel}$$

{% mathjax() %}
$$
\begin{align*}
K_1 &= \frac{a^2}{c^2}, K_2 = \frac{a^2}{b^2}\\
D^2(x(t)) &= \ddot{x}, D^2 y(t) = \ddot{y}, D^2 z(t) = \ddot{z}\\
\end{align*}
$$
{% end %}



From the constraint,

{% mathjax() %}
$$
\begin{align*}
a^2 x &= a^2 b^2 c^2 - a^2 b^2 z - a^2 c^2 y \\
x &= \frac{a^2 b^2 c^2 - a^2 b^2 z - a^2 c^2 y}{b^2 c^2} \\
x &= a^2 - K_1 z - K_2 y
\\
=> \dot{x} &= - K_1 \dot{z} - K_2 \dot{y} \\
=> \ddot{x} &= -K_1 (\ddot{z}z + \dot{z}^2) -K_2 (\ddot{y}y + \dot{y}^2)
\end{align*}
$$
{% end %}



From the first equation,

$\lambda = \frac{m a^2 \ddot{x}}{x}$

Substituting $\lambda$ into the second equation, we get:

{% mathjax() %}
$$
\begin{align*}
b^2 \cancel{m} \ddot{y} &=  2 y \frac{\cancel{m} a^2 \ddot{x}}{x} \\
=> \ddot{y} &= 2 y \frac{a^2}{b^2} \left(\frac{-K_1 (\ddot{z}z + \dot{z}^2) -K_2 (\ddot{y}y + \dot{y}^2)}{a^2 - K_1 z - K_2 y}\right)\\
=> \ddot{y} &= - 2 y K_2 \frac{K_1 (\ddot{z}z + \dot{z}^2) + K_2 (\ddot{y}y + \dot{y}^2)}{a^2 - K_1 z - K_2 y}
\end{align*}
$$
{% end %}



Substituting $\lambda$ into the third equation, we get:

{% mathjax() %}
$$
\begin{align*}
c^2 \cancel{m} \ddot{z} &=  2 y \frac{\cancel{m} a^2 \ddot{x}}{x} \\
=> \ddot{z} &= 2 z \frac{a^2}{c^2} \left(\frac{-K_1 (\ddot{z}z + \dot{z}^2) -K_2 (\ddot{y}y + \dot{y}^2)}{a^2 - K_1 z - K_2 y}\right)\\
=> \ddot{z} &= - 2 z K_1 \frac{K_1 (\ddot{z}z + \dot{z}^2) + K_2 (\ddot{y}y + \dot{y}^2)}{a^2 - K_1 z - K_2 y}
\end{align*}
$$
{% end %}



```clojure

```
