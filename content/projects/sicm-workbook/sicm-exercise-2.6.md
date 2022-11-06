+++
title = "Exercise 2.6: Principal moments of inertia"
date = "2022-11-07T03:04:57Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



## Exercise 2.5: Principal moments of inertia





**For each of the configurations described below find the principal moments of inertia with respect to the center of mass, and find the corresponding principal axes.**

---

**a. A regular tetrahedron consisting of four equal point masses tied together with rigid massless wire.**



Let the sides of the tetrohedron be two units long. The coordinates of the masses are ([Reference](https://en.wikipedia.org/wiki/Tetrahedron#Coordinates_for_a_regular_tetrahedron)]:


{% mathjax() %}
$$
(\pm 1, 0, -\frac{1}{\sqrt{2}}), (0, \pm 1, \frac{1}{\sqrt{2}})\\
$$
{% end %}




If the point masses all have mass $m$, the moments of inertia are:


{% mathjax() %}
$$
\begin{align*}
I_{00} &= \sum_i m_i \left(y_i^2 + z_i^2 \right)\\
       &= m (0 + \frac{1}{2} + 0 + \frac{1}{2} + 1 + \frac{1}{2} + 1 + \frac{1}{2} = 4m\\
I_{01} &= -\sum\nolimits_i m_i x_i y_i \\
       &= -m ( 0 + 0 + 0 + 0 ) = 0\\
I_{02} &= -\sum\nolimits_i m_i x_i z_i \\
       &= -m ( -\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + 0 + 0) = 0\\
\\
I_{10} &= - \sum\nolimits_i m_i y_i x_i\\
       &= - m (0 + 0 + 0 + 0) = 0\\
I_{11} &= \sum\nolimits_i m_i \left(x_i^2 + z_i^2 \right)\\
       &= m(1 + \frac{1}{2} + 1 + \frac{1}{2} + 0 + \frac{1}{2} + 0 + \frac{1}{2}) = 4m\\
I_{12} &= -\sum\nolimits_i m_i y_i z_i\\
       &= - m(0 + 0 + \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} ) = 0
\\
I_{20} &= - \sum\nolimits_i m_i z_i x_i\\
       &= - m(-\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + 0 + 0) = 0\\
I_{21} &= - \sum\nolimits_i m_i z_i y_i\\
       &= - m(0 + 0 + \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}) = 0\\
I_{22} &= \sum\nolimits_i m_i \left(x_i^2 + y_i^2 \right)\\
       &= m(1 + 0 + 1 + 0 + 1 + 0 + 1 + 0) = 4m\\
\end{align*}
$$
{% end %}




The inertia matrix is:


{% mathjax() %}
$$
\begin{align*}
I &= \begin{bmatrix}4m & 0 & 0\\
                     0 & 4m & 0\\
                     0 & 0 & 4m\end{bmatrix}
\end{align*}
$$
{% end %}




Since the matrix is already diagonal, the values of the diagonal elements are the principal moments of inertia:


{% mathjax() %}
$$
A = B = C = 4m\\
$$
{% end %}




The principal axes are $\hat{x}, \hat{y}, \hat{z}$.



---
**b. A cube of uniform density**

Assume origin at center of the cube. The moments of inertia are:


{% mathjax() %}
$$
\begin{align*}
I_{xx} = \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \left(y^2 + z^2\right) \rho~dx dy dz\\
I_{yy} = \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \left(x^2 + z^2\right) \rho~dx dy dz\\
I_{zz} = \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \left(x^2 + y^2\right) \rho~dx dy dz\\
\end{align*}
$$
{% end %}




where $\rho$ is the density of the material, $\rho = \frac{M}{L^3}$. Since the cube is symmetric, the moments of inertia are all equal to each other, $I_{xx} = I_{yy} = I_{zz}$

Products of inertia are:


{% mathjax() %}
$$
\begin{align*}
I_{xy} &= \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} xy \rho~dx dy dz\\
I_{yz} &= \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} yz \rho~dx dy dz\\
I_{zx} &= \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} zx \rho~dx dy dz\\
\end{align*}
$$
{% end %}




