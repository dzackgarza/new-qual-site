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
---

::: {.problem}
Let $R$ be a ring and $M$ an $R\dash$module.
Recall that $M$ is *Noetherian* iff any strictly increasing chain of submodule $M_1 \subsetneq M_2 \subsetneq \cdots$ is finite.
Call a proper submodule $M' \subsetneq M$ *intersection-decomposable* if it can not be written as the intersection of two proper submodules $M' = M_1\intersect M_2$ with $M_i \subsetneq M$.

Prove that for every Noetherian module $M$, any proper submodule $N\subsetneq M$ can be written as a finite intersection $N = N_1 \intersect \cdots \intersect N_k$ of intersection-indecomposable modules.
:::

::: {.solution}
<1>1. The printed definition does not define intersection-indecomposability.

::: {.proof}
Every proper submodule $N$ satisfies $N=N\cap N$, with both factors proper in $M$. Consequently no proper submodule meets the printed condition. The intended condition is that $N=N_1\cap N_2$ forces $N=N_1$ or $N=N_2$, equivalently that $N$ cannot be expressed as the intersection of two submodules strictly larger than $N$.
:::

<1>2. Under the corrected definition, every proper submodule of a Noetherian module is a finite intersection of intersection-indecomposable submodules.

::: {.proof}
Suppose otherwise, and let $\mathcal S$ be the family of proper submodules not admitting such a finite intersection. The ascending chain condition implies that every nonempty family of submodules has a maximal member, so choose an inclusion-maximal $N\in\mathcal S$. It cannot itself be intersection-indecomposable, since then a single factor would suffice. Hence
\[
N=N_1\cap N_2,\qquad N\subsetneq N_1,\quad N\subsetneq N_2.
\]
Both $N_i$ are proper, since $N_1=M$ would imply $N=N_2$, and similarly for $N_2=M$. By maximality of $N$, each $N_i$ is a finite intersection of intersection-indecomposable submodules. Combining these two finite intersections gives such a decomposition of $N$, contradicting $N\in\mathcal S$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 identifies the failure of the statement as printed, and step <1>2 proves the standard corrected assertion.
:::
:::
