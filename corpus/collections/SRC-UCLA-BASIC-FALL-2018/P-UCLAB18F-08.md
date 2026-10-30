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
Let $X$ be a real symmetric $n\times n$ matrix and let $z\in\CC$ with $\operatorname{Im}z>0$.
Put
$$
G=(X-zI)^{-1}.
$$
Show that for each $i$,
$$
\sum_{j=1}^n\abs{G_{ij}}^2=\frac{\operatorname{Im}G_{ii}}{\operatorname{Im}z}.
$$
:::

::: {.solution}

::: pf

::: pf-step

The matrix
$$
X-zI
$$
is invertible.


::: pf-proof

Suppose
$$
(X-zI)v=0
$$
for some
$$
v\in\CC^n.
$$
Then
$$
Xv=zv.
$$
Since $X$ is real symmetric, it is Hermitian, so every eigenvalue of $X$ is real.
But
$$
\operatorname{Im}z>0,
$$
so $z$ is not real.
Hence no nonzero $v$ can satisfy the displayed equation.
Thus
$$
\ker(X-zI)=\{0\},
$$
and the square matrix is invertible.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
G^*
=(X-\overline z\,I)^{-1}
}.
$$


::: pf-proof

Since
$$
G=(X-zI)^{-1},
$$
taking adjoints gives
$$
G^*
=
\bigl((X-zI)^{-1}\bigr)^*
=
\bigl((X-zI)^*\bigr)^{-1}.
$$
Because $X^*=X$,
$$
(X-zI)^*
=
X-\overline z\,I.
$$

:::

:::

::: {.pf-step #s1-3}

The resolvent identity gives
$$
\boxed{
G-G^*
=(z-\overline z)\,GG^*
}.
$$


::: pf-proof

For invertible matrices $A,B$,
$$
A^{-1}-B^{-1}
=
A^{-1}(B-A)B^{-1}.
$$
Apply this with
$$
A=X-zI,
\qquad
B=X-\overline z\,I.
$$
Then
$$
B-A
=(z-\overline z)I.
$$
Using step [](#s1-2){.pf-ref},
$$
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
$$

:::

:::

::: {.pf-step #s1-4}

Taking the $(i,i)$ entry in step [](#s1-3){.pf-ref} gives
$$
2i\,\operatorname{Im}G_{ii}
=
2i\,\operatorname{Im}z\,(GG^*)_{ii}.
$$


::: pf-proof

The left side is
$$
(G-G^*)_{ii}
=
G_{ii}-\overline{G_{ii}}
=
2i\,\operatorname{Im}G_{ii}.
$$
Also
$$
z-\overline z
=
2i\,\operatorname{Im}z.
$$
Substitute these into the diagonal entry of step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

One has
$$
(GG^*)_{ii}
=
\sum_{j=1}^n\abs{G_{ij}}^2.
$$


::: pf-proof

By matrix multiplication,
$$
(GG^*)_{ii}
=
\sum_{j=1}^n
G_{ij}(G^*)_{ji}.
$$
Since
$$
(G^*)_{ji}
=
\overline{G_{ij}},
$$
this becomes
$$
\sum_{j=1}^n
G_{ij}\overline{G_{ij}}
=
\sum_{j=1}^n\abs{G_{ij}}^2.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore, for every $i$,
$$
\boxed{
\sum_{j=1}^n\abs{G_{ij}}^2
=
\frac{\operatorname{Im}G_{ii}}
{\operatorname{Im}z}
}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} and divide by
$$
2i\,\operatorname{Im}z.
$$
This denominator is nonzero because
$$
\operatorname{Im}z>0.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required identity.

:::

:::

:::
