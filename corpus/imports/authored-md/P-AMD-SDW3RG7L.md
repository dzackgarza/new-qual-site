---
schema: qual/card@1
id: P-AMD-SDW3RG7L
kind: problem
title: (1) Assume the infinite series
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - power-series
  - entire-functions
relations: []
review: draft
---

::: {.problem}
(1) Assume the infinite series
    $\displaystyle  \sum_{n=0}^\infty c_n z^n$ converges in $|z| < R$
    and let $f(z)$ be the limit. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
    \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

    (2) Deduce Liouville's theorem from (1). Liouville's theorem: If
    $f(z)$ is entire and bounded, then $f$ is constant.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. Let $f(z) = \sum_{n=0}^\infty c_n z^n$ converge in the disk $D(0, R) = \{z \in \mathbb{C} : |z| < R\}$. Prove that for any $0 \leq r < R$,
   $$\frac{1}{2\pi} \int_0^{2\pi} |f(r e^{i\theta})|^2 \, d\theta = \sum_{n=0}^\infty |c_n|^2 r^{2n}.$$
2. Deduce Liouville's theorem: any bounded entire function is constant.

---

### Part 1: Parseval's Identity for Power Series

<1>1. **The power series $f(r e^{i\theta}) = \sum_{n=0}^\infty c_n r^n e^{in\theta}$ converges uniformly with respect to $\theta \in [0, 2\pi]$ for any fixed $r < R$.**
  <2>1. Since the radius of convergence of $\sum_{n=0}^\infty c_n z^n$ is $R$, and $r < R$, there exists $r_0$ such that $r < r_0 < R$.
    *Proof:* Density of real numbers.
  <2>2. The series $\sum_{n=0}^\infty |c_n| r^n$ converges by the root test / standard properties of power series inside the disk of convergence.
    *Proof:* A power series converges absolutely at every point inside its open disk of convergence.
  <2>3. For all $\theta \in [0, 2\pi]$ and all $n \geq 0$, $|c_n (r e^{i\theta})^n| = |c_n| r^n$.
    *Proof:* Multiplicativity of modulus and $|e^{in\theta}| = 1$.
  <2>4. By the Weierstrass $M$-test, the series $\sum_{n=0}^\infty c_n r^n e^{in\theta}$ converges uniformly for $\theta \in [0, 2\pi]$.
    *Proof:* The terms are bounded by the summable constants $M_n = |c_n| r^n$.
  <2>5. Q.E.D.

<1>2. **The conjugate series $\overline{f(r e^{i\theta})} = \sum_{m=0}^\infty \overline{c_m} r^m e^{-im\theta}$ also converges uniformly for $\theta \in [0, 2\pi]$.**
  <2>1. $|\overline{c_m} r^m e^{-im\theta}| = |c_m| r^m$.
    *Proof:* $|\overline{w}| = |w|$ and $|e^{-im\theta}| = 1$.
  <2>2. By the Weierstrass $M$-test with the same bounds $M_m = |c_m| r^m$, the conjugate series converges uniformly on $[0, 2\pi]$.
    *Proof:* Follows from <1>1.<2>2.
  <2>3. Q.E.D.

