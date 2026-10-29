---
schema: qual/card@1
id: P-XLANN
kind: problem
title: $\norm{g}_p\to\norm{g}_\infty$ as $p\to\infty$ on $[0,1]$, and $\norm{\Lambda_g}_{(L^1)^*}=\norm{g}_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - L∞
  - Lp Spaces
  - Riesz Representation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}

Let $g \in L^\infty([0, 1])$.

(a) Prove that
$$
\lim_{p \to \infty} \norm{g}_{L^p([0, 1])} = \norm{g}_{L^\infty([0, 1])}.
$$

(b) Prove that the map
$$
\Lambda_g: L^1([0, 1]) \to \CC, \qquad f \mapsto \int_0^1 f(x) g(x) \, dx
$$
defines a continuous linear functional in $(L^1([0, 1]))^*$ with $\norm{\Lambda_g}_{(L^1)^*} = \norm{g}_{L^\infty([0, 1])}$.

:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) Upper bound: $\limsup_{p \to \infty} \norm{g}_{L^p} \le \norm{g}_{L^\infty}$.

::: pf-proof

::: pf-step

For almost every $x \in [0, 1]$, $|g(x)| \le \norm{g}_{L^\infty}$.

:::

::: pf-step

Integrating over $[0, 1]$ for any $p \ge 1$:
$$\norm{g}_{L^p} = \left( \int_0^1 |g(x)|^p \, dx \right)^{1/p} \le \left( \int_0^1 \norm{g}_{L^\infty}^p \, dx \right)^{1/p} = \norm{g}_{L^\infty} (m([0, 1]))^{1/p} = \norm{g}_{L^\infty} (1)^{1/p} = \norm{g}_{L^\infty}.$$

:::

::: pf-step

Taking the limit superior as $p \to \infty$:
$$\limsup_{p \to \infty} \norm{g}_{L^p} \le \norm{g}_{L^\infty}.$$

:::

:::

:::

::: {.pf-step #s2}

(a) Lower bound: $\liminf_{p \to \infty} \norm{g}_{L^p} \ge \norm{g}_{L^\infty}$.

::: pf-proof

::: pf-step

If $\norm{g}_{L^\infty} = 0$, then $g = 0$ almost everywhere, so $\norm{g}_{L^p} = 0$ for all $p$ and the limit is $0$.

:::

::: pf-step

Assume $\norm{g}_{L^\infty} > 0$. For any $0 < M < \norm{g}_{L^\infty}$, define the superlevel set $E_M = \{x \in [0, 1] : |g(x)| > M\}$.

:::

::: pf-step

By definition of the essential supremum, $m(E_M) > 0$.

:::

::: pf-step

Restricting the $L^p$ integral to $E_M$:
$$\norm{g}_{L^p} = \left( \int_0^1 |g(x)|^p \, dx \right)^{1/p} \ge \left( \int_{E_M} |g(x)|^p \, dx \right)^{1/p} \ge \left( \int_{E_M} M^p \, dx \right)^{1/p} = M (m(E_M))^{1/p}.$$

:::

::: pf-step

Since $m(E_M) \in (0, 1]$, $(m(E_M))^{1/p} \to 1$ as $p \to \infty$.

:::

::: pf-step

Thus $\liminf_{p \to \infty} \norm{g}_{L^p} \ge M \lim_{p \to \infty} (m(E_M))^{1/p} = M$.

:::

::: pf-step

Taking the supremum over all $M < \norm{g}_{L^\infty}$ yields $\liminf_{p \to \infty} \norm{g}_{L^p} \ge \norm{g}_{L^\infty}$.

:::

:::

:::

::: pf-step

(a) $\lim_{p \to \infty} \norm{g}_{L^p} = \norm{g}_{L^\infty}$.

::: pf-proof

Combining step [](#s1){.pf-ref} and step [](#s2){.pf-ref} gives $\lim_{p \to \infty} \norm{g}_{L^p} = \norm{g}_{L^\infty}$.

:::

:::

::: {.pf-step #s4}

(b) $\Lambda_g$ is linear and $\norm{\Lambda_g} \le \norm{g}_{L^\infty}$.

::: pf-proof

::: pf-step

Linearity of $\Lambda_g$ follows directly from linearity of the Lebesgue integral.

:::

::: pf-step

For any $f \in L^1([0, 1])$:
$$|\Lambda_g(f)| = \left| \int_0^1 f(x) g(x) \, dx \right| \le \int_0^1 |f(x)| |g(x)| \, dx \le \norm{g}_{L^\infty} \int_0^1 |f(x)| \, dx = \norm{g}_{L^\infty} \norm{f}_{L^1}.$$

:::

::: pf-step

Therefore $\Lambda_g$ is a bounded linear functional on $L^1([0, 1])$ with operator norm
$$\norm{\Lambda_g}_{(L^1)^*} = \sup_{f \neq 0} \frac{|\Lambda_g(f)|}{\norm{f}_{L^1}} \le \norm{g}_{L^\infty}.$$

:::

:::

:::

::: {.pf-step #s5}

(b) Lower bound: $\norm{\Lambda_g} \ge \norm{g}_{L^\infty}$.

::: pf-proof

::: pf-step

If $\norm{g}_{L^\infty} = 0$, then $\norm{\Lambda_g} = 0 = \norm{g}_{L^\infty}$.

:::

::: pf-step

Assume $\norm{g}_{L^\infty} > 0$. Fix $0 < M < \norm{g}_{L^\infty}$ and let $E = \{x \in [0, 1] : |g(x)| \ge M\}$, so $m(E) > 0$.

:::

::: pf-step

Define the test function $f \in L^1([0, 1])$ by
$$f(x) = \frac{\overline{\operatorname{sgn}(g(x))}}{m(E)} \mathbf{1}_E(x) = \begin{cases} \frac{\overline{g(x)}}{|g(x)| m(E)} & x \in E \text{ and } g(x) \neq 0, \\ 0 & \text{otherwise.} \end{cases}$$

:::

::: pf-step

Compute the $L^1$ norm of $f$:
$$\norm{f}_{L^1} = \int_E \frac{1}{m(E)} \, dx = \frac{m(E)}{m(E)} = 1.$$

:::

::: pf-step

Evaluate $\Lambda_g(f)$:
$$\Lambda_g(f) = \int_0^1 f(x) g(x) \, dx = \frac{1}{m(E)} \int_E \frac{\overline{g(x)} g(x)}{|g(x)|} \, dx = \frac{1}{m(E)} \int_E |g(x)| \, dx \ge \frac{1}{m(E)} \int_E M \, dx = M.$$

:::

::: pf-step

Since $\norm{f}_{L^1} = 1$, the operator norm satisfies $\norm{\Lambda_g} \ge |\Lambda_g(f)| \ge M$.

:::

::: pf-step

Since this holds for all $M < \norm{g}_{L^\infty}$, we conclude $\norm{\Lambda_g}_{(L^1)^*} \ge \norm{g}_{L^\infty}$.

:::

:::

:::

::: pf-step

(b) $\norm{\Lambda_g}_{(L^1)^*} = \norm{g}_{L^\infty}$.

::: pf-proof

Combining step [](#s4){.pf-ref} and step [](#s5){.pf-ref} yields $\norm{\Lambda_g}_{(L^1)^*} = \norm{g}_{L^\infty}$.

:::

:::

:::

:::

