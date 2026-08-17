---
schema: qual/card@1
id: P-MMAQ-TRKDERZNBP
kind: problem
title: Let $\theset{f_n}$ be a sequence of continuous functions such that…
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - series-of-functions
  - continuity
relations: []
review: draft
---

::: problem
Let $\theset{f_n}$ be a sequence of continuous functions such that $\sum f_n$ converges uniformly.

Prove that $\sum f_n$ is also continuous.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $\{f_n\}$ are continuous functions and $\sum f_n$ converges uniformly, then $\sum f_n$ is continuous.

<1>1. The partial sums are continuous.
    <2>1. For each $N$, $S_N \definedas \sum_{n=1}^N f_n$ is continuous.
        Proof: A finite sum of continuous functions is continuous.
    <2>2. Q.E.D.
        Proof: Immediate from <2>1.

<1>2. The limit $S \definedas \sum_{n=1}^\infty f_n$ is continuous.
    <2>1. $S_N \to S$ uniformly on the domain.
        Proof: This is exactly the hypothesis that $\sum f_n$ converges uniformly (uniform convergence of the partial sums).
    <2>2. A uniform limit of continuous functions is continuous.
        Proof: Fix a point $x_0$ and $\eps > 0$; choose $N$ with $\abs{S_N(x) - S(x)} < \eps/3$ for all $x$ (uniform convergence), then $\delta$ with $\abs{S_N(x) - S_N(x_0)} < \eps/3$ whenever $\abs{x - x_0} < \delta$ (continuity of $S_N$); then $\abs{S(x) - S(x_0)} < \eps$ by the triangle inequality (the standard $\eps/3$ argument).
    <2>3. Hence $S$ is continuous.
        Proof: By <2>2 applied to the sequence $S_N$.
    <2>4. Q.E.D.
        Proof: $S = \sum f_n$ is continuous.
:::
