---
schema: qual/card@1
id: E-FJZCL
kind: exercise
title: Convergence of $\frac1z\sum_{k=1}^\infty\frac{z^k}{k}$ on $S^1\setminus\{1\}$
  by summation by parts
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Show that $\frac{1}{z}\sum_{k=1}^\infty \frac{z^k}{k}$ converges for all $z \in S^1 \setminus \{1\}$ using summation by parts.
:::

::: solution
**Goal:** Prove convergence of the series $\sum_{k=1}^\infty \frac{z^k}{k}$ for any $z = e^{i\theta} \in S^1$ with $z \ne 1$ using summation by parts (Dirichlet's Test).

<1>1. Summation by Parts Identity:
    *Proof:*
    <2>1. Let $a_k = z^k$ and $b_k = \frac{1}{k}$.
    <2>2. Define the partial sums $A_n = \sum_{k=1}^n z^k$ for $n \ge 1$ (with $A_0 = 0$).
    <2>3. By summation by parts (Abel summation) for any $N \ge 1$:
        $$\sum_{k=1}^N a_k b_k = \sum_{k=1}^N (A_k - A_{k-1}) b_k = A_N b_N + \sum_{k=1}^{N-1} A_k (b_k - b_{k+1}).$$
    <2>4. Substituting $b_k = \frac{1}{k}$:
        $$\sum_{k=1}^N \frac{z^k}{k} = \frac{A_N}{N} + \sum_{k=1}^{N-1} \frac{A_k}{k(k+1)}.$$

<1>2. Boundedness of the Partial Sums $A_n$:
    *Proof:*
    <2>1. Since $z \in S^1 \setminus \{1\}$, $|z| = 1$ and $z \ne 1$, so $1 - z \ne 0$.
    <2>2. Using the finite geometric series formula:
        $$A_n = \sum_{k=1}^n z^k = z \frac{1 - z^n}{1 - z}.$$
    <2>3. Taking absolute values:
        $$|A_n| = \left| z \frac{1 - z^n}{1 - z} \right| \le \frac{|z|(1 + |z|^n)}{|1 - z|} = \frac{2}{|1 - z|}.$$
    <2>4. Thus, there is a constant $M = \frac{2}{|1 - z|} < \infty$ such that $|A_n| \le M$ for all $n \ge 1$.

<1>3. Taking the limit as $N \to \infty$:
    *Proof:*
    <2>1. **Boundary term:**
        $$\left| \frac{A_N}{N} \right| \le \frac{M}{N} \xrightarrow{N \to \infty} 0.$$
    <2>2. **Infinite series term:**
        $$\sum_{k=1}^\infty \left| \frac{A_k}{k(k+1)} \right| \le M \sum_{k=1}^\infty \frac{1}{k(k+1)} = M \sum_{k=1}^\infty \left(\frac{1}{k} - \frac{1}{k+1}\right) = M \cdot 1 < \infty.$$
    <2>3. Since the series $\sum_{k=1}^\infty \frac{A_k}{k(k+1)}$ is absolutely convergent, it converges in $\mathbb{C}$.
    <2>4. Therefore:
        $$\lim_{N \to \infty} \sum_{k=1}^N \frac{z^k}{k} = \sum_{k=1}^\infty \frac{A_k}{k(k+1)} \in \mathbb{C}.$$

<1>4. Conclusion:
    The series converges on $S^1 \setminus \{1\}$. Multiplying by the non-zero scalar $\frac{1}{z}$ preserves convergence. Q.E.D.
:::
