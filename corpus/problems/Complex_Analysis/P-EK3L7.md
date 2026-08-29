---
schema: qual/card@1
id: P-EK3L7
kind: problem
title: $\frac1z\sum_{k=1}^\infty z^k/k$ converges on $S^1\setminus\{1\}$
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

::: problem
Show that $\frac{1}{z}\sum_{k=1}^\infty \frac{z^k}{k}$ converges for all $z \in S^1 \setminus \{1\}$ using summation by parts (Dirichlet's test).
:::

::: solution
**Goal:** Prove convergence of $\sum_{k=1}^\infty \frac{z^k}{k}$ on the punctured unit circle $S^1 \setminus \{1\} = \{e^{i\theta} \mid \theta \in (0, 2\pi)\}$ via summation by parts.

<1>1. Summation by parts formula (Abel summation):
    *Proof:*
    <2>1. Let $a_k = z^k$ and $b_k = \frac{1}{k}$.
    <2>2. Let $A_n = \sum_{k=1}^n a_k = \sum_{k=1}^n z^k$ be the partial sums of $a_k$ (with $A_0 = 0$).
    <2>3. Using summation by parts for $N \ge 1$:
        $$\sum_{k=1}^N a_k b_k = \sum_{k=1}^N (A_k - A_{k-1}) b_k = \sum_{k=1}^N A_k b_k - \sum_{k=1}^N A_{k-1} b_k = A_N b_N + \sum_{k=1}^{N-1} A_k (b_k - b_{k+1}).$$
    <2>4. Substituting $b_k = \frac{1}{k}$:
        $$\sum_{k=1}^N \frac{z^k}{k} = \frac{A_N}{N} + \sum_{k=1}^{N-1} A_k \left(\frac{1}{k} - \frac{1}{k+1}\right) = \frac{A_N}{N} + \sum_{k=1}^{N-1} \frac{A_k}{k(k+1)}.$$

<1>2. Uniform boundedness of the partial sums $A_n$ on $S^1 \setminus \{1\}$:
    *Proof:*
    <2>1. For $z \in S^1 \setminus \{1\}$, $z \ne 1$, so $1 - z \ne 0$.
    <2>2. The geometric series sum is:
        $$A_n = \sum_{k=1}^n z^k = z \sum_{j=0}^{n-1} z^j = z \frac{1 - z^n}{1 - z}.$$
    <2>3. By the triangle inequality:
        $$|A_n| = \left| z \frac{1 - z^n}{1 - z} \right| = \frac{|z| |1 - z^n|}{|1 - z|} \le \frac{1 \cdot (1 + |z|^n)}{|1 - z|} = \frac{2}{|1 - z|}.$$
    <2>4. Thus, for any fixed $z \in S^1 \setminus \{1\}$, $|A_n| \le M_z \coloneqq \frac{2}{|1 - z|}$ for all $n \ge 1$.

<1>3. Convergence of both terms as $N \to \infty$:
    *Proof:*
    <2>1. **Boundary term:**
        $$\left| \frac{A_N}{N} \right| \le \frac{M_z}{N} \xrightarrow{N \to \infty} 0.$$
    <2>2. **Summation term:**
        $$\sum_{k=1}^\infty \left| \frac{A_k}{k(k+1)} \right| \le M_z \sum_{k=1}^\infty \frac{1}{k(k+1)} = M_z \sum_{k=1}^\infty \left( \frac{1}{k} - \frac{1}{k+1} \right) = M_z \cdot 1 < \infty.$$
    <2>3. Since the series $\sum_{k=1}^\infty \frac{A_k}{k(k+1)}$ is absolutely convergent, it converges in $\mathbb{C}$.

<1>4. Conclusion:
    $$\sum_{k=1}^\infty \frac{z^k}{k} = \lim_{N \to \infty} \sum_{k=1}^N \frac{z^k}{k} = \sum_{k=1}^\infty \frac{A_k}{k(k+1)}$$
    converges for every $z \in S^1 \setminus \{1\}$. Multiplying by the non-zero factor $\frac{1}{z}$ preserves convergence. Q.E.D.
:::
