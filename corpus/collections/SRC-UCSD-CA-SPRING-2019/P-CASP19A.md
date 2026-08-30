---
schema: qual/card@1
id: P-CASP19A
kind: problem
title: "Entire function bounded by log(|f| + 2) is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $f$ be an entire function.
Assume $|f| \leq \log(|f| + 2)$ on $\mathbb{C}$.
Prove $f$ is constant.

::: {.solution}
<1>1. The inequality $|f(z)| \le \log(|f(z)| + 2)$ holds for all $z \in \mathbb{C}$.
Proof: hypothesis.

<1>2. The function $h(t) = t - \log(t + 2)$ satisfies $h(0) = -\log 2 < 0$ and $h(t) \to \infty$ as $t \to \infty$, and $h'(t) = 1 - 1/(t+2) > 0$ for $t > 0$.
Proof: calculus.

<1>3. Hence the set $\{t \ge 0 : t \le \log(t + 2)\}$ is bounded.
Proof: <1>2 ($h(t) \le 0$ only for bounded $t$).

<1>4. Therefore $|f(z)|$ is uniformly bounded (there is $M$ with $|f(z)| \le M$ for all $z$). Proof: <1>1 and <1>3.

<1>5. By Liouville's theorem, a bounded entire function is constant.
Proof: Liouville's theorem.

<1>6. Hence $f$ is constant.
Proof: <1>4 and <1>5.

<1>7. Q.E.D. Proof: <1>6.
:::
:::
