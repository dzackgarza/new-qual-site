---
schema: qual/card@1
id: E-SS5.EX-4
kind: exercise
title: "SS 5.4: Growth and zeros of a product with geometrically spaced zeros"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Let $t > 0$ be given and fixed, and define $F(z)$ by
$$
F(z) = \prod_{n=1}^{\infty} (1 - e^{-2\pi n t} e^{2\pi i z}).
$$
Note that the product defines an entire function of $z$.

(a) Show that $|F(z)| \le A e^{a |z|^2}$, hence $F$ is of order 2.

(b) Show that $F$ vanishes exactly when $z = -i n t + m$ for $n \ge 1$ and $m \in \mathbb{Z}$ (integers).
Deduce that if $\{z_k\}$ is an enumeration of these zeros, we have
$$
\sum_k \frac{1}{|z_k|^2} = \infty \quad \text{but} \quad \sum_k \frac{1}{|z_k|^{2+\varepsilon}} < \infty \quad \text{for any } \varepsilon > 0.
$$
:::

::: solution
**Goal:** Prove that the Jacobi theta-type infinite product $F(z)$ is an entire function of order 2, determine its zero lattice, and compute its exponent of convergence.

<1>1. Part (b): Zeros of the Infinite Product $F(z)$:
    *Proof:*
    <2>1. A convergent infinite product of holomorphic functions vanishes if and only if at least one of its factors vanishes.
    <2>2. The $n$-th factor $(1 - e^{-2\pi n t} e^{2\pi i z}) = 0$ if and only if:
        $$e^{2\pi i z} = e^{2\pi n t} = e^{2\pi i (-i n t)}.$$
    <2>3. Since the complex exponential has period $2\pi i$, this holds if and only if:
        $$2\pi i z = 2\pi n t + 2\pi i m \quad (m \in \mathbb{Z}) \iff z = -i n t + m \quad (n \ge 1, m \in \mathbb{Z}).$$
    <2>4. Thus the zeros of $F(z)$ are the doubly-indexed lattice points:
        $$\mathcal{Z} = \{ -i n t + m \mid n \in \mathbb{Z}_{\ge 1}, m \in \mathbb{Z} \}.$$
    <2>5. The squared distance to the origin is:
        $$|z_{n, m}|^2 = m^2 + n^2 t^2.$$
    <2>6. **Divergence for exponent 2:**
        Using integral comparison on the half-plane $\mathbb{R} \times [1, \infty)$:
        $$\sum_{n=1}^\infty \sum_{m=-\infty}^\infty \frac{1}{m^2 + n^2 t^2} \approx \int_1^\infty \int_{-\infty}^\infty \frac{1}{x^2 + y^2 t^2} \, dx \, dy = \int_1^\infty \frac{\pi}{y t} \, dy = \frac{\pi}{t} [\ln y]_1^\infty = \infty.$$
    <2>7. **Convergence for exponent $2 + \varepsilon$:**
        For any $\varepsilon > 0$:
        $$\sum_{n=1}^\infty \sum_{m=-\infty}^\infty \frac{1}{(m^2 + n^2 t^2)^{1 + \varepsilon/2}} \approx \iint_{y \ge 1} \frac{1}{(x^2 + y^2 t^2)^{1 + \varepsilon/2}} \, dx \, dy \le C \int_1^\infty \frac{1}{r^{1 + \varepsilon}} \, dr = \frac{C}{\varepsilon} < \infty.$$

<1>2. Part (a): Order of Growth of $F(z)$:
    *Proof:*
    <2>1. Let $z \in \mathbb{C}$ with $y = \operatorname{Im}(z)$.
    <2>2. We split the infinite product $F(z) = F_1(z) F_2(z)$ at index $N = \lfloor c |z| \rfloor + 1$ (where $c = \frac{1}{t}$):
        $$F_1(z) = \prod_{n=1}^N (1 - e^{-2\pi n t} e^{2\pi i z}), \qquad F_2(z) = \prod_{n=N+1}^\infty (1 - e^{-2\pi n t} e^{2\pi i z}).$$
    <2>3. **Bounding $F_2(z)$:**
        - For $n \ge N+1 > \frac{|z|}{t} + 1$, the exponent satisfies $-2\pi n t + 2\pi |z| \le -2\pi (n - N) t$.
        - Using the inequality $|1 - w| \le e^{|w|}$ for all $w$:
          $$|F_2(z)| \le \prod_{n=N+1}^\infty (1 + e^{-2\pi n t} e^{2\pi |z|}) \le \exp\left( e^{2\pi |z|} \sum_{n=N+1}^\infty e^{-2\pi n t} \right) \le \exp\left( \frac{e^{-2\pi t}}{1 - e^{-2\pi t}} \right) = A < \infty.$$
    <2>4. **Bounding $F_1(z)$:**
        - Each factor in $F_1(z)$ satisfies:
          $$|1 - e^{-2\pi n t} e^{2\pi i z}| \le 1 + e^{-2\pi n t} e^{2\pi |z|} \le 1 + e^{2\pi |z|} \le 2 e^{2\pi |z|}.$$
        - Multiplying over $n = 1, \dots, N$:
          $$|F_1(z)| \le (2 e^{2\pi |z|})^N = 2^N e^{2\pi N |z|}.$$
        - Substituting $N \le c |z| + 1 = \frac{1}{t} |z| + 1$:
          $$|F_1(z)| \le 2^{\frac{|z|}{t} + 1} e^{2\pi \left(\frac{|z|}{t} + 1\right) |z|} \le C e^{\frac{2\pi}{t} |z|^2 + C' |z|} \le A' e^{a |z|^2}$$
          for any constant $a > \frac{2\pi}{t}$.
    <2>5. Combining the bounds:
        $$|F(z)| = |F_1(z)| \cdot |F_2(z)| \le A' e^{a |z|^2} \cdot A = A'' e^{a |z|^2}.$$
    <2>6. This proves that $F(z)$ has order of growth $\rho \le 2$.
    <2>7. Since the zeros have exponent of convergence $\rho_1 = 2$ (by Step 1), by Hadamard's Theorem the order is exactly $\rho = 2$.

<1>3. Conclusion:
    $F(z)$ is an entire function of order 2 with zeros $\{ -int + m \}$ and exponent of convergence 2. Q.E.D.
:::
