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
- Prove that every simple abelian group is cyclic.
:::

::: {.solution}
Let $G$ be a nontrivial simple abelian group. Choose $1\ne g\in G$. Since $G$ is abelian, every subgroup is normal, so the nontrivial subgroup $\langle g\rangle$ must equal $G$. Hence $G$ is cyclic.

If $G$ were infinite, then $G\cong\mathbb Z$, which has the proper nontrivial subgroup $2\mathbb Z$, contradicting simplicity. Thus $G$ is finite cyclic, say of order $n$. If $n$ were composite, a proper divisor of $n$ would give a proper nontrivial subgroup of $G$. Therefore $n=p$ is prime.

Hence every simple abelian group is isomorphic to $\mathbb Z/p\mathbb Z$ for some prime $p$.
:::
