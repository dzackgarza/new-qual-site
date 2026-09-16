---
schema: qual/card@1
id: P-AGFS15-05
kind: problem
title: Divisors of coordinates and differentials on a cubic curve
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained Algebraic Geometry FS 15 exam-guidelines PDF dated August 12, 2015.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the local parameters at the three branch points and at infinity and computed the orders of y and dx directly.
---

::: {.problem}
Assume $\operatorname{char}k=0$.
Let
\[
C:\quad y^2=(x-e_1)(x-e_2)(x-e_3)\subset\mathbb A^2,
\]
where $e_1,e_2,e_3\in k$ are pairwise distinct.
Let $P_j=(e_j,0)\in C$, and let $P_\infty$ be the point at infinity of the projective closure $\overline C\subset\mathbb P^2$.

Show that
\[
\operatorname{div}(dx)=[P_1]+[P_2]+[P_3]-3[P_\infty],
\]
\[
\operatorname{div}(y)=[P_1]+[P_2]+[P_3]-3[P_\infty],
\]
and hence
\[
\operatorname{div}\!\left(\frac{dx}{y}\right)=0.
\]
In particular, $dx/y$ is a regular nowhere-vanishing differential on $\overline C$.
:::


::: {.solution}
Let
\[
g(x)=(x-e_1)(x-e_2)(x-e_3).
\]
Because the \(e_j\) are pairwise distinct and \(\operatorname{char}k=0\), the projective cubic \(\overline C\) is nonsingular. We compute orders at the three points \(P_j\) and at \(P_\infty\).

<1>1. At each \(P_j\), \(y\) has order \(1\) and \(dx\) has order \(1\).
::: {.proof}
Fix \(j\), and write
\[
g(x)=(x-e_j)g_j(x),
\qquad
 g_j(e_j)=\prod_{i\ne j}(e_j-e_i)\ne0.
\]
Near \(P_j\), the curve equation is
\[
y^2=(x-e_j)g_j(x).
\]
Since \(g_j(e_j)
e0\), the function \(g_j(x)\) is a unit in the local ring at \(P_j\). Moreover,
\[
\frac{\partial}{\partial x}\bigl(y^2-g(x)\bigr)(P_j)=-g'(e_j)\ne0,
\]
so \(y\) is a local parameter at \(P_j\). Hence
\[
\operatorname{ord}_{P_j}(y)=1.
\]
The defining equation then gives
\[
2\operatorname{ord}_{P_j}(y)
=\operatorname{ord}_{P_j}(x-e_j),
\]
so
\[
\operatorname{ord}_{P_j}(x-e_j)=2.
\]

Differentiate \(y^2=(x-e_j)g_j(x)\):
\[
2y\,dy=\bigl(g_j(x)+(x-e_j)g_j'(x)\bigr)\,dx.
\]
The factor in parentheses is a unit at \(P_j\), while \(y\) has order \(1\) and \(dy\) has order \(0\) because \(y\) is a local parameter. Therefore
\[
\operatorname{ord}_{P_j}(dx)=1.
\]
:::

<1>2. At \(P_\infty\), \(y\) and \(dx\) both have order \(-3\).
::: {.proof}
The projective closure is
\[
Y^2Z=(X-e_1Z)(X-e_2Z)(X-e_3Z),
\]
and its unique point with \(Z=0\) is
\[
P_\infty=[0:1:0].
\]
Work in the chart \(Y\ne0\), with
\[
u=X/Y,
\qquad
v=Z/Y.
\]
Then \(P_\infty=(0,0)\), and the equation becomes
\[
v=(u-e_1v)(u-e_2v)(u-e_3v).
\]
The derivative of
\[
G(u,v)=v-(u-e_1v)(u-e_2v)(u-e_3v)
\]
with respect to \(v\) is \(1\) at \((0,0)\). Thus \(u\) is a local parameter at \(P_\infty\). Expanding the equation shows
\[
v=u^3\cdot\varepsilon(u)
\]
for a unit \(\varepsilon(u)\) with \(\varepsilon(0)=1\). Hence
\[
\operatorname{ord}_{P_\infty}(v)=3.
\]

On the original affine chart,
\[
x=\frac XZ=\frac uv,
\qquad
y=\frac YZ=\frac1v.
\]
Therefore
\[
\operatorname{ord}_{P_\infty}(x)=1-3=-2,
\qquad
\operatorname{ord}_{P_\infty}(y)=-3.
\]
Since \(x=u^{-2}\eta(u)\) for a unit \(\eta\) with \(\eta(0)\ne0\), differentiation gives
\[
dx=(-2\eta(0)u^{-3}+\text{higher-order terms})\,du.
\]
Because \(\operatorname{char}k=0\), the leading coefficient is nonzero, so
\[
\operatorname{ord}_{P_\infty}(dx)=-3.
\]
:::

<1>3. Assemble the divisors.
::: {.proof}
The only zeros of \(y\) are \(P_1,P_2,P_3\), each of order \(1\), and its only pole is \(P_\infty\), of order \(3\). Thus
\[
\operatorname{div}(y)
=[P_1]+[P_2]+[P_3]-3[P_\infty].
\]

By <1>1, \(dx\) has a simple zero at each \(P_j\), and by <1>2 it has a pole of order \(3\) at \(P_\infty\). These account for degree \(0\), the degree of a canonical divisor on this genus-one curve, so there are no further zeros or poles. Hence
\[
\operatorname{div}(dx)
=[P_1]+[P_2]+[P_3]-3[P_\infty].
\]
Therefore
\[
\operatorname{div}\!\left(\frac{dx}{y}\right)
=\operatorname{div}(dx)-\operatorname{div}(y)=0.
\]
Thus \(dx/y\) has neither zeros nor poles, so it is a regular nowhere-vanishing differential on \(\overline C\).
:::
:::
