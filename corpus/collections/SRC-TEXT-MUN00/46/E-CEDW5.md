---
schema: qual/card@1
id: E-CEDW5
kind: problem
title: Power series partial sums converge compactly but not uniformly
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Consider the sequence of functions $f_n: (-1, 1) \to \mathbb{R}$, defined by

$$
f_n(x) = \sum_{k=1}^{n} k x^k.
$$

(a) Show that $(f_n)$ converges in the topology of compact convergence; conclude that the limit function is continuous.
(This is a standard fact about power series.)

(b) Show that $(f_n)$ does not converge in the uniform topology.
:::

::: {.solution}
<1>1. Part (a): Convergence in the topology of compact convergence:
<2>1. For each $x \in (-1, 1)$, the power series converges pointwise to:
\[
f(x) = \sum_{k=1}^\infty k x^k = x \sum_{k=1}^\infty k x^{k-1} = x \frac{d}{dx}\left(\frac{1}{1-x}\right) = \frac{x}{(1-x)^2}.
\]
::: {.proof}
derivative of geometric series for $|x| < 1$.
:::
<2>2. Let $K \subseteq (-1, 1)$ be a compact subset.
Since $K$ is bounded and closed in $(-1, 1)$, there exists $r \in [0, 1)$ such that $K \subseteq [-r, r]$.
::: {.proof}
$r = \sup_{x \in K} |x| < 1$ by compactness of $K$.
:::
<2>3. For any $x \in K$, we estimate the remainder of the series:
\[
|f(x) - f_n(x)| = \left| \sum_{k=n+1}^\infty k x^k \right| \le \sum_{k=n+1}^\infty k |x|^k \le \sum_{k=n+1}^\infty k r^k.
\]
::: {.proof}
triangle inequality for infinite series.
:::
<2>4. The numerical series $\sum_{k=1}^\infty k r^k$ converges by the Ratio Test ($\lim_{k \to \infty} \frac{(k+1)r^{k+1}}{k r^k} = r < 1$).
Thus the tail sum satisfies $\lim_{n \to \infty} \sum_{k=n+1}^\infty k r^k = 0$, so:
\[
\sup_{x \in K} |f(x) - f_n(x)| \le \sum_{k=n+1}^\infty k r^k \to 0 \quad \text{as } n \to \infty.
\]
Thus $(f_n)$ converges to $f$ uniformly on every compact subset $K \subset (-1, 1)$ (i.e. in the topology of compact convergence).
::: {.proof}
Weierstrass $M$-test on compact sets.
:::
<2>5. Since each partial sum $f_n(x)$ is a polynomial (hence continuous) and $f_n \to f$ compactly, the limit $f$ is continuous on $(-1, 1)$.
::: {.proof}
Uniform Limit Theorem for compact convergence.
:::

<1>2. Part (b): Non-convergence in the uniform topology:
<2>1. Convergence in the uniform topology on $(-1, 1)$ requires that $\sup_{x \in (-1, 1)} |f(x) - f_n(x)| \to 0$ as $n \to \infty$.
::: {.proof}
definition of uniform metric $d_u(f, g) = \sup |f - g|$.
:::
<2>2. For any fixed $n \ge 1$ and $x \in (0, 1)$:
\[
f(x) - f_n(x) = \frac{x}{(1 - x)^2} - \sum_{k=1}^n k x^k.
\]
As $x \to 1^-$, $\sum_{k=1}^n k x^k \to \sum_{k=1}^n k = \frac{n(n+1)}{2} < \infty$, while $\lim_{x \to 1^-} \frac{x}{(1 - x)^2} = +\infty$.
::: {.proof}
divergence of $\frac{1}{(1-x)^2}$ at the boundary $x = 1$.
:::
<2>3. Therefore, for every $n \ge 1$:
\[
\sup_{x \in (-1, 1)} |f(x) - f_n(x)| = +\infty.
\]
Thus $(f_n)$ does not converge to $f$ uniformly on $(-1, 1)$, and cannot converge to any function in the uniform topology.
::: {.proof}
infinite uniform distance for all $n$.
:::

<1>3. Conclusion:
$(f_n)$ converges in the topology of compact convergence to the continuous function $f(x) = \frac{x}{(1-x)^2}$, but does not converge in the uniform topology. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
