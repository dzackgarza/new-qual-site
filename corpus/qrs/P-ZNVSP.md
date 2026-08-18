---
schema: qual/card@1
id: P-ZNVSP
kind: problem
title: Density of $f(\mathbb{H})$ for a holomorphic map of the half-plane real precisely on $\mathbb{R}$
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-reflection
  - picard
  - open-mapping-theorem
relations: []
review: draft
solved: true
---

::: problem
Suppose $f: \HH\union \RR\to \CC$ satisfies the following:

- $f(i) = i$

- $f$ is continuous

- $f$ is analytic on $\HH$

- $f(z) \in \RR \iff z\in \RR$.

Show that $f(\HH)$ is a dense subset of $\HH$.
:::

::: {.solution}
Ideas:

- If an entire function doesn't have dense image, it's constant by Liouville using the proof idea of Casorati-Weierstrass.

- Conjugate $f$ by $T:\HH\to \DD$ where $T(z) = {z-i\over z+i}$, then $\tilde f(0) = 0$

- Use that $T(\RR) = S^1$, so $\abs{\tilde f(z)} = 1$ when $\abs{z} = 1$.

- Schwarz reflection applies to $\tilde f$ to define an entire function -- if $f$ isn't dense, then the extension of $\tilde f$ isn't dense...?

- No clue how to use $f(i) = i$, although it implies $\tilde f(0) = 0$ and Schwarz applies.
:::

