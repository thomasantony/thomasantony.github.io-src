+++
title = "Exercise 2.2: Steiner's Theorem"
date = "2022-11-04T05:30:04Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



### Exercise 2.2: Steiner's theorem

**Let I be the moment of inertia of a body with respect to some given line through the center of mass. Show that the moment of inertia I′ with respect to a second line parallel to the first is**


{% mathjax() %}
$$
I' = I + M R^2\\
$$
{% end %}




**where $M$ is the mass of the body and $R$ is the distance between the lines.**






$$\require{cancel}$$


The position of any particle with respect to the axis can be resolved into a parallel component and a perpendicular component. Only the perpendicular component influences the moment of inertia and so the analysis can be performed in a plane perpendicular to the axis and generalized to the whole object. 

So consider a cross sectional area of the object such that the original axis is perpendicular to this area. Let the center of mass of the area be the origin of the coordinate frame, with basis vectors $\hat{x}$ and $\hat{y}$ in the plane and perpendicular to each other, and $\hat{z}$ being the rotational axis. Let the new parallel axis be passing through the point $w$ on this plane at position $(x_w, y_w)$, parallel to the $\hat{z}$ axis. The distance of this point $w$ from the origin is $R = \sqrt{x_w^2 + y_w^2}$.

The moment of inertia of about the original axis through the center of mass is:


{% mathjax() %}
$$
\begin{align*}
I &= \sum\nolimits_\alpha m_\alpha r_\alpha ^2
\end{align*}
$$
{% end %}




where $r_\alpha$ is the distance of the particle at index $\alpha$ from the origin (the center of mass) and is equal to $\sqrt{x^2_\alpha + y^2_\alpha}$. 

The distance a particle $\alpha$ to the new axis is given by $d_\alpha = \sqrt{ (x_\alpha - x_w)^2 + (y_\alpha - y_w)^2 }$. Therefore, the moment of inertia about the new axis is:


{% mathjax() %}
$$
\begin{align*}
I' &= \sum\nolimits_\alpha m_\alpha d_\alpha ^2 \\
   &= \sum\nolimits_\alpha m_\alpha \left( (x_\alpha - x_w)^2 + (y_\alpha - y_w)^2 \right)\\
   &= \sum\nolimits_\alpha m_\alpha \left( x_\alpha^2 + x^2_w - 2x_\alpha x_w + y^2_\alpha +y^2_w - 2y_\alpha y_w \right) \\
   &= \sum\nolimits_\alpha m_\alpha \left( \underbrace{(x_\alpha^2 + y^2_\alpha)}_{=r_\alpha ^2} + \underbrace{(x^2_w + y^2_w)}_{=R^2} - 2x_\alpha x_w  - 2y_\alpha y_w \right) \\
   &= \sum\nolimits_\alpha m_\alpha r_\alpha ^2 + \sum\nolimits_\alpha m_\alpha R^2 -2 x_w \sum\nolimits_\alpha m_\alpha x_\alpha -2 y_w \sum\nolimits_\alpha m_\alpha y_\alpha
\end{align*}
$$
{% end %}




The total mass of the body $M = \sum\nolimits_\alpha m_\alpha$. Since the origin is the center of mass of the plane, $ \sum\nolimits_\alpha m_\alpha x_\alpha = \sum\nolimits_\alpha m_\alpha y_\alpha = 0$.

{% mathjax() %}
$$
\begin{align*}
I' &= \sum\nolimits_\alpha m_\alpha r_\alpha ^2 + \sum\nolimits_\alpha m_\alpha R^2 -2 x_w \cancel{\sum\nolimits_\alpha m_\alpha x_\alpha} -2 y_w \cancel{\sum\nolimits_\alpha m_\alpha y_\alpha}
\end{align*}
$$
{% end %}




Therefore, the moment of inertia about the parallel axis is:


{% mathjax() %}
$$
I' = I + MR^2\\
$$
{% end %}


