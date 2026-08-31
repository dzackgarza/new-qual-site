---
schema: qual/card@1
id: P-KBH2K
kind: problem
title: Cesàro means vanish if $a_n\to 0$ or $\sum a_n/n$ converges
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Series of Numbers
  - Limits
relations: []
review: draft
---

::: problem
Let $(a_n)_{n=1}^\infty$ be a sequence of real numbers.

(a) Prove that if $\lim_{n \to \infty} a_n = 0$, then
$$
\lim_{n \to \infty} \frac{a_1 + a_2 + \cdots + a_n}{n} = 0.
$$

(b) Prove that if the series $\sum_{n=1}^{\infty} \frac{a_n}{n}$ converges, then
$$
\lim_{n \to \infty} \frac{a_1 + a_2 + \cdots + a_n}{n} = 0.
$$
:::

::: solution
**Goal:** Prove the Cesàro limit theorem for null sequences in (a), and deduce Kronecker's Lemma via summation by parts in (b).

<1>1. Part (a): Cesàro mean of a null sequence converges to 0.
    *Proof:*
    <2>1. Let $\varepsilon > 0$ be given.
    <2>2. Since $\lim_{n \to \infty} a_n = 0$, there exists an integer $N_0 \in \mathbb{N}$ such that
    $$|a_k| < \frac{\varepsilon}{2} \quad \text{for all } k > N_0.$$
    <2>3. For any $n > N_0$, split the sum into the initial segment and the tail:
    $$\left| \frac{1}{n} \sum_{k=1}^n a_k \right| \le \frac{1}{n} \sum_{k=1}^{N_0} |a_k| + \frac{1}{n} \sum_{k=N_0+1}^n |a_k|.$$
    <2>4. Bound the second term:
    $$\frac{1}{n} \sum_{k=N_0+1}^n |a_k| < \frac{1}{n} \sum_{k=N_0+1}^n \frac{\varepsilon}{2} = \frac{n - N_0}{n} \frac{\varepsilon}{2} < \frac{\varepsilon}{2}.$$
    <2>5. For the first term, the sum $C = \sum_{k=1}^{N_0} |a_k|$ is a fixed constant independent of $n$. Choose $N_1 > N_0$ such that for all $n > N_1$:
    $$\frac{C}{n} = \frac{1}{n} \sum_{k=1}^{N_0} |a_k| < \frac{\varepsilon}{2}.$$
    <2>6. For all $n > N_1$:
    $$\left| \frac{1}{n} \sum_{k=1}^n a_k \right| \le \frac{C}{n} + \frac{n - N_0}{n} \frac{\varepsilon}{2} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
    <2>7. Since $\varepsilon > 0$ was arbitrary, $\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n a_k = 0$.

<1>2. Generalization of Cesàro mean: If $x_n \to L$, then $\frac{1}{n} \sum_{k=1}^n x_k \to L$.
    *Proof:*
    <2>1. Let $y_n = x_n - L$. Then $y_n \to 0$.
    <2>2. By Part (a), $\frac{1}{n} \sum_{k=1}^n y_k \to 0$.
    <2>3. Then $\frac{1}{n} \sum_{k=1}^n x_k = \frac{1}{n} \sum_{k=1}^n (y_k + L) = \frac{1}{n} \sum_{k=1}^n y_k + L \to 0 + L = L$.

<1>3. Part (b): Convergence of $\sum \frac{a_n}{n} \implies \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n a_k = 0$ (Kronecker's Lemma).
    *Proof:*
    <2>1. Let $S_n = \sum_{k=1}^n \frac{a_k}{k}$ for $n \ge 1$, and set $S_0 = 0$.
    <2>2. By hypothesis, the series converges, so $\lim_{n \to \infty} S_n = S \in \mathbb{R}$.
    <2>3. Note that $\frac{a_k}{k} = S_k - S_{k-1}$, so $a_k = k(S_k - S_{k-1})$ for each $k \ge 1$.
    <2>4. Summation by parts:
    $$\sum_{k=1}^n a_k = \sum_{k=1}^n k(S_k - S_{k-1}) = \sum_{k=1}^n k S_k - \sum_{k=1}^n k S_{k-1} = \sum_{k=1}^n k S_k - \sum_{j=0}^{n-1} (j + 1) S_j.$$
    <2>5. Group like terms:
    $$\sum_{k=1}^n a_k = n S_n + \sum_{k=1}^{n-1} k S_k - \sum_{j=1}^{n-1} j S_j - \sum_{j=0}^{n-1} S_j = n S_n - \sum_{j=0}^{n-1} S_j.$$
    <2>6. Divide by $n$:
    $$\frac{1}{n} \sum_{k=1}^n a_k = S_n - \frac{1}{n} \sum_{j=0}^{n-1} S_j.$$
    <2>7. Since $\lim_{n \to \infty} S_n = S$, the sequence $(S_j)_{j=0}^\infty$ converges to $S$.
    <2>8. By <1>2, the Cesàro average satisfies $\lim_{n \to \infty} \frac{1}{n} \sum_{j=0}^{n-1} S_j = S$.
    <2>9. Therefore:
    $$\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n a_k = \lim_{n \to \infty} S_n - \lim_{n \to \infty} \frac{1}{n} \sum_{j=0}^{n-1} S_j = S - S = 0.$$

<1>4. Conclusion:
    *Proof:*
    Both conditions imply that the arithmetic mean $\frac{1}{n} \sum_{k=1}^n a_k$ converges to 0.
:::
