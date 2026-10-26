---
schema: qual/card@1
id: P-UCLAB05F-05
kind: problem
title: The plane is not a countable union of straight-line subsets
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
Prove carefully that $\mathbb R^2$ is not a countable union of sets $S_i$, $i=1,2,\ldots$, with each $S_i$ contained in some straight line $L_i$ in $\mathbb R^2$.
:::

Let
\[
C=\{(t,t^2):t\in\mathbb R\}
\]
be the standard parabola.

::: pf

::: pf-step

Every straight line in $\mathbb R^2$ meets $C$ in at most two points.


::: pf-proof

If the line is vertical, it has equation
\[
x=c
\]
and therefore meets $C$ only at
\[
(c,c^2).
\]

If the line is not vertical, it has equation
\[
y=mx+b.
\]
A point $(t,t^2)$ lies on this line exactly when
\[
t^2=mt+b,
\]
or
\[
t^2-mt-b=0.
\]
This quadratic equation has at most two real roots. Hence the line meets $C$ in at most two points.

:::

:::

::: pf-step

If
\[
\mathbb R^2=\bigcup_{i=1}^{\infty}S_i
\qquad\text{with}\qquad
S_i\subseteq L_i,
\]
then
\[
C=\bigcup_{i=1}^{\infty}(C\cap S_i).
\]


::: pf-proof

Intersect the assumed equality with $C$ and distribute intersection over the union.

:::

:::

::: pf-step

Each set $C\cap S_i$ is finite.


::: pf-proof

Since
\[
C\cap S_i\subseteq C\cap L_i,
\]
step <1>1 shows that $C\cap S_i$ has at most two elements.

:::

:::

::: pf-step

Under the assumption in step <1>2, the parabola $C$ would be countable.


::: pf-proof

By step <1>3, each $C\cap S_i$ is finite. A countable union of finite sets is countable, so the union in step <1>2 would be countable.

:::

:::

::: pf-step

The parabola $C$ is uncountable.


::: pf-proof

The map
\[
\mathbb R\to C,
\qquad
t\mapsto(t,t^2),
\]
is a bijection. Since $\mathbb R$ is uncountable, so is $C$.

:::

:::

::: pf-step

Therefore $\mathbb R^2$ cannot be a countable union of subsets of straight lines.


::: pf-proof

Steps <1>4 and <1>5 contradict the assumption in step <1>2. Hence no such countable family $(S_i)$ can cover $\mathbb R^2$.

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
