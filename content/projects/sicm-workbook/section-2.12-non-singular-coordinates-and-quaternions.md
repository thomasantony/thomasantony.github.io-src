+++
title = "Section 2.12: Nonsingular Coordinates and Quaternions"
date = "2022-11-16T05:29:39Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "note"
+++






### 2.12 Nonsingular Coordinates and Quaternions



> The Euler angles provide a convenient way to parameterize the orientation of a rigid body. However, the equations of motion derived for them have singularities. Though we can avoid the singularities by using other Euler-like combinations with different singularities, this kludge is not very satisfying.


* We know from Euler's theorem that any orientation can be reached with a single rotation. Specifying this rotation requires specifying its axis and the angle of rotation.

* One possibility: Use latitude and longitude to define the axis. But this becomes undefined in the case of zero rotation

* Another possibility: Use a vector whose direction is that of the axis vector and whose length defines the amount of rotation. In this case, rotation by $2\pi$ is equal to no rotation at all. Every rotation can be represented by a countably infinite number of vectors, each with a length of $\theta + 2M\pi$ for an integer $M$. This makes it problematic to invert the mapping from other representations of rotation.

* A fix for the above point is to scale the vector by sine of half of the rotation angle. With this choice a rotation by zero angle will have the same orientation vector as a rotation by $2\pi$. But there is still another problem: rotations by $\theta$ and $2\pi - \theta$ are not distinguished. That is, a vector may represent both the "short-rotation" and the "long rotation" for the same orientation.

* We can solve this by keeping track of the cosine of half the angle of rotation (though in reality we just need the sign of the cosine). Wrapping this all up into 4-tuples gives us Hamilton's *quaternions*.

For a rotation by angle $\theta$ about axis $\hat{n}$, the components of a quaternion defining the rotation are:


{% mathjax() %}
$$
(\cos(\theta/2),~\sin(\theta/2)\hat{n}_x,~\sin(\theta/2)\hat{n}_y,~\sin(\theta/2)\hat{n}_z)
$$
{% end %}




This is a unit quaternion as the sum of squares of its components is equal to one. The first element is called the "real part", $r$, and the other three elements can form a tuple $v$ called the "imaginary part". The angle of rotation can be obtained by computing $\theta = \arctan(\|v\|, r)$, and the axis direction is $v/\|v\|$.


* The rotation represented by a quaternion is not changed by reversing the sign of all its components. This is because changing the sign of v reverses the axis but does not change the angle and changing the sign of the first component changes the angle $\theta$ to $2\pi − \theta$, so the actual rotation is unchanged.

### DCM from Quaternion

Given the four elements of a quaternion, we can do compute the corresponding rotation matrix. First we get the angle $\theta$ and axis, $\hat{n}$ when given a quaternion. We rotate by angle $\theta$ about the $z$ axis and then transform this rotation by a rotation to the axis specified by the colatitude ($\varphi$) and longitude ($\lambda$) of the axis $\hat{n}$:


{% mathjax() %}
$$
\mathbf{R}(\theta, \hat{n}) = \mathbf{R}_z(\lambda)\mathbf{R}_y(\varphi)~\mathbf{R}_z(\theta)~\mathbf{R}_y(\varphi)^\mathscr{T}\mathbf{R}_z(\lambda)^\mathscr{T}
$$
{% end %}




where $\varphi = \arccos(\hat{n_z})$ and $\lambda = \arctan(\hat{n}_y, \hat{n}_x)$.

```clojure
(defn my-angle-axis->rotation-matrix [theta n]
  (let [nx (ref n 0)
        ny (ref n 1)
        nz (ref n 2)
        colatitude (acos nz)
        longitude (atan ny nx)]
      (* (rotate-z-matrix longitude)
         (rotate-y-matrix colatitude)
         (rotate-z-matrix theta)
         (transpose (rotate-y-matrix colatitude))
         (transpose (rotate-z-matrix longitude)))))

(rendermd (my-angle-axis->rotation-matrix (/ pi 4) (up 0 0 1)))
```


