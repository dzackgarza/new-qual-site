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
For $n \geq 1$, show that one can not cover the complex projective space $\mathbb{CP}^n$ by $n$ open subsets $U_1, U_2, \cdots, U_n$ such that each $U_i$ is contractible.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $u\in H^2(\mathbb{CP}^n;\mathbb Z)$ be the standard generator. Then $u^n\ne0$.

::: pf-proof

$H^*(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z[u]/(u^{n+1})$.

:::

:::

::: pf-step

If $U_i\subset\mathbb{CP}^n$ is contractible, then $u|_{U_i}=0$.

::: pf-proof

$H^2(U_i;\mathbb Z)=0$ for a contractible space.

:::

:::

::: {.pf-step #s3}

If $\mathbb{CP}^n=U_1\cup\cdots\cup U_n$, then $u^n=0$.

::: pf-proof

For each $i$, exactness of the pair gives a relative lift $\widetilde u_i\in H^2(\mathbb{CP}^n,U_i)$ of $u$. Their relative cup product lies in
$$H^{2n}(\mathbb{CP}^n,U_1\cup\cdots\cup U_n)=H^{2n}(\mathbb{CP}^n,\mathbb{CP}^n)=0,$$
and maps to $u^n$ in absolute cohomology.

:::

:::

::: pf-step

This contradicts step [](#s1){.pf-ref}. Therefore $\mathbb{CP}^n$ cannot be covered by $n$ contractible open subsets.

::: pf-proof

Immediate from steps [](#s1){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
