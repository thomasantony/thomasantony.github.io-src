+++
title = "Exercise 2.4: Jupiter"
date = "2022-11-05T23:47:04Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



## Exercise 2.4: Jupiter





---
**a. The density of a planet increases toward the center. Provide an argument that the moment of inertia of a planet is less than that of a sphere of uniform density of the same mass and radius.**



The higher masses at the center of the planet are scaled by the smaller distances and the smaller masses at the periphery are multiplied the larger distances. With uniform density, there would be more mass at the periphery, contributing to a higher total moment of inertia.



---
**b. The density as a function of radius inside Jupiter is well approximated by**


{% mathjax() %}
$$
\rho(r) = \frac{M}{R^3} \frac{\sin{(\pi r/R)}}{4r/R}
$$
{% end %}




**where $M$ is the mass and $R$ is the radius of Jupiter. Find the moment of inertia of Jupiter in terms of $M$ and $R$.**



```
               | z axis
               |
               |
              >|      |<--- r sinΦ
         , - ~ ~ ~ - ,|  
     , '       |------<>' ,  
   ,           |      /    ,
  ,            | Φ  /R      ,
 ,             |   /         ,
 ,             +-/--------R-->,
 ,             |             ,
  ,            |            ,
   ,           |           ,
     ,         |        , '
       ' - , _ _ _ ,  '
               |
```



Consider an infinitesimal volume at position $(r, \theta, \phi)$ where $r$ is the radial distance from the center, $\theta$ is the longitude and $\phi$ is the colatitude. Assume that the north-south axis is the axis we are interested in. The distance of the volume from the axis is $r_\perp = r\sin\phi$. The dimensions of the elemental volume are $dr$ in the radial direction, $d\theta$ along the longitude and $d\phi$ along the colatitude. The arc lengths of the "sides" of the element are $r\sin\phi d\theta$ and $r d\phi$. The volume is $dV = r\sin\phi~d\theta~rd\phi~dr$.


{% mathjax() %}
$$
\begin{align*}
I &= \iiint_Q r_\perp^2 dm \\
  &= \iiint_Q r^2 \sin^2{\phi}~\rho(r)~dV \\
  &= \iiint_Q r^2 \sin^2{\phi}~\rho(r)~r\sin\phi~d\theta~rd\phi~dr \\
  &= \iiint_Q r^2 \sin^2{\phi}~\rho(r)~r^2 \sin{\phi}~d\theta~d\phi~dr \\
  &= \iiint_Q \rho(r) r^4 \sin^3{\phi}~d\theta~d\phi~dr \\
  &= \int_0^R \int_{-\pi}^{\pi} \int_{0}^{\pi} \rho(r) r^4 \sin^3{\phi}~d\phi~d\theta~dr\\
  &= \int_0^R \rho(r) r^4 \int_{-\pi}^{\pi} \int_{0}^{\pi} \sin^3{\phi}~d\phi~d\theta~dr\\
\end{align*}
$$
{% end %}




Reference: [https://math.stackexchange.com/questions/1475096/why-does-the-volume-element-in-spherical-polar-coordinates-contain-a-sine-of-the](https://math.stackexchange.com/questions/1475096/why-does-the-volume-element-in-spherical-polar-coordinates-contain-a-sine-of-the)

```python
r = symbols('r', positive=True)
theta, phi = symbols('theta phi', real=True)
M, R = symbols('M R', positive=True)

rho = M/R**3 * sin(pi*r/R)/(4*r/R)

integral_1 = integrate( sin(phi)**3, (phi, 0, pi))
integral_2 = integrate( integral_1, (theta, -pi, pi) )
integral_3 = integrate( rho * r**4 * integral_2, (r, 0, R))
simplify(integral_3)
```

{% mathjax() %}
$\displaystyle \frac{2 M R^{2} \left(-6 + \pi^{2}\right)}{3 \pi^{2}}$
{% end %}




The moment of inertia of Jupiter is:

{% mathjax() %}
$$
I = \frac{2}{3\pi^2} MR^2 \left(\pi^2 -6\right)
$$
{% end %}


