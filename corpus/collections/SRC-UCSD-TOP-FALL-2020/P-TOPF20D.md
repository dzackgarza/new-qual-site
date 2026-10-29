---
schema: qual/card@1
id: P-TOPF20D
kind: problem
title: "CP^n cannot be covered by n contractible open subsets"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Projective Spaces
  - Covering Dimension
relations: []
review: draft
---

::: {.problem}
For $n \geq 1$, show that one can not cover the complex projective space $\CP^n$ by $n$ open subsets $U_1, U_2, \cdots, U_n$ such that each $U_i$ is contractible.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $u\in H^2(\CP^n;\ZZ)$ be the standard generator. Then $u^n\ne0$.

::: pf-proof

$H^*(\CP^n;\ZZ)\cong\ZZ[u]/(u^{n+1})$.

:::

:::

::: pf-step

If $U_i\subset\CP^n$ is contractible, then $u|_{U_i}=0$.

::: pf-proof

$H^2(U_i;\ZZ)=0$ for a contractible space.

:::

:::

::: {.pf-step #s3}

If $\CP^n=U_1\cup\cdots\cup U_n$, then $u^n=0$.

::: pf-proof

For each $i$, exactness of the pair gives a relative lift $\widetilde u_i\in H^2(\CP^n,U_i)$ of $u$. Their relative cup product lies in
$$H^{2n}(\CP^n,U_1\cup\cdots\cup U_n)=H^{2n}(\CP^n,\CP^n)=0,$$
and maps to $u^n$ in absolute cohomology.

:::

:::

::: pf-step

This contradicts step [](#s1){.pf-ref}. Therefore $\CP^n$ cannot be covered by $n$ contractible open subsets.

::: pf-proof

Immediate from steps [](#s1){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
