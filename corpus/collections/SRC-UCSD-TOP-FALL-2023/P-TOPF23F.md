---
schema: qual/card@1
id: P-TOPF23F
kind: problem
title: "The quotient map S^n to RP^n is not null-homotopic"
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Show that for any $n \geq 1$ the natural quotient map $S^n \to \mathbb{RP}^n$ is not null-homotopic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $n=1$, the covering $p:S^1\to\mathbb{RP}^1\cong S^1$ has degree $2$, hence is not null-homotopic.

::: pf-proof

A null-homotopic map $S^1\to S^1$ has degree $0$.

:::

:::

::: {.pf-step #s2}

For $n\ge2$, a covering map induces an isomorphism on $\pi_n$:
$$
p_*:\pi_n(S^n)\xrightarrow{\cong}\pi_n(\mathbb{RP}^n).
$$

::: pf-proof

Covering maps induce isomorphisms on all homotopy groups in dimensions at least $2$.

:::

:::

::: {.pf-step #s3}

The homotopy class of $p$ is $p_*([\operatorname{id}_{S^n}])$, which is nonzero.

::: pf-proof

Since $\pi_n(S^n)\cong\mathbb Z$ and $[\operatorname{id}]$ is a generator, the isomorphism in step [](#s2){.pf-ref} sends it to a nonzero element.

:::

:::

::: pf-step

Therefore $p$ is not null-homotopic for any $n\ge1$.

::: pf-proof

Combine steps [](#s1){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
