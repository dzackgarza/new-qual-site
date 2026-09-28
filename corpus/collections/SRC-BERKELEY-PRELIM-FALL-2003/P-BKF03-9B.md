---
schema: qual/card@1
id: P-BKF03-9B
kind: problem
title: Positivity of $\lambda$ for $\Delta u+\lambda u=0$ on the disk with $u_n=-au$ on the boundary
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Green-identity argument and made the
    strict-positivity step explicit: zero gradient energy would make u
    constant, and the Robin condition with a>0 would force that constant to
    vanish.
---

::: {.problem}
Let $\lambda , a \in \mathbb { R }$ , with $a > 0$ . Let $u ( x , y )$ be an infinitely differentiable function defined on an open neighborhood of $x ^ { 2 } + y ^ { 2 } \leq 1$ such that

$$
\begin{array} { c } { { \Delta u + \lambda u = 0 } } \\ { { u _ { n } = - a u } } \end{array}
$$

$$
\begin{array} { r } { \mathrm { ~ i n ~ } x ^ { 2 } + y ^ { 2 } < 1 } \\ { \mathrm { ~ o n ~ } x ^ { 2 } + y ^ { 2 } = 1 . } \end{array}
$$

Here $\Delta$ is the Laplacian $\partial ^ { 2 } / \partial x ^ { 2 } + \partial ^ { 2 } / \partial y ^ { 2 }$ , and $u _ { n }$ denotes the directional derivative of u in the direction of the outward unit normal (pointing away from the origin).
Prove that if u is not identically zero in $x ^ { 2 } + y ^ { 2 } < 1$ , then $\lambda > 0$
:::

::: {.solution}
Let
$$
\Omega=\{(x,y)\in\RR^2:x^2+y^2<1\}.
$$

<1>1. One has
$$
\int_\Omega u^2\,dA>0.
$$

::: {.proof}
The function $u$ is continuous and is not identically zero on
$\Omega$. Hence there is a point at which $\abs{u}>0$, and continuity
gives an open neighborhood on which $u^2$ is bounded below by a
positive constant. Therefore its integral over $\Omega$ is strictly
positive.
:::

<1>2. The differential equation and boundary condition imply the
energy identity
$$
\lambda\int_\Omega u^2\,dA
=
\int_\Omega \abs{\nabla u}^2\,dA
+
a\int_{\partial\Omega}u^2\,ds.
$$

::: {.proof}
Multiply
$$
\Delta u+\lambda u=0
$$
by $u$ and integrate over $\Omega$. Green's first identity gives
$$
\begin{aligned}
0
&=
\int_\Omega u(\Delta u+\lambda u)\,dA
\\
&=
\int_{\partial\Omega}u\,u_n\,ds
-
\int_\Omega\abs{\nabla u}^2\,dA
+
\lambda\int_\Omega u^2\,dA.
\end{aligned}
$$
Using $u_n=-au$ on $\partial\Omega$ yields
$$
0
=
-a\int_{\partial\Omega}u^2\,ds
-
\int_\Omega\abs{\nabla u}^2\,dA
+
\lambda\int_\Omega u^2\,dA,
$$
which rearranges to the asserted identity.
:::

<1>3. The right-hand side in step <1>2 is strictly positive.

::: {.proof}
Both terms are nonnegative because $a>0$. Suppose their sum were zero.
Then
$$
\int_\Omega\abs{\nabla u}^2\,dA=0.
$$
The function $\abs{\nabla u}^2$ is continuous and nonnegative, so it
must vanish identically on $\Omega$. Thus $\nabla u=0$ throughout the
connected set $\Omega$, and $u$ is constant there. Smoothness on a
neighborhood of the closed disk makes the same constant the boundary
value, and its outward normal derivative is then zero. The boundary
condition gives
$$
0=u_n=-au.
$$
Since $a>0$, this forces $u=0$, contradicting the hypothesis that $u$
is not identically zero. Hence the right-hand side of step <1>2 is
strictly positive.
:::

<1>4. One has
$$
\boxed{\lambda>0}.
$$

::: {.proof}
By step <1>1, the factor
$\int_\Omega u^2\,dA$ on the left-hand side of the identity in step
<1>2 is positive. By step <1>3, its right-hand side is positive.
Dividing by $\int_\Omega u^2\,dA$ therefore gives $\lambda>0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
