---
schema: qual/card@1
id: FE-EUOB2
kind: example
title: A power series of radius $1$ diverging at every point of $S^1$
prompts:
- Give a power series with radius of convergence $1$ that diverges at every point of $S^1$.
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Series of Functions
  - Counterexamples
relations: []
review: draft
---

::: {.example}
The power series $\sum_{n=1}^\infty nz^n$ has radius of convergence $1$ and diverges at every $z$ with $\abs{z}=1$.
Its radius is $1$ because $\limsup_n n^{1/n}=1$.
For $\abs{z}=1$ the terms satisfy $\abs{nz^n}=n\not\to0$, so the series diverges.

The radius is that of [@Ahl73, ch. 2, §2.4, Theorem 2], whose Hadamard formula is the $\limsup$ the card evaluates; the book says of the circle $\abs z=R$ that nothing is claimed about convergence on it, so the boundary sentence is the card's own, from the vanishing of the terms that a convergent series requires.
:::
