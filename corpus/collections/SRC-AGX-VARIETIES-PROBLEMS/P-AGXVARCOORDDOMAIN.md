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

::: {.problem}
When is the coordinate ring $k[X]$ a domain?
:::

::: {.solution}
Write
$$
k[X]=k[x_1,\ldots,x_n]/I(X).
$$

<1>1. $k[X]$ is an integral domain if and only if $I(X)$ is a prime ideal.
::: {.proof}
For any commutative ring $R$ and ideal $I\subseteq R$, the quotient $R/I$ is an integral domain exactly when $I$ is prime. Applying this with
$$
R=k[x_1,\ldots,x_n]
$$
and $I=I(X)$ gives the claim.
:::

<1>2. $I(X)$ is prime if and only if $X$ is irreducible.
::: {.proof}
This is the affine algebraic-set irreducibility criterion [[PR-7OT2Z]]: closed subsets of $X$ correspond to radical ideals containing $I(X)$, and $X$ is irreducible exactly when its defining radical ideal is prime.
:::

<1>3. Therefore
$$
\boxed{k[X]\text{ is an integral domain}\iff X\text{ is irreducible}.}
$$
::: {.proof}
Combine step <1>1 with step <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 gives the requested criterion.
:::
:::
