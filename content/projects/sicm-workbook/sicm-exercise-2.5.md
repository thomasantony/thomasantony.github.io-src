+++
title = "Exercise 2.5: A constraint on the moments of inertia"
date = "2022-11-06T00:07:04Z"
draft = false

[extra]
latex = true
chapter = "2"
page_type = "exercise"
+++



## Exercise 2.5: A constraint on the moments of inertia





**Show that the sum of any two of the moments of inertia is greater than or equal to the third moment of inertia. You may assume the moments of inertia are with respect to orthogonal axes.**



Consider an arbitrary orthogonal coordinate frame with axes $x$, $y$ and $z$. The inertia matrix of a body in this coordinate frame is:

{% mathjax() %}
$$
\begin{align*}
I = \begin{bmatrix}\sum\nolimits_i m_i \left(y_i^2 + z_i^2 \right) & -\sum\nolimits_i m_i x_i y_i & -\sum\nolimits_i m_i x_i z_i\\
- \sum\nolimits_i m_i y_i x_i & \sum\nolimits_i m_i \left(x_i^2 + z_i^2 \right) & -\sum\nolimits_i m_i y_i z_i\\
- \sum\nolimits_i m_i z_i x_i & -\sum\nolimits_i m_i z_i y_i & \sum\nolimits_i m_i \left(x_i^2 + y_i^2 \right)\\
\end{bmatrix}
\end{align*}
$$
{% end %}



Therefore the moments of inertia are: $\left[ \sum\nolimits_i m_i \left(y_i^2 + z_i^2 \right), \sum\nolimits_i m_i \left(x_i^2 + z_i^2 \right), \sum\nolimits_i m_i \left(x_i^2 + y_i^2 \right) \right]$


{% mathjax() %}
$$
\begin{align*}
I_{xx} + I_{yy} - I_{zz} &= \sum\nolimits_i m_i \left(y_i^2 + z_i^2 \right) + \sum\nolimits_i m_i \left(x_i^2 + z_i^2 \right) - \sum\nolimits_i m_i \left(x_i^2 + y_i^2 \right)\\
                &= \sum\nolimits_i m_i \left(\cancel{y_i^2} + 2 z_i^2 + \cancel{x_i^2} - \cancel{x_i^2} - \cancel{y_i^2}\right)\\
                &= \sum\nolimits_i m_i \left(2 z_i^2\right)\\
\end{align*}
$$
{% end %}



Since $z_i^2$ are all positive, $\sum\nolimits_i m_i \left(2 z_i^2\right) \geq 0$. Therefore, 

{% mathjax() %}
$$
\begin{align*}
I_{xx} + I_{yy} - I_{zz} &\geq 0 \\
\implies I_{xx} + I_{yy} &\geq I_{zz} \\
\end{align*}
$$
{% end %}


