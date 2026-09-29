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

::: pf

::: {.pf-step #f-is-true}
(f) is true.

::: pf-proof

::: pf-step
On each $[\eps, 1]$, Riemann integrability of the nonnegative $f$ gives Lebesgue integrability there, with equal integrals.

::: pf-proof
A bounded Riemann integrable function on a compact interval is Lebesgue integrable and the two integrals agree; here $f$ is Riemann integrable on $[\eps,1]$ by hypothesis.
:::

:::

::: {.pf-step #decreasing-sets-exhaust}
For a decreasing sequence $\eps_k \to 0^+$, the functions $f \chi_{[\eps_k, 1]}$ increase pointwise to $f \chi_{(0,1]}$.

::: pf-proof
As $\eps_k$ decreases, the sets $[\eps_k, 1]$ increase and exhaust $(0,1]$.
:::

:::

::: {.pf-step #monotone-convergence-integral}
Monotone convergence: $\int_{(0,1]} f = \lim_k \int_{\eps_k}^1 f = \lim_{\eps \to 0^+} \int_\eps^1 f < \infty$.

::: pf-proof
Monotone convergence applied to step [](#decreasing-sets-exhaust){.pf-ref}, using that the limit in the hypothesis exists and is finite; the point $\theset{0}$ has measure zero.
:::

:::

::: {.pf-step #f-lebesgue-integrable}
Hence $f$ is Lebesgue integrable on $[0,1]$.

::: pf-proof
By step [](#monotone-convergence-integral){.pf-ref} the Lebesgue integral of the nonnegative measurable function $f$ over $[0,1]$ is finite.
:::

:::

:::

::: pf-qed
By step [](#f-lebesgue-integrable){.pf-ref}.
:::

:::

::: {.pf-step #g-is-true}
(g) is true: the Riemann–Lebesgue lemma.

::: pf-proof

::: {.pf-step #dense-subspace-suffices}
If the claim holds for every $f$ in a dense subspace of $L^1[0,1]$, it holds for every $f \in L^1[0,1]$.

::: pf-proof
The map $f \mapsto \int_0^1 f(x) \sin(n\pi x) ~dx$ is bounded linear on $L^1[0,1]$ with norm $\leq 1$, so if the claim holds on a dense subspace it holds everywhere by a $3\eps$ argument.
:::

:::

::: {.pf-step #indicator-case}
For an indicator $f = \chi_{[a,b]}$, $\int_0^1 f(x) \sin(n\pi x) ~dx = \frac{\cos(n\pi a) - \cos(n\pi b)}{n\pi} \to 0$.

::: pf-proof
Direct antiderivative computation: $\int_a^b \sin(n\pi x) ~dx = \frac{-\cos(n\pi x)}{n\pi}\big|_a^b$.
:::

:::

::: {.pf-step #step-function-case}
By linearity, the claim holds for every step function.

::: pf-proof
Step functions are finite linear combinations of indicators, and step [](#indicator-case){.pf-ref} handles each.
:::

:::

::: {.pf-step #step-functions-dense}
Step functions are dense in $L^1[0,1]$.

::: pf-proof
Simple functions are dense in $L^1[0,1]$, and by regularity of Lebesgue measure each indicator of a measurable set is an $L^1$-limit of indicators of finite unions of intervals.
:::

:::

:::

::: pf-qed
Combine steps [](#dense-subspace-suffices){.pf-ref}, [](#step-function-case){.pf-ref}, and [](#step-functions-dense){.pf-ref}.
:::

:::

::: {.pf-step #h-is-false}
(h) is false.

::: pf-proof

::: {.pf-step #f-defined}
Let $f(x) \definedas x \sin(1/x)$ for $x \in (0,1]$, with $f(0) \definedas 0$.

::: pf-proof
This defines a function on $[0,1]$; continuity at $0$ follows from $\abs{x\sin(1/x)} \leq x \to 0$.
:::

:::

::: {.pf-step #f-continuous}
$f$ is continuous on $[0,1]$.

::: pf-proof
$x \mapsto x \sin(1/x)$ is continuous on $(0,1]$ as a composition of continuous functions, and step [](#f-defined){.pf-ref} gives continuity at $0$.
:::

:::

::: {.pf-step #f-not-bounded-variation}
$f$ is not of bounded variation.

::: pf-proof
Take the partition points $x_k = \frac{2}{(2k+1)\pi}$; then $f(x_k) = (-1)^k x_k$, so $\abs{f(x_k) - f(x_{k+1})} = x_k + x_{k+1} \geq x_k = \frac{2}{(2k+1)\pi}$. The sum $\sum_k \frac{2}{(2k+1)\pi}$ diverges by comparison with the harmonic series, so the variations over the partitions $\{0, x_N, \ldots, x_1, x_0, 1\}$ are unbounded and the total variation is infinite.
:::

:::

:::

::: pf-qed
By steps [](#f-continuous){.pf-ref} and [](#f-not-bounded-variation){.pf-ref}, $f$ is continuous on $[0,1]$ and not of bounded variation, so (h) is false.
:::

:::

::: pf-qed
Conclusion: (f) and (g) are true; (h) is false.

By steps [](#f-is-true){.pf-ref}, [](#g-is-true){.pf-ref}, and [](#h-is-false){.pf-ref}.
:::

:::
