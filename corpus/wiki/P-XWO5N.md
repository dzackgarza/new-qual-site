---
schema: qual/card@1
id: P-XWO5N
kind: problem
title: The Blaschke factor $z\mapsto\frac{w-z}{1-\bar{w}z}$ as a biholomorphism of
  $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
  - Schwarz Lemma
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
a. Let $z, w \in \CC$ with $\bar z w \neq 1$. 
Prove that
\[
\abs{w-z \over 1 - \bar w z} < 1 \quad\text{ if } \abs{z}<1,~ \abs{w} < 1
\]
with equality when $\abs{z} = 1$ or $\abs{w} = 1$.

b. Prove that for a fixed $w\in \DD$, the mapping $F: z\mapsto {w-z \over 1 - \bar w z}$ satisfies

- $F$ maps $\DD$ to itself and is holomorphic.
- $F(0) = w$ and $F(w) = 0$.
- $\abs{z} = 1$ implies $\abs{F(z)} = 1$.
- $F$ is a bijection.

:::

:::{.solution}

**Part 1**: 
See Spring 2021.1 above.

**Part 2, holomorphicity**: 
This is clearly meromorphic, as it's a rational function, and has a singularity only at $z$ such that $\bar w z = 1$.
This can only happen if $z, w \in S^1$: taking the modulus yields
\[
\bar w z = 1 \implies \abs{w}^2\abs{z}^2 = 1 
,\]
and moreover since $\abs{w}^2 \leq 1$ and $\abs{z}^2\leq 1$, the only way this product can be one is when $\abs{w}^2 = \abs{z}^2 = 1$.
This also forces $z=1/\bar w$.

The claim is that the singularity $1/\bar w$ is removable.
Note that $1\over w = \bar w$ on the circle, so $1/\bar{w} = \bar{\bar w} = 2$, so
\[
\qty{ z- \bar{w}\inv } \qty{w-z \over 1-\bar w z}
&= \qty{\bar w z - 1 \over \bar w} \qty{w-z \over 1-\bar w z} \\
&= \bar{w}\inv(w-z) \\
&= w(w-z) \\
&\converges{z\to \bar w\inv=w }\to 0
.\]

**Part 2, being a bijection**: 
This follows from finding an explicit inverse, using that $F^2 = \id$:
\[
F(F(z))
&= \frac{w- \qty{ \frac{w-z}{1-\bar{w} z} } }{1-\bar{w} 
\qty{ \frac{w-z}{1-\bar{w} z} } } \\
&= \frac{w(1-\bar{w} z)-(w-z)}{q-\bar{w} z-\bar{w}(w-z)} \\
&= \frac{w-|w|^{2} z-w+z}{1-\bar{w} z-|w|^{2}+\bar{w} z} \\
&= \frac{z\left(1-|w|^{2}\right)}{1-|w|^{2}} \\
&= z
.\]


**Part 2, being an involution**: 
A direct check shows that $F(w) = 0$, since the numerator vanishes, and $F(0) = {w - 0 \over 1 - 0} = w$.

**Part 3, preserving the circle**: 
Follows from the estimate in part 1.

:::

