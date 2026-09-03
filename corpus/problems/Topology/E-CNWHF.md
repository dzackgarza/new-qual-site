---
schema: qual/card@1
id: E-CNWHF
kind: problem
title: Compact metric spaces are complete
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Show that every compact metric space $(X, d)$ is complete (every Cauchy sequence in $X$ converges to a point in $X$).
:::

::: solution
**Goal:** Prove that a compact metric space $(X, d)$ is complete.

<1>1. Setting and Cauchy Sequence:
    *Proof:*
    <2>1. Let $(X, d)$ be a compact metric space.
    <2>2. Let $(x_n)_{n=1}^\infty$ be a Cauchy sequence in $X$: for every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that:
        $$m, n \ge N \implies d(x_n, x_m) < \varepsilon.$$

<1>2. Existence of a convergent subsequence (Sequential Compactness):
    *Proof:*
    <2>1. In any metric space, compactness is equivalent to sequential compactness.
    <2>2. Therefore, every sequence in $X$ has a convergent subsequence.
    <2>3. There exists a subsequence $(x_{n_k})_{k=1}^\infty$ and a point $x \in X$ such that:
        $$\lim_{k \to \infty} x_{n_k} = x.$$

<1>3. The entire Cauchy sequence converges to $x$:
    *Proof:*
    <2>1. Let $\varepsilon > 0$ be given.
    <2>2. **From the Cauchy property:** Choose $N_1 \in \mathbb{N}$ such that for all $m, n \ge N_1$:
        $$d(x_n, x_m) < \frac{\varepsilon}{2}.$$
    <2>3. **From subsequence convergence:** Choose $K \in \mathbb{N}$ such that for all $k \ge K$:
        $$d(x_{n_k}, x) < \frac{\varepsilon}{2}.$$
    <2>4. Choose an index $k \ge K$ large enough so that $n_k \ge N_1$ (which is always possible since $n_k \to \infty$).
    <2>5. Then for any $n \ge N_1$, by the triangle inequality with $m = n_k$:
        $$d(x_n, x) \le d(x_n, x_{n_k}) + d(x_{n_k}, x) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
    <2>6. Thus $\lim_{n \to \infty} x_n = x \in X$.

<1>4. Conclusion:
    Every Cauchy sequence in $X$ converges to a limit in $X$, so $(X, d)$ is complete. Q.E.D.
:::