{% mathjax() %}$$
\mathsf{matrix-by-rows}\left(\begin{pmatrix}\displaystyle{0.7071067811865476} \cr \cr \displaystyle{-0.7071067811865475} \cr \cr \displaystyle{0}\end{pmatrix}, \begin{pmatrix}\displaystyle{0.7071067811865475} \cr \cr \displaystyle{0.7071067811865476} \cr \cr \displaystyle{0}\end{pmatrix}, \begin{pmatrix}\displaystyle{0.0} \cr \cr \displaystyle{0.0} \cr \cr \displaystyle{1}\end{pmatrix}\right)
$$
{% end %}



```clojure
(defn quaternion->angle-axis [q]
  (let [v (quat/three-vector q)
        sintheta (sqrt (dot-product v v))
        theta (* 2 (atan sintheta (quat/real-part q)))
        axis (/ v sintheta)]
    (up theta axis)))

;; Quaternion to DCM
(defn quaternion->DCM [q]
  (let [aa (quaternion->angle-axis q)
        theta (ref aa 0)
        n (ref aa 1)]
      (angle-axis->rotation-matrix theta n)))

;; 30 degrees about z axis
(render (quaternion->DCM (quat/make (cos (/ (/ pi 6) 2)) 0 0 (sin (/ (/ pi 6) 2)))))
```

{% mathjax() %}
matrix-by-rows(up(0.8660254037844387, -0.49999999999999994, 0), up(0.49999999999999994, 0.8660254037844387, 0), up(0.0, 0.0, 1))
{% end %}




The matrix terms here are all divided by the magnitude of $q$ which can be ignored since we use unit quaternions. Once this is removed, we get the following form for the rotation matrix from a quaternion $(q_0, q_1, q_2, q_3)$:


{% mathjax() %}
$$
\begin{pmatrix}q_0^2 + q_1^2 - q_2^2 -q_3^2 & -2q_0q_3 + 2q_1q_2 & 2q_0q_2 + 2q_1q_3 \\
2q_0q_3 + 2q_1q_2 & q_0^2 - q_1^2 + q_2^2 - q_3^2 & -2q_0q_1 + 2q_2q_3\\
-2q_0q_2 + 2q_1q_3 & 2q_0q_1 + 2q_2q_3 & q_0^2 - q_1^2 - q_2^2 + q_3^2\\
\end{pmatrix}
$$
{% end %}



```clojure
(defn quaternion->rotation-matrix [q]
  (let [q-vec (quat/->vector q)
        q0 (ref q-vec 0) 
        q1 (ref q-vec 1)
        q2 (ref q-vec 2)
        q3 (ref q-vec 3)
        m-2
            (+ (expt q0 2) (expt q1 2)
               (expt q2 2) (expt q3 2))]
      (/ (matrix-by-rows
           (list (- (+ (expt q0 2) (expt q1 2))
                    (+ (expt q2 2) (expt q3 2)))
                 (* 2 (- (* q1 q2) (* q0 q3)))
                 (* 2 (+ (* q1 q3) (* q0 q2))))
           (list (* 2 (+ (* q1 q2) (* q0 q3)))
                 (- (+ (expt q0 2) (expt q2 2))
                    (+ (expt q1 2) (expt q3 2)))
                 (* 2 (- (* q2 q3) (* q0 q1))))
           (list (* 2 (- (* q1 q3) (* q0 q2)))
                 (* 2 (+ (* q2 q3) (* q0 q1)))
                 (- (+ (expt q0 2) (expt q3 2))
                    (+ (expt q1 2) (expt q2 2)))))
         m-2)))

;; This function can be further used to compute the components of angular velocity using M->omega-body

(rendermat
  ((rigid/M->omega-body
     (compose quaternion->rotation-matrix quat/make))
   (up 't
       (up 'q_0 'q_1 'q_2 'q_3)
       (up 'qdot_0 'qdot_1 'qdot_2 'qdot_3))))
```


