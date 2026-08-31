---
schema: qual/card@1
id: P-KH5ZV
kind: problem
title: Absolute continuity of $\int_E|f|$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
  - Measure Theory
relations: []
review: draft
---

::: problem
Let $f \in L^1(\mathbb{R})$. Prove that for every $\varepsilon > 0$, there exists $\delta > 0$ such that for every Lebesgue measurable set $E \subseteq \mathbb{R}$ with $m(E) < \delta$,
$$
\int_E |f(x)| \, dx < \varepsilon.
$$
:::

::: solution
**Goal:** Prove the absolute continuity of the Lebesgue integral by truncating $|f|$ by height $N$ and applying the Monotone Convergence Theorem.

<1>1. Pointwise convergence and monotonicity of truncations:
    *Proof:*
    <2>1. For each integer $N \ge 1$, define the truncated function:
    $$f_N(x) = \min(|f(x)|, N) = \begin{cases} |f(x)| & \text{if } |f(x)| \le N, \\ N & \text{if } |f(x)| > N. \end{cases}$$
    <2>2. For every $x \in \mathbb{R}$, $0 \le f_N(x) \le f_{N+1}(x)$ and $\lim_{N \to \infty} f_N(x) = |f(x)|$.
    <2>3. Each $f_N$ is measurable and bounded by $N$.

<1>2. Approximation of $|f|$ by $f_N$ in $L^1(\mathbb{R})$:
    *Proof:*
    <2>1. By the Monotone Convergence Theorem:
    $$\lim_{N \to \infty} \int_{\mathbb{R}} f_N(x) \, dx = \int_{\mathbb{R}} |f(x)| \, dx.$$
    <2>2. Since $f \in L^1(\mathbb{R})$, $\int_{\mathbb{R}} |f(x)| \, dx < \infty$.
    <2>3. Thus:
    $$\lim_{N \to \infty} \int_{\mathbb{R}} (|f(x)| - f_N(x)) \, dx = \int_{\mathbb{R}} |f(x)| \, dx - \lim_{N \to \infty} \int_{\mathbb{R}} f_N(x) \, dx = 0.$$
    <2>4. Let $\varepsilon > 0$. There exists an integer $N_0 \ge 1$ such that
    $$\int_{\mathbb{R}} (|f(x)| - f_{N_0}(x)) \, dx < \frac{\varepsilon}{2}.$$

<1>3. Choice of $\delta > 0$ and integration bound:
    *Proof:*
    <2>1. Define $\delta = \frac{\varepsilon}{2 N_0} > 0$.
    <2>2. Let $E \subseteq \mathbb{R}$ be any measurable set with $m(E) < \delta$.
    <2>3. Decompose the integral over $E$:
    $$\int_E |f(x)| \, dx = \int_E (|f(x)| - f_{N_0}(x)) \, dx + \int_E f_{N_0}(x) \, dx.$$
    <2>4. Bound the first term using non-negativity and <1>2:
    $$\int_E (|f(x)| - f_{N_0}(x)) \, dx \le \int_{\mathbb{R}} (|f(x)| - f_{N_0}(x)) \, dx < \frac{\varepsilon}{2}.$$
    <2>5. Bound the second term using the bound $0 \le f_{N_0}(x) \le N_0$:
    $$\int_E f_{N_0}(x) \, dx \le \int_E N_0 \, dx = N_0 \cdot m(E) < N_0 \cdot \delta = N_0 \cdot \frac{\varepsilon}{2 N_0} = \frac{\varepsilon}{2}.$$
    <2>6. Combining the two estimates:
    $$\int_E |f(x)| \, dx < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

<1>4. Conclusion:
    *Proof:*
    For any $\varepsilon > 0$, choosing $\delta = \frac{\varepsilon}{2 N_0}$ ensures $\int_E |f| < \varepsilon$ whenever $m(E) < \delta$.
:::

