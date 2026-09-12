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
---

::: {.problem}
Show that $H_*(X; \QQ) = H_*(X;\ZZ)\tensor \QQ$ $H^*(X; \ZZ) = \hom(H_*(X; \ZZ), \QQ)$
:::

::: {.solution}
<1>1. The homology statement is correct:
$$
\boxed{H_n(X;\mathbb Q)\cong H_n(X;\mathbb Z)\otimes\mathbb Q.}
$$
::: {.proof}
The universal coefficient theorem for homology gives a natural short exact sequence
$$
0\to H_n(X;\mathbb Z)\otimes\mathbb Q\to H_n(X;\mathbb Q)\to \operatorname{Tor}_1^{\mathbb Z}(H_{n-1}(X;\mathbb Z),\mathbb Q)\to0.
$$
The group $\mathbb Q$ is flat over $\mathbb Z$, so the Tor term vanishes.
:::

<1>2. The cohomology formula in the card has a coefficient typo. The correct statement is
$$
\boxed{H^n(X;\mathbb Q)\cong \operatorname{Hom}_{\mathbb Z}(H_n(X;\mathbb Z),\mathbb Q).}
$$
::: {.proof}
The cohomological universal coefficient theorem gives
$$
0\to \operatorname{Ext}^1_{\mathbb Z}(H_{n-1}(X;\mathbb Z),\mathbb Q)
\to H^n(X;\mathbb Q)
\to \operatorname{Hom}_{\mathbb Z}(H_n(X;\mathbb Z),\mathbb Q)
\to0.
$$
The abelian group $\mathbb Q$ is divisible, hence injective as a $\mathbb Z$-module, so the Ext term vanishes.
:::

<1>3. As literally written, $H^*(X;\mathbb Z)=\operatorname{Hom}(H_*(X;\mathbb Z),\mathbb Q)$ is false.
::: {.proof}
Take $X=S^1$. Then $H^1(S^1;\mathbb Z)\cong\mathbb Z$, whereas
$$
\operatorname{Hom}(H_1(S^1;\mathbb Z),\mathbb Q)\cong\operatorname{Hom}(\mathbb Z,\mathbb Q)\cong\mathbb Q.
$$
:::
:::
