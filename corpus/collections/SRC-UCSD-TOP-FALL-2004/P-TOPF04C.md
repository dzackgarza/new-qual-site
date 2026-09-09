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

::: problem
Show that $\mathbb{RP}^k$ is not a retract of $\mathbb{RP}^n$ for $k < n$.
:::

::: {.solution}
<1>1. Suppose there were a retraction
$$
r:\mathbb{RP}^n\to\mathbb{RP}^k
$$
with $r\circ i=\operatorname{id}_{\mathbb{RP}^k}$, where $i$ is the standard inclusion.
::: {.proof}
We argue by contradiction.
:::

<1>2. With $\mathbb F_2$ coefficients,
$$
H^*(\mathbb{RP}^m;\mathbb F_2)\cong\mathbb F_2[x]/(x^{m+1}),\qquad |x|=1.
$$
::: {.proof}
This is the standard cellular cohomology ring of real projective space.
:::

<1>3. Let $x\in H^1(\mathbb{RP}^k;\mathbb F_2)$ be the generator. Since $i^*r^*=\operatorname{id}$, the class $r^*x$ is the generator of $H^1(\mathbb{RP}^n;\mathbb F_2)$.
::: {.proof}
The map $i^*:H^1(\mathbb{RP}^n)\to H^1(\mathbb{RP}^k)$ is an isomorphism, so the only class whose restriction is $x$ is the degree-one generator.
:::

<1>4. But
$$
0=r^*(x^{k+1})=(r^*x)^{k+1}\ne0
$$
in $H^{k+1}(\mathbb{RP}^n;\mathbb F_2)$ because $k<n$.
::: {.proof}
In $\mathbb{RP}^k$, $x^{k+1}=0$. In $\mathbb{RP}^n$, the $(k+1)$-st power of the degree-one generator is nonzero whenever $k+1\le n$.
:::

<1>5. Therefore no such retraction exists.
::: {.proof}
The contradiction in <1>4 disproves <1>1.
:::
:::
