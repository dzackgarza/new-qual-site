---
schema: qual/card@1
id: D-QP7WI
kind: definition
title: Poincaré duality
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
  - Orientation
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and $M$ a closed [[D-YD6DR|$R$-orientable]] $n$-manifold with [[D-TS7TZ|fundamental class]] $[M]\in H_n(M;R)$.
The \dfn{Poincaré duality map} is
$$
D\colon H^k(M;R)\to H_{n-k}(M;R),\qquad D(\alpha)\coloneqq[M]\frown\alpha,
$$
given by the [[D-RQS4J|cap product]] with $[M]$.
:::

::: {.theorem}
Let $R$ be a commutative ring and $M$ a closed $R$-orientable $n$-manifold with fundamental class $[M]\in H_n(M;R)$.
Then the Poincaré duality map $D\colon H^k(M;R)\to H_{n-k}(M;R)$, $\alpha\mapsto[M]\frown\alpha$, is an isomorphism for every $k$ [@Hat02].
:::

::: {.remark title="Variations"}
An orientable manifold is $R$-orientable for every commutative ring $R$, so cap product with the fundamental class gives $H^k(M;R)\cong H_{n-k}(M;R)$ for every closed orientable $n$-manifold $M$ and every $R$, for example $R=\ZZ$ or a field.
Every closed manifold is $\ZZ/2$-orientable, so the duality holds for all closed manifolds with $\ZZ/2$ coefficients.
:::

::: {.remark}
Both hypotheses are needed with $\ZZ$ coefficients.
For $n\geq 1$, the orientable manifold $\RR^n$ is not closed, and $H^0(\RR^n;\ZZ)\cong\ZZ$ while $H_n(\RR^n;\ZZ) = 0$.
The closed manifold $\RP^2$ is not orientable, and $H^0(\RP^2;\ZZ)\cong\ZZ$ while $H_2(\RP^2;\ZZ) = 0$.
:::
