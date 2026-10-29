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
Prove carefully that $\RR^2$ is not a countable union of sets $S_i$, $i=1,2,\ldots$, with each $S_i$ contained in some straight line $L_i$ in $\RR^2$.
:::

::: {.solution}

Let
\[
C=\{(t,t^2):t\in\RR\}
\]
be the standard parabola.

::: pf

::: {.pf-step #s1-1}

Every straight line in $\RR^2$ meets $C$ in at most two points.


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

::: {.pf-step #s1-2}

If
\[
\RR^2=\bigcup_{i=1}^{\infty}S_i
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

::: {.pf-step #s1-3}

Each set $C\cap S_i$ is finite.


::: pf-proof

Since
\[
C\cap S_i\subseteq C\cap L_i,
\]
step [](#s1-1){.pf-ref} shows that $C\cap S_i$ has at most two elements.

:::

:::

::: {.pf-step #s1-4}

Under the assumption in step [](#s1-2){.pf-ref}, the parabola $C$ would be countable.


::: pf-proof

By step [](#s1-3){.pf-ref}, each $C\cap S_i$ is finite. A countable union of finite sets is countable, so the union in step [](#s1-2){.pf-ref} would be countable.

:::

:::

::: {.pf-step #s1-5}

The parabola $C$ is uncountable.


::: pf-proof

The map
\[
\RR\to C,
\qquad
t\mapsto(t,t^2),
\]
is a bijection. Since $\RR$ is uncountable, so is $C$.

:::

:::

::: {.pf-step #s1-6}

Therefore $\RR^2$ cannot be a countable union of subsets of straight lines.


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} contradict the assumption in step [](#s1-2){.pf-ref}. Hence no such countable family $(S_i)$ can cover $\RR^2$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
