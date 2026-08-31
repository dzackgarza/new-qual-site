---
schema: qual/card@1
id: E-SS6.PR-1
kind: exercise
title: "Estimates for the Riemann zeta function and its derivative near $\\Re(s)=1$"
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
1. This problem provides further estimates for $\zeta$ and $\zeta'$ near $\operatorname{Re}(s) = 1$.

(a) Use Proposition 2.5 and its corollary to prove
$$
\zeta(s) = \sum_{1 \leq n < N} n^{-s} + \frac{N^{1-s}}{s-1} + \sum_{n \geq N} \delta_n(s)
$$
for every integer $N \geq 2$, whenever $\operatorname{Re}(s) > 0$, where $\delta_n(s) = n^{-s} - \int_n^{n+1} x^{-s}\,dx$.

(b) Show that $|\zeta(1+it)| = O(\log |t|)$ as $|t| \to \infty$ by using the previous result with $N = \lfloor |t| \rfloor$.

(c) Show that $|\zeta'(1+it)| = O((\log |t|)^2)$ as $|t| \to \infty$.

(d) Show that if $t \neq 0$ and $t$ is fixed, then the partial sums of the series $\sum_{n=1}^\infty n^{-1-it}$ are bounded, but the series does not converge.

2. Prove that for $\operatorname{Re}(s) > 0$,
$$
\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx,
$$
where $\{x\} = x - \lfloor x \rfloor$ is the fractional part of $x$.

3. If $Q(x) = \{x\} - 1/2$, then we can write the expression in the previous problem as
$$
\zeta(s) = \frac{s}{s-1} - \frac{1}{2} - s \int_1^\infty \frac{Q(x)}{x^{s+1}}\,dx.
$$
Let us construct $Q_k(x)$ recursively so that
$$
\int_0^1 Q_k(x)\,dx = 0, \quad \frac{dQ_{k+1}}{dx} = Q_k(x), \quad Q_0(x) = Q(x), \quad \text{and} \quad Q_k(x+1) = Q_k(x).
$$
Then prove that for $\operatorname{Re}(s) > -k$,
$$
\zeta(s) = \frac{s}{s-1} - \frac{1}{2} - \frac{s(s+1)\cdots(s+k)}{k!} \int_1^\infty \frac{Q_k(x)}{x^{s+k+1}}\,dx.
$$
:::

::: solution
**Goal:** Establish asymptotic bounds for $\zeta(s)$ and $\zeta'(s)$ near $\Re(s)=1$ and integral representations yielding its meromorphic continuation.

<1>1. Part 1(a): Expansion for $\zeta(s)$ with truncation parameter $N$.
    ::: {.proof}
    <2>1. For $\Re(s) > 1$, the Dirichlet series converges absolutely:
    $$\zeta(s) = \sum_{n=1}^\infty n^{-s} = \sum_{n=1}^{N-1} n^{-s} + \sum_{n=N}^\infty n^{-s}.$$
    <2>2. For each $n \ge N$, write $n^{-s} = \int_n^{n+1} x^{-s}\,dx + \delta_n(s)$, where $\delta_n(s) = \int_n^{n+1} (n^{-s} - x^{-s})\,dx$.
    <2>3. Summing the integral terms gives
    $$\sum_{n=N}^\infty \int_n^{n+1} x^{-s}\,dx = \int_N^\infty x^{-s}\,dx = \left[ \frac{x^{1-s}}{1-s} \right]_N^\infty = \frac{N^{1-s}}{s-1},$$
    which converges for $\Re(s) > 1$.
    <2>4. Thus for $\Re(s) > 1$,
    $$\zeta(s) = \sum_{1 \le n < N} n^{-s} + \frac{N^{1-s}}{s-1} + \sum_{n \ge N} \delta_n(s).$$
    <2>5. By the Mean Value Theorem applied to $f(x) = x^{-s}$ on $[n, n+1]$, $|n^{-s} - x^{-s}| \le |s| n^{-\Re(s)-1}$, so
    $$|\delta_n(s)| \le |s| n^{-\Re(s)-1}.$$
    The series $\sum_{n \ge N} \delta_n(s)$ converges locally uniformly for $\Re(s) > 0$, defining a holomorphic function on $\Re(s) > 0$.
    <2>6. By analytic continuation, the identity holds for all $\Re(s) > 0$ with $s \neq 1$.

