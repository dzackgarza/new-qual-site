---
schema: qual/card@1
id: P-LQXXN
kind: problem
title: Odd-degree elements generate the same field as their squares
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent Hungerford chapter-V solutions-manual transcription explicitly labeling the statement Exercise V.1.8.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if $u\in F$ is algebraic of odd degree over $K$, then so is $u^2$, and moreover $K(u) = K(u^2)$.
:::

::: solution
Let
\[
n=[K(u):K],
\]
which is odd by hypothesis.

<1>1. The element $u^2$ is algebraic over $K$.
::: proof
Since $u$ is algebraic over $K$, the extension $K(u)/K$ is finite. The element
$u^2$ belongs to the finite extension $K(u)$, so it is algebraic over $K$.
:::

<1>2. One has
\[
[K(u):K(u^2)]\le2.
\]
::: proof
The element $u$ is a root of
\[
X^2-u^2\in K(u^2)[X].
\]
Therefore the minimal polynomial of $u$ over $K(u^2)$ has degree at most $2$,
which is exactly the asserted inequality.
:::

<1>3. The degree $[K(u):K(u^2)]$ divides the odd integer $n$.
::: proof
By <1>1, the tower
\[
K\subseteq K(u^2)\subseteq K(u)
\]
consists of finite extensions. The tower law gives
\[
n=[K(u):K]
=[K(u):K(u^2)]\,[K(u^2):K].
\]
Thus $[K(u):K(u^2)]$ divides $n$.
:::

<1>4. Consequently
\[
[K(u):K(u^2)]=1.
\]
::: proof
By <1>2 this degree is either $1$ or $2$. By <1>3 it divides the odd integer
$n$, so it cannot equal $2$.
:::

<1>5. Therefore
\[
K(u)=K(u^2).
\]
::: proof
The inclusion $K(u^2)\subseteq K(u)$ is immediate. By <1>4 the extension has
degree $1$, hence the two fields are equal.
:::
:::
