---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W3
kind: problem
title: 'Prove the uniform-limit continuity theorem directly'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - continuity
  - convergence-of-functions
relations:
- kind: uses
  target: T-RA-WORKSHOP-D7-6-1
review: draft
---

::: {.problem title="?"}
Assume that $\{f_n\}$ is a sequence of continuous functions $f_n:E\subset\mathbb R\to\mathbb R$ which converges uniformly to $f$.
Prove the results of Theorem 6.1 directly.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Prove directly that the uniform limit $f$ of continuous functions $f_n: E \to \mathbb R$ is continuous.

<1>1. $f$ is a function $E \to \mathbb R$.
    Proof: $f_n(x)$ converges for every $x \in E$ (uniform convergence implies pointwise), so $f(x) := \lim_n f_n(x)$ is a well-defined real number at each $x$.

<1>2. Fix $x_0 \in E$ and $\varepsilon > 0$. Choose $N$ with $\|f_n - f\|_\infty < \varepsilon/3$ for all $n \ge N$.
    Proof: uniform convergence of $f_n$ to $f$.

<1>3. Choose $\delta > 0$ such that $|x - x_0| < \delta \Rightarrow |f_N(x) - f_N(x_0)| < \varepsilon/3$.
    Proof: $f_N$ is continuous at $x_0$.

<1>4. For $|x - x_0| < \delta$: $|f(x) - f(x_0)| \le |f(x) - f_N(x)| + |f_N(x) - f_N(x_0)| + |f_N(x_0) - f(x_0)| < \varepsilon/3 + \varepsilon/3 + \varepsilon/3 = \varepsilon$.
    Proof: the first and third terms are $< \varepsilon/3$ by <1>2 (uniform closeness of $f_N$ to $f$), the middle by <1>3.

<1>5. $f$ is continuous at $x_0$.
    Proof: <1>4 gives the $\varepsilon$-$\delta$ condition at $x_0$; $x_0$ was arbitrary, so $f$ is continuous on $E$.

:::
