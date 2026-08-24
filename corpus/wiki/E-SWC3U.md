---
schema: qual/card@1
id: E-SWC3U
kind: exercise
title: $\bigl|\frac{w-z}{1-\bar{w}z}\bigr|$ on the closed disk, and $z\mapsto\frac{w-z}{1-\bar{w}z}$
  is an automorphism of $\mathbb{D}$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
  - Schwarz Lemma
relations: []
review: draft
---

:::{.problem title="?"}
a.
Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
Prove that
$$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \; \; \; \mbox{if} \; |z| < 1 \; \mbox{and}\; |w| < 1,$$
and also that
$$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \; \; \; \mbox{if} \; |z| = 1 \; \mbox{or}\; |w| = 1.$$

b.
Prove that for fixed $w$ in the unit disk $\mathbb D$, the
mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the following conditions:

  - $F$ maps $\mathbb D$ to itself and is holomorphic. 

  - $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and $F(w) = 0$.

  - $\abs{F(z)} = 1$ if $|z| = 1$.

  - $F: {\mathbb D} \mapsto {\mathbb D}$ is bijective.

> Hint: Calculate $F \circ F$.

:::
