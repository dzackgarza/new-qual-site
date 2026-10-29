---
schema: qual/card@1
id: FD-YYLYR
kind: corollary
title: Finite fields are perfect
slogan: 'Frobenius is an automorphism of every finite field.'
prompts:
- Why is every finite field perfect?
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Finite Fields
relations: []
review: draft
---

::: {.corollary}
Every finite field is [[D-KQFIV|perfect]].
:::

::: {.proof}
Let $k$ be a finite field of characteristic $p$. The Frobenius map
$$
F\colon k\longrightarrow k,
\qquad
F(a)=a^p,
$$
is an injective field homomorphism, hence is surjective because $k$ is finite. Therefore $k$ is perfect by [[PR-IK6AM]].
:::
