---
schema: qual/card@1
id: P-KIAFG
kind: problem
title: Dedekind domains and class numbers
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Ideals
  - Commutative Algebra
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
What is a Dedekind domain, what is its ideal class group, and what is the class number?
:::

::: {.solution}
A **Dedekind domain** is an integral domain $R$ satisfying any of the standard equivalent conditions; one common definition is:

1. $R$ is Noetherian;
2. $R$ is integrally closed in its fraction field;
3. every nonzero prime ideal is maximal.

Equivalently, every nonzero proper ideal factors uniquely as a product of nonzero prime ideals.

Let $K=\operatorname{Frac}(R)$. The nonzero fractional ideals of $R$ form an abelian group under multiplication. The nonzero principal fractional ideals
\[
(a)=aR,
\qquad a\in K^\times,
\]
form a subgroup. The quotient
\[
\operatorname{Cl}(R)
=\{\text{nonzero fractional ideals}\}/\{\text{principal fractional ideals}\}
\]
is the **ideal class group**.

Its elements measure the obstruction to ideals being principal. In particular,
\[
\operatorname{Cl}(R)=0
\iff R\text{ is a PID}.
\]

When the class group is finite, its order
\[
h(R)=|\operatorname{Cl}(R)|
\]
is the **class number**. For the ring of integers $\OO_K$ of a number field, the class group is finite, so the class number is always defined. Class number $1$ means that $\OO_K$ is a PID and hence a UFD.
:::
