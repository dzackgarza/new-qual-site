---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-04
kind: problem
title: A compact union of two Hausdorff subspaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The topology is now checked to be a
    topology rather than presented, compactness is derived from finiteness, the failure of
    Hausdorffness is proved from the shape of the open sets, and the two subspaces are verified to be
    Hausdorff so that the hypotheses of the question are met. Not checked: the workshop sheet, which
    the collection retains as a problem file only; the statement is as transcribed on the card. No
    retained solution set covers the exercise, so the argument is the card's own. No statement
    repair.
---

::: {.problem}
Let $X$ be a compact space.
If $X=A\cup B$ with both $A$ and $B$ Hausdorff, must $X$ be Hausdorff?
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the problem sheets alone, so the argument is the card's own. The answer is no, and the counterexample is the two-point Sierpiński space.

::: pf

::: {.pf-step #topology}
$\tau=\{\varnothing,\{1\},X\}$ is a topology on $X=\{0,1\}$.

::: pf-proof
A topology must contain $\varnothing$ and $X$ and be closed under finite intersections and arbitrary unions. The family consists of $\varnothing,\{1\},X$: the intersection of $\{1\}$ with itself or with either of the others is $\varnothing$ or $\{1\}$, and the union of $\{1\}$ with either of the others is $\{1\}$ or $X$; both are in $\tau$.
:::

:::

::: {.pf-step #compact}
$(X,\tau)$ is compact.

::: pf-proof
Any open cover of $X$ contains some member containing $0$, and the only open set containing $0$ is $X$ itself, since $\varnothing$ and $\{1\}$ do not contain $0$. So any open cover has $\{X\}$ as a subcover, or more plainly contains $X$; hence a finite subcover exists.
:::

:::

::: {.pf-step #not_hausdorff}
$(X,\tau)$ is not Hausdorff.

::: pf-proof
Suppose $0\in U$, $1\in V$ with $U,V$ open and disjoint. The only open set containing $0$ is $X$, so $U=X$; then $V\subseteq X=U$, so $U\cap V=V$, and disjointness forces $V=\varnothing$, which does not contain $1$. So no such pair exists and the space is not Hausdorff.
:::

:::

::: {.pf-step #pieces}
$A=\{0\}$ and $B=\{1\}$ are Hausdorff in the subspace topology and $X=A\cup B$.

::: pf-proof
A singleton with its subspace topology is Hausdorff: its only two points coincide, and the condition on distinct pairs is vacuous. The union is all of $X$ because $X=\{0,1\}$.
:::

:::

::: {.pf-step}
A compact space need not be Hausdorff even when it is the union of two Hausdorff subspaces.

::: pf-proof
Steps [](#topology){.pf-ref} to [](#pieces){.pf-ref} give a compact space $X$, not Hausdorff, written as the union of the two Hausdorff subspaces $\{0\}$ and $\{1\}$. So the answer to the question is no, and the Sierpiński two-point space is the counterexample.
:::

:::

:::

:::
