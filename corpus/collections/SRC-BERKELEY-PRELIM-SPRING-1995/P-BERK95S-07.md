---
schema: qual/card@1
id: P-BERK95S-07
kind: problem
title: Equal suprema force equality under a strictly increasing transform at some point
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f,g:[0,1]\to[0,\infty)$ be continuous and suppose
\[
\sup_{0\le x\le1}f(x)=\sup_{0\le x\le1}g(x).
\]
Prove that there exists $t\in[0,1]$ such that
\[
f(t)^2+3f(t)=g(t)^2+3g(t).
\]
:::

::: {.solution}
Set
$$
M\coloneqq
\max_{[0,1]}f
=
\max_{[0,1]}g.
$$
The maxima exist because $f$ and $g$ are continuous on the compact
interval $[0,1]$.

<1>1. There are points $x_f,x_g\in[0,1]$ such that
$$
(f-g)(x_f)\ge0,
\qquad
(f-g)(x_g)\le0.
$$

::: {.proof}
Choose
$$
f(x_f)=M,
\qquad
g(x_g)=M.
$$
Since $g(x_f)\le M$,
$$
(f-g)(x_f)=M-g(x_f)\ge0.
$$
Similarly, $f(x_g)\le M$, so
$$
(f-g)(x_g)=f(x_g)-M\le0.
$$
:::

<1>2. There is $t\in[0,1]$ such that
$$
f(t)=g(t).
$$

::: {.proof}
The function $f-g$ is continuous. If either value in step <1>1 is
zero, take the corresponding point. Otherwise the two values have
opposite signs, so the intermediate value theorem gives a zero
between $x_f$ and $x_g$.
:::

<1>3.
$$
f(t)^2+3f(t)=g(t)^2+3g(t).
$$

::: {.proof}
Substitute the equality $f(t)=g(t)$ from step <1>2 into both sides.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
