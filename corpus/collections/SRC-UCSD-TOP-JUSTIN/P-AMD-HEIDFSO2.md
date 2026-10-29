---
schema: qual/card@1
id: P-AMD-HEIDFSO2
kind: problem
title: $H_*(X; \QQ) = H_*(X;\ZZ)\otimes\QQ$ and $H^*(X; \ZZ) = \operatorname{Hom}(H_*(X;
  \ZZ), \QQ)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source printed H^*(X; Z) on the left of the cohomology formula and omitted the conjunction; it now reads H^*(X; Q) = Hom(H_*(X; Z), Q).
---

::: {.problem}
Show that $H_*(X; \QQ) = H_*(X;\ZZ)\tensor \QQ$ and $H^*(X; \QQ) = \hom(H_*(X; \ZZ), \QQ)$.
:::

::: {.solution}

::: pf

::: pf-step

The homology statement holds:
$$
\boxed{H_n(X;\mathbb Q)\cong H_n(X;\mathbb Z)\otimes\mathbb Q.}
$$

::: pf-proof

The universal coefficient theorem for homology gives a natural short exact sequence
$$
0\to H_n(X;\mathbb Z)\otimes\mathbb Q\to H_n(X;\mathbb Q)\to \operatorname{Tor}_1^{\mathbb Z}(H_{n-1}(X;\mathbb Z),\mathbb Q)\to0.
$$
The group $\mathbb Q$ is flat over $\mathbb Z$, so the Tor term vanishes.

:::

:::

::: pf-step

The cohomology statement holds:
$$
\boxed{H^n(X;\mathbb Q)\cong \operatorname{Hom}_{\mathbb Z}(H_n(X;\mathbb Z),\mathbb Q).}
$$

::: pf-proof

The cohomological universal coefficient theorem gives
$$
0\to \operatorname{Ext}^1_{\mathbb Z}(H_{n-1}(X;\mathbb Z),\mathbb Q)
\to H^n(X;\mathbb Q)
\to \operatorname{Hom}_{\mathbb Z}(H_n(X;\mathbb Z),\mathbb Q)
\to0.
$$
The abelian group $\mathbb Q$ is divisible, hence injective as a $\mathbb Z$-module, so the Ext term vanishes.

:::

:::

:::

:::
