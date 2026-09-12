---
schema: qual/card@1
id: E-BNX60
kind: problem
title: Local finiteness of the shifted double intervals
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
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

Check the statements in Example 1 of §39: the collection

$$
\mathcal{A} = \ts{(n, n+2) \mid n \in \mathbb{Z}}
$$

is locally finite in $\mathbb{R}$, while the collections

$$
\mathcal{B} = \ts{(0, 1/n) \mid n \in \mathbb{Z}_+} \quad \text{and} \quad \mathcal{C} = \ts{(1/(n+1), 1/n) \mid n \in \mathbb{Z}_+}
$$

are locally finite in $(0, 1)$ but not in $\mathbb{R}$.
:::

::: {.solution}
For
\[
\mathcal A=\{(n,n+2):n\in\mathbb Z\},
\]
fix \(x\in\mathbb R\). Choose \(0<\varepsilon<1/2\). If \((x-\varepsilon,x+\varepsilon)\) meets \((n,n+2)\), then
\[
n<x+\varepsilon,
\qquad
n>x-\varepsilon-2.
\]
Only finitely many integers \(n\) satisfy these two inequalities. Hence \(\mathcal A\) is locally finite in \(\mathbb R\).

Now let
\[
\mathcal B=\{(0,1/n):n\ge1\}.
\]
For \(x\in(0,1)\), choose a neighborhood \(V\subset(0,1)\) whose left endpoint is positive, say \(V\subset(a,1)\) with \(a>0\). If \(n>1/a\), then \((0,1/n)\subset(0,a)\), so it misses \(V\). Thus only finitely many members of \(\mathcal B\) meet \(V\), and \(\mathcal B\) is locally finite in \((0,1)\). In \(\mathbb R\), however, every neighborhood of \(0\) meets every sufficiently small interval \((0,1/n)\), hence infinitely many members of \(\mathcal B\). So \(\mathcal B\) is not locally finite in \(\mathbb R\).

Finally let
\[
\mathcal C=\{(1/(n+1),1/n):n\ge1\}.
\]
For each \(x\in(0,1)\), choose a sufficiently small neighborhood avoiding all but the one or two adjacent intervals whose endpoints bracket \(x\); equivalently, since \(1/n\to0\), once a neighborhood of \(x\) has positive lower endpoint, all sufficiently large members of \(\mathcal C\) lie below it. Hence \(\mathcal C\) is locally finite in \((0,1)\). But every neighborhood of \(0\) in \(\mathbb R\) meets \((1/(n+1),1/n)\) for all sufficiently large \(n\), so \(\mathcal C\) is not locally finite in \(\mathbb R\).
:::
