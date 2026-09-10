---
schema: qual/card@1
id: P-DG3XG
kind: problem
title: If $M/K$ is Galois, whether $L/K$ or $M/L$ is Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Counterexamples
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

::: {.problem}
Let $K \subset L \subset M$ be a tower of finite degree field extensions.
In each of the following parts, either prove the assertion or give a counterexample (with justification).

1. If $M/K$ is Galois, then $L/K$ is Galois

2. If $M/K$ is Galois, then $M/L$ is Galois.
:::


::: {.solution}
<1>1. The assertion “if $M/K$ is Galois, then $L/K$ is Galois” is false.
::: {.proof}
Take
\[
K=\QQ,\qquad L=\QQ(\sqrt[3]{2}),\qquad M=\QQ(\sqrt[3]{2},\zeta_3),
\]
where $\zeta_3$ is a primitive cube root of unity. Then $M$ is the splitting field of $x^3-2$ over $\QQ$, so $M/\QQ$ is finite Galois.

However, $L/\QQ$ is not normal: $x^3-2$ is irreducible over $\QQ$, has a root $\sqrt[3]{2}\in L$, and its other two roots are nonreal, hence not in the real field $L$. Thus $L/\QQ$ is not Galois.
:::

<1>2. The assertion “if $M/K$ is Galois, then $M/L$ is Galois” is true.
::: {.proof}
Since $M/K$ is finite Galois, it is separable and normal. Separability passes to the larger base field $L$: the minimal polynomial over $L$ of any element of $M$ divides its separable minimal polynomial over $K$.

For normality, every $L$-embedding $\sigma:M\to\overline K$ is in particular a $K$-embedding. Normality of $M/K$ forces $\sigma(M)=M$. Hence $M/L$ is normal.

Thus $M/L$ is finite, separable, and normal, so it is Galois.
:::
:::
