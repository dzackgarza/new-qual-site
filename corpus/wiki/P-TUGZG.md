---
schema: qual/card@1
id: P-TUGZG
kind: problem
title: A uniformly convergent series of continuous functions is continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Continuity
relations: []
review: draft
solved: true
---

Let $\theset{f_n}$ be a sequence of continuous functions such that $\sum f_n$ converges uniformly.

Prove that $\sum f_n$ is also continuous.


:::{.concept}
\envlist

- The uniform limit theorem.
- $\eps/3$ trick.
:::

:::{.solution}
\envlist

:::{.claim}
If $F_N\to F$ uniformly with each $F_N$ continuous, then $F$ is continuous.
:::

:::{.proof title="of claim"}
\envlist

- Follows from an $\varepsilon/3$ argument: 
  \[  
  \abs{F(x) - F(y} \leq 
  \abs{F(x) - F_N(x)} + \abs{F_N(x) - F_N(y)} + \abs{F_N(y) - F(y)} 
  \leq \eps \to 0
  .\]

  - The first and last $\eps/3$ come from uniform convergence of $F_N\to F$.
  - The middle $\eps/3$ comes from continuity of each $F_N$.

:::

- Now setting $F_N\definedas \sum_{n=1}^N f_n$ yields a finite sum of continuous functions, which is continuous.
- Each $F_N$ is continuous and $F_N\to F$ uniformly, so $F$ is continuous.

:::
