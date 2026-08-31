---
schema: qual/card@1
id: P-UMAQ5
kind: problem
title: A continuous $f\in L^1(\RR)$ need not tend to $0$ at infinity, but a uniformly
  continuous one must
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - L¹
  - Counterexamples
  - Limits
relations: []
review: draft
---

::: problem
(a) Give an example of a continuous function $f \in L^1(\mathbb{R})$ such that $f(x) \not\to 0$ as $|x| \to \infty$.

(b) Show that if $f \in L^1(\mathbb{R})$ is *uniformly continuous*, then
$$
\lim_{|x| \to \infty} f(x) = 0.
$$
:::

::: solution
**Goal:** Construct a sequence of narrowing triangular spikes of height 1 in (a), and use uniform continuity to lower-bound the integral on disjoint intervals in (b).

<1>1. Part (a): Explicit counterexample for continuous $L^1$ functions.
    *Proof:*
    <2>1. For each integer $n \ge 2$, define the symmetric triangle function supported on $\left[n - \frac{1}{n^2}, n + \frac{1}{n^2}\right]$:
    $$f_n(x) = \begin{cases} 1 - n^2 |x - n| & \text{if } |x - n| \le \frac{1}{n^2}, \\ 0 & \text{otherwise}. \end{cases}$$
    <2>2. Define $f: \mathbb{R} \to \mathbb{R}$ by $f(x) = \sum_{n=2}^\infty f_n(x)$.
    <2>3. Continuity:
        - For distinct $n, m \ge 2$, the supports $\left[n - \frac{1}{n^2}, n + \frac{1}{n^2}\right]$ and $\left[m - \frac{1}{m^2}, m + \frac{1}{m^2}\right]$ are disjoint since $\frac{1}{n^2} \le \frac{1}{4} < \frac{1}{2}$.
        - On any bounded open neighborhood, at most one $f_n$ is non-zero, so $f$ is continuous on $\mathbb{R}$.
    <2>4. Integrability ($f \in L^1(\mathbb{R})$):
        - The integral of each triangular spike is the area of a triangle of base $\frac{2}{n^2}$ and height $1$:
        $$\int_{\mathbb{R}} f_n(x) \, dx = \frac{1}{2} \cdot \frac{2}{n^2} \cdot 1 = \frac{1}{n^2}.$$
        - By the Monotone Convergence Theorem:
        $$\int_{\mathbb{R}} |f(x)| \, dx = \sum_{n=2}^\infty \int_{\mathbb{R}} f_n(x) \, dx = \sum_{n=2}^\infty \frac{1}{n^2} < \infty.$$
        - Thus $f \in L^1(\mathbb{R})$.
    <2>5. Failure to converge to 0:
        - For each $n \ge 2$, $f(n) = f_n(n) = 1$.
        - Along the sequence $x_n = n \to \infty$, $\lim_{n \to \infty} f(x_n) = 1 \ne 0$.
        - Therefore $f(x) \not\to 0$ as $|x| \to \infty$.

<1>2. Part (b): Uniform continuity forces $\lim_{|x| \to \infty} f(x) = 0$.
    *Proof:*
    <2>1. Suppose for contradiction that $\lim_{|x| \to \infty} f(x) \ne 0$.
    <2>2. Then there exists $\varepsilon_0 > 0$ and a sequence $(x_n)_{n=1}^\infty$ with $|x_n| \to \infty$ such that
    $$|f(x_n)| \ge \varepsilon_0 \quad \text{for all } n \ge 1.$$
    <2>3. Since $f$ is uniformly continuous on $\mathbb{R}$, there exists $\delta > 0$ such that
    $$|x - y| < \delta \implies |f(x) - f(y)| < \frac{\varepsilon_0}{2}.$$
    <2>4. For each $n \ge 1$ and all $x \in (x_n - \delta, x_n + \delta)$:
    $$|f(x)| \ge |f(x_n)| - |f(x) - f(x_n)| \ge \varepsilon_0 - \frac{\varepsilon_0}{2} = \frac{\varepsilon_0}{2}.$$
    <2>5. Since $|x_n| \to \infty$, we can choose a subsequence $(x_{n_k})_{k=1}^\infty$ such that the open intervals $I_k = (x_{n_k} - \delta, x_{n_k} + \delta)$ are pairwise disjoint (for instance, ensuring $|x_{n_{k+1}} - x_{n_k}| \ge 2\delta$).
    <2>6. Integrate $|f|$ over the union of disjoint intervals:
    $$\int_{\mathbb{R}} |f(x)| \, dx \ge \sum_{k=1}^\infty \int_{I_k} |f(x)| \, dx \ge \sum_{k=1}^\infty \left( \frac{\varepsilon_0}{2} \cdot 2\delta \right) = \sum_{k=1}^\infty (\varepsilon_0 \delta) = \infty.$$
    <2>7. This contradicts $f \in L^1(\mathbb{R})$ ($\int_{\mathbb{R}} |f| < \infty$).
    <2>8. Therefore $\lim_{|x| \to \infty} f(x) = 0$.

<1>3. Conclusion:
    *Proof:*
    A continuous $L^1$ function may produce narrow spikes of height 1 with summable areas, but uniform continuity prevents spike narrowing and forces $\lim_{|x| \to \infty} f(x) = 0$.
:::


