+++
title = "Section 2.5: Principal Moments of Inertia"
date = "2022-11-05T17:53:57Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++







## 2.5 Principal Moments of Inertia



In the [previous section](/projects/sicm-workbook/section-2.4-inertia-tensor), we showed how the inertia tensor transforms under a rotation:


{% mathjax() %}
$$
\mathbf{I}' = \mathbf{R}^{\mathscr{T}} \mathbf{I} \mathbf{R} \tag{2.35}
$$
{% end %}




This transformation can be used to show that there are special rectangular coordinate frames for which the inertia tensor is diagonal, that is, $I^\prime_{ij} = 0\text{ for }i \neq j$. Let's assume that $\mathbf{I}^\prime$ is diagonal and we need to solve for the rotation matrix $\mathbf{R}$ the gets us $\mathbf{I}^\prime$ from $\mathbf{I}$.

Left-multiply both sides of Eq. 2.35 by $\mathbf{R}$ to get: 


{% mathjax() %}
$$
\begin{align*}
\mathbf{R} \mathbf{I'} &= \mathbf{R}\mathbf{R}^{\mathscr{T}} \mathbf{I} \mathbf{R} \\
&= \mathbf{I} \mathbf{R}\tag{2.36}
\end{align*}
$$
{% end %}




We can extract out the columns of this matrix by mutliplying it on the right with the coordinate axis unit vectors, $\mathbf{e}_i$. These vectors have a 1 in the $i$-th row and zero elsewhere. Multiply $\mathbf{R}$ with $\mathbf{e}_i$ extracts out the basis vector of the rotated frame, $\mathbf{e}^\prime_i$. That is, $\mathbf{e}^\prime_i = \mathbf{R} \mathbf{e}_i$. Right-multiplying Eq. 2.36 by $\mathbf{e}_i$, we get:


{% mathjax() %}
$$
\mathbf{R} \mathbf{I^\prime} \mathbf{e}_i = \mathbf{I}\mathbf{R}\mathbf{e}_i = \mathbf{I}\mathbf{e}^\prime_i\tag{2.37}
$$
{% end %}




Since $\mathbf{I}^\prime$ is diagonal, 


{% mathjax() %}
$$
\mathbf{I}\mathbf{e}^\prime_i = I^\prime_{ii} \mathbf{e}^\prime_i \tag{2.38}
$$
{% end %}




From Eqs. 2.37 and 2.38, we get:


{% mathjax() %}
$$
\mathbf{I} \mathbf{e}^\prime_i = I^\prime_{ii} \mathbf{e}^\prime_i\\
$$
{% end %}





This equation says that transforming the vector $\mathbf{e}^\prime_i$ using the matrix $\mathbf{I}$ is equivalent to scaling the vector by the scalar value $I^\prime_{ii}$. This means that $I^\prime_{ii}$ is an eigen-value and $\mathbf{e}^\prime_i$ is the associated eigen-vector of $\mathbf{I}$.


Since $\mathbf{e}^\prime_i$ are the columns of a rotation matrix, and rotqtion matrix are orthogonal, the vectors themselves are orthonormal, i.e. they are unit vectors and their dot products with each other are zero. 


For a real, symmetric matrix (like $\mathbf{I}$). the eigen values are real. If the eigen values are distinct, then the eigen-vectors are orthogonal. However, if the eigen values are not distinct (say in the case of a symmetric body liuke a sphere), we have degrees of freedom on choosing the eigen vectors - and we may pick $\mathbf{e}_i$ that are orthogonal. For example, for a cylinder, one of the eigen vectors(corresponding to the central axis) are distinct and the other two (corrsponding to the diameters of the circular faces) are equal. This means that any of the diameters can be considered an eigen vector.

This the rotated coordinate system has a special orientation with respect to the body. The basis vectors correspond to particular directions w.r.t the body. The axes through the center of mass in these directions are defined as the *principal axes*. Thus the moments of inertia about the principal axes are the eigenvalues $I^\prime_{ii}$ and are called the *principal moments of inertia*.

The principal moments of inertia are often labeled according their size: $A \leq B \leq C$ with the corresponding axes: $\hat{a}$, $\hat{b}$ or $\hat{c}$. The components of some vector $\mathbf{x}$ when represented in terms of the principal axes are called *body components* of the vector. Rewriting the kinetic energy in terms of the principal moments of inertia,


{% mathjax() %}
$$
T_R = \frac{1}{2} \left[ A(\omega^a)^2 + B(\omega^b)^2 + C(\omega^c)^2\right]\tag{2.41}
$$
{% end %}




where $(\omega^a, \omega^b, \omega^c)$ are the components of the angular momentum vector on the principal axes.

```clojure
(defn T-body [A B C]
    (fn [omega-body]
  (* 1/2
     (+ (* A (square (ref omega-body 0)))
        (* B (square (ref omega-body 1)))
        (* C (square (ref omega-body 2)))))))

(rendermd ((T-body 'A 'B 'C)
           (up 'omega_a 'omega_b 'omega_c)))
```


{% mathjax() %}$$
\frac{1}{2}\,A\,{{\omega}_a}^{2} + \frac{1}{2}\,B\,{{\omega}_b}^{2} + \frac{1}{2}\,C\,{{\omega}_c}^{2}
$$
{% end %}



```clojure

```
