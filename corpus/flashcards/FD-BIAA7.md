---
schema: qual/card@1
id: FD-BIAA7
kind: definition
title: 'The Schwarz lemma'
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---

::: {.definition title="The Schwarz lemma"}
In parts:

- $f(z) = \sum_{k\geq 1}c_k z^k$ since $f(0) = 0$ implies $c_0 = 0$.

- $g(z) \da f(z)/z = \sum_{k\geq 1}c_k z^{k-1}$ and $g(0) = c_1 = f'(0)$.

- $\abs{f}\leq 1\implies \abs{g} \leq r\inv$ on $\abs{z} = r$, thus on $\abs{z} \leq r$ by MMP.

- Take the limit $r\to 1$.

- Part 2: extremum in interior implies $g(z) \equiv c$ is constant.

- $\abs{f'(0)} = 1$ or $f(z) = z$ for some $z\neq 0$ implies $\abs{c} = 1$.
:::
