---
schema: qual/card@1
id: E-3RLT2
kind: problem
title: A sequentially compact metric space is totally bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "a sequentially compact space is totally bounded"; total boundedness needs a metric, so the statement now takes a sequentially compact metric space.'
---

::: {.exercise}

Show that a sequentially compact metric space is totally bounded.

:::

::: {.solution}

Let $(X, d)$ be a sequentially compact metric space, and suppose for contradiction that for some $\varepsilon_0 > 0$ no finite collection of open $\varepsilon_0$-balls covers $X$.

::: pf

::: {.pf-step #separated}

There is a sequence $(x_n)_{n\ge1}$ in $X$ with $d(x_n, x_m) \geq \varepsilon_0$ for all $n \neq m$.

::: pf-proof

Choose $x_1 \in X$. Given $x_1, \ldots, x_k$, the finitely many balls $B(x_i, \varepsilon_0)$, $1 \le i \le k$, do not cover $X$, so there is
$$
x_{k+1} \in X \setminus \bigcup_{i=1}^k B(x_i, \varepsilon_0),
$$
and then $d(x_{k+1}, x_i) \geq \varepsilon_0$ for all $i \leq k$.

:::

:::

::: pf-step

The sequence of step [](#separated){.pf-ref} has no convergent subsequence, contradicting sequential compactness.

::: pf-proof

A convergent subsequence $(x_{n_k})$ is Cauchy, so $d(x_{n_j}, x_{n_k}) < \varepsilon_0$ for all large $j \ne k$; but $n_j \ne n_k$ gives $d(x_{n_j}, x_{n_k}) \geq \varepsilon_0$.

:::

:::

:::

:::
