---
schema: qual/card@1
id: P-FHW1-14
kind: problem
title: Power sums over a finite field
classification:
  areas: [algebra]
  topics: [Finite Fields]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $\FF_q$ be a finite field with $q$ elements. Compute $\displaystyle\sum_{a\in\FF_q}a^k$ for $k>0$.
:::

::: {.solution}
The multiplicative group $\FF_q^\times$ is cyclic of order $q-1$, and the sum is an element of $\FF_q$; the integer $q-1$ is written for its class there.

::: pf

::: {.pf-step #generator}
Choose a generator $\gamma$ of $\FF_q^\times$.

::: pf-proof
The multiplicative group of a finite field is cyclic: it is a finite subgroup of the multiplicative group of a field, and a finite subgroup of the multiplicative group of a field is cyclic.
:::

:::

::: {.pf-step #sum}
$$
\sum_{a\in\FF_q}a^k=\boxed{\begin{cases}q-1, & q-1\mid k,\\ 0, & q-1\nmid k.\end{cases}}
$$

::: pf-proof
The term $a=0$ contributes $0$ because $k>0$, so the sum equals $\sum_{j=0}^{q-2}(\gamma^j)^k=\sum_{j=0}^{q-2}(\gamma^k)^j$.
If $q-1$ divides $k$ then $\gamma^k=1$ and each of the $q-1$ summands is $1$, giving $q-1$.
Otherwise $\gamma^k\ne1$, and multiplying the sum $S=\sum_{j=0}^{q-2}(\gamma^k)^j$ by $\gamma^k$ permutes the terms, so $(\gamma^k-1)S=(\gamma^k)^{q-1}-1=0$; since $\gamma^k-1\ne0$ in the field $\FF_q$, $S=0$.
:::

:::

:::

:::
