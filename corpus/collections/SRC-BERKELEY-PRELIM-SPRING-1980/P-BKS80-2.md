---
schema: qual/card@1
id: P-BKS80-2
kind: problem
title: Pointwise limits of uniformly Lipschitz functions are continuous
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the mean-value-theorem Lipschitz bound and its passage to the pointwise limit for each fixed pair of points.
---

::: {.problem}
For each $n\ge1$, let $f_n:\RR\to\RR$ be differentiable with
\[
|f_n'(x)|\le1
\]
for all $n,x$. Suppose $f_n(x)\to g(x)$ for every $x\in\RR$.
Prove that $g$ is continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every $f_n$ is $1$-Lipschitz:
$$
|f_n(x)-f_n(y)|\le|x-y|
$$
for all $x,y\in\RR$.

::: pf-proof

Fix $n$ and $x\ne y$. By the mean value theorem, there is a point $c$
between $x$ and $y$ such that
$$
f_n(x)-f_n(y)=f_n'(c)(x-y).
$$
Hence
$$
|f_n(x)-f_n(y)|
\le
|x-y|
$$
because $|f_n'(c)|\le1$. The case $x=y$ is immediate.

:::

:::

::: {.pf-step #s2}

The pointwise limit $g$ is also $1$-Lipschitz:
$$
|g(x)-g(y)|\le|x-y|
$$
for all $x,y\in\RR$.

::: pf-proof

Fix $x,y\in\RR$. By pointwise convergence,
$$
f_n(x)-f_n(y)\longrightarrow g(x)-g(y).
$$
Taking limits in the inequality from step [](#s1){.pf-ref} and using continuity of
the absolute-value function gives
$$
|g(x)-g(y)|\le|x-y|.
$$

:::

:::

::: {.pf-step #s3}

The function $g$ is continuous on $\RR$.

::: pf-proof

Fix $x\in\RR$ and $\varepsilon>0$. If
$$
|y-x|<\varepsilon,
$$
then step [](#s2){.pf-ref} gives
$$
|g(y)-g(x)|\le|y-x|<\varepsilon.
$$
Thus $g$ is continuous at every $x$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
