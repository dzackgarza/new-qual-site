---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W1
kind: problem
title: Uniform continuity and a continuous non-uniformly-continuous example
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
State the definition of uniform continuity.
Give an example of a function $f:(0,1)\to\mathbb R$ which is continuous but not uniformly continuous.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Definition of uniform continuity.
Proof: $f : D \subseteq \mathbb{R} \to \mathbb{R}$ is uniformly continuous on $D$ if for every $\epsilon > 0$ there is $\delta > 0$ such that for all $x, y \in D$, $|x - y| < \delta \implies |f(x) - f(y)| < \epsilon$.
(The difference from plain continuity: the same $\delta$ must work for all pairs $x, y$, independent of where they sit.)
<1>2. Example: $f(x) = 1/x$ on $(0,1)$ is continuous but not uniformly continuous.
<2>1. Continuous: $f$ is a quotient of continuous functions with nonzero denominator on $(0,1)$, hence continuous at every point of $(0,1)$.
<2>2. Not uniformly continuous: take $x_n = 1/n$ and $y_n = 1/(2n)$.
Then $x_n, y_n \in (0,1)$ and $|x_n - y_n| = 1/(2n) \to 0$, but $|f(x_n) - f(y_n)| = |n - 2n| = n \to \infty$.
Hence no $\delta > 0$ can control pairs $(x_n, y_n)$ with $|x_n - y_n| \to 0$, so the uniform-continuity definition fails (with any $\epsilon$, say $\epsilon = 1$). <1>3. Q.E.D.
:::
