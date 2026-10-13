---
schema: qual/card@1
id: P-PRECALC1-13
kind: problem
title: Lower limit $c$ in $3x^5+96=\int_c^x g(t)\,dt$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the map from R to R of Problem 13 on page 3 of Week1_solns.pdf.
---

::: {.problem}
Find $c \in \mathbb{R}$ such that $g : \mathbb{R} \to \mathbb{R}$ satisfies $3x^5 + 96 = \int_c^x g(t)\,dt$.
:::

::: {.solution}
Assume
\[
3x^5+96
=
\int_c^x g(t)\,dt
\]
for all \(x\in\mathbb R\).

<1>1. Differentiate both sides with respect to \(x\):
\[
\boxed{
15x^4=g(x)}.
\]

::: {.proof}
The derivative of
\[
3x^5+96
\]
is
\[
15x^4.
\]
By the fundamental theorem of calculus,
\[
\frac{d}{dx}
\int_c^x g(t)\,dt
=
g(x).
\]
:::

<1>2. Set
\[
x=c
\]
in the original identity.

::: {.proof}
The identity is assumed to hold for every real \(x\).
:::

<1>3. Then
\[
3c^5+96
=
\int_c^c g(t)\,dt
=
0.
\]

::: {.proof}
An integral over an interval of zero length is zero.
:::

<1>4. Hence
\[
c^5=-32.
\]

::: {.proof}
From step <1>3,
\[
3c^5=-96.
\]
Divide by \(3\).
:::

<1>5. Therefore
\[
\boxed{c=-2}.
\]

::: {.proof}
Since
\[
(-2)^5=-32,
\]
and the fifth-power function is strictly increasing on \(\mathbb R\), this
solution is unique.
:::

<1>6. With
\[
g(t)=15t^4
\]
and
\[
c=-2,
\]
one indeed has
\[
\int_{-2}^x15t^4\,dt
=
3x^5+96.
\]

::: {.proof}
\[
\begin{aligned}
\int_{-2}^x15t^4\,dt
&=
\left[
3t^5
\right]_{-2}^x\\
&=
3x^5-3(-2)^5\\
&=
3x^5+96.
\end{aligned}
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 gives the required lower limit, and step <1>6 verifies it.
:::
:::
