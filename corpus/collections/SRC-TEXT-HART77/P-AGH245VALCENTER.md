---
schema: qual/card@1
id: P-AGH245VALCENTER
kind: problem
title: Centers of valuations on separated and proper schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Valuative Criteria
  - Valuation Rings
  - Proper Morphisms
relations: []
review: draft
---

::: problem
Let $X$ be an integral scheme of finite type over a field $k$, having function field $K$.
We say that a valuation of $K/k$ has **center** $x$ on $X$ if its valuation ring $R$ dominates the local ring $\OO_{x, X}$.

a. If $X$ is separated over $k$, then the center of any valuation of $K/k$ on $X$, if it exists, is unique.

b. If $X$ is proper over $k$, then every valuation of $K/k$ has a unique center on $X$.
Note: if $X$ is a variety over $k$, the criterion of (b) is sometimes taken as the definition of a complete variety.

c. Prove the converses of (a) and (b). *Hint:* while (a) and (b) follow easily from the valuative criteria, their converses require some comparison of valuations in different fields.

d. If $X$ is proper over $k$, and if $k$ is algebraically closed, show that $\Gamma(X, \OO_X) = k$.
*Hint:* let $a \in \Gamma(X, \OO_X)$ with $a \not\in k$.
Show that there is a valuation ring $R$ of $K/k$ with $a\inv \in \mfm_R$, then use (b) to get a contradiction.
:::
