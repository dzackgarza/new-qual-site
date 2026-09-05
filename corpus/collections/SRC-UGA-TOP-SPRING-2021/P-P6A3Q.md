---
schema: qual/card@1
id: P-P6A3Q
kind: problem
title: Free null-homotopy of every circle map forces trivial fundamental group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement and the meaning of freely against problem 4 of the official UGA Spring 2021 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the moving-basepoint issue directly from the boundary of the free-homotopy square rather than treating free homotopy as based homotopy.
---

::: {.problem}
Suppose that $X$ is a topological space and $x_0\in X$, and suppose that every continuous map $\gamma: S^1 \to X$ is freely homotopic to the constant map to $x_0$.
Prove that $\pi_1(X, x_0) = \ts{ e }$.

> Note that "freely" means there are no conditions on basepoints.
:::

::: {.solution}
<1>1. Let $[\gamma]\in\pi_1(X,x_0)$ be arbitrary.
::: {.proof}
Choose a representative loop
\[
\gamma:S^1\longrightarrow X
\]
based at $x_0$.
Fix the basepoint
\[
*=1\in S^1,
\]
so that
\[
\gamma(*)=x_0.
\]
By hypothesis, there is a free homotopy
\[
H:S^1\times[0,1]\longrightarrow X
\]
from $\gamma$ to the constant map at $x_0$:
\[
H(z,0)=\gamma(z),
\qquad
H(z,1)=x_0.
\]
:::

<1>2. The track of the basepoint during the free homotopy is a loop at $x_0$.
::: {.proof}
Define
\[
\alpha(t)=H(*,t).
\]
At the two endpoints,
\[
\alpha(0)=H(*,0)=\gamma(*)=x_0
\]
and
\[
\alpha(1)=H(*,1)=x_0.
\]
Thus $\alpha$ is a loop based at $x_0$.
:::

<1>3. The loop $\gamma*\alpha*\alpha^{-1}$ is null-homotopic.
::: {.proof}
Let
\[
q:[0,1]\longrightarrow S^1,
\qquad
q(s)=e^{2\pi i s},
\]
and define
\[
F:[0,1]^2\longrightarrow X,
\qquad
F(s,t)=H(q(s),t).
\]
Since $q(0)=q(1)=*$, the four oriented sides of the square map as follows:

- the bottom edge $t=0$, from left to right, maps to $\gamma$;
- the right edge $s=1$, from bottom to top, maps to $\alpha$;
- the top edge $t=1$, from right to left, maps to the constant loop at $x_0$;
- the left edge $s=0$, from top to bottom, maps to $\alpha^{-1}$.

Hence the restriction of $F$ to the oriented boundary $\partial[0,1]^2$ represents
\[
\gamma*\alpha*c_{x_0}*\alpha^{-1}.
\]
But this boundary map extends over the whole square by $F$.
Since the square is a disk, its boundary loop is null-homotopic.
Therefore
\[
[\gamma][\alpha][\alpha]^{-1}=e
\]
in $\pi_1(X,x_0)$.
:::

<1>4. The class $[\gamma]$ is trivial.
::: {.proof}
From <1>3,
\[
[\gamma][\alpha][\alpha]^{-1}=e.
\]
Since
\[
[\alpha][\alpha]^{-1}=e,
\]
we obtain
\[
[\gamma]=e.
\]
The class $[\gamma]$ was arbitrary, so
\[
\boxed{\pi_1(X,x_0)=\{e\}}.
\]
:::
:::
