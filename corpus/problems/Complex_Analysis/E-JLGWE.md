---
schema: qual/card@1
id: E-JLGWE
kind: problem
title: Extended Liouville theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Let $f$ be an entire function. Assume that for some $k \in \mathbb{N}$, and sufficiently large $|z|$, we have that $|f(z)| \leq A+B|z|^{k}$. Prove that $f$ is a polynomal of degree at most $k$.

:::

::: {.solution}
Induct on $k\ge0$. For $k=0$, $\abs f\le A+B$ outside a disk and $f$ is bounded on the disk by continuity, so $f$ is constant by Liouville.

For $k\geq1$, assume the statement for $k-1$ and let $\abs{f(z)}\le A+B\abs z^k$ for $\abs z\ge R$. Consider
\[
g(z) \definedas 
\begin{cases}
{f(z) - f(0) \over z} & z\neq 0, 
\\
f'(0) & z=0,
\end{cases}
\]
which is entire. For $\abs z\geq\max(R,1)$,
\[
\abs{g(z)} \leq {A+\abs{f(0)}+B\abs{z}^k \over \abs{z}} \leq \qty{A+\abs{f(0)}}+B\abs{z}^{k-1}
.\]
By the induction hypothesis $g$ is a polynomial of degree at most $k-1$, so $f(z)=f(0)+zg(z)$ is a polynomial of degree at most $k$.
:::

