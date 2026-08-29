---
schema: qual/card@1
id: P-YEZTR
kind: problem
title: $\lim a_n/a_{n+1}=z_0$ for the power series of a function with a pole at $z_0\in\partial\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Suppose that $f$ is holomorphic on an open set containing the closed unit disk $\overline{\mathbb{D}} = \{z \in \mathbb{C} \mid |z| \le 1\}$ except for a single pole at $z_0 \in \partial\mathbb{D}$ ($|z_0| = 1$).
Let $\sum_{n=0}^\infty a_n z^n$ be the Maclaurin series expansion of $f$ in $\mathbb{D}$.
Prove that:
$$\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0.$$
:::

::: solution
**Goal:** Prove that $\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0$ by isolating the principal part of the pole at $z_0$.

<1>1. Principal Part at the Pole $z_0$:
    *Proof:*
    <2>1. Let $k \ge 1$ be the order of the pole of $f$ at $z_0 \in \partial\mathbb{D}$.
    <2>2. The principal part of the Laurent expansion of $f(z)$ at $z_0$ is:
        $$P(z) = \sum_{j=1}^k \frac{c_j}{(z_0 - z)^j} \quad \text{with } c_k \ne 0.$$
    <2>3. Define $g(z) = f(z) - P(z)$.
    <2>4. By construction, $g(z)$ has a removable singularity at $z_0$, and since $f$ has no other singularities on $\overline{\mathbb{D}}$, $g(z)$ is holomorphic on a larger disk $D_R(0)$ of radius $R > 1$.

<1>2. Power Series Expansion of the Principal Part:
    *Proof:*
    <2>1. For $|z| < 1$, using the binomial series:
        $$\frac{1}{(z_0 - z)^j} = \frac{1}{z_0^j \left(1 - \frac{z}{z_0}\right)^j} = \frac{1}{z_0^j} \sum_{n=0}^\infty \binom{n + j - 1}{j - 1} \left(\frac{z}{z_0}\right)^n = \sum_{n=0}^\infty \binom{n + j - 1}{j - 1} z_0^{-(n+j)} z^n.$$
    <2>2. Thus, the $n$-th Taylor coefficient of $P(z) = \sum_{n=0}^\infty p_n z^n$ is:
        $$p_n = \sum_{j=1}^k c_j \binom{n + j - 1}{j - 1} z_0^{-(n+j)}.$$
    <2>3. The leading term as $n \to \infty$ corresponds to $j = k$:
        $$\binom{n + k - 1}{k - 1} = \frac{n^{k-1}}{(k-1)!} + O(n^{k-2}).$$
    <2>4. Therefore:
        $$p_n = \frac{c_k}{(k-1)!} n^{k-1} z_0^{-(n+k)} \left( 1 + O\left(\frac{1}{n}\right) \right).$$

<1>3. Power Series of the Remainder $g(z)$:
    *Proof:*
    <2>1. Let $g(z) = \sum_{n=0}^\infty b_n z^n$.
    <2>2. Since $g$ is holomorphic on $D_R(0)$ with $R > 1$, Cauchy's estimates imply that for any $1 < r < R$:
        $$|b_n| \le M r^{-n} = O(r^{-n}) \quad (r > 1).$$
    <2>3. Since $r > 1$, $b_n$ decays exponentially to 0 as $n \to \infty$.

<1>4. Asymptotic Ratio of Coefficients $a_n = p_n + b_n$:
    *Proof:*
    <2>1. The coefficients of $f(z)$ are $a_n = p_n + b_n$.
    <2>2. Because $b_n = O(r^{-n})$ decays exponentially while $|p_n| \sim C n^{k-1}$ grows polynomially:
        $$a_n = p_n + O(r^{-n}) = \frac{c_k}{(k-1)!} n^{k-1} z_0^{-(n+k)} \left( 1 + O\left(\frac{1}{n}\right) \right).$$
    <2>3. Computing the ratio $\frac{a_n}{a_{n+1}}$:
        $$\frac{a_n}{a_{n+1}} = \frac{\frac{c_k}{(k-1)!} n^{k-1} z_0^{-(n+k)} \left( 1 + O\left(\frac{1}{n}\right) \right)}{\frac{c_k}{(k-1)!} (n+1)^{k-1} z_0^{-(n+1+k)} \left( 1 + O\left(\frac{1}{n+1}\right) \right)} = z_0 \cdot \left( \frac{n}{n+1} \right)^{k-1} \cdot \frac{1 + O(1/n)}{1 + O(1/n)}.$$
    <2>4. Taking the limit as $n \to \infty$:
        $$\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0 \cdot 1^{k-1} \cdot 1 = z_0.$$

<1>5. Conclusion:
    $\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0$. Q.E.D.
:::
