---
schema: qual/card@1
id: P-TVSSR
kind: problem
title: Galois group of $x^3+6x+3$
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
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Compute the Galois group of the cubic polynomial $f(x) = x^3 + 6x + 3$ over $\mathbb{Q}$.
:::

::: {.solution}
The polynomial
\[
f(x)=x^3+6x+3
\]
is Eisenstein at $3$, hence irreducible over $\mathbb Q$. Therefore its Galois group is a transitive subgroup of $S_3$, so it is either $A_3$ or $S_3$.

For a depressed cubic $x^3+px+q$, the discriminant is
\[
\Delta=-4p^3-27q^2.
\]
Here
\[
\Delta=-4\cdot6^3-27\cdot3^2=-1107=-3^3\cdot41,
\]
which is not a square in $\mathbb Q$.

For an irreducible cubic, the Galois group lies in $A_3$ exactly when the discriminant is a square. Hence
\[
\boxed{\operatorname{Gal}(f/\mathbb Q)\cong S_3}.
\]
Equivalently, $f'(x)=3x^2+6>0$, so $f$ has one real root and one nonreal conjugate pair; complex conjugation is therefore a transposition in the transitive Galois group.
:::
