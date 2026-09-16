---
schema: qual/card@1
id: PR-Q2IFX
kind: proposition
title: Subfields of the finite field $\FF_{p^k}$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
---

::: {.proposition}
Let $p$ be a prime and $k,\ell\geq 1$.
The field $\FF_{p^k}$ contains a subfield with $p^\ell$ elements if and only if $\ell\mid k$.
In that case the subfield is unique, equal to $\theset{x\in\FF_{p^k}\suchthat x^{p^\ell}=x}$.
:::

::: {.proof}
If $F\subseteq\FF_{p^k}$ is a subfield with $p^\ell$ elements, then $\FF_{p^k}$ is an $F$-vector space of some dimension $d$, so $p^k=(p^\ell)^d$ and $\ell\mid k$.

Conversely, suppose $\ell\mid k$.
Every element of $\FF_{p^k}$ is a root of $x^{p^k}-x$, which has degree $p^k$, so $x^{p^k}-x=\prod_{a\in\FF_{p^k}}(x-a)$.
Since $\ell\mid k$, $p^\ell-1$ divides $p^k-1$, so $x^{p^\ell-1}-1$ divides $x^{p^k-1}-1$ and $x^{p^\ell}-x$ divides $x^{p^k}-x$.
Hence $x^{p^\ell}-x$ has $p^\ell$ distinct roots in $\FF_{p^k}$.
They form the fixed set of the field automorphism $x\mapsto x^{p^\ell}$, which is a subfield with $p^\ell$ elements.
Every element of a subfield with $p^\ell$ elements satisfies $x^{p^\ell}=x$, so such a subfield is contained in, and hence equal to, this set.
:::
