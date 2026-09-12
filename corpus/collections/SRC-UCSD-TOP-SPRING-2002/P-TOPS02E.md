---
schema: qual/card@1
id: P-TOPS02E
kind: problem
title: "The covering map S^n to RP^n is not null-homotopic"
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

::: problem
Let $p : S^n \to \mathbb{RP}^n$ be the covering space map.
Prove $p$ is not null-homotopic.
:::

::: {.solution}
<1>1. For $n=1$, the covering $p:S^1\to\mathbb{RP}^1\cong S^1$ has degree $2$, hence is not null-homotopic.
::: {.proof}
A null-homotopic map $S^1\to S^1$ has degree $0$.
:::

<1>2. For $n\ge2$, a covering map induces an isomorphism on $\pi_n$:
$$
p_*:\pi_n(S^n)\xrightarrow{\cong}\pi_n(\mathbb{RP}^n).
$$
::: {.proof}
Covering maps induce isomorphisms on all homotopy groups in dimensions at least $2$.
:::

<1>3. The homotopy class of $p$ is $p_*([\operatorname{id}_{S^n}])$, which is nonzero.
::: {.proof}
Since $\pi_n(S^n)\cong\mathbb Z$ and $[\operatorname{id}]$ is a generator, the isomorphism in <1>2 sends it to a nonzero element.
:::

<1>4. Therefore $p$ is not null-homotopic for any $n\ge1$.
::: {.proof}
Combine <1>1 and <1>3.
:::
:::
