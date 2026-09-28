---
schema: qual/card@1
id: P-RAU6K
kind: problem
title: A cubic with Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Give an example of a cubic polynomial over $\mathbb{Q}$ with Galois group $S_3$, and prove that its Galois group is indeed $S_3$.
:::

::: {.solution}
Take
\[
f(x)=x^3-2.
\]
It is irreducible over $\mathbb Q$ by Eisenstein at $2$. Its discriminant is
\[
\Delta(f)=-108,
\]
which is not a square in $\mathbb Q$.

For an irreducible cubic, the Galois group is a transitive subgroup of $S_3$, hence either $A_3$ or $S_3$. It is contained in $A_3$ exactly when the discriminant is a square. Therefore
\[
\operatorname{Gal}(f/\mathbb Q)\cong S_3.
\]

Equivalently, the splitting field is
\[
\mathbb Q(\sqrt[3]2,\zeta_3).
\]
The real cubic field $\mathbb Q(\sqrt[3]2)$ has degree $3$, while adjoining the nonreal element $\zeta_3$ gives degree $2$, so the splitting field has degree $6$.
:::
