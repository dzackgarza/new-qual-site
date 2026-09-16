---
schema: qual/card@1
id: D-ZNVPP
kind: definition
title: Connected space
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

::: {.definition}
A topological space $X$ is \dfn{connected} if there do not exist disjoint nonempty open subsets $A, B\subseteq X$ with $X = A\union B$.
:::

::: {.proposition}
Let $X$ be a topological space.

(a) $X$ is connected if and only if the only subsets of $X$ that are both open and closed are $\emptyset$ and $X$.

(b) A subspace $Y\subseteq X$ is connected if and only if there do not exist disjoint nonempty subsets $A, B\subseteq Y$ with $Y = A\union B$, $\cl_X(A) \intersect B = \emptyset$, and $A \intersect \cl_X(B) = \emptyset$.
:::

::: {.concept}
[@Mun00, §23, Lemma 23.1].
:::
