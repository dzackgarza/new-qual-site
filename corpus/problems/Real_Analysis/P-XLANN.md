---
schema: qual/card@1
id: P-XLANN
kind: problem
title: $\|g\|_p\to\|g\|_\infty$ as $p\to\infty$ on $[0,1]$, and $\|\Lambda_g\|_{(L^1)^*}=\|g\|_\infty$
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

::: problem
Let $g \in L^\infty([0, 1])$.

(a) Prove that
$$
\lim_{p \to \infty} \|g\|_{L^p([0, 1])} = \|g\|_{L^\infty([0, 1])}.
$$

(b) Prove that the map
$$
\Lambda_g: L^1([0, 1]) \to \mathbb{C}, \qquad f \mapsto \int_0^1 f(x) g(x) \, dx
$$
defines a continuous linear functional in $(L^1([0, 1]))^*$ with $\|\Lambda_g\|_{(L^1)^*} = \|g\|_{L^\infty([0, 1])}$.
:::

::: solution
**Goal:** Prove the $L^p \to L^\infty$ norm limit as $p \to \infty$ on $[0, 1]$ in (a), and compute the operator norm $\|\Lambda_g\|_{(L^1)^*} = \|g\|_{L^\infty}$ in (b).

<1>1. Part (a): Upper bound $\limsup_{p \to \infty} \|g\|_{L^p} \le \|g\|_{L^\infty}$.
::: {.proof}
<2>1. For almost every $x \in [0, 1]$, $|g(x)| \le \|g\|_{L^\infty}$.
<2>2. Integrating over $[0, 1]$ for any $p \ge 1$:
$$\|g\|_{L^p} = \left( \int_0^1 |g(x)|^p \, dx \right)^{1/p} \le \left( \int_0^1 \|g\|_{L^\infty}^p \, dx \right)^{1/p} = \|g\|_{L^\infty} (m([0, 1]))^{1/p} = \|g\|_{L^\infty} (1)^{1/p} = \|g\|_{L^\infty}.$$
<2>3. Taking the limit superior as $p \to \infty$:
$$\limsup_{p \to \infty} \|g\|_{L^p} \le \|g\|_{L^\infty}.$$
:::

<1>2. Part (a): Lower bound $\liminf_{p \to \infty} \|g\|_{L^p} \ge \|g\|_{L^\infty}$.
::: {.proof}
<2>1. If $\|g\|_{L^\infty} = 0$, then $g = 0$ almost everywhere, so $\|g\|_{L^p} = 0$ for all $p$ and the limit is $0$.
<2>2. Assume $\|g\|_{L^\infty} > 0$. For any $0 < M < \|g\|_{L^\infty}$, define the superlevel set $E_M = \{x \in [0, 1] : |g(x)| > M\}$.
<2>3. By definition of the essential supremum, $m(E_M) > 0$.
<2>4. Restricting the $L^p$ integral to $E_M$:
$$\|g\|_{L^p} = \left( \int_0^1 |g(x)|^p \, dx \right)^{1/p} \ge \left( \int_{E_M} |g(x)|^p \, dx \right)^{1/p} \ge \left( \int_{E_M} M^p \, dx \right)^{1/p} = M (m(E_M))^{1/p}.$$
<2>5. Since $m(E_M) \in (0, 1]$, $(m(E_M))^{1/p} \to 1$ as $p \to \infty$.
<2>6. Thus $\liminf_{p \to \infty} \|g\|_{L^p} \ge M \lim_{p \to \infty} (m(E_M))^{1/p} = M$.
<2>7. Taking the supremum over all $M < \|g\|_{L^\infty}$ yields $\liminf_{p \to \infty} \|g\|_{L^p} \ge \|g\|_{L^\infty}$.
:::

<1>3. Part (a): Conclusion of the limit.
::: {.proof}
Combining <1>1 and <1>2 gives $\lim_{p \to \infty} \|g\|_{L^p} = \|g\|_{L^\infty}$.
:::

<1>4. Part (b): Well-definedness and upper bound $\|\Lambda_g\| \le \|g\|_{L^\infty}$.
::: {.proof}
<2>1. Linearity of $\Lambda_g$ follows directly from linearity of the Lebesgue integral.
<2>2. For any $f \in L^1([0, 1])$:
$$|\Lambda_g(f)| = \left| \int_0^1 f(x) g(x) \, dx \right| \le \int_0^1 |f(x)| |g(x)| \, dx \le \|g\|_{L^\infty} \int_0^1 |f(x)| \, dx = \|g\|_{L^\infty} \|f\|_{L^1}.$$
<2>3. Therefore $\Lambda_g$ is a bounded linear functional on $L^1([0, 1])$ with operator norm
$$\|\Lambda_g\|_{(L^1)^*} = \sup_{f \neq 0} \frac{|\Lambda_g(f)|}{\|f\|_{L^1}} \le \|g\|_{L^\infty}.$$
:::

<1>5. Part (b): Lower bound $\|\Lambda_g\| \ge \|g\|_{L^\infty}$.
::: {.proof}
<2>1. If $\|g\|_{L^\infty} = 0$, then $\|\Lambda_g\| = 0 = \|g\|_{L^\infty}$.
<2>2. Assume $\|g\|_{L^\infty} > 0$. Fix $0 < M < \|g\|_{L^\infty}$ and let $E = \{x \in [0, 1] : |g(x)| \ge M\}$, so $m(E) > 0$.
<2>3. Define test function $f(x) \in L^1([0, 1])$ by:
$$f(x) = \frac{\overline{\operatorname{sgn}(g(x))}}{m(E)} \mathbf{1}_E(x) = \begin{cases} \frac{\overline{g(x)}}{|g(x)| m(E)} & x \in E \text{ and } g(x) \neq 0, \\ 0 & \text{otherwise.} \end{cases}$$
<2>4. Compute the $L^1$ norm of $f$:
$$\|f\|_{L^1} = \int_E \frac{1}{m(E)} \, dx = \frac{m(E)}{m(E)} = 1.$$
<2>5. Evaluate $\Lambda_g(f)$:
$$\Lambda_g(f) = \int_0^1 f(x) g(x) \, dx = \frac{1}{m(E)} \int_E \frac{\overline{g(x)} g(x)}{|g(x)|} \, dx = \frac{1}{m(E)} \int_E |g(x)| \, dx \ge \frac{1}{m(E)} \int_E M \, dx = M.$$
<2>6. Since $\|f\|_{L^1} = 1$, the operator norm satisfies $\|\Lambda_g\| \ge |\Lambda_g(f)| \ge M$.
<2>7. Since this holds for all $M < \|g\|_{L^\infty}$, we conclude $\|\Lambda_g\|_{(L^1)^*} \ge \|g\|_{L^\infty}$.
:::

<1>6. Conclusion:
::: {.proof}
Combining <1>4 and <1>5 yields $\|\Lambda_g\|_{(L^1)^*} = \|g\|_{L^\infty}$.
:::
