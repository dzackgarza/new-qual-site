---
schema: qual/card@1
id: P-AITX4
kind: problem
title: If $f:[0,1]\to\mathbb{R}$ is
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Continuity
relations: []
review: draft
---

::: problem
If $f:[0,1]\to\mathbb{R}$ is continuous, prove that $$\displaystyle\lim_{n\to\infty}\int_0^1 f(x^n)\,dx=f(0).$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $f(x^n) \to f(0)$ pointwise for every $x \in [0,1)$.
Proof: $x^n \to 0$ for $0 \le x < 1$; $f$ is continuous, so $f(x^n) \to f(0)$.

<1>2. $f(x^n) \to f(0)$ for almost every $x \in [0,1]$.
Proof: <1>1 covers all $x$ except $x = 1$, a null set.

<1>3. The family is dominated: $|f(x^n)| \le \|f\|_\infty$ for all $n$ and all $x$.
Proof: $f$ is continuous on the compact interval $[0,1]$, hence bounded; $x^n \in [0,1]$.

<1>4. Q.E.D. Proof: dominated convergence (<1>2, <1>3) gives $\lim_n\int_0^1 f(x^n)\,dx = \int_0^1 f(0)\,dx = f(0)$.
:::
