---
schema: qual/card@1
id: P-QTPHE
kind: problem
title: Similarity and matrix equivalence are equivalence relations
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA Hungerford problem-set reproduction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that similarity is an equivalence relation on $M_n(R)$, and \*equivalence\* is an equivalence relation on $M_{m\times n}(R)$.
:::

::: solution
Recall that $A,B\in M_n(R)$ are similar if
\[
B=P^{-1}AP
\]
for some $P\in\operatorname{GL}_n(R)$, and that
$A,B\in M_{m\times n}(R)$ are equivalent if
\[
B=PAQ
\]
for some $P\in\operatorname{GL}_m(R)$ and
$Q\in\operatorname{GL}_n(R)$.

<1>1. Similarity is reflexive.
::: proof
For every $A\in M_n(R)$,
\[
A=I_n^{-1}AI_n,
\]
so $A$ is similar to itself.
:::

<1>2. Similarity is symmetric.
::: proof
If $B=P^{-1}AP$, then multiplying by $P$ on the left and $P^{-1}$ on the right
gives
\[
A=PBP^{-1}=(P^{-1})^{-1}B(P^{-1}).
\]
Since $P^{-1}$ is invertible, $A$ is similar to $B$.
:::

<1>3. Similarity is transitive.
::: proof
If
\[
B=P^{-1}AP
\qquad\text{and}\qquad
C=Q^{-1}BQ,
\]
then
\[
C=Q^{-1}P^{-1}APQ=(PQ)^{-1}A(PQ).
\]
Thus $C$ is similar to $A$.
:::

<1>4. Matrix equivalence is reflexive.
::: proof
For every $A\in M_{m\times n}(R)$,
\[
A=I_mAI_n.
\]
:::

<1>5. Matrix equivalence is symmetric.
::: proof
If $B=PAQ$ with $P,Q$ invertible, then
\[
A=P^{-1}BQ^{-1}.
\]
Hence $A$ is equivalent to $B$.
:::

<1>6. Matrix equivalence is transitive.
::: proof
If
\[
B=PAQ
\qquad\text{and}\qquad
C=RBS,
\]
with all four change-of-basis matrices invertible, then
\[
C=(RP)A(QS).
\]
Both $RP\in\operatorname{GL}_m(R)$ and $QS\in\operatorname{GL}_n(R)$, so
$C$ is equivalent to $A$.
:::

<1>7. Therefore similarity and matrix equivalence are equivalence relations on
their respective matrix sets.
::: proof
Each relation is reflexive, symmetric, and transitive by the preceding steps.
:::
:::
