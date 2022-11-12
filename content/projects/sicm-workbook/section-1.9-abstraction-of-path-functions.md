+++
title = "Section 1.9: Abstraction of Path Functions"
date = "2022-10-27T01:12:46Z"
draft = false

[extra]
latex = true
chapter = "1"
page_type = "note"
+++





## 1.9 Abstraction of Path Functions



**Note: This section may seem rather dry from its title. But this is driving towards some important results.**

When we were deriving the local-tuple transformation $C$, corresponding to a coordinate transformation $F$, the main factor was finding the relationship between the velocities in the two coordinate systems (e.g. $v$ and $v'$). We did this by inserting coordinate paths into the transformation function, $F$, finding its derivatives and then extracting out the velocity components.


{% mathjax() %}
$$
\begin{align*}
x &= F(t, x') \\
=> v &= \partial_0 F + \partial_1 F v'
\end{align*}
$$
{% end %}




This last step is an example from a more general scenario where we want to abstract a local tuple function from a path function. Consider a function, $f$ of the local tuple. We typically apply $f$ to a path by composing it with $\Gamma$. $\Gamma$ is a function which extracts the local tuple from a path (the path itself is usually denoted computationally as symbolic coordinate functions like $x(t)$, $y(t)$ etc.). Given $f$, a corresponding path-dependent function $\bar{f}[q]$ can be defined using $\Gamma$ as $\bar{f}[q] = f \circ \Gamma[q]$. The question now is given $\bar{f}$, how can we reconstitute $f$. 

We know that $f$ depends only on a certain finite number of components, $n$ of the local-tuple (say, $t$, $x$ and $v$). Therefore $\bar{f}$ also depends only on the corresponding local components of the path. It is important to note that the path may be more complex than can be represented by $n$ components. Even so, the path-dependent function $\bar{f}$ *still* has same value for all the paths that share the same first $n$ local components. 

By "reconstituting" $f$, what we mean here is that we want to find the value of $f$ for some local tuple argument, when we only know the function definition of $\bar{f}$. To do this, we take the argument of $f$ (which is a finite initial segment of the local tuple), constructing a path that has this local description (say, using a power series), and then finding the value of $\bar{f}$ for this path.


Two paths that have the same $n$ initial components of the local tuple in its description (or "have the same local description up to the nth derivative") are said to *osculate with order $n$ contact*. One example of this is a path, and a truncated power series representation of the path up to order $n$, have order $n$ contact. If we have a power-series representation of the path available up to $n$-th order, and a local tuple function takes fewer than $n$ components of the local tuple, then as far as this function is concerned, the path and the trunctated power series are equivalent. 

Let $O$ be a function that generates an osculating path with the given local tuple components, i.e.


{% mathjax() %}
$$
\begin{align*}
O(t, q, v, ...)(t) &= q \\
D(O(t, q, v, ...))(t) &= v\\
\text{etc. and in general:}\\
(t, q, v, ...) &= \Gamma[O(t, q, v, ...)](t)
\end{align*}
$$
{% end %}




$O$ is defined to take a finite number of local tuple components, $n$. $O$ can be considered to be "inverse" of the $\Gamma$ function. One caveat is that it only make sense to use $O$ when we have concrete expressions defining the entire local tuple of interest, rather than symbolic functions. One possible way of construction $O$ is using a power series:


{% mathjax() %}
$$
O(t, q, v, ...)(t') = q + v(t' - t) + \frac{1}{2} a (t' - t)^2 + ...\\
$$
{% end %}




So, given a path function $\bar{f}$, we can reconstitute the $f$ function as:


{% mathjax() %}
$$
\begin{align*}
f(t, q, v, ...) &= (f \circ \Gamma[O(t, q, v, ...)]) (t)\\
                &= \bar{f}[O(t,q,v,...)](t)
\end{align*}
$$
{% end %}




Using this we can define $\bar{\Gamma}$ as a function that takes a path function and returns the corresponding local-tuple function, $f = \bar{\Gamma}[\bar{f}]$.  $\bar{\Gamma}$ is defined as:


{% mathjax() %}
$$
\bar{\Gamma}[f](t, q, v, ...) = \bar{f}[O(t, q, v, ...)](t)
$$
{% end %}




$\bar{\Gamma}$ is defined in Clojure below. `osculating-path` is the implementation of the $O$ function.

```clojure
(defn osculating-path2
    "Defines a path function f(t) using a Taylor series about the time given in reference state"
    [state_ref]
    (let [[t_ref q_ref] state_ref
           N (count state_ref)]
    (fn [t]
      (let [dt (- t t_ref)]
            (loop [n 2
                   sum q_ref
                   dt**n-by-n! dt]
            (if (= n N) ;; exit loop when n == N
                sum       ;; return sum
            (recur (inc n)      ;; update loop variables and repeat
                   (+ sum (* (nth state_ref n) dt**n-by-n!))
                   (/ (* dt**n-by-n! dt) n)))
)))))
        
(defn Gamma-bar2 [f-bar]
    (fn f [local]
        (let [t (first local)]
            ((f-bar (osculating-path2 local)) t)
        )
    )
)

```



Despite it's name `Gamma-bar2` is **not** the inverse of $\Gamma[q]$. $\Gamma[q]$ takes a path, and returns a local tuple (the inverse of $\Gamma[q]$ is actually $O$ which takes a local tuple and returns a path). `Gamma-bar2` takes a function of a path, and returns a function of local tuples -- this is a subtle but important difference. One operates on the path/tuple, and the other operates on functions of paths/tuples.

`Gamma-bar2` can be used to define a more general version of the `F->C` function.  The procedure `F->C` first constructs a path-dependent procedure `f-bar` that takes a coordinate path in the primed system and returns the local tuple of the corresponding path in the unprimed coordinate system. It then uses `Gamma-bar2` to abstract f-bar to arbitrary local tuples in the primed coordinate system. The resulting procedure `C` can take local tuples with `n` components in the primed coordinate system and generate local tuples of `n` terms in the unprimed coordinate system.


E.g. `p->r` which is defined as:

```clojure
(defn p->r [[t, [r, phi], [rdot, phidot]]]
  (let [x (* r (cos phi))
        y (* r (sin phi))]
    (up x y)
  )
)
```
`p->r` takes a local tuple in polar coordinates and returns a **path** in rectangular coordinates (**NOT** the local tuple). `f-bar` takes the **input path** `q-prime` in polar coordinates. Converts it into local tuple in polar coordinates using `Gamma[q-prime]`. This local tuple is then passed to `p->r` which returns a **path** in rectangular coordinates. This is then passed to `Gamma` to return the local tuple of `n` components in rectangular coordinates. `Gamma-bar` ensures that the input which consists of a polar local tuple of `n` components is converted to a path before being handed off to `f-bar` which then returns a local tuple of `n` components in rectangular coordinates.

So to summarize, `p->r` takes in a **tuple** and outputs a **path** or coordinate function in rectangular coordinates. However, instead of passing in a tuple directly to `p->r`, we pass in a **path**, and convert it into a tuple first by calling `(Gamma q-prime)`. The output of `p->r` is then wrapped in `Gamma <> n` to extract `n` components of the local tuple out of this new path, which is then returned to the caller. This whole function is a path-dependent function that takes a path in polar coordinates as the input and spits out a local tuple in rectangular coordinates. Wrapping this in `Gamma-bar` makes it a function that instead takes a local tuple as input.

```clojure
(defn super-F->C [F]
    (fn C [local]
        (let [n (count local)
              f-bar (fn [q-prime]
                    (let [q (compose F (Gamma q-prime))]
                        (Gamma q n)))]
            ((Gamma-bar2 f-bar) local))
))

(defn p2r [[_, [r, phi], _]]
  (let [x (* r (cos phi))
        y (* r (sin phi))]
    (up x y)
  )
)
;; This can be demonstrated using the existing coordinate conversion 
;; function p->r which converts from polar coordinates to rectangular 
;; coordinates. Here it is shown operating on a local tuple with 4 terms.
(rendertex
  ((super-F->C p2r)
   (up 't (up 'r 'theta) (up 'rdot 'thetadot) (up 'rdotdot 'thetadotdot))))
```



This is a very convoluted function at first look but also elegant in certain ways. My understanding is that we go through this roundabout way of path->tuple->path->tuple so that we can expand/contract the number of components of the path description that we are interested in. One example of this can be seen when applying `F->C` to the `coordinate` function which simply extracts the position out of the local tuple (it returns the same local tuple that was passed in). 

```
(rendertex
  ((super-F->C coordinate)
   (up 't (up 'r 'theta) (up 'rdot 'thetadot) (up 'rdotdot 'thetadotdot))))
```


{% mathjax() %}
$$
\begin{pmatrix}\displaystyle{t} \cr \cr \displaystyle{\begin{pmatrix}\displaystyle{r} \cr \cr \displaystyle{\theta}\end{pmatrix}} \cr \cr \displaystyle{\begin{pmatrix}\displaystyle{\dot r} \cr \cr \displaystyle{\dot {\theta}}\end{pmatrix}} \cr \cr \displaystyle{\begin{pmatrix}\displaystyle{\ddot r} \cr \cr \displaystyle{\ddot {\theta}}\end{pmatrix}}\end{pmatrix}
$$
{% end %}





The `F` function "contracts" (probably inaccurate terminology here) the local tuple that is passed in into just the position coordinates aka "path". And to extract out more components from this, it is necessary to wrap the input in `Gamma` and the function itself in `Gamma-bar`.



`Gamma-bar` can also be used to compute the total time derivative $D_t F$ of the local tuple function $F$. 

{% mathjax() %}
$$
D_t (F \circ \Gamma[q]) = \bar{\Gamma}[ D(F \circ \Gamma[q]) ]
$$
{% end %}



**Need more explanation as to why this works**

>   Given a procedure $F$ implementing a local-tuple function and a path $q$, we construct a new procedure `(compose F (Gamma q))`. The   procedure `DF-on-path` implements the derivative of this function of time. We then abstract this off the path with `Gamma-bar` to give the total time derivative.

`Dt` takes as input a function of the local tuple `F` and outputs a function of the local tuple. This function when evaluated for a some local tuple state, returns the time-derivative of `F` at that time. `Dt` is used to define the Euler-Lagrange operator in the next section

```clojure
(defn Dt [F]
  (fn DtF [state]
    (let [n (count state)
          DF-on-path (fn [q]
                    (D (compose F (Gamma q (- n 1)))))]
      ((Gamma-bar DF-on-path) state)))
  )
```



### Lagrange equations "at a moment" or the Euler Lagrange operator

The Euler-Lagrange equations can be defined as a path-dependent function, $\bar{\mathscr{E}}[L][q]$, the operates on a path, $q$ and returns zero if it s feasible path (according to the Lagrangian $L$).


{% mathjax() %}
$$
\bar{\mathscr{E}}[L][q] = D_t(\partial_2 L \circ \Gamma[q]) - \partial_1 L \circ \Gamma[q]
$$
{% end %}




These path-dependent E-L equations can be converted to local-tuple function, $\mathscr{E}[L]$ using `Gamma-bar`. 


{% mathjax() %}
$$
\mathscr{E}[L] = \bar{\Gamma}(\bar{\mathcal{E}}[L]) \\
$$
{% end %}




$\mathscr{E}[L] \circ \Gamma[q] = 0$ for realizable paths. $\mathscr{E}$ is called the **Euler-Lagrange operator**.


{% mathjax() %}
$$
\mathscr{E}[L] = D_t \partial_2 L - \partial_1 L \tag{1.180}
$$
{% end %}



```clojure
(defn my-Euler-Lagrange-operator [L]
  (- (Dt ((partial 2) L)) ((partial 1) L)))

(defn L-harmonic [m k]
    (fn [[_ q v]]
        (- (* 1/2 m (square v)) (* 1/2 k (square q)))))

(rendermd
((my-Euler-Lagrange-operator
   (L-harmonic 'm 'k))
 (up 't 'x 'v 'a)))
```

```clojure
(rendermd
((compose
   (Euler-Lagrange-operator (L-harmonic 'm 'k))
   (Gamma (literal-function 'x) 4))
 't)
    )
```



The **Euler-Lagrange operator** takes in a Lagrangian function as input and directly create a new function which will define the Euler-Lagrange equations on passing in the local tuple. 


### Summary

The functions/operators introduced in this section such as `Gamma-bar`, `Dt` and `Euler-Lagrange-operator` seem to be aimed at delaying evaluation as much as possible. We can stay in the realm of functions until the very end where we evaluate it on a local tuple to get the answer. Because these functions are eventually operating on paths, we need to make sure they are represented as path-dependent functions before transforming them. However, we wrap the path-dependant function in `Gamma-bar` at the end to make sure that we can still pass in the input as a local tuple.

While there is still more I could understand about the mechanism/logic by which this is possible, this is where I will stop for now.
