---
schema: qual/card@1
id: D-BYIZA
kind: definition
title: Ext group
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Cohomology
relations: []
review: draft
---

::: {.definition}
Let $A$ and $G$ be abelian groups, and let
$$
\cdots \to F_2 \to F_1 \to F_0 \to A \to 0
$$
be a free resolution of $A$.
Applying $\Hom(\wait, G)$ to $\cdots\to F_1\to F_0$ gives a cochain complex $0\to\Hom(F_0,G)\to\Hom(F_1,G)\to\cdots$, and the \dfn{Ext group} $\Ext^n(A, G)$ is its $n$th cohomology group; it is independent of the choice of free resolution [@Hat02, §3.1, pp. 193--195].
:::

::: {.remark}
One has $\Ext^0(A,G) \cong \Hom(A,G)$ and $\Ext^n(A,G) = 0$ for $n\geq 2$.
For $m\geq 1$,
$$
\Ext^1(\ZZ, G) = 0, \qquad \Ext^1(\ZZ/m, G) \cong G/mG
$$
[@Hat02, §3.1, p. 195].
:::