{% mathjax() %}$$
\begin{bmatrix}\displaystyle{\begin{pmatrix}\displaystyle{\frac{2\,q_0\,{\dot q}_1 -2\,q_1\,{\dot q}_0 -2\,q_2\,{\dot q}_3 + 2\,q_3\,{\dot q}_2}{{q_0}^{2} + {q_1}^{2} + {q_2}^{2} + {q_3}^{2}}} \cr \cr \displaystyle{\frac{2\,q_0\,{\dot q}_2 + 2\,q_1\,{\dot q}_3 -2\,q_2\,{\dot q}_0 -2\,q_3\,{\dot q}_1}{{q_0}^{2} + {q_1}^{2} + {q_2}^{2} + {q_3}^{2}}} \cr \cr \displaystyle{\frac{2\,q_0\,{\dot q}_3 -2\,q_1\,{\dot q}_2 + 2\,q_2\,{\dot q}_1 -2\,q_3\,{\dot q}_0}{{q_0}^{2} + {q_1}^{2} + {q_2}^{2} + {q_3}^{2}}}\end{pmatrix}}\end{bmatrix}
$$
{% end %}





Ignoring the denominator, the quaternion is independent of the scale of the quaternion. And since it is a fucntion of time, the rates of $q$ are also independent of scale. This can be further simplified by representing the products in the numerator as a matrix product. Define the following matrices:


{% mathjax() %}
$$
\begin{align*}
\mathbf{i} &= \begin{pmatrix}0 & +1 & 0 & 0\\
-1 & 0 & 0 & 0\\
0 & 0 & 0 & -1\\
0 & 0 & +1 & 0\\\end{pmatrix}\\
\mathbf{j} &= \begin{pmatrix}0 & 0 & +1 & 0\\
0 & 0 & 0 & +1\\
-1 & 0 & 0 & 0\\
0 & -1 & 0 & 0\\\end{pmatrix}\\
\mathbf{k} &= \begin{pmatrix}0 & 0 & 0 & +1\\
0 & 0 & -1 & 0\\
0 & +1 & 0 & 0\\
-1 & 0 & 0 & 0\\\end{pmatrix}\tag{2.125}
\end{align*}
$$
{% end %}




The angular velocity components can now be written as :


{% mathjax() %}
$$
\begin{align*}
\omega^a &= 2\mathscr{q}^\mathscr{T}\mathbf{i}\dot{\mathscr{q}}~/~\|\mathscr{q}\|^2\\
\omega^b &= 2\mathscr{q}^\mathscr{T}\mathbf{j}\dot{\mathscr{q}}~/~\|\mathscr{q}\|^2\\
\omega^c &= 2\mathscr{q}^\mathscr{T}\mathbf{k}\dot{\mathscr{q}}~/~\|\mathscr{q}\|^2\\
\end{align*}
$$
{% end %}




where $\mathscr{q}$ is a column vector of the components of $q$. The anti-symmetric matrices $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$ have the interesting properties that make it the basis vectors for the quaternions:


{% mathjax() %}
$$
\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = \mathbf{i}\mathbf{j}\mathbf{k} = -\mathbf{1}
$$
{% end %}




where $\mathbf{1}$ is the identity matrix.


### Composition of rotations

An easy way to compose ttwo rotations would be to convert ehm to DCMs and multiply them. However this results in a very messy results where each component is scaled by a factor of $\|q\|\|p\|$ (which is equal to $1$ for unit quaternions). Eliminating this scale factor, we get the following form for composition of quaternions


{% mathjax() %}
$$
\begin{pmatrix}
p_0q_0-p_1q_1-p_2q_2-p_3q_3\\
p_0q_1+p_1q_0-p_2q_3+p_3q_2\\
p_0q_2+p_1q_3+p_2q_0-p_3q_1\\
p_0q_3-p_1q_2+p_2q_1+p_3q_0\\
\end{pmatrix}
$$
{% end %}




This can be re-stated as:


{% mathjax() %}
$$
r_0 = q_0p_0 - v_q \cdot v_p\\
$$
{% end %}




{% mathjax() %}
$$
v_r = q_0v_p+p_0v_q + v_q \times v_p\\
$$
{% end %}




where $r_0$ is the scalar part of the result, $v_r$ is the vector part of the result and $v_p$ and $v_q$ are the vector parts of the original quaternions. This can be considered to be the product of the two quaternions. 


{% mathjax() %}
$$
\mathbf{r} = \mathbf{q}\mathbf{p}
$$
{% end %}


