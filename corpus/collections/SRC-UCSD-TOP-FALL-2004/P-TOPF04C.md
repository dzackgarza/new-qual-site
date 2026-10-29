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
Show that $\RP^k$ is not a retract of $\RP^n$ for $k < n$.
:::

::: {.solution}

::: pf

::: {.pf-step #suppose-retraction-exists}
Suppose there were a retraction
$$
r:\RP^n\to\RP^k
$$
with $r\circ i=\operatorname{id}_{\RP^k}$, where $i$ is the standard inclusion.

::: pf-proof
We argue by contradiction.
:::

:::

::: pf-step
With $\FF_2$ coefficients,
$$
H^*(\RP^m;\FF_2)\cong\FF_2[x]/(x^{m+1}),\qquad |x|=1.
$$

::: pf-proof
This is the standard cellular cohomology ring of real projective space.
:::

:::

::: pf-step
Let $x\in H^1(\RP^k;\FF_2)$ be the generator. Since $i^*r^*=\operatorname{id}$, the class $r^*x$ is the generator of $H^1(\RP^n;\FF_2)$.

::: pf-proof
The map $i^*:H^1(\RP^n)\to H^1(\RP^k)$ is an isomorphism, so the only class whose restriction is $x$ is the degree-one generator.
:::

:::

::: {.pf-step #contradiction-power}
But
$$
0=r^*(x^{k+1})=(r^*x)^{k+1}\ne0
$$
in $H^{k+1}(\RP^n;\FF_2)$ because $k<n$.

::: pf-proof
In $\RP^k$, $x^{k+1}=0$. In $\RP^n$, the $(k+1)$-st power of the degree-one generator is nonzero whenever $k+1\le n$.
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
