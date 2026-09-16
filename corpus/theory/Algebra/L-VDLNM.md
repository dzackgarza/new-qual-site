---
schema: qual/card@1
id: L-VDLNM
kind: lemma
title: The characteristic polynomial is the product of the invariant factors
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Structure Theorem
  - Canonical Forms
relations: []
review: draft
---

::: {.lemma}
Let $k$ be a field, let $A\in\Mat_n(k)$, and let $f_1\divides f_2\divides\cdots\divides f_n$ be the invariant factors of $A$: the monic diagonal entries of the Smith normal form of $xI-A$ over $k[x]$, some of which may equal $1$.
Then
$$
\det(xI-A)=\prod_{j=1}^nf_j(x).
$$
:::

::: {.proof}
The Smith normal form is $P(xI-A)Q$ with $P,Q$ invertible over $k[x]$, so $\det P$ and $\det Q$ are nonzero constants and $\det(xI-A)$ is a nonzero constant multiple of $\prod_jf_j$.
Both polynomials are monic, so they are equal.
:::
