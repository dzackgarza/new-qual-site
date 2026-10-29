---
schema: qual/card@1
id: P-TOPF04B
kind: problem
title: "The covering projection S^n to RP^n is not null-homotopic"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Consider the standard covering projection $S^n \to \RP^n$ which maps antipodal points to the same point in $\RP^n$.
Prove that the covering projection is not null-homotopic.
:::

::: {.solution}

::: pf

::: pf-step
For $n=1$, the map $S^1\to\RP^1\cong S^1$ has degree $2$, so it is not null-homotopic.

::: pf-proof
A null-homotopic circle map has degree zero.
:::

:::

::: pf-step
For $n\ge2$, a covering map induces an isomorphism on $\pi_n$:
$$
p_*:\pi_n(S^n)\xrightarrow{\cong}\pi_n(\RP^n).
$$

::: pf-proof
Covering maps induce isomorphisms on homotopy groups in dimensions at least $2$.
:::

:::

::: pf-step
Since $[\operatorname{id}_{S^n}]$ generates $\pi_n(S^n)\cong\ZZ$, the class
$$
[p]=p_*[\operatorname{id}_{S^n}]
$$
is nonzero.

::: pf-proof
An isomorphism sends a nonzero generator to a nonzero element.
:::

:::

::: pf-step
Hence the covering projection is not null-homotopic for any $n\ge1$.

::: pf-proof
A map is null-homotopic exactly when its homotopy class is zero.
:::

:::

:::

:::