:::
<1>2. Part 1(b): Bound $|\zeta(1+it)| = O(\log |t|)$ as $|t| \to \infty$.
    ::: {.proof}
    <2>1. Set $s = 1+it$ with $|t| \ge 2$, and choose $N = \lfloor |t| \rfloor \ge 2$.
    <2>2. In the expansion from <1>1:
    $$\left| \sum_{1 \le n < N} n^{-1-it} \right| \le \sum_{n=1}^{N-1} \frac{1}{n} \le 1 + \int_1^N \frac{dx}{x} = 1 + \log N \le 1 + \log |t|.$$
    <2>3. For the pole term:
    $$\left| \frac{N^{1-s}}{s-1} \right| = \left| \frac{N^{-it}}{it} \right| = \frac{1}{|t|} \le \frac{1}{2} = O(1).$$
    <2>4. For the tail: using $|\delta_n(1+it)| \le |1+it| n^{-2} \le (1+|t|) n^{-2}$,
    $$\left| \sum_{n=N}^\infty \delta_n(1+it) \right| \le (1+|t|) \sum_{n=N}^\infty \frac{1}{n^2} \le (1+|t|) \frac{1}{N-1} \le \frac{1+|t|}{|t|-1} \le 3 = O(1).$$
    <2>5. Summing the three bounds gives $|\zeta(1+it)| \le \log |t| + O(1) = O(\log |t|)$.

:::
<1>3. Part 1(c): Bound $|\zeta'(1+it)| = O((\log |t|)^2)$ as $|t| \to \infty$.
    ::: {.proof}
    <2>1. Differentiating the identity from <1>1 with respect to $s$:
    $$\zeta'(s) = -\sum_{1 \le n < N} n^{-s} \log n - \frac{N^{1-s} \log N}{s-1} - \frac{N^{1-s}}{(s-1)^2} + \sum_{n=N}^\infty \delta_n'(s).$$
    <2>2. At $s = 1+it$ with $N = \lfloor |t| \rfloor$:
    $$\left| \sum_{1 \le n < N} n^{-1-it} \log n \right| \le \sum_{n=1}^{N-1} \frac{\log n}{n} \le \int_1^N \frac{\log x}{x}\,dx + O(1) = \frac{1}{2} (\log N)^2 + O(1) \le \frac{1}{2}(\log |t|)^2 + O(1).$$
    <2>3. The terms involving $N^{1-s}$ satisfy
    $$\left| \frac{N^{-it} \log N}{it} \right| = \frac{\log N}{|t|} = O(1), \qquad \left| \frac{N^{-it}}{(it)^2} \right| = \frac{1}{|t|^2} = O(1).$$
    <2>4. Differentiating $\delta_n(s) = \int_n^{n+1} (n^{-s} - x^{-s})\,dx$ gives $|\delta_n'(1+it)| \le C |t| \frac{\log n}{n^2}$, so
    $$\left| \sum_{n=N}^\infty \delta_n'(1+it) \right| \le C |t| \sum_{n=N}^\infty \frac{\log n}{n^2} = O\left(|t| \frac{\log N}{N}\right) = O(\log |t|).$$
    <2>5. Therefore $|\zeta'(1+it)| = O((\log |t|)^2)$.

:::
<1>4. Part 1(d): Partial sums are bounded but do not converge for $t \neq 0$.
    ::: {.proof}
    <2>1. Let $S_m(t) = \sum_{n=1}^m n^{-1-it}$. Applying <1>1 with $s = 1+it$ and $N = m+1$:
    $$S_m(t) = \zeta(1+it) - \frac{(m+1)^{-it}}{it} - \sum_{n=m+1}^\infty \delta_n(1+it).$$
    <2>2. The tail satisfies $\left| \sum_{n=m+1}^\infty \delta_n(1+it) \right| \le (1+|t|) \frac{1}{m} \le 1+|t|$ for all $m \ge 1$.
    <2>3. Since $|\zeta(1+it)|$ is a constant for fixed $t$, and $|(m+1)^{-it}/(it)| = 1/|t|$ is constant, $|S_m(t)| \le |\zeta(1+it)| + \frac{1}{|t|} + (1+|t|)$ is uniformly bounded in $m$.
    <2>4. If $S_m(t)$ converged to $\zeta(1+it)$ as $m \to \infty$, then $(m+1)^{-it} = e^{-it \log(m+1)}$ would converge as $m \to \infty$. But for $t \neq 0$, the sequence $e^{-it \log(m+1)}$ oscillates around the unit circle and has no limit.
    <2>5. Hence the series $\sum_{n=1}^\infty n^{-1-it}$ diverges.

