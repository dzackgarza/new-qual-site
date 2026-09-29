---
schema: qual/card@1
id: P-TOPF04E
kind: problem
title: "Borsuk-Ulam theorem: no antipodal-preserving map from S^n to S^m for n > m >= 1"
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Antipodal Map
relations: []
review: draft
---

::: {.problem}
Prove the Borsuk-Ulam theorem that if $n > m \geq 1$, then there is no map $f : S^n \to S^m$ which commutes with the antipodal map.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose an antipodal-equivariant map
$$
f:S^n\to S^m,\qquad f(-x)=-f(x),
$$
exists with $n>m\ge1$.

::: pf-proof

We derive a contradiction.

:::

:::

::: pf-step

The map descends to
$$
\bar f:\mathbb{RP}^n\to\mathbb{RP}^m.
$$

::: pf-proof

Equivariance sends antipodal orbits to antipodal orbits.

:::

:::

::: {.pf-step #s3}

The induced map on $H^1(-;\mathbb F_2)$ sends the generator $u\in H^1(\mathbb{RP}^m;\mathbb F_2)$ to the generator $v\in H^1(\mathbb{RP}^n;\mathbb F_2)$.

::: pf-proof

A generator of $\pi_1(\mathbb{RP}^n)$ lifts to a path from $x$ to $-x$. Its image under $f$ runs from $f(x)$ to $-f(x)$, so its projection is the nontrivial loop in $\mathbb{RP}^m$. Thus $\bar f_*$ is nontrivial on $\pi_1\cong\mathbb Z/2$, hence $\bar f^*$ is nontrivial, and therefore an isomorphism, on one-dimensional $H^1(-;\mathbb F_2)$.

:::

:::

::: pf-step

In the projective-space cohomology rings,
$$
u^{m+1}=0,
$$
but
$$
v^{m+1}\ne0
$$
because $m+1\le n$.

::: pf-proof

Use
$$
H^*(\mathbb{RP}^r;\mathbb F_2)=\mathbb F_2[t]/(t^{r+1}).
$$

:::

:::

::: {.pf-step #s5}

Naturality gives the contradiction
$$
0=\bar f^*(u^{m+1})=(\bar f^*u)^{m+1}=v^{m+1}\ne0.
$$

::: pf-proof

Cohomology pullback is a ring homomorphism and step [](#s3){.pf-ref} identifies $\bar f^*u=v$.

:::

:::

::: pf-step

Hence no antipodal-equivariant map $S^n\to S^m$ exists when $n>m\ge1$.

::: pf-proof

The assumption in step [](#s1){.pf-ref} leads to step [](#s5){.pf-ref}.

:::

:::

:::

:::
