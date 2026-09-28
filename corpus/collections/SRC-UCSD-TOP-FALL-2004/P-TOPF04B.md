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
Consider the standard covering projection $S^n \to \mathbb{RP}^n$ which maps antipodal points to the same point in $\mathbb{RP}^n$.
Prove that the covering projection is not null-homotopic.
:::

::: {.solution}
<1>1. For $n=1$, the map $S^1\to\mathbb{RP}^1\cong S^1$ has degree $2$, so it is not null-homotopic.
::: {.proof}
A null-homotopic circle map has degree zero.
:::

<1>2. For $n\ge2$, a covering map induces an isomorphism on $\pi_n$:
$$
p_*:\pi_n(S^n)\xrightarrow{\cong}\pi_n(\mathbb{RP}^n).
$$
::: {.proof}
Covering maps induce isomorphisms on homotopy groups in dimensions at least $2$.
:::

<1>3. Since $[\operatorname{id}_{S^n}]$ generates $\pi_n(S^n)\cong\mathbb Z$, the class
$$
[p]=p_*[\operatorname{id}_{S^n}]
$$
is nonzero.
::: {.proof}
An isomorphism sends a nonzero generator to a nonzero element.
:::

<1>4. Hence the covering projection is not null-homotopic for any $n\ge1$.
::: {.proof}
A map is null-homotopic exactly when its homotopy class is zero.
:::
:::
