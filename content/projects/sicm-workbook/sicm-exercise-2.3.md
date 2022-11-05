+++
title = "Exercise 2.3: Some useful moments of inertia"
date = "2022-11-05T19:11:34Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



## Exercise 2.3: Some useful moments of inertia

**Show that the moments of inertia of the following objects are as given:**





---
**a. The moment of inertia of a sphere of uniform density with mass $M$ and radius $R$ about any line through the center is** $\frac{2}{5} M R^2$



$$\require{cancel}$$

The moment of inertia of a body about some axis is given by the expression:


{% mathjax() %}
$$
I_{P}=\iiint _{Q}\rho (x,y,z)\left\|\mathbf {r} \right\|^{2}dV\\
$$
{% end %}




Since the sphere is symmetric, the moment of inertia about any axis through its center of mass is the same. Here we assume that the axis is the $z$ axis. We split the sphere into a collection of infinitesimally thin concentric cylinderical shells around the $z$ axis. 

The moment of inertia is:


{% mathjax() %}
$$
I = \int x^2 dm\\
$$
{% end %}




where $r$ is the distance of a cylinderal shell from the $z$ axis and $dm$ is its mass. The mass $dm$ is equal to $\rho dV$ where $\rho$ is the density of the material and $dV$ is the volume of the cylindrical shell. 

For a sphere of radius $R$, the density $\rho$ is:


{% mathjax() %}
$$
\rho = \frac{M}{\frac{4}{3}\pi R^3} = \frac{3M}{4\pi R^3}\\
$$
{% end %}




```


       z
       |
  .---------.
 (     |     ) --
 ||~--------~|| |
 ||    |     || |
 ||    |     || |
 ||    |     || y
 ||    |     || |
 ||    |<-x->|| |
-------.------------- 
 ||          ||
 ||          ||
 ||          ||
 ||          ||
 ||          ||
 ||          ||
 (------------)
```

The height of the cylindrical shell at distance $x$ from the $z$ axis is equal to $2y$. The thickness of shell is erqual to $dx$ . Therefore volume of the cylindrical shell is:


{% mathjax() %}
$$
\begin{align*}
dV &= 2 \pi r h \Delta r\\
   &= 2 \pi x (2y) dx \\
   &= 4 \pi x \sqrt{R^2 - x^2} dx\\
\end{align*}
$$
{% end %}




Therefore the mass of the cylindrical shell is:


{% mathjax() %}
$$
\begin{align*}
dm &= \rho dV \\
   &= \frac{3 M}{\cancel{4\pi} R^3} \cancel{4 \pi} x \sqrt{R^2 - x^2} dx \\
dm   &= \frac{3 M}{R^3} x \sqrt{R^2 - x^2} dx\\
\end{align*}
$$
{% end %}




The moment of inertia is:


{% mathjax() %}
$$
\begin{align*}
I = \int_{-R}^{+R} x^2 dm \\
  = \int_{-R}^{+R} x^2 \frac{3 M}{R^3} x \sqrt{R^2 - x^2} dx \\
  = \frac{3 M}{R^3}\int_{-R}^{+R} x^3 \sqrt{R^2 - x^2} dx\\
\end{align*}
$$
{% end %}




This expression is integrated using `sympy` below:

```python
R, M = symbols('R M', positive=True)
x = symbols('x', real=True)
(3*M / R**3) * integrate(x**3 * sqrt(R**2 - x**2), (x, 0, R))
```

{% mathjax() %}
$\displaystyle \frac{2 M R^{2}}{5}$
{% end %}




---
**b. The moment of inertia of a spherical shell with mass $M$ and radius $R$ about any line through the center is:** $\frac{2}{3} MR^2$



Again, we can pick any diameter as the axis, and we choose the $z$-axis. Consider an infinitesimally thin ring around the z-axis that is part of the shell (which is itself of radius $R$). 


```
               | z axis
               |
         , - ~ ~ ~ - ,  
     , '=======|=======' ,  <-- thickness is R dθ
   ,           |      /    ,
  ,            | θ  /R      ,
 ,             |   /         ,
 ,             +-/--------R-->,
 ,             |             ,
  ,            |            ,
   ,           |           ,
     ,         |        , '
       ' - , _ _ _ ,  '
               |
```

If the angle of a line from the origin to the edge of the ring to the $z$ axis is $\theta$, the radius of the ring is therefore $R\sin{\theta}$. The thickness of the ring is $R d\theta$. Area of the ring is:


{% mathjax() %}
$$
\begin{align*}
dA &= 2\pi (r) Rd\theta \\
   &= 2\pi R\sin{\theta} R d\theta\\
   &= 2\pi R^2 \sin{\theta} d\theta
\end{align*}
$$
{% end %}



If $\sigma$ is the area-density of the sphere ($\sigma = \frac{M}{4 \pi R^2}$), the mass of the ring $dm = dA \sigma$. The moment of inertia of the ring is therefore:


