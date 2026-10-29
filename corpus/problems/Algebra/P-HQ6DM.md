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
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source leaves the ring $R$ undeclared and numbers the parts 1 and 2 with bold labels; the statement declares $R$ commutative and labels the parts (a) and (b).
---

::: {.problem}
Let $R$ be a commutative ring. Prove that each of the following is an equivalence relation.

(a) Similarity on $M_n(R)$: $A\sim B$ if there exists $P\in\GL_n(R)$ such that
$$
B=PAP^{-1}.
$$

(b) Matrix equivalence on $M_{m\times n}(R)$: $A\approx B$ if there exist
$$
P\in\GL_m(R),
\qquad
Q\in\GL_n(R)
$$
such that
$$
B=PAQ.
$$
:::

::: {.solution}

::: pf

::: pf-step

Similarity is reflexive, symmetric, and transitive.

::: pf-proof

Reflexivity: $A=I_nAI_n^{-1}$.

Symmetry: if $B=PAP^{-1}$, then
$$
A=P^{-1}BP.
$$

Transitivity: if
$$
B=PAP^{-1},
\qquad
C=QBQ^{-1},
$$
then
$$
C=(QP)A(QP)^{-1}.
$$
Thus similarity is an equivalence relation.

:::

:::

::: pf-step

Matrix equivalence is reflexive, symmetric, and transitive.

::: pf-proof

Reflexivity: for $A\in M_{m\times n}(R)$,
$$
A=I_m A I_n.
$$

Symmetry: if $B=PAQ$ with $P\in\GL_m(R)$ and $Q\in\GL_n(R)$, then
$$
A=P^{-1}BQ^{-1}.
$$

Transitivity: if
$$
B=PAQ,
\qquad
C=P'BQ'
$$
with $P'\in\GL_m(R)$ and $Q'\in\GL_n(R)$, then
$$
C=(P'P)A(QQ'),
$$
and $P'P$, $QQ'$ are invertible. Thus matrix equivalence is an equivalence relation.

:::

:::

:::

:::
