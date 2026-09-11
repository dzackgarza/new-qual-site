---
schema: qual/card@1
id: P-AGH411REGULAROUTSIDEP
kind: problem
title: Existence of a rational function regular away from a single point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Linear Systems
  - Divisors
relations: []
review: draft
---

::: problem
Let $X$ be a curve, and let $P \in X$ be a point.
Then there exists a nonconstant rational function $f \in K(X)$, which is regular everywhere except at $P$.
:::

::: solution
Such a function is a section $f\in \globsec{X; \mcl(nD) }$ for some large enough $n$ measuring the order of the pole at $P$, where $D = [P]$ is the divisor of $P$.
So it suffices to show that $h^0(\mcl(nD)) > 0$ for some $n$.
RR says $$\chi(\mcl(nD)) = \deg D + 1 - g \implies h^0(\mcl(nD)) - h^1(\mcl(nD)) = n + 1-g.$$ Claim: if $n$ is large, $h^1(\mcl(nD)) = 0$ and thus $h^0(\mcl(nD)) = n+1 -g$, and since $g$ is fixed and $n$ can vary, $h^0(\mcl(nD)) > 0$ for some $n$.

Why this claim is true: by Serre duality,
$$
H^1(X; \mcl(nD)) \cong H^0(X; K_X \tensor \mcl(nD)\dual )\dual =
H^0(X; K_X \tensor \mcl(-nD))\dual = H^0(X; \mcl(K_X - nD))\dual
$$
so $h^1(\mcl(nD)) = h^0(\mcl(K_X - nD)) =0$ as soon as $\deg(K_X - nD) < 0$, which happens for large $n$ since $\deg(K_X - nD) = 2g-2-n$.
:::
