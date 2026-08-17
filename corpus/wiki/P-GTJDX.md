---
schema: qual/card@1
id: P-GTJDX
kind: problem
title: "Let $z, w \\in \\CC$ with $\\bar z w \\neq 1$. Prove that $\\abs{w-z \\over 1 - \\bar w z} < 1 \\quad\\text{ if } \\abs{z}<1,~ \\abs{w} < 1$ with equality when $\\abs{z} = 1$ or $\\abs{w} = 1$. Prove\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - blaschke-factors
  - schwarz-lemma
  - biholomorphisms
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
\envlist

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
:::

:::{.solution title="part 1"}
\[
0 &\leq (1 - \abs{w}^2)(1-\abs{z}^2) \\
\implies \abs{w}^2 + \abs{z}^2 &\leq 1 + \abs{w}^2 \abs{z}^2 \\
\implies \abs{w}^2 + \abs{z}^2 - 2\Re(\bar{w} z) &\leq 1 + \abs{w}^2 \abs{z}^2 - 2\Re(\bar{w} z) \\
\implies \abs{w-z}^2 &\leq \abs{1-\bar{w}z}^2
.\]
Note that if either $\abs{w}^2 = 1$ or $\abs{z}^2 = 1$ then the first line is an equality, yielding equality in the final line.
:::

:::{.solution title="part 2"}
\envlist

- That $F: \DD\to \DD$: follows from the inequality, since $\abs{z}, \abs{w} < 1$ for $z,w\in \DD$.
Holomorphicity: follows from the fact that rational expressions of holomorphic functions are holomorphic away from where the denominators vanish.
- Then just note that $\abs{\bar{w} z} \leq \abs{w}\abs{z} < 1$, so $\abs{1 - \bar{w} z} > 0$.

- $F(0) = {w-0 \over 1-0} = w$
- $F(w) = {w-w\over 1 - \bar w w} = 0$
- $\abs{z} = 1$ yields equality in part 1.

> Other notes: $F$ is bijective on $\DD$:
\[
F(F(z))
&= {w - \qty{w-z\over 1-\bar w z} \over 1 - \bar{w}\qty{w-z\over 1 - \bar w z} } \\
&= {w(1-\bar w z) - (w-z) \over (1-\bar w z) - \bar w (w-z)} \\
&= {z-\abs{w}^2 z \over 1 - \abs{w}^2 }\\
&= z
.\]


:::


