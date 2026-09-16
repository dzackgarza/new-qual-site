---
schema: qual/card@1
id: FD-BWVRA
kind: proposition
title: Surjective maps are the maps with a right inverse
prompts:
- What condition on inverses characterises a surjective function?
classification:
  areas:
  - algebra
  topics:
  - Functions and Relations
relations: []
review: draft
---

::: {.proposition}
Let $f\colon X\to Y$ be a map of sets.
Then $f$ is surjective, that is, for every $y\in Y$ there exists $x\in X$ with $f(x)=y$, if and only if $f$ has a right inverse: a map $g\colon Y\to X$ with $f(g(y))=y$ for every $y\in Y$.
:::

::: {.proof}
If $g$ is a right inverse, then each $y\in Y$ equals $f(g(y))$, so $f$ is surjective.
Conversely, if $f$ is surjective, then each fiber $f^{-1}(y)$ is nonempty, and the axiom of choice gives a map $g\colon Y\to X$ with $g(y)\in f^{-1}(y)$ for every $y$; then $f(g(y))=y$.
:::
