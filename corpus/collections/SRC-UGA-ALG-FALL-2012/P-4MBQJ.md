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
There is a small defect in the printed definition: if the two factors are only
required to be proper submodules of $M$, then every proper $N$ satisfies
$N=N\cap N$, so no proper submodule would be intersection-indecomposable.
The standard intended definition is that $N$ is intersection-indecomposable
if
\[
N=N_1\cap N_2
\]
implies $N=N_1$ or $N=N_2$; equivalently, $N$ cannot be written as the
intersection of two submodules which both strictly contain $N$.

With this correction, suppose for contradiction that some proper submodule of
$M$ is not a finite intersection of intersection-indecomposable submodules.
Let $\mathcal S$ be the set of all such counterexamples. Since $M$ is
Noetherian, every nonempty family of submodules has a maximal member under
inclusion, so choose a maximal $N\in\mathcal S$.

The submodule $N$ itself cannot be intersection-indecomposable, because then it
would already be a finite intersection with one factor. Hence there are
submodules $N_1,N_2$ with
\[
N\subsetneq N_1,\qquad N\subsetneq N_2,
\qquad N=N_1\cap N_2.
\]
Both $N_1$ and $N_2$ are proper: if, say, $N_1=M$, then
$N=N_1\cap N_2=N_2$, contradicting $N\subsetneq N_2$.

By maximality of $N$ in $\mathcal S$, neither $N_1$ nor $N_2$ belongs to
$\mathcal S$. Therefore there are intersection-indecomposable submodules
$Q_1,\ldots,Q_r$ and $Q_{r+1},\ldots,Q_s$ such that
\[
N_1=Q_1\cap\cdots\cap Q_r,
\qquad
N_2=Q_{r+1}\cap\cdots\cap Q_s.
\]
Consequently
\[
N=N_1\cap N_2
=Q_1\cap\cdots\cap Q_s,
\]
contradicting $N\in\mathcal S$. Thus $\mathcal S$ is empty, and every proper
submodule of a Noetherian module is a finite intersection of
intersection-indecomposable submodules.
:::
