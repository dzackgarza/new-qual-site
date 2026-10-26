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

::: pf

::: {.pf-step #s1-1}
$k[X]$ is an integral domain if and only if $I(X)$ is a prime ideal.

::: pf-proof
For any commutative ring $R$ and ideal $I\subseteq R$, the quotient $R/I$ is an integral domain exactly when $I$ is prime. Applying this with
$$
R=k[x_1,\ldots,x_n]
$$
and $I=I(X)$ gives the claim.
:::

:::

::: {.pf-step #s1-2}
$I(X)$ is prime if and only if $X$ is irreducible.

::: pf-proof
This is the affine algebraic-set irreducibility criterion [[PR-7OT2Z]]: closed subsets of $X$ correspond to radical ideals containing $I(X)$, and $X$ is irreducible exactly when its defining radical ideal is prime.
:::

:::

::: pf-step
Therefore
$$
\boxed{k[X]\text{ is an integral domain}\iff X\text{ is irreducible}.}
$$

::: pf-proof
Combine step [](#s1-1){.pf-ref} with step [](#s1-2){.pf-ref}.
:::

:::

::: pf-qed
Step [](#s1-1){.pf-ref} through step [](#s1-2){.pf-ref} give the requested criterion.
:::

:::

:::
