---
schema: qual/card@1
id: P-AGXVARCOORDDOMAIN
kind: problem
title: When the coordinate ring $k[X]$ is an integral domain
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Integral Domains
  - Irreducibility
relations: []
review: draft
---

::: problem
When is the coordinate ring $k[X]$ a domain?
:::

::::: {.solution}
Let $X \subseteq \AA^n$ be an affine algebraic set over an algebraically closed field $k$, with ideal $I(X)$ and coordinate ring $k[X] = k[x_1, \ldots, x_n]/I(X)$.
Then $k[X]$ is an integral domain if and only if $I(X)$ is prime, if and only if $X$ is irreducible.

::: {.proof}
1. A quotient $R/I$ is an integral domain exactly when $I$ is a prime ideal, so the first equivalence holds.

2. Suppose $X = X_1 \cup X_2$ with $X_1, X_2 \subsetneq X$ closed.
   Since $X_i \neq X$, the ideal $I(X_i)$ strictly contains $I(X)$, so there are $f_i \in I(X_i) \setminus I(X)$.
   Then $f_1 f_2$ vanishes on $X_1 \cup X_2 = X$, so $f_1 f_2 \in I(X)$ while neither factor is, and $I(X)$ is not prime.

3. Suppose $I(X)$ is not prime: $f g \in I(X)$ with $f, g \notin I(X)$.
   Then $X = (X \cap V(f)) \cup (X \cap V(g))$, and neither piece is all of $X$, since $f$ and $g$ do not vanish identically on $X$.
   So $X$ is reducible.
:::
:::::
