---
schema: qual/card@1
id: P-GWP4W
kind: problem
title: Simple abelian groups are cyclic
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Abelian Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}

Prove that every simple abelian group is cyclic.

:::

::: {.solution}

Let $G$ be a simple abelian group; in particular $G$ is nontrivial.

::: pf

::: pf-step

$G$ is cyclic.

::: pf-proof

Choose $g\in G$ with $g\ne 1$. Since $G$ is abelian, every subgroup is normal, so the nontrivial subgroup $\langle g\rangle$ equals $G$ by simplicity.

:::

:::

::: pf-step

$G\cong\ZZ/p\ZZ$ for a prime $p$.

::: pf-proof

If $G$ were infinite, then $G\cong\ZZ$, which has the proper nontrivial subgroup $2\ZZ$, contradicting simplicity. So $G$ is cyclic of finite order $n>1$. If $n$ were composite, a proper divisor $d>1$ of $n$ would give a proper nontrivial subgroup of order $d$. Therefore $n$ is prime.

:::

:::

:::

:::
