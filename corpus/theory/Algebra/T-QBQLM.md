---
schema: qual/card@1
id: T-QBQLM
kind: theorem
title: Construction of $\GF(p^n)$ as $\FF_p[x]/(f)$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.theorem}
Let $p$ be a prime, $n\geq 1$, and $f \in \FF_p[x]$ an [[D-BVMTZ|irreducible]] polynomial of degree $n$, and let $\alpha$ be a root of $f$ in an extension field of $\FF_p$.
Then
$$
\GF(p^n)\cong \frac{\FF_p[x]}{(f)} \cong \FF_p[\alpha] = \spanof_{\FF_p}\theset{1, \alpha, \ldots, \alpha^{n-1}}.
$$
:::
