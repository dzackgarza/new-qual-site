---
schema: qual/card@1
id: P-HQ6DM
kind: problem
title: Similarity and equivalence of matrices are equivalence relations
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Canonical Forms
  - Smith Normal Form
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Prove that each of the following is an equivalence relation.

1. **Similarity** on $M_n(R)$: $A\sim B$ if there exists $P\in\operatorname{GL}_n(R)$ such that
\[
B=PAP^{-1}.
\]

2. **Matrix equivalence** on $M_{m\times n}(R)$: $A\approx B$ if there exist
\[
P\in\operatorname{GL}_m(R),
\qquad
Q\in\operatorname{GL}_n(R)
\]
such that
\[
B=PAQ.
\]
:::


::: {.solution}
<1>1. Similarity is reflexive, symmetric, and transitive.
::: {.proof}
Reflexivity: $A=I_nAI_n^{-1}$.

Symmetry: if $B=PAP^{-1}$, then
\[
A=P^{-1}BP.
\]

Transitivity: if
\[
B=PAP^{-1},
\qquad
C=QBQ^{-1},
\]
then
\[
C=(QP)A(QP)^{-1}.
\]
Thus similarity is an equivalence relation.
:::

<1>2. Matrix equivalence is reflexive, symmetric, and transitive.
::: {.proof}
Reflexivity: for $A\in M_{m\times n}(R)$,
\[
A=I_m A I_n.
\]

Symmetry: if $B=PAQ$ with $P\in\operatorname{GL}_m(R)$ and $Q\in\operatorname{GL}_n(R)$, then
\[
A=P^{-1}BQ^{-1}.
\]

Transitivity: if
\[
B=PAQ,
\qquad
C=RBS
\]
with $R\in\operatorname{GL}_m(R)$ and $S\in\operatorname{GL}_n(R)$, then
\[
C=(RP)A(QS),
\]
and $RP$, $QS$ are invertible. Thus matrix equivalence is an equivalence relation.
:::
:::
