+++
title = "Exercise 1.38: Properties of ℰ, the Euler Lagrange Operator"
date = "2022-10-27T06:15:32Z"
draft = false

[extra]
latex = true
+++



### Exercise 1.38: Properties of $\mathscr{E}$, the Euler-Lagrange Operator

**Refer to [Section 1.9](/projects/sicm-workbook/section-1-9-abstraction-of-path-functions#lagrange-equations-at-a-moment-or-the-euler-lagrange-operator) for more details**

Let $F$ and $G$ be two Lagrangian-like functions of a local tuple, $C$ be a local-tuple transformation function, and $c$ a constant. Demonstrate the following properties:



---
#### a. $\mathscr{E}[F+G]=\mathscr{E}[F]+\mathscr{E}[G]$

{% mathjax() %}
$$
\begin{align*}
\mathscr{E}[F+G] &= D_t\partial_2 (F + G) - \partial_1 (F + G) \\
 &= D_t\partial_2 F - \partial_1 F + D_t\partial_2 G - \partial_1 G \\
 \\
\therefore \mathscr{E}[F+G] &= \mathscr{E}[F] + \mathscr{E}[G] \\
\end{align*}
$$
{% end %}





---
#### b. $\mathscr{E}[cF]=c\mathscr{E}[F]$

{% mathjax() %}
$$
\begin{align*}
\mathscr{E}[cF] &= D_t\partial_2 (cF) - \partial_1 (cF) \\
 &= c D_t\partial_2 F - c \partial_1 F = c (D_t\partial_2 F - \partial_1 F)\\
 \\
\therefore \mathscr{E}[cF] &= c \mathscr{E}[F]
\end{align*}
$$
{% end %}





---
#### c. $\mathscr{E}[FG]=\mathscr{E}[F]G+F\mathscr{E}[G]+(D_t F)\partial_2 G+\partial_2 F(D_t G)$


{% mathjax() %}
$$
\begin{align*}
\mathscr{E}[FG] &= D_t\partial_2 (FG) - \partial_1 (FG) \\
 &= D_t G\partial_2 F + F \partial_2 G) - F\partial_1 G -G\partial_1 F\\
 &= D_t (G\partial_2 F) + D_t(F \partial_2 G) - F\partial_1 G -G\partial_1 F \\
 &= (D_t G)(\partial_2 F) + (D_t \partial_2 F)(G) + (D_t F)(\partial_2 G) + (D_t \partial_2 G)(F) - F (\partial_1 G) -G (\partial_1 F) \quad ; \text{Rearranging terms .. }\\ 
 &= \left(D_t \partial_2 F - \partial_1 F \right)(G) + F\left(D_t \partial_2 G - \partial_1 G\right) + (D_t F)\partial_2 G + (D_t G)\partial_2 F \\
 \\
\therefore \mathscr{E}[FG] &= \mathscr{E}[F] G + F\mathscr{E}[G] + (D_t F)\partial_2 G + (D_t G)\partial_2 F 
\end{align*}
$$
{% end %}





---
#### d. $\mathscr{E}[F \circ C]=D_t(D F\circ C)\partial_2C+D F \circ C\mathscr{E}[C]$


{% mathjax() %}
$$
\begin{align*}
\mathscr{E}[F \circ C] &= D_t(\partial_2 (F \circ C)) - \partial_1 (F \circ C) \\
&= D_t \big( (DF \circ C)(\partial_2 C) \big) - (DF \circ C )\partial_1 C \qquad;\text{by chain rule}\frac{\partial F(C(v))}{\partial v} = \underbrace{\frac{\partial F}{\partial C}}_{= DF \circ C} \frac{\partial C}{\partial v}\\
&= D_t (DF \circ C) (\partial_2 C) + (DF \circ C) D_t \partial_2 C - (DF \circ C )\partial_1 C \\
\\
\therefore \mathscr{E}[F \circ C] &= D_t (DF \circ C) (\partial_2 C) + (DF \circ C)\mathscr{E}[C]
\end{align*}
$$
{% end %}
