---
schema: qual/card@1
id: P-UCLAB04F-04
kind: problem
title: Continuity of distance from a fixed point in a metric space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Exam Fall 2004 PDF.
---

::: {.problem}
Suppose $(\mathcal M,\rho)$ is a metric space, $x,y\in\mathcal M$, and $(x_n)$ is a sequence in $\mathcal M$ such that $x_n\to x$.
Prove that
$$
\rho(x_n,y)\longrightarrow\rho(x,y).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $n$,
$$
\bigl|\rho(x_n,y)-\rho(x,y)\bigr|
\le
\rho(x_n,x).
$$


::: pf-proof

The triangle inequality gives
$$
\rho(x_n,y)
\le
\rho(x_n,x)+\rho(x,y),
$$
so
$$
\rho(x_n,y)-\rho(x,y)
\le
\rho(x_n,x).
$$
Interchanging $x_n$ and $x$ gives
$$
\rho(x,y)
\le
\rho(x,x_n)+\rho(x_n,y)
=
\rho(x_n,x)+\rho(x_n,y),
$$
so
$$
\rho(x,y)-\rho(x_n,y)
\le
\rho(x_n,x).
$$
Combining the two inequalities yields the claim.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\rho(x_n,y)\longrightarrow\rho(x,y).
$$


::: pf-proof

Since $x_n\to x$,
$$
\rho(x_n,x)\to0.
$$
By step [](#s1-1){.pf-ref},
$$
0
\le
\bigl|\rho(x_n,y)-\rho(x,y)\bigr|
\le
\rho(x_n,x)\to0.
$$
The squeeze theorem therefore gives
$$
\boxed{\rho(x_n,y)\to\rho(x,y)}.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} is the required conclusion.

:::

:::

:::
