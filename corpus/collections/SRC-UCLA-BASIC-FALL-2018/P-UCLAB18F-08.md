---
schema: qual/card@1
id: P-UCLAB18F-08
kind: problem
title: Resolvent row norm identity for a symmetric matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $X$ be a real symmetric $n\times n$ matrix and let $z\in\mathbb C$ with $\operatorname{Im}z>0$.
Put
\[
G=(X-zI)^{-1}.
\]
Show that for each $i$,
\[
\sum_{j=1}^n|G_{ij}|^2=\frac{\operatorname{Im}G_{ii}}{\operatorname{Im}z}.
\]
:::

::: pf

::: pf-step

The matrix
\[
X-zI
\]
is invertible.


::: pf-proof

Suppose
\[
(X-zI)v=0
\]
for some
\[
v\in\mathbb C^n.
\]
Then
\[
Xv=zv.
\]
Since $X$ is real symmetric, it is Hermitian, so every eigenvalue of $X$ is real.
But
\[
\operatorname{Im}z>0,
\]
so $z$ is not real.
Hence no nonzero $v$ can satisfy the displayed equation.
Thus
\[
\ker(X-zI)=\{0\},
\]
and the square matrix is invertible.

:::

:::

::: pf-step

One has
\[
\boxed{
G^*
=(X-\overline z\,I)^{-1}
}.
\]


::: pf-proof

Since
\[
G=(X-zI)^{-1},
\]
taking adjoints gives
\[
G^*
=
\bigl((X-zI)^{-1}\bigr)^*
=
\bigl((X-zI)^*\bigr)^{-1}.
\]
Because $X^*=X$,
\[
(X-zI)^*
=
X-\overline z\,I.
\]

:::

:::

::: pf-step

The resolvent identity gives
\[
\boxed{
G-G^*
=(z-\overline z)\,GG^*
}.
\]


::: pf-proof

For invertible matrices $A,B$,
\[
A^{-1}-B^{-1}
=
A^{-1}(B-A)B^{-1}.
\]
Apply this with
\[
A=X-zI,
\qquad
B=X-\overline z\,I.
\]
Then
\[
B-A
=(z-\overline z)I.
\]
Using step <1>2,
\[
\begin{aligned}
G-G^*
&=
(X-zI)^{-1}
-
(X-\overline z\,I)^{-1}\\
&=
(X-zI)^{-1}
\bigl((z-\overline z)I\bigr)
(X-\overline z\,I)^{-1}\\
&=
(z-\overline z)\,GG^*.
\end{aligned}
\]

:::

:::

::: pf-step

Taking the $(i,i)$ entry in step <1>3 gives
\[
2i\,\operatorname{Im}G_{ii}
=
2i\,\operatorname{Im}z\,(GG^*)_{ii}.
\]


::: pf-proof

The left side is
\[
(G-G^*)_{ii}
=
G_{ii}-\overline{G_{ii}}
=
2i\,\operatorname{Im}G_{ii}.
\]
Also
\[
z-\overline z
=
2i\,\operatorname{Im}z.
\]
Substitute these into the diagonal entry of step <1>3.

:::

:::

::: pf-step

One has
\[
(GG^*)_{ii}
=
\sum_{j=1}^n|G_{ij}|^2.
\]


::: pf-proof

By matrix multiplication,
\[
(GG^*)_{ii}
=
\sum_{j=1}^n
G_{ij}(G^*)_{ji}.
\]
Since
\[
(G^*)_{ji}
=
\overline{G_{ij}},
\]
this becomes
\[
\sum_{j=1}^n
G_{ij}\overline{G_{ij}}
=
\sum_{j=1}^n|G_{ij}|^2.
\]

:::

:::

::: pf-step

Therefore, for every $i$,
\[
\boxed{
\sum_{j=1}^n|G_{ij}|^2
=
\frac{\operatorname{Im}G_{ii}}
{\operatorname{Im}z}
}.
\]


::: pf-proof

Combine steps <1>4 and <1>5 and divide by
\[
2i\,\operatorname{Im}z.
\]
This denominator is nonzero because
\[
\operatorname{Im}z>0.
\]

:::

:::

::: pf-qed

Step <1>6 is the required identity.

:::

:::
