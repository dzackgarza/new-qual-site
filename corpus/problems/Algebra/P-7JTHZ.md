---
schema: qual/card@1
id: P-7JTHZ
kind: problem
title: Galois extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
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
What is a Galois extension?
:::


::: {.solution}
Let $L/K$ be an algebraic field extension.

<1>1. The extension $L/K$ is called **Galois** if it is both normal and separable.
::: {.proof}
This is the standard definition. Separability means that every element of $L$ is separable over $K$. Normality means that every irreducible polynomial in $K[x]$ having a root in $L$ splits completely over $L$.
:::

<1>2. If $L/K$ is finite, then $L/K$ is Galois if and only if
\[
|\operatorname{Aut}_K(L)|=[L:K].
\]
::: {.proof}
For a finite extension, the number of $K$-embeddings of $L$ into an algebraic closure is at most $[L:K]$, with equality exactly when the extension is separable. If $L/K$ is also normal, every such embedding has image $L$, hence is a $K$-automorphism. Conversely, if the automorphism group already has $[L:K]$ elements, then there are as many $K$-embeddings as the degree, so the extension is separable; and every $K$-embedding lands in $L$, which gives normality.
:::

<1>3. Equivalently, a finite extension is Galois if and only if it is the splitting field over $K$ of a separable polynomial.
::: {.proof}
A splitting field is normal. If the polynomial is separable, the extension it generates is separable, hence Galois. Conversely, a finite normal extension is the splitting field of the product of the minimal polynomials of finitely many generators, and separability of the extension makes that product separable after removing repeated irreducible factors.
:::
:::