:::
<1>5. Part 2: First integral representation via fractional part.
    ::: {.proof}
    <2>1. For $\Re(s) > 1$ and $M \in \mathbb{N}$, apply Abel summation (integration by parts):
    $$\sum_{n=1}^M n^{-s} = \int_{1^-}^M x^{-s}\,d\lfloor x \rfloor = \frac{\lfloor M \rfloor}{M^s} + s \int_1^M \frac{\lfloor x \rfloor}{x^{s+1}}\,dx = M^{1-s} + s \int_1^M \frac{x - \{x\}}{x^{s+1}}\,dx.$$
    <2>2. Split the integral:
    $$s \int_1^M \frac{x}{x^{s+1}}\,dx = s \int_1^M x^{-s}\,dx = s \left[ \frac{x^{1-s}}{1-s} \right]_1^M = \frac{s}{s-1} (1 - M^{1-s}).$$
    <2>3. Thus
    $$\sum_{n=1}^M n^{-s} = \frac{s}{s-1} + M^{1-s} \left(1 - \frac{s}{s-1}\right) - s \int_1^M \frac{\{x\}}{x^{s+1}}\,dx = \frac{s}{s-1} - \frac{M^{1-s}}{s-1} - s \int_1^M \frac{\{x\}}{x^{s+1}}\,dx.$$
    <2>4. For $\Re(s) > 1$, as $M \to \infty$, $|M^{1-s}| = M^{1-\Re(s)} \to 0$.
    <2>5. Because $0 \le \{x\} < 1$, the integral $\int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx$ converges absolutely and uniformly on compact subsets of $\Re(s) > 0$.
    <2>6. Taking $M \to \infty$ gives $\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx$ for $\Re(s) > 1$, and by analytic continuation this holds for all $\Re(s) > 0$ with $s \neq 1$.

:::
<1>6. Part 3: Recursive periodic refinement.
    ::: {.proof}
    <2>1. Substitute $\{x\} = Q(x) + 1/2$ into Part 2:
    $$\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{1/2}{x^{s+1}}\,dx - s \int_1^\infty \frac{Q(x)}{x^{s+1}}\,dx = \frac{s}{s-1} - \frac{1}{2} - s \int_1^\infty \frac{Q(x)}{x^{s+1}}\,dx.$$
    <2>2. For $k \ge 1$, the function $Q_k(x)$ is periodic with period 1 and continuous on $\mathbb{R}$ with $Q_k(0) = Q_k(1) = 0$ (since $\int_0^1 Q_{k-1} = 0$).
    <2>3. Integrating by parts repeatedly using $Q_j(x) = \frac{d}{dx} Q_{j+1}(x)$ and $\frac{d}{dx} x^{-(s+j+1)} = -(s+j+1) x^{-(s+j+2)}$:
    $$\int_1^\infty \frac{Q_j(x)}{x^{s+j+1}}\,dx = \left[ \frac{Q_{j+1}(x)}{x^{s+j+1}} \right]_1^\infty + (s+j+1) \int_1^\infty \frac{Q_{j+1}(x)}{x^{s+j+2}}\,dx.$$
    <2>4. The boundary terms vanish at $\infty$ (for $\Re(s) > -j$) and at $x=1$ because $Q_{j+1}(1) = 0$.
    <2>5. By induction on $k$, for $\Re(s) > -k$:
    $$\zeta(s) = \frac{s}{s-1} - \frac{1}{2} - s(s+1)\cdots(s+k) \int_1^\infty \frac{Q_k(x)}{x^{s+k+1}}\,dx.$$
    This gives the analytic continuation of $\zeta(s)$ to $\Re(s) > -k$.
:::
:::
