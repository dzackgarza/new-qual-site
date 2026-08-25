---
schema: qual/card@1
id: P-MMAQ-TCJZEHD655
kind: problem
title: If $\limsup a_n\le l$, then $\limsup\frac1n\sum_{i=1}^n a_i\le l$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Numbers
relations: []
review: draft
---

::: problem
If $\limsup_{n\rightarrow \infty} a_n\leq l$, show that $\limsup_{n\rightarrow \infty}\sum_{i=1}^n{a_i/n}\leq l$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $\limsup_{n \to \infty} a_n \leq l$, show $\limsup_{n \to \infty} \frac{1}{n}\sum_{i=1}^n a_i \leq l$ (the Cesàro means do not increase the limsup).

<1>1. Reduction to the case $l \in \RR$; the cases $l = \pm\infty$ are handled at the end.
Proof: If $l = +\infty$ the claim is trivial.
If $l = -\infty$, the argument of <1>2 applied with $l$ replaced by arbitrarily negative $K$ gives the claim.
So assume $l$ is finite.

<1>2. Proof for finite $l$.
<2>1. Fix $\eps > 0$.
Since $\limsup_n a_n \leq l$, there is $N$ such that $a_n < l + \eps$ for all $n \geq N$.
Proof: By definition of $\limsup$ as the infimum of eventual upper bounds: $\limsup_n a_n \leq l$ implies every value $l + \eps$ (with $\eps > 0$) is an eventual upper bound of $\{a_n\}$.
<2>2. Split the Cesàro mean: $\frac{1}{n}\sum_{i=1}^n a_i = \frac{1}{n}\sum_{i=1}^{N-1} a_i + \frac{1}{n}\sum_{i=N}^{n} a_i \leq \frac{C}{n} + \frac{n - N + 1}{n}(l + \eps)$, where $C = \sum_{i=1}^{N-1} a_i$ is fixed.
Proof: The first sum is a fixed finite quantity $C$ (it may be negative; the bound still holds); the second sum has $n - N + 1$ terms each $< l + \eps$ by <2>1. <2>3. Taking $\limsup$ as $n \to \infty$: $\limsup_n \frac{1}{n}\sum_{i=1}^n a_i \leq \limsup_n \left(\frac{C}{n} + \frac{n - N + 1}{n}(l + \eps)\right) = l + \eps$.
Proof: $C/n \to 0$ and $(n - N + 1)/n \to 1$, so the right side converges to $l + \eps$; the inequality passes to $\limsup$ (for any sequences $x_n \leq y_n$, $\limsup x_n \leq \limsup y_n$). <2>4. Since $\eps > 0$ was arbitrary, $\limsup_n \frac{1}{n}\sum_{i=1}^n a_i \leq l$.
Proof: Let $\eps \to 0$ in <2>3. <2>5. Q.E.D. Proof: This proves the claim for finite $l$; the cases $l = \pm \infty$ were handled in <1>1.
:::
