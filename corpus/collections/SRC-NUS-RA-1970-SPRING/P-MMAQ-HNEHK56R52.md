---
schema: qual/card@1
id: P-MMAQ-HNEHK56R52
kind: problem
title: Improper nonnegative Riemann integrals in $L^1$, the Riemann–Lebesgue lemma,
  and continuous functions of unbounded variation
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Convergence of Functions
  - L¹
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove or disprove each of the following statements.

(f) If $f$ is Riemann integrable on $[\eps, 1]$ for all $0 < \eps < 1$, then $f$ is Lebesgue integrable on $[0,1]$ if $f$ is nonnegative and the following limit exists $\lim_{\varepsilon\to 0^+} \int_\varepsilon^1 f dx$.

(g) If $f$ is integrable on $[0,1]$, then $\lim_{n\to\infty} \int_0^1 f(x)\sin(n\pi x)dx = 0$.

(h) If $f$ is continuous on $[0, 1]$, then it is of bounded variation on $[0, 1]$.
:::

::: {.solution}
<1>1. (f) is true.
<2>1. On each $[\eps, 1]$, Riemann integrability of the nonnegative $f$ gives Lebesgue integrability there, with equal integrals.
::: {.proof}
A bounded Riemann integrable function on a compact interval is Lebesgue integrable and the two integrals agree; here $f$ is Riemann integrable on $[\eps,1]$ by hypothesis.
:::
<2>2. For a decreasing sequence $\eps_k \to 0^+$, the functions $f \chi_{[\eps_k, 1]}$ increase pointwise to $f \chi_{(0,1]}$.
::: {.proof}
As $\eps_k$ decreases, the sets $[\eps_k, 1]$ increase and exhaust $(0,1]$.
:::
<2>3. Monotone convergence: $\int_{(0,1]} f = \lim_k \int_{\eps_k}^1 f = \lim_{\eps \to 0^+} \int_\eps^1 f < \infty$.
::: {.proof}
Monotone convergence applied to <2>2, using that the limit in the hypothesis exists and is finite; the point $\theset{0}$ has measure zero.
:::
<2>4. Hence $f$ is Lebesgue integrable on $[0,1]$.
::: {.proof}
By <2>3 the Lebesgue integral of the nonnegative measurable function $f$ over $[0,1]$ is finite.
:::
<2>5. Q.E.D.
::: {.proof}
By <2>4.
:::

<1>2. (g) is true: the Riemann–Lebesgue lemma.
<2>1. If the claim holds for every $f$ in a dense subspace of $L^1[0,1]$, it holds for every $f \in L^1[0,1]$.
::: {.proof}
The map $f \mapsto \int_0^1 f(x) \sin(n\pi x) ~dx$ is bounded linear on $L^1[0,1]$ with norm $\leq 1$, so if the claim holds on a dense subspace it holds everywhere by a $3\eps$ argument.
:::
<2>2. For an indicator $f = \chi_{[a,b]}$, $\int_0^1 f(x) \sin(n\pi x) ~dx = \frac{\cos(n\pi a) - \cos(n\pi b)}{n\pi} \to 0$.
::: {.proof}
Direct antiderivative computation: $\int_a^b \sin(n\pi x) ~dx = \frac{-\cos(n\pi x)}{n\pi}\big|_a^b$.
:::
<2>3. By linearity, the claim holds for every step function.
::: {.proof}
Step functions are finite linear combinations of indicators, and <2>2 handles each.
:::
<2>4. Step functions are dense in $L^1[0,1]$.
::: {.proof}
Simple functions are dense in $L^1[0,1]$, and by regularity of Lebesgue measure each indicator of a measurable set is an $L^1$-limit of indicators of finite unions of intervals.
:::
<2>5. Q.E.D.
::: {.proof}
Combine <2>1, <2>3, <2>4.
:::

<1>3. (h) is false.
<2>1. Let $f(x) \definedas x \sin(1/x)$ for $x \in (0,1]$, with $f(0) \definedas 0$.
::: {.proof}
This defines a function on $[0,1]$; continuity at $0$ follows from $\abs{x\sin(1/x)} \leq x \to 0$.
:::
<2>2. $f$ is continuous on $[0,1]$.
::: {.proof}
$x \mapsto x \sin(1/x)$ is continuous on $(0,1]$ as a composition of continuous functions, and <2>1 gives continuity at $0$.
:::
<2>3. $f$ is not of bounded variation.
::: {.proof}
Take the partition points $x_k = \frac{2}{(2k+1)\pi}$; then $f(x_k) = (-1)^k x_k$, so $\abs{f(x_k) - f(x_{k+1})} = x_k + x_{k+1} \geq x_k = \frac{2}{(2k+1)\pi}$. The sum $\sum_k \frac{2}{(2k+1)\pi}$ diverges by comparison with the harmonic series, so the variations over the partitions $\{0, x_N, \ldots, x_1, x_0, 1\}$ are unbounded and the total variation is infinite.
:::
<2>4. Q.E.D.
::: {.proof}
By <2>2 and <2>3, $f$ is continuous on $[0,1]$ and not of bounded variation, so (h) is false.
:::

<1>4. Conclusion: (f) and (g) are true; (h) is false.
::: {.proof}
By <1>1, <1>2, and <1>3.
:::
:::
