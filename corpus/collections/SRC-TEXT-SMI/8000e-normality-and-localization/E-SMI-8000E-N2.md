---
schema: qual/card@1
id: E-SMI-8000E-N2
kind: problem
title: Minimal nonzero primes of a UFD are principal
classification:
  areas:
  - algebra
  topics:
  - Integral Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
In a ufd $R$, prove all "minimal" prime ideals are principal — i.e. if the only prime ideal contained in $P$ is $\theset{0}$, then $P$ is principal.
:::

::: {.solution}
If $P = 0$, then $P = (0)$ is principal, so assume $P \neq 0$.

::: pf

::: pf-step

$P$ contains an irreducible element $p$.

::: pf-proof

Choose $0 \neq a \in P$. Since $P$ is proper, $a$ is a nonunit, so $a = p_1 p_2 \cdots p_k$ with $k \ge 1$ and each $p_i$ irreducible, because $R$ is a UFD. Since $P$ is prime and $p_1 \cdots p_k \in P$, some $p_i \in P$.

:::

:::

::: {.pf-step #s2}

$(p)$ is a nonzero prime ideal contained in $P$.

::: pf-proof

In a UFD every irreducible element is prime, so $(p)$ is a prime ideal; it is nonzero because $p \neq 0$, and $(p) \subseteq P$ because $p \in P$.

:::

:::

::: pf-qed

By hypothesis the only prime ideal properly contained in $P$ is $0$. By step [](#s2){.pf-ref}, $(p)$ is a nonzero prime contained in $P$, so $(p) = P$, and $P$ is principal.

:::

:::

:::
