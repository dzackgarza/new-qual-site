---
schema: qual/card@1
id: P-UCLAB03F-05
kind: problem
title: A second-order Taylor polynomial with cubic remainder in two variables
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Let $f:\RR^2\to\RR$ have continuous partial derivatives of order $3$.
Write down explicitly, in terms of partial derivatives of $f$, a quadratic polynomial $P(x,y)$ such that
\[
|f(x,y)-P(x,y)|
\leq C(x^2+y^2)^{3/2}
\]
for all $(x,y)$ in some sufficiently small neighborhood of $(0,0)$, where $C$ may depend on $f$ but not on $x$ or $y$.
Then prove this estimate.
:::

::: {.solution}

Define
\[
\boxed{
P(x,y)
=
f(0,0)
+f_x(0,0)x
+f_y(0,0)y
+\frac12f_{xx}(0,0)x^2
+f_{xy}(0,0)xy
+\frac12f_{yy}(0,0)y^2
}.
\]

::: pf

::: {.pf-step #s1-1}

There exist $r>0$ and $B>0$ such that every third-order partial derivative of $f$ has absolute value at most $B$ on
\[
\{(u,v):u^2+v^2\le r^2\}.
\]


::: pf-proof

There are finitely many third-order partial derivatives. Each is continuous by hypothesis, hence bounded on the compact closed ball of sufficiently small radius $r$ about $(0,0)$. Taking $B$ to be the maximum of these finitely many bounds gives the claim.

:::

:::

::: {.pf-step #s1-2}

Fix $(x,y)$ with
\[
x^2+y^2\le r^2
\]
and define
\[
g(t)=f(tx,ty),
\qquad
0\le t\le1.
\]
Then
\[
g(0)=f(0,0),
\]
\[
g'(0)=f_x(0,0)x+f_y(0,0)y,
\]
and
\[
g''(0)
=
f_{xx}(0,0)x^2
+2f_{xy}(0,0)xy
+f_{yy}(0,0)y^2.
\]


::: pf-proof

The line segment from $(0,0)$ to $(x,y)$ lies in the closed ball of radius $r$. The chain rule gives
\[
g'(t)=f_x(tx,ty)x+f_y(tx,ty)y.
\]
Differentiating once more and using equality of mixed second partials gives
\[
g''(t)
=
f_{xx}(tx,ty)x^2
+2f_{xy}(tx,ty)xy
+f_{yy}(tx,ty)y^2.
\]
Evaluating at $t=0$ gives the stated formulas.

:::

:::

::: {.pf-step #s1-3}

For $0\le t\le1$,
\[
g'''(t)
=
f_{xxx}(tx,ty)x^3
+3f_{xxy}(tx,ty)x^2y
+3f_{xyy}(tx,ty)xy^2
+f_{yyy}(tx,ty)y^3.
\]


::: pf-proof

Differentiate the expression for $g''(t)$ from step [](#s1-2){.pf-ref}. Equality of mixed partial derivatives follows from the continuity of the third-order partials, so the three terms of type $x^2y$ combine into $3f_{xxy}x^2y$, and similarly for the terms of type $xy^2$.

:::

:::

::: {.pf-step #s1-4}

For $0\le t\le1$,
\[
|g'''(t)|
\le
B(|x|+|y|)^3
\le
2\sqrt2\,B(x^2+y^2)^{3/2}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref} and the formula in step [](#s1-3){.pf-ref},
\[
\begin{aligned}
|g'''(t)|
&\le
B\bigl(
|x|^3+3|x|^2|y|+3|x||y|^2+|y|^3
\bigr)\\
&=
B(|x|+|y|)^3.
\end{aligned}
\]
By Cauchy--Schwarz,
\[
|x|+|y|
\le
\sqrt2\sqrt{x^2+y^2}.
\]
Cubing gives the second inequality.

:::

:::

::: {.pf-step #s1-5}

There exists $\xi\in(0,1)$ such that
\[
f(x,y)-P(x,y)=\frac{g'''(\xi)}6.
\]


::: pf-proof

Taylor's theorem with Lagrange remainder for the one-variable function $g$ at $t=0$, evaluated at $t=1$, gives
\[
g(1)
=
g(0)+g'(0)+\frac12g''(0)+\frac16g'''(\xi)
\]
for some $\xi\in(0,1)$. By step [](#s1-2){.pf-ref}, the first three terms on the right are exactly $P(x,y)$, while $g(1)=f(x,y)$.

:::

:::

::: {.pf-step #s1-6}

For every $(x,y)$ with $x^2+y^2\le r^2$,
\[
\boxed{
|f(x,y)-P(x,y)|
\le
\frac{\sqrt2\,B}{3}(x^2+y^2)^{3/2}
}.
\]


::: pf-proof

By step [](#s1-5){.pf-ref} and then step [](#s1-4){.pf-ref},
\[
|f(x,y)-P(x,y)|
\le
\frac16|g'''(\xi)|
\le
\frac{2\sqrt2\,B}{6}(x^2+y^2)^{3/2}.
\]
This is the displayed estimate.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the required estimate with
\[
C=\frac{\sqrt2\,B}{3}.
\]

:::

:::

:::