{% mathjax() %}
$$
\begin{align*}
dI &= r^2 dm \\
   &= R^2 \sin^2{\theta} dm \\
   &= R^2 \sin^2{\theta} \sigma dA \\
   &= (R^2 \sin^2{\theta}) \sigma (2\pi R^2 \sin{\theta} d\theta)\\
   &= (R^2 \sin^2{\theta}) (\frac{M}{\cancelto{2}{4} \cancel{\pi R^2}} \cancel{2} \cancel{\pi R^2} \sin{\theta} d\theta)\\
   &= R^2\frac{M}{2} \sin^3{\theta} d \theta\\
\end{align*}
$$
{% end %}



To obtain the moment of inertia of the body, we integrate $dI$ over $\theta$ from $0$ to $\pi$ ($\theta = 0$ corresponds to the "north pole" of the sphere and $\theta = \pi$ corresponds to the south pole.)


Reference: [https://www.youtube.com/watch?v=Y2X0xjwxxwI](https://www.youtube.com/watch?v=Y2X0xjwxxwI)

```python
R, M = symbols('R M', positive=True)
theta = symbols('theta', real=True)

M * R**2 / 2 * integrate(sin(theta)**3, (theta, 0, pi))
```

{% mathjax() %}
$\displaystyle \frac{2 M R^{2}}{3}$
{% end %}




---
**c. The moment of inertia of a cylinder of uniform density with mass M and radius R about the axis of the cylinder is** $\frac{1}{2} M R^2$



```


      z
      |
  .--------.
 (    |    ) --
 |~--------~|  |
 |    |     |  |
 |    |     |  |
 |    |     | H/2
 |    |     |  |
 |    |<-R->|  |
-------.------------- 
 |          |
 |          |
 |          |
 |          |
 |          |
 |          |
 (----------)
```

Let $z$ axis be the axis of the cylinder. Split the cylinder into concentric infinitesimally thin cylindrical shell around the $z$ axis. The radius of such a shell is $x$ and its thickness is $dx$. The volume of the shell is:

{% mathjax() %}
$$
\begin{align*}
dV &= 2 \pi r h \Delta r\\
   &= 2 \pi x H dx
\end{align*}
$$
{% end %}



The density of the cylinder is $\rho = \frac{M}{\pi R^2 H}$. Therefore the mass of the cylindrical shell is:


{% mathjax() %}
$$
\begin{align*}
dm &= \rho dV \\
   &= \frac{M}{\cancel{\pi} R^2 \cancel{H}} 2 \cancel{\pi} x \cancel{H} dx\\
   &= \frac{2 M}{R^2} x dx\\
\end{align*}
$$
{% end %}



Therefore the moment of inertia of the entire cylinder is:

{% mathjax() %}
$$
\begin{align*}
I &= \int dI\\
  &= \int_0^R x^2 dm \\
  &= \int_0^R x^2 \frac{2 M}{R^2} x dx \\
  &= \frac{2 M}{R^2} \int_0^R x^3 dx \\
  &= \frac{2 M}{R^2} \left.\left[ \frac{x^4}{4}\right]\right\vert_{0}^{R}\\
  &= \frac{\cancel{2} M}{\cancel{R^2}} \left[ \frac{R^\cancelto{2}{4}}{\cancelto{2}{4}} \right]\\
  &= \frac{1}{2}MR^2\\
\end{align*}
$$
{% end %}





---
**d. The moment of inertia of a thin rod of uniform density per unit length with mass M and length L about an axis perpendicular to the rod through the center of mass is** $\frac{1}{12} ML^2$



```
              y-axis
              ^
              |
              |<---- L/2 --->|
              |              | 
              |       dx     |
              |      >||<    | 
              |---x-->||     |
==============+==============| --> x-axis

```

Consider an element at distance $x$ from the center of mass with length $dx$. The mass of this element is $dm = dx \sigma$ if $\sigma$ is the linear-density of the rod, $\sigma = \frac{M}{L}$.

The moment of inertia of this element is:


{% mathjax() %}
$$
dI = x^2 dm = x^2 \sigma dx = \frac{M}{L} x^2 dx\\
$$
{% end %}




Therefore the moment of inertia of the rod is:


{% mathjax() %}
$$
\begin{align*}
I &= \int_{-L/2}^{L/2} \frac{M}{L} x^2 dx \\
  &= \frac{M}{L} \left.\left[ \frac{x^3}{3} \right]\right\vert_{-L/2}^{L/2}\\
  &= \frac{M}{L} \left[ \frac{L^3}{24} - \frac{-L^3}{24} \right] \\
  &= \frac{M}{\cancel{L}} \left[ \frac{L^\cancelto{2}{3}}{12} \right]\\
  &= \frac{1}{12} M L^2\\
\end{align*}
$$
{% end %}


