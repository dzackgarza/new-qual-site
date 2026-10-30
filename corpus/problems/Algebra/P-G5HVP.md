---
schema: qual/card@1
id: P-G5HVP
kind: problem
title: A finite separable extension is normal iff it is the splitting field of a polynomial
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
---

::: {.problem}

Let $L/K$ be a finite separable extension. Show that $L/K$ is normal if and only if $L$ is the splitting field over $K$ of some polynomial in $K[x]$.

:::

::: {.solution}

::: pf

::: pf-step

If $L/K$ is normal, then $L$ is the splitting field over $K$ of a polynomial in $K[x]$.

::: pf-proof

Since $L/K$ is finite, $L=K(\alpha_1,\ldots,\alpha_r)$ for some $\alpha_i\in L$. Let $m_i\in K[x]$ be the minimal polynomial of $\alpha_i$ over $K$. Each $m_i$ is irreducible over $K$ and has the root $\alpha_i$ in $L$, so by normality $m_i$ splits in $L$. Hence $f=\prod_i m_i$ splits in $L$, and $L$ is generated over $K$ by roots of $f$, so $L$ is the splitting field of $f$ over $K$.

:::

:::

::: pf-step

If $L$ is the splitting field over $K$ of a polynomial $f\in K[x]$, then $L/K$ is normal.

::: pf-proof

A splitting field of a polynomial is a normal extension; this is a standard theorem and uses no separability.

:::

:::

:::

:::

::: {.remark title="Variations"}
The polynomial may be required to be separable. For $L/K$ normal and separable, $L$ is the splitting field of the product of the distinct minimal polynomials of a basis, and each of those is separable.
:::
