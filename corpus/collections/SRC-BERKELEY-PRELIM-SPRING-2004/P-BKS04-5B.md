---
schema: qual/card@1
id: P-BKS04-5B
kind: problem
title: A finite group with pairwise noncommuting elements of prescribed orders
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $n_1,\ldots,n_r$ be integers $\geq2$. Prove that there is a finite group $G$ containing elements $g_1,\ldots,g_r$ such that $g_i$ has exact order $n_i$ for each $i$, and $g_ig_j\neq g_jg_i$ for $i\neq j$.
:::

::: {.solution}
Let $T_1,\ldots,T_r$ be disjoint sets with $\#T_i=n_i-1$. Let $S$ be the union of the $T_i$ together with one more element $x$ outside all the $T_i$. Let $G$ be the set of permutations of $S$.

Choose $g_i\in G$ such that $g_i$ acts as an $n_i$-cycle on $T_i\cup\{x\}$, and acts as the identity on the complement.
Then $g_i$ has order $n_i$. If $i\neq j$, then $(g_ig_j)(x)=g_i(g_j(x))\in g_i(T_j)=T_j$, and similarly $(g_jg_i)(x)\in T_i$, so $g_ig_j\neq g_jg_i$.
:::
