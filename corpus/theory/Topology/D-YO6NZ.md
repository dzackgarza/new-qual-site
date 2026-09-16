---
schema: qual/card@1
id: D-YO6NZ
kind: definition
title: Characterizations of connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
A \dfn{separation} of $X$ is a pair $(U, V)$ of disjoint nonempty open subsets of $X$ with $X = U\union V$.
The space $X$ is \dfn{disconnected} if it has a separation, and connected otherwise.
:::

::: {.proposition}
For a topological space $X$, the following are equivalent:

(a) $X$ is connected.

(b) The only subsets of $X$ that are both open and closed are $\emptyset$ and $X$.

(c) Every continuous map from $X$ to the discrete space $\ts{0, 1}$ is constant.
:::

::: {.proposition}
Let $X$ be a topological space and $Y\subseteq X$ a subspace.
Then $Y$ is disconnected if and only if there exist disjoint nonempty subsets $A, B\subseteq Y$ with $Y = A\union B$ such that neither contains a [[D-Y6JAS|limit point]] of the other, that is, $\cl_X(A)\intersect B = \emptyset$ and $A\intersect\cl_X(B) = \emptyset$.
:::

::: {.example}
The subspace $\QQ\subseteq\RR$ is disconnected, and every connected subspace of $\QQ$ has at most one point, so the connected components of $\QQ$ are its singletons.
For rationals $p < q$ and an irrational $r$ with $p<r<q$, the sets $\QQ\intersect(-\infty, r)$ and $\QQ\intersect(r, \infty)$ form a separation of $\QQ$.
:::

::: {.concept}
[@Mun00].
:::