<1>3. **Compute the integral of the product $|f(r e^{i\theta})|^2 = f(r e^{i\theta}) \overline{f(r e^{i\theta})}$.**
  <2>1. The product $|f(r e^{i\theta})|^2 = \left(\sum_{n=0}^\infty c_n r^n e^{in\theta}\right) \left(\sum_{m=0}^\infty \overline{c_m} r^m e^{-im\theta}\right) = \sum_{n=0}^\infty \sum_{m=0}^\infty c_n \overline{c_m} r^{n+m} e^{i(n-m)\theta}$ converges uniformly on $[0, 2\pi]$.
    *Proof:* The Cauchy product of two absolutely and uniformly convergent series converges uniformly.
  <2>2. Uniform convergence justifies term-by-term integration:
  $$\frac{1}{2\pi}\int_0^{2\pi} |f(r e^{i\theta})|^2 \, d\theta = \sum_{n=0}^\infty \sum_{m=0}^\infty c_n \overline{c_m} r^{n+m} \left( \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)\theta} \, d\theta \right).$$
    *Proof:* Fubini's theorem / term-by-term integration for uniformly convergent series.
  <2>3. For any integers $n, m \geq 0$:
  $$\frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)\theta} \, d\theta = \begin{cases} 1 & \text{if } n = m, \\ 0 & \text{if } n \neq m. \end{cases}$$
    *Proof:* If $n = m$, the integrand is $e^0 = 1$, so the integral is $\frac{2\pi}{2\pi} = 1$. If $n \neq m$, $\int_0^{2\pi} e^{i(n-m)\theta}\,d\theta = \left[\frac{e^{i(n-m)\theta}}{i(n-m)}\right]_0^{2\pi} = \frac{1 - 1}{i(n-m)} = 0$.
  <2>4. Substituting <2>3 into <2>2, all terms with $n \neq m$ vanish, leaving only the diagonal terms $n = m$:
  $$\frac{1}{2\pi} \int_0^{2\pi} |f(r e^{i\theta})|^2 \, d\theta = \sum_{n=0}^\infty c_n \overline{c_n} r^{2n} \cdot 1 = \sum_{n=0}^\infty |c_n|^2 r^{2n}.$$
    *Proof:* $c_n \overline{c_n} = |c_n|^2$.
  <2>5. Q.E.D.

---

### Part 2: Deduction of Liouville's Theorem

<1>4. **Let $f$ be an entire function bounded by $M < \infty$ on $\mathbb{C}$. Then $f$ is constant.**
  <2>1. Since $f$ is entire, its Taylor series $f(z) = \sum_{n=0}^\infty c_n z^n$ centered at $0$ has radius of convergence $R = \infty$.
    *Proof:* Entire functions are analytic on the whole complex plane $\mathbb{C}$.
  <2>2. By hypothesis, $|f(z)| \leq M$ for all $z \in \mathbb{C}$.
    *Proof:* Hypothesis that $f$ is bounded.
  <2>3. For any $r > 0$, by the result of Part 1 (<1>3):
  $$\sum_{n=0}^\infty |c_n|^2 r^{2n} = \frac{1}{2\pi}\int_0^{2\pi} |f(r e^{i\theta})|^2 \, d\theta \leq \frac{1}{2\pi}\int_0^{2\pi} M^2 \, d\theta = M^2.$$
    *Proof:* Monotonicity of the integral and $|f(r e^{i\theta})| \leq M$.
  <2>4. Since all terms in the series $\sum_{n=0}^\infty |c_n|^2 r^{2n}$ are non-negative, for each individual index $k \geq 1$:
  $$|c_k|^2 r^{2k} \leq \sum_{n=0}^\infty |c_n|^2 r^{2n} \leq M^2 \implies |c_k|^2 \leq \frac{M^2}{r^{2k}}.$$
    *Proof:* Dropping all non-negative terms $n \neq k$ from the sum.
  <2>5. Since $f$ is entire, the inequality $|c_k|^2 \leq \frac{M^2}{r^{2k}}$ holds for all $r > 0$. Taking the limit as $r \to \infty$:
  $$|c_k|^2 \leq \lim_{r\to\infty} \frac{M^2}{r^{2k}} = 0 \quad (\text{for every } k \geq 1).$$
    *Proof:* $2k > 0$ for $k \geq 1$, so $r^{2k} \to \infty$ as $r \to \infty$.
  <2>6. Therefore, $c_k = 0$ for all $k \geq 1$.
    *Proof:* $|c_k| \geq 0$ and $|c_k|^2 \leq 0 \implies c_k = 0$.
  <2>7. Thus, $f(z) = c_0$ is a constant function for all $z \in \mathbb{C}$.
    *Proof:* $f(z) = c_0 + \sum_{k=1}^\infty 0 \cdot z^k = c_0$.
  <2>8. Q.E.D.
:::
