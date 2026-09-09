---
schema: qual/card@1
id: P-G3FZI
kind: problem
title: Galois group of $x^3-2$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
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
Compute the Galois group of $x^3 - 2$ over the rationals.
:::


::: {.solution}
Let $\alpha=\sqrt[3]{2}$ and let $\zeta_3$ be a primitive cube root of unity.

<1>1. The polynomial $x^3-2$ is irreducible over $\QQ$.
::: {.proof}
It is Eisenstein at the prime $2$.
:::

<1>2. Its splitting field is
\[
L=\QQ(\alpha,\zeta_3).
\]
::: {.proof}
The three roots are
\[
\alpha,\ \zeta_3\alpha,\ \zeta_3^2\alpha.
\]
:::

<1>3. One has $[L:\QQ]=6$.
::: {.proof}
By <1>1, $[\QQ(\alpha):\QQ]=3$. The field $\QQ(\alpha)$ is real, while $\zeta_3$ is nonreal, so $\zeta_3\notin\QQ(\alpha)$. Since $\zeta_3$ has degree $2$ over $\QQ$, adjoining it doubles the degree:
\[
[L:\QQ]=6.
\]
:::

<1>4. Therefore
\[
\operatorname{Gal}(L/\QQ)\cong S_3.
\]
::: {.proof}
The Galois group acts faithfully on the three roots, so it embeds in $S_3$. Since $L/\QQ$ is Galois of degree $6$, the Galois group has order $6$, hence equals $S_3$.
:::
:::
