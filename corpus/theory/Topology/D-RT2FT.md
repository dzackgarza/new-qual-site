---
schema: qual/card@1
id: D-RT2FT
kind: definition
title: Surjection and right inverses
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
A map of sets $\pi\colon A\to B$ is a \dfn{surjection} if for every $b\in B$ there exists $a\in A$ with $\pi(a)=b$.
A \dfn{right inverse} of $\pi$ is a map $f\colon B\to A$ with $\pi\circ f=\id_B$.
:::

::: {.proposition}
Assuming the axiom of choice, a map of sets $\pi\colon A\to B$ is a surjection if and only if it has a right inverse.
:::

::: {.remark}
In a category, a morphism with a right inverse is a split epimorphism.
A continuous surjection need not have a continuous right inverse: $t\mapsto e^{2\pi it}$ from $\RR$ onto $S^1$ has none, since a continuous $f\colon S^1\to\RR$ with $e^{2\pi if(z)}=z$ would make $\id_{S^1}$ factor through the contractible space $\RR$ and so be nullhomotopic.
:::
