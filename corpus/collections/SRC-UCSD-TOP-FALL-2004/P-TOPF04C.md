---
schema: qual/card@1
id: P-TOPF04C
kind: problem
title: "RP^k is not a retract of RP^n for k < n"
classification:
  areas:
  - topology
  topics:
  - Projective Spaces
  - Retracts
relations: []
review: draft
---

::: {.problem}
Show that $\mathbb{RP}^k$ is not a retract of $\mathbb{RP}^n$ for $k < n$.
:::

::: {.solution}

::: pf

::: {.pf-step #suppose-retraction-exists}
Suppose there were a retraction
$$
r:\mathbb{RP}^n\to\mathbb{RP}^k
$$
with $r\circ i=\operatorname{id}_{\mathbb{RP}^k}$, where $i$ is the standard inclusion.

::: pf-proof
We argue by contradiction.
:::

:::

::: pf-step
With $\mathbb F_2$ coefficients,
$$
H^*(\mathbb{RP}^m;\mathbb F_2)\cong\mathbb F_2[x]/(x^{m+1}),\qquad |x|=1.
$$

::: pf-proof
This is the standard cellular cohomology ring of real projective space.
:::

:::

::: pf-step
Let $x\in H^1(\mathbb{RP}^k;\mathbb F_2)$ be the generator. Since $i^*r^*=\operatorname{id}$, the class $r^*x$ is the generator of $H^1(\mathbb{RP}^n;\mathbb F_2)$.

::: pf-proof
The map $i^*:H^1(\mathbb{RP}^n)\to H^1(\mathbb{RP}^k)$ is an isomorphism, so the only class whose restriction is $x$ is the degree-one generator.
:::

:::

::: {.pf-step #contradiction-power}
But
$$
0=r^*(x^{k+1})=(r^*x)^{k+1}\ne0
$$
in $H^{k+1}(\mathbb{RP}^n;\mathbb F_2)$ because $k<n$.

::: pf-proof
In $\mathbb{RP}^k$, $x^{k+1}=0$. In $\mathbb{RP}^n$, the $(k+1)$-st power of the degree-one generator is nonzero whenever $k+1\le n$.
:::

:::

::: pf-step
Therefore no such retraction exists.

::: pf-proof
The contradiction in step [](#contradiction-power){.pf-ref} disproves step [](#suppose-retraction-exists){.pf-ref}.
:::

:::

:::

:::
