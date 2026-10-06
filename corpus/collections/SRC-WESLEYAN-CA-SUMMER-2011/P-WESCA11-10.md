---
schema: qual/card@1
id: P-WESCA11-10
kind: problem
title: 'Evaluate a real integral by residues'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Evaluate
\[
\int_0^\infty\frac{x^2}{x^4+5x^2+6}\,dx
\]
using the residue theorem.
:::

::: {.solution}
Set
\[
F(z)
\coloneqq
\frac{z^2}{z^4+5z^2+6}
=
\frac{z^2}{(z^2+2)(z^2+3)}.
\]

<1>1. One has the partial-fraction decomposition
\[
F(z)
=
-\frac{2}{z^2+2}
+
\frac{3}{z^2+3}.
\]

::: {.proof}
Write
\[
\frac{z^2}{(z^2+2)(z^2+3)}
=
\frac{A}{z^2+2}
+
\frac{B}{z^2+3}.
\]
Then
\[
z^2
=
A(z^2+3)+B(z^2+2),
\]
so
\[
A+B=1,
\qquad
3A+2B=0.
\]
Solving gives
\[
A=-2,
\qquad
B=3.
\]
:::

<1>2. The poles of $F$ in the upper half-plane are
\[
z=i\sqrt2
\qquad\text{and}\qquad
z=i\sqrt3.
\]

::: {.proof}
The denominator factors as
\[
(z-i\sqrt2)(z+i\sqrt2)
(z-i\sqrt3)(z+i\sqrt3).
\]
Exactly the two roots with positive imaginary part lie in the upper
half-plane.
:::

<1>3. The residues are
\[
\operatorname{Res}_{z=i\sqrt2}F
=
\frac{i}{\sqrt2}
\]
and
\[
\operatorname{Res}_{z=i\sqrt3}F
=
-\frac{i\sqrt3}{2}.
\]

::: {.proof}
Using step <1>1,
\[
\operatorname{Res}_{z=i\sqrt2}F
=
-2
\operatorname{Res}_{z=i\sqrt2}
\frac1{z^2+2}.
\]
Since
\[
z^2+2
=
(z-i\sqrt2)(z+i\sqrt2),
\]
one gets
\[
\operatorname{Res}_{z=i\sqrt2}
\frac1{z^2+2}
=
\frac1{2i\sqrt2}.
\]
Therefore
\[
\operatorname{Res}_{z=i\sqrt2}F
=
-\frac1{i\sqrt2}
=
\frac{i}{\sqrt2}.
\]

Similarly,
\[
\operatorname{Res}_{z=i\sqrt3}F
=
3\frac1{2i\sqrt3}
=
-\frac{i\sqrt3}{2}.
\]
:::

<1>4. Let $C_R$ be the upper semicircle of radius $R$, with $R>\sqrt3$.
Then
\[
\int_{C_R}F(z)\,dz
\longrightarrow
0
\qquad
(R\to\infty).
\]

::: {.proof}
For sufficiently large $R$ and
\[
|z|=R,
\]
one has
\[
|z^4+5z^2+6|
\ge
|z|^4-5|z|^2-6.
\]
Hence
\[
|F(z)|
\le
\frac{R^2}{R^4-5R^2-6}
=
O(R^{-2}).
\]
The length of $C_R$ is
\[
\pi R.
\]
The ML inequality therefore gives
\[
\left|
\int_{C_R}F(z)\,dz
\right|
=
O(R^{-1})
\longrightarrow0.
\]
:::

<1>5. The integral over the full real line is
\[
\int_{-\infty}^{\infty}
\frac{x^2}{x^4+5x^2+6}\,dx
=
\pi(\sqrt3-\sqrt2).
\]

::: {.proof}
Apply the residue theorem to the upper-half-plane semicircular contour.
Steps <1>2--<1>3 give
\[
\begin{aligned}
\int_{-R}^{R}F(x)\,dx
+
\int_{C_R}F(z)\,dz
&=
2\pi i
\left(
\frac{i}{\sqrt2}
-
\frac{i\sqrt3}{2}
\right).
\end{aligned}
\]
Let
\[
R\to\infty.
\]
By step <1>4, the arc integral vanishes. Thus
\[
\begin{aligned}
\int_{-\infty}^{\infty}F(x)\,dx
&=
2\pi i^2
\left(
\frac1{\sqrt2}
-
\frac{\sqrt3}{2}
\right)\\
&=
-2\pi
\left(
\frac{\sqrt2}{2}
-
\frac{\sqrt3}{2}
\right)\\
&=
\pi(\sqrt3-\sqrt2).
\end{aligned}
\]
:::

<1>6. Therefore
\[
\boxed{
\int_0^\infty
\frac{x^2}{x^4+5x^2+6}\,dx
=
\frac\pi2
(\sqrt3-\sqrt2).
}
\]

::: {.proof}
The integrand is even, so
\[
\int_{-\infty}^{\infty}F(x)\,dx
=
2
\int_0^\infty F(x)\,dx.
\]
Apply step <1>5 and divide by $2$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required residue-theorem evaluation.
:::
:::
