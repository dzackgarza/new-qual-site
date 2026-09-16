---
schema: qual/card@1
id: PR-RPL4Q
kind: proposition
title: Free modules are projective
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Projective Modules
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a ring.
Every [[D-LIEMF|free]] $R$-module is [[D-RHJMK|projective]].
:::

::: {.proof}
Let $F$ be free with basis $(e_i)_{i\in I}$, let $g\colon N\to M$ be a surjective $R$-linear map, and let $f\colon F\to M$ be $R$-linear.
For each $i\in I$ choose $n_i\in N$ with $g(n_i)=f(e_i)$.
There is a unique $R$-linear map $\tilde f\colon F\to N$ with $\tilde f(e_i)=n_i$ for all $i$, and $g\circ\tilde f$ agrees with $f$ on the basis, so $g\circ\tilde f=f$.
:::
