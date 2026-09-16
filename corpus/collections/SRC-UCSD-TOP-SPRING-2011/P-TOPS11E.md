---
schema: qual/card@1
id: P-TOPS11E
kind: problem
title: "No free Z/2 action on a closed orientable 4-manifold with rank-1 H_2"
classification:
  areas:
  - topology
  topics:
  - Group Actions
  - Manifolds
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $M$ be a closed orientable $4$-manifold whose second homology $H_2(M; \mathbb{Z})$ has rank $1$.
Show that there does not exist a free action of the group $\mathbb{Z}_2$ on $M$.
:::

::: {.solution}
<1>1. Let $b_i=\operatorname{rank}H_i(M;\mathbb Z)$. Since $M$ is closed and orientable of dimension $4$, Poincaré duality gives
$$
b_0=b_4=1,\qquad b_1=b_3.
$$
::: {.proof}
This is the rank form of integral Poincaré duality.
:::

<1>2. Since $b_2=1$ by hypothesis,
$$
\chi(M)=1-b_1+1-b_3+1=3-2b_1,
$$
which is odd.
::: {.proof}
Insert the Betti numbers into the alternating-sum formula for Euler characteristic and use $b_3=b_1$.
:::

<1>3. If a free $\mathbb Z/2$-action existed, the quotient map
$$
M\to M/(\mathbb Z/2)
$$
would be a two-sheeted covering of a finite CW complex.
::: {.proof}
A free action of a finite group on a closed manifold is properly discontinuous and the quotient is again a compact manifold; the orbit map is a covering.
:::

<1>4. Euler characteristic would then satisfy
$$
\chi(M)=2\chi(M/(\mathbb Z/2)),
$$
which is even.
::: {.proof}
Euler characteristic multiplies by the degree of a finite covering.
:::

<1>5. This contradicts <1>2. Therefore
$$
\boxed{\text{no free }\mathbb Z/2\text{-action exists on }M.}
$$
::: {.proof}
An integer cannot be both odd and even.
:::
:::
