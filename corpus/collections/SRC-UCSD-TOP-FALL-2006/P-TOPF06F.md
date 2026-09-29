---
schema: qual/card@1
id: P-TOPF06F
kind: problem
title: "Even-degree maps from S^{2n+1} to RP^{2n+1} exist; odd-degree maps do not"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Projective Spaces
  - Spheres
relations: []
review: draft
---

::: {.problem}
Let $k$ be an even integer, and let $n$ be any positive integer.
Show that there is a map $f : S^{2n+1} \to \mathbb{RP}^{2n+1}$ of degree $k$.
Show that there is no map from $S^{2n+1}$ to $\mathbb{RP}^{2n+1}$ of odd degree.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
q:S^{2n+1}\to\mathbb{RP}^{2n+1}
$$
be the antipodal quotient. Since $2n+1$ is odd, both manifolds are orientable and $q$ has degree $2$ after compatible choices of orientation.

::: pf-proof

The antipodal map on $S^{2n+1}$ has degree $(-1)^{2n+2}=1$, so the quotient is an oriented two-sheeted covering. Its degree is therefore $2$.

:::

:::

::: {.pf-step #s2}

For any even integer $k$, choose a self-map $h:S^{2n+1}\to S^{2n+1}$ of degree $k/2$ and put $f=q\circ h$.

::: pf-proof

Sphere self-maps exist in every integer degree. Multiplicativity of degree gives
$$
\deg f=(\deg q)(\deg h)=2(k/2)=k.
$$

:::

:::

::: {.pf-step #s3}

Conversely, every map $f:S^{2n+1}\to\mathbb{RP}^{2n+1}$ lifts through $q$ to a map $\widetilde f:S^{2n+1}\to S^{2n+1}$.

::: pf-proof

The sphere is simply connected for $2n+1\ge3$, so the covering-space lifting criterion is automatic.

:::

:::

::: {.pf-step #s4}

Therefore
$$
f=q\circ\widetilde f,\qquad \deg f=2\deg\widetilde f,
$$
so every such degree is even.

::: pf-proof

Apply multiplicativity of degree to the factorization in step [](#s3){.pf-ref} and use $\deg q=2$.

:::

:::

::: pf-step

Thus
$$
\boxed{\text{the possible degrees are exactly the even integers}.}
$$

::: pf-proof

Existence is step [](#s2){.pf-ref} and necessity is step [](#s4){.pf-ref}.

:::

:::

:::

:::
