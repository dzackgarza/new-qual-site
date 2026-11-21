---
schema: qual/card@1
id: P-CAS24B
kind: problem
title: Sublevel set of a nowhere-zero entire function has unbounded components
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire nowhere zero function.
Define $U = \{z : \abs{f(z)} < 1\}$.
If $U \neq \emptyset$, show that the connected components of $U$ are unbounded.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/SP24_math_220_exam.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. The earlier version of the card ran two points together — that the boundary of the component is nonempty, and that $\abs{f}=1$ exactly on it — and it did not state which form of the maximum modulus principle it applies; both are separated here.

Throughout, $f\colon\CC\to\CC$ is entire and nowhere zero, $U\coloneqq\theset{z\in\CC\mid\abs{f(z)}<1}\neq\varnothing$, $V$ is a connected component of $U$, and $g\coloneqq1/f$, which is entire because $f$ has no zeros.

::: pf

::: {.pf-step #boundary-nonempty}
If $V$ is bounded, then $\partial V\neq\varnothing$.

::: pf-proof
$V$ is nonempty, being a component of the nonempty set $U$, and open. A bounded subset of $\CC$ is not all of $\CC$, so the open nonempty set $V$ has a boundary point: taking $z\notin V$ and $v\in V$, the segment from $v$ to $z$ meets $\partial V$.
:::

:::

::: {.pf-step #boundary-values}
$\partial V\subset\theset{\abs{f}=1}$.

:::: pf-proof

::: {.pf-step #at-most-one}
$\abs{f}\leq1$ on $\partial V$.

::: pf-proof
Each point of $V$ satisfies $\abs{f}<1$, and $f$ is continuous, so a limit of points of $V$ satisfies $\abs{f}\leq1$; every point of $\partial V$ is such a limit.
:::

:::

::: {.pf-step #at-least-one}
$\abs{f}\geq1$ on $\partial V$.

::: pf-proof
Let $z\in\partial V$ and suppose $\abs{f(z)}<1$. Then $z\in U$, which is open, so $z$ is an interior point of $U$ and lies in some connected component $W$ of $U$. Since $z\in\partial V$, every neighbourhood of $z$ meets $V$, and $W$ is a neighbourhood of $z$, so $W\cap V\neq\varnothing$; components are the classes of a partition of $U$, so $W=V$ and $z\in V$, contradicting $z\in\partial V$ (a boundary point of $V$ is not in the open set $V$). Hence $\abs{f(z)}\geq1$.
:::

:::

::: {.pf-step}
The two inequalities give $\abs{f}=1$ on $\partial V$.

::: pf-proof
Steps [](#at-most-one){.pf-ref} and [](#at-least-one){.pf-ref} give $\abs{f}\leq1\leq\abs{f}$ at each boundary point.
:::

:::

::::

:::

::: {.pf-step #maximum-principle}
If $V$ were bounded, the maximum modulus principle would give $\abs{g}\leq1$ on $V$.

::: pf-proof
$g=1/f$ is holomorphic on all of $\CC$, hence on a neighbourhood of the compact set $\overline{V}$ when $V$ is bounded. The maximum modulus principle for a bounded domain says that $\abs{g}$ attains its maximum over $\overline{V}$ on the boundary $\partial V$, which is nonempty by step [](#boundary-nonempty){.pf-ref}; and $\abs{g}=\abs{1/f}=1$ there by step [](#boundary-values){.pf-ref}. Hence $\abs{g(z)}\leq1$ for $z\in V$.
:::

:::

::: pf-step
Therefore every component of $U$ is unbounded.

::: pf-proof
Suppose $V$ were bounded. For $z\in V$ one has $\abs{f(z)}<1$, so $\abs{g(z)}=\abs{1/f(z)}>1$; but step [](#maximum-principle){.pf-ref} gives $\abs{g(z)}\leq1$ on $V$. This contradiction shows that no component of $U$ is bounded, which is the assertion. Note where each hypothesis is used: $f$ nowhere zero makes $g$ entire, and $U\neq\varnothing$ supplies the nonempty component $V$ on which the contradiction is raised.
:::

:::

:::

:::
