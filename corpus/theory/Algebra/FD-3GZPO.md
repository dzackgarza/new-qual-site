---
schema: qual/card@1
id: FD-3GZPO
kind: definition
title: Algebraically closed field
prompts:
- What does it mean for a field to be algebraically closed?
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
A field $k$ is \dfn{algebraically closed} if every nonconstant polynomial $f\in k[x]$ has a root in $k$.
:::

::: {.proposition}
For a field $k$, the following are equivalent:

- $k$ is algebraically closed.

- Every nonconstant $f\in k[x]$ splits into linear factors over $k$.

- The only algebraic extension of $k$ is $k$ itself.
:::

::: {.proof}
If every nonconstant polynomial has a root, then dividing off a linear factor $x-a$ at each stage and inducting on the degree shows that every nonconstant polynomial splits.
If every polynomial splits and $L/k$ is algebraic, then the minimal polynomial over $k$ of each $\alpha\in L$ is irreducible and splits, so it is linear and $\alpha\in k$.
If $k$ has no proper algebraic extension and $f$ is nonconstant, then for an irreducible factor $g$ of $f$ the field $k[x]/(g)$ is an algebraic extension of degree $\deg g$, so $\deg g=1$ and $f$ has a root in $k$.
:::
