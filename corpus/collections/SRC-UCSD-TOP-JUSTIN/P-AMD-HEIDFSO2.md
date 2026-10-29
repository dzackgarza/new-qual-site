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
\boxed{H_n(X;\QQ)\cong H_n(X;\ZZ)\otimes\QQ.}
$$

::: pf-proof

The universal coefficient theorem for homology gives a natural short exact sequence
$$
0\to H_n(X;\ZZ)\otimes\QQ\to H_n(X;\QQ)\to \operatorname{Tor}_1^{\ZZ}(H_{n-1}(X;\ZZ),\QQ)\to0.
$$
The group $\QQ$ is flat over $\ZZ$, so the Tor term vanishes.

:::

:::

::: pf-step

The cohomology statement holds:
$$
\boxed{H^n(X;\QQ)\cong \operatorname{Hom}_{\ZZ}(H_n(X;\ZZ),\QQ).}
$$

::: pf-proof

The cohomological universal coefficient theorem gives
$$
0\to \operatorname{Ext}^1_{\ZZ}(H_{n-1}(X;\ZZ),\QQ)
\to H^n(X;\QQ)
\to \operatorname{Hom}_{\ZZ}(H_n(X;\ZZ),\QQ)
\to0.
$$
The abelian group $\QQ$ is divisible, hence injective as a $\ZZ$-module, so the Ext term vanishes.

:::

:::

:::

:::
