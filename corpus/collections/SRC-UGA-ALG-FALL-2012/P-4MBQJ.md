---
schema: qual/card@1
id: P-4MBQJ
kind: problem
title: Proper submodules of a Noetherian module are finite intersections of intersection-indecomposable
  submodules
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Modules
  - Primary Decomposition
relations: []
review: draft
audit:
- event: source-corrected
  by: deepseek-v4.1-flash-free
  date: 2026-10-27
  note: >-
    The printed definition is degenerate: N = N intersect N makes every proper
    submodule decomposable. The remark records the standard definition used by
    the proof.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source called a proper submodule intersection-decomposable when it is not an intersection of two proper submodules, a condition N = N cap N defeats; the statement now defines intersection-indecomposable by N = M_1 cap M_2 with N strictly inside both M_i being impossible.
---

::: {.problem}
Let $R$ be a ring and $M$ an $R\dash$module.
Recall that $M$ is *Noetherian* iff any strictly increasing chain of submodule $M_1 \subsetneq M_2 \subsetneq \cdots$ is finite.
Call a proper submodule $M' \subsetneq M$ *intersection-indecomposable* if it can not be written as the intersection $M' = M_1\intersect M_2$ of two submodules with $M' \subsetneq M_i$ for $i=1,2$.

Prove that for every Noetherian module $M$, any proper submodule $N\subsetneq M$ can be written as a finite intersection $N = N_1 \intersect \cdots \intersect N_k$ of intersection-indecomposable modules.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every proper submodule of a Noetherian module is a finite intersection of intersection-indecomposable submodules.


::: pf-proof

Suppose otherwise, and let $\mathcal S$ be the family of proper submodules not admitting such a finite intersection. The ascending chain condition implies that every nonempty family of submodules has a maximal member, so choose an inclusion-maximal $N\in\mathcal S$. It cannot itself be intersection-indecomposable, since then a single factor would suffice. Hence
$$
N=N_1\cap N_2,\qquad N\subsetneq N_1,\quad N\subsetneq N_2.
$$
Both $N_i$ are proper, since $N_1=M$ would imply $N=N_2$, and similarly for $N_2=M$. By maximality of $N$, each $N_i$ is a finite intersection of intersection-indecomposable submodules. Combining these two finite intersections gives such a decomposition of $N$, contradicting $N\in\mathcal S$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the assertion.

:::

:::

:::
