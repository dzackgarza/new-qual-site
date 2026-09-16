---
schema: qual/card@1
id: PR-TZN4M
kind: proposition
title: Characterization of finite normal extensions as splitting fields
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and $L/k$ a field extension.
Then $L/k$ is finite and [[D-LZTAK|normal]] if and only if $L$ is the splitting field over $k$ of some nonzero polynomial $f\in k[x]$.
:::

::: {.proof}
Fix an algebraic closure $\bar k$ containing $L$.

Suppose $L/k$ is finite and normal, and write $L=k(\beta_1,\ldots,\beta_r)$.
Let $f$ be the product of the minimal polynomials of the $\beta_i$ over $k$.
By normality each factor splits in $L$, and $L$ is generated over $k$ by roots of $f$, so $L$ is the splitting field of $f$.

Conversely, let $L=k(\alpha_1,\ldots,\alpha_n)$, where $\alpha_1,\ldots,\alpha_n$ are the roots of $f$ in $L$ and $f$ splits in $L$.
Then $L/k$ is finite.
A $k$-embedding $\sigma\colon L\to\bar k$ sends each $\alpha_i$ to a root of $f$, and $f$ splits in $L$, so $\sigma$ permutes $\theset{\alpha_1,\ldots,\alpha_n}$ and $\sigma(L)=L$.
By [[PR-OZYUC]], $L/k$ is normal.
:::
