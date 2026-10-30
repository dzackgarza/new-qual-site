---
schema: qual/card@1
id: P-AMH-ALG-SG16-31
kind: problem
title: Reducibility of $x^2+3$ over $\FF_7$ and an intermediate ideal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $g(x)=x^2+3\in\FF_7[x]$, where $\FF_7=\{0,1,2,3,4,5,6\}$ is the field of seven elements.
(a) Prove that $g$ is reducible in $\FF_7[x]$.
(b) Let $\langle g\rangle\subseteq\FF_7[x]$ denote the principal ideal $\{gh\mid h\in\FF_7[x]\}$.
Find an ideal $I\subseteq\FF_7[x]$ such that $\langle g\rangle\subsetneq I\subsetneq\FF_7[x]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
In $\FF_7[x]$, $g(x)=(x-2)(x+2)$.

::: pf-proof
$(x-2)(x+2)=x^2-4=x^2+3$, because $-4\equiv3\pmod 7$.
:::

:::

::: {.pf-step #s1-2}
Part (a): $g$ is reducible.

::: pf-proof
Step [](#s1-1){.pf-ref} writes $g$ as a product of two polynomials of degree $1$.
:::

:::

::: {.pf-step #s1-3}
Let $I=\langle x-2\rangle$. Then $\langle g\rangle\subseteq I$.

::: pf-proof
For $h\in\FF_7[x]$, step [](#s1-1){.pf-ref} gives $hg=\bigl((x+2)h\bigr)(x-2)\in I$.
:::

:::

::: {.pf-step #s1-4}
$x-2\notin\langle g\rangle$ and $1\notin I$.

::: pf-proof
A nonzero multiple of $g$ has degree at least $2$, and $\deg(x-2)=1$. A nonzero multiple of $x-2$ has degree at least $1$, and $\deg 1=0$.
:::

:::

::: pf-step
Part (b): $\boxed{I=\langle x-2\rangle}$ satisfies $\langle g\rangle\subsetneq I\subsetneq\FF_7[x]$.

::: pf-proof
Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.
:::

:::

:::

:::
