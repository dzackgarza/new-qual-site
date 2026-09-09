---
schema: qual/card@1
id: P-RRQVK
kind: problem
title: Galois group of $x^7-1$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
What is the Galois group of $x^7 - 1$ over the rationals?
:::

::: {.solution}
The roots of $x^7-1$ are the seventh roots of unity, so its splitting field over $\mathbb Q$ is
\[
K=\mathbb Q(\zeta_7),
\]
where $\zeta_7$ is primitive. Since
\[
\Phi_7(x)=x^6+x^5+\cdots+x+1
\]
is irreducible over $\mathbb Q$, we have $[K:\mathbb Q]=6$.

Every $\mathbb Q$-automorphism of $K$ is determined by
\[
\zeta_7\longmapsto \zeta_7^a,
\qquad a\in(\mathbb Z/7\mathbb Z)^\times,
\]
and every such choice gives an automorphism. Hence
\[
\operatorname{Gal}(K/\mathbb Q)
\cong(\mathbb Z/7\mathbb Z)^\times.
\]
The latter group is cyclic of order $6$, so
\[
\operatorname{Gal}(x^7-1/\mathbb Q)\cong C_6.
\]
:::
