---
schema: qual/card@1
id: E-WURI3
kind: exercise
title: The Fourier transform of an $L^1$ function is bounded and uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Uniform Continuity
  - L¹
relations: []
review: draft
solved: true
---

::: exercise
- Show that if $f\in L^1$ then $\hat f$ is bounded and uniformly continuous.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $\hat f$ is bounded: $|\hat f(\xi)| \le \|f\|_1$ for every $\xi$.
Proof: $|\hat f(\xi)| = \left|\int f(x)e^{-ix\xi}\,dx\right| \le \int |f(x)|\,dx = \|f\|_1$.

<1>2. $\hat f$ is uniformly continuous.
<2>1. $|\hat f(\xi + h) - \hat f(\xi)| \le \int |f(x)|\,|e^{-ihx} - 1|\,dx$.
Proof: $|\hat f(\xi+h) - \hat f(\xi)| = \left|\int f(x)e^{-ix\xi}(e^{-ihx} - 1)\,dx\right| \le \int |f(x)||e^{-ihx}-1|\,dx$.
<2>2. The bound tends to $0$ as $h \to 0$.
Proof: dominated convergence — $|e^{-ihx} - 1| \le 2$ and $|f| \in L^1$, while $e^{-ihx} \to 1$ pointwise as $h \to 0$.
<2>3. The convergence is uniform in $\xi$.
Proof: the bound in <2>1 is independent of $\xi$.
<2>4. Q.E.D. Proof: <2>1–<2>3 show $\sup_\xi|\hat f(\xi + h) - \hat f(\xi)| \to 0$ as $h \to 0$, which is exactly uniform continuity.

<1>3. Q.E.D. Proof: <1>1 and <1>2.
:::
