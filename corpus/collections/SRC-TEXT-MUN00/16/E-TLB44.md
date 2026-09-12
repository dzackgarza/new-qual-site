---
schema: qual/card@1
id: E-TLB44
kind: problem
title: Open sets in a closed interval versus open sets in the line
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Consider the set $Y = [-1, 1]$ as a subspace of $\mathbb{R}$.
Which of the following sets are open in $Y$?
Which are open in $\mathbb{R}$?

$$
A = \ts{x \mid \tfrac{1}{2} < \abs{x} < 1},
$$

$$
B = \ts{x \mid \tfrac{1}{2} < \abs{x} \leq 1},
$$

$$
C = \ts{x \mid \tfrac{1}{2} \leq \abs{x} < 1},
$$

$$
D = \ts{x \mid \tfrac{1}{2} \leq \abs{x} \leq 1},
$$

$$
E = \ts{x \mid 0 < \abs{x} < 1 \text{ and } 1/x \notin \mathbb{Z}_+}.
$$
:::

::: {.solution}
Write the sets explicitly:
\[
A=(-1,-\tfrac12)\cup(\tfrac12,1),
\]
\[
B=[-1,-\tfrac12)\cup(\tfrac12,1],
\]
\[
C=(-1,-\tfrac12]\cup[\tfrac12,1),
\]
and
\[
D=[-1,-\tfrac12]\cup[\tfrac12,1].
\]
Thus $A$ is open both in $\mathbb R$ and in $Y=[-1,1]$. The set $B$ is open in $Y$, since
\[
[-1,-\tfrac12)=Y\cap(-2,-\tfrac12),\qquad
(\tfrac12,1]=Y\cap(\tfrac12,2),
\]
but it is not open in $\mathbb R$ because it contains the boundary points $\pm1$. The sets $C$ and $D$ are not open even in $Y$, since the included points $\pm\tfrac12$ have no sufficiently small relative neighborhood contained in the set; consequently they are not open in $\mathbb R$ either.

Finally
\[
E=(-1,0)\cup\left((0,1)-\{1/n:n\ge2\}\right).
\]
The set $\{1/n:n\ge2\}$ has no accumulation point in $(0,1)$ except $0$, which is not in $E$. Hence every point of $E$ has an ordinary open interval contained in $E$, so $E$ is open in $\mathbb R$ and therefore also in $Y$.
:::
