---
schema: qual/card@1
id: P-ZYJDF
kind: problem
title: A polynomial with Galois group $\ZZ/3\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Polynomials
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

::: problem
Construct an explicit polynomial over $\mathbb{Q}$ whose Galois group is the cyclic group of order 3:
$$\operatorname{Gal}(f/\mathbb{Q}) \cong \mathbb{Z}/3\mathbb{Z}.$$
Prove that your polynomial satisfies this condition.
:::

::: solution
Take
\[
f(x)=x^3-3x+1.
\]
By the rational root test, its only possible rational roots are $\pm1$, and
\[
f(1)=-1,
\qquad
f(-1)=3.
\]
Thus $f$ is irreducible over $\mathbb Q$.

For a depressed cubic $x^3+px+q$, the discriminant is
\[
\Delta=-4p^3-27q^2.
\]
Here $p=-3$ and $q=1$, so
\[
\Delta=108-27=81=9^2.
\]
An irreducible cubic has transitive Galois group, hence either $A_3$ or $S_3$, and it lies in $A_3$ exactly when its discriminant is a square. Therefore
\[
\boxed{\operatorname{Gal}(f/\mathbb Q)\cong A_3\cong C_3}.
\]
:::
