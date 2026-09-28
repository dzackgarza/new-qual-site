---
schema: qual/card@1
id: PR-ENHVC
kind: proposition
title: A polynomial is separable if and only if $\gcd(f, f') = 1$
slogan: 'A polynomial is separable exactly when it is coprime to its derivative; their gcd records repeated roots.'
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and $f \in k[x]$ a nonzero polynomial.
Then $f$ is [[D-ZT46D|separable]] if and only if $\gcd(f, f') = 1$ in $k[x]$, that is, if and only if $f$ and $f'$ have no common root in an algebraic closure $\bar{k}$.
Moreover, the repeated roots of $f$ in $\bar{k}$ are exactly the roots of $\gcd(f, f')$.
:::
