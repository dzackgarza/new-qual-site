---
schema: qual/card@1
id: P-QUXEB
kind: problem
title: Convergence of $\sum nz^n$, $\sum z^n/n^2$, and $\sum z^n/n$ on $S^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
---

::: problem
Prove the following statements concerning the convergence of power series on the unit circle $S^1 = \{z \in \mathbb{C} : |z| = 1\}$:

(a) $\sum_{n=1}^\infty n z^n$ does not converge at any point of $S^1$.

(b) $\sum_{n=1}^\infty \frac{z^n}{n^2}$ converges at every point of $S^1$.

(c) $\sum_{n=1}^\infty \frac{z^n}{n}$ converges at every point of $S^1$ except $z = 1$, where it diverges.
:::

::: solution
**Goal:** Determine the convergence behavior of $\sum n z^n$, $\sum \frac{z^n}{n^2}$, and $\sum \frac{z^n}{n}$ on the boundary circle $S^1$.

<1>1. Part (a): Divergence of $\sum_{n=1}^\infty n z^n$ on $S^1$.
    *Proof:*
    <2>1. Let $z \in S^1$, so $|z| = 1$.
    <2>2. The $n$-th term of the series is $c_n = n z^n$.
    <2>3. Compute the modulus of $c_n$:
    $$|c_n| = |n z^n| = n |z|^n = n \cdot 1^n = n.$$
    <2>4. As $n \to \infty$, $|c_n| = n \to \infty$, which implies $\lim_{n \to \infty} c_n \ne 0$.
    <2>5. By the Term Test for divergence, the series $\sum_{n=1}^\infty n z^n$ diverges at every point $z \in S^1$.

<1>2. Part (b): Convergence of $\sum_{n=1}^\infty \frac{z^n}{n^2}$ on $S^1$.
    *Proof:*
    <2>1. Let $z \in S^1$, so $|z| = 1$.
    <2>2. Compute the modulus of the $n$-th term:
    $$\left| \frac{z^n}{n^2} \right| = \frac{|z|^n}{n^2} = \frac{1}{n^2}.$$
    <2>3. The real $p$-series $\sum_{n=1}^\infty \frac{1}{n^2}$ converges because $p = 2 > 1$.
    <2>4. By the Direct Comparison Test, $\sum_{n=1}^\infty \frac{z^n}{n^2}$ converges absolutely for every $z \in S^1$.
    <2>5. Since absolute convergence in $\mathbb{C}$ implies convergence, the series converges at every point of $S^1$.

<1>3. Part (c): Divergence at $z = 1$.
    *Proof:*
    <2>1. At $z = 1 \in S^1$, the series evaluates to
    $$\sum_{n=1}^\infty \frac{1^n}{n} = \sum_{n=1}^\infty \frac{1}{n}.$$
    <2>2. This is the harmonic series ($p$-series with $p = 1$), which diverges to $+\infty$.

<1>4. Part (c): Convergence at $z \in S^1 \setminus \{1\}$ via Dirichlet's Test.
    *Proof:*
    <2>1. Let $z \in S^1$ with $z \ne 1$. Write the series as $\sum_{n=1}^\infty a_n b_n$, where $a_n = \frac{1}{n}$ and $b_n = z^n$.
    <2>2. Monotonicity and limit of $a_n$: $a_n > 0$, $a_{n+1} = \frac{1}{n+1} < \frac{1}{n} = a_n$, and $\lim_{n \to \infty} a_n = 0$.
    <2>3. Partial sums of $b_n$: For each $N \ge 1$, the geometric sum is
    $$B_N = \sum_{k=1}^N z^k = z \sum_{k=0}^{N-1} z^k = z \frac{1 - z^N}{1 - z}.$$
    <2>4. Boundedness of $B_N$: Since $|z| = 1$, the triangle inequality yields
    $$|B_N| = |z| \frac{|1 - z^N|}{|1 - z|} = \frac{|1 - z^N|}{|1 - z|} \le \frac{1 + |z|^N}{|1 - z|} = \frac{2}{|1 - z|}.$$
    <2>5. Since $z \ne 1$, the bound $M_z = \frac{2}{|1 - z|}$ is finite and independent of $N$, so $|B_N| \le M_z$ for all $N \ge 1$.
    <2>6. By summation by parts, for any $N > M \ge 1$:
    $$\sum_{n=M}^N a_n b_n = a_N B_N - a_M B_{M-1} - \sum_{n=M}^{N-1} (a_{n+1} - a_n) B_n.$$
    <2>7. Bounding the tail using $|B_n| \le M_z$ and telescoping $a_{n+1} - a_n \le 0$:
    $$\left| \sum_{n=M}^N a_n b_n \right| \le M_z a_N + M_z a_M + M_z \sum_{n=M}^{N-1} (a_n - a_{n+1}) = 2 M_z a_M = \frac{2 M_z}{M}.$$
    <2>8. Since $\lim_{M \to \infty} \frac{2 M_z}{M} = 0$, the sequence of partial sums satisfies the Cauchy criterion in $\mathbb{C}$.
    <2>9. Therefore $\sum_{n=1}^\infty \frac{z^n}{n}$ converges for every $z \in S^1 \setminus \{1\}$.

<1>5. Conclusion:
    *Proof:*
    The three parts (a), (b), and (c) are established.
:::