As calculated below, the inertia matrix is diagonal with elements equal to $\frac{M L^2}{6}$. Therefore the principal moments of inertia are:


{% mathjax() %}
$$
A = B = C = \frac{M L^2}{6}
$$
{% end %}



The principal axes are $\hat{x}, \hat{y}, \hat{z}$.

```python
x, y, z = symbols('x y z', real=True)
M, L = symbols('M L', positive=True)
rho = M/L**3

Ixx = rho * integrate(y**2 + z**2, (x, -L/2, L/2), (y, -L/2, L/2), (z, -L/2, L/2))
Iyy = rho * integrate(x**2 + z**2, (x, -L/2, L/2), (y, -L/2, L/2), (z, -L/2, L/2))
Izz = rho * integrate(x**2 + y**2, (x, -L/2, L/2), (y, -L/2, L/2), (z, -L/2, L/2))

Ixy = rho * integrate(x*y, (x, -L/2, L/2), (y, -L/2, L/2), (z, -L/2, L/2))
Iyz = rho * integrate(y*z, (x, -L/2, L/2), (y, -L/2, L/2), (z, -L/2, L/2))
Ixz = rho * integrate(x*z, (x, -L/2, L/2), (y, -L/2, L/2), (z, -L/2, L/2))

Iyx, Izy, Izx = Ixy, Iyz, Ixz

I = Matrix([[Ixx, Ixy, Ixz],
            [Iyx, Iyy, Iyz],
            [Izx, Izy, Izz]])

I
```

{% mathjax() %}
$\displaystyle \left[\begin{matrix}\frac{L^{2} M}{6} & 0 & 0\\0 & \frac{L^{2} M}{6} & 0\\0 & 0 & \frac{L^{2} M}{6}\end{matrix}\right]$
{% end %}




---
**c. Five equal point masses rigidly connected by massless stuff. The point masses are at the rectangular coordinates:
(−1, 0, 0), (1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1).**



The center of mass is at $[\frac{1}{5}, \frac{1}{5}, \frac{1}{5}]$.

```python
import numpy as np

points = np.array([[-1, 0, 0],
                   [1, 0, 0],
                   [1, 1, 0],
                   [0, 0, 0],
                   [0, 0, 1]])


N = points.shape[0]
center_of_mass = points.mean(axis=0)
cx,cy,cz = center_of_mass

Ixx = sum([(y - cy)**2 + (z - cz)**2 for x, y, z in points])
Iyy = sum([(x - cx)**2 + (z - cz)**2 for x, y, z in points])
Izz = sum([(x - cx)**2 + (y - cy)**2 for x, y, z in points])

Iyz = sum([(y - cy)*(z - cz)**2 for x, y, z in points])
Ixz = sum([(x - cx)*(z - cz)**2 for x, y, z in points])
Ixy = sum([(x - cx)*(y - cy)**2 for x, y, z in points])

I = Matrix([[Ixx, Ixy, Ixz],
            [Iyx, Iyy, Iyz],
            [Izx, Izy, Izz]]) * m

I
```

{% mathjax() %}
$\displaystyle \left[\begin{matrix}1.6 m & 0.48 m & - 0.12 m\\0 & 3.6 m & - 0.12 m\\0 & 0 & 3.6 m\end{matrix}\right]$
{% end %}


```python
eigenvects = I.eigenvects()
eigenvects
```


    [(1.6*m,
      1,
      [Matrix([
       [1.0],
       [  0],
       [  0]])]),
     (3.6*m,
      2,
      [Matrix([
       [0.24],
       [ 1.0],
       [   0]])])]



```python
a = eigenvects[0][2][0]
b = eigenvects[1][2][0]

c = a.cross(b)
c
```

{% mathjax() %}
$\displaystyle \left[\begin{matrix}0\\0\\1.0\end{matrix}\right]$
{% end %}




The principal moments of inertia are:


{% mathjax() %}
$$
A = 1.6m, B = C = 3.6m\\
$$
{% end %}




The principal axes are: $\hat{x},~ 0.24\hat{x} + 1.0\hat{y},~\hat{z}$
