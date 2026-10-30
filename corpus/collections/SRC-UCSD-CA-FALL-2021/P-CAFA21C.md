---
schema: qual/card@1
id: P-CAFA21C
kind: problem
title: "Entire function satisfying a quadratic equation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $a, b : \CC \to \CC$ be entire functions.
Let $f : \CC \to \CC$ be an entire function such that
$$
f(z)^2 + a(z)f(z) + b(z) = 0.
$$

(i) Show that if $a, b$ have finite order, then $f$ is also of finite order.

(ii) Show that if $a, b$ are polynomials, then $f$ is also a polynomial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Establish a pointwise bound on $\abs{f(z)}$ in terms of $\abs{a(z)}$ and $\abs{b(z)}$:

::: pf-proof

::: pf-step
By the given relation, $f(z)^2 = -a(z)f(z) - b(z)$.

::: pf-proof
rearrange $f(z)^2 + a(z)f(z) + b(z) = 0$.
:::

:::

::: pf-step
Applying the triangle inequality:
$$
\abs{f(z)}^2 \le \abs{a(z)} \abs{f(z)} + \abs{b(z)}.
$$

::: pf-proof
$\abs{-w} = \abs{w}$ and triangle inequality.
:::

:::

::: {.pf-step #s1-3}
If $\abs{f(z)} \le 1$, then $\abs{f(z)} \le 1 + \abs{a(z)} + \abs{b(z)}$.

::: pf-proof
since $\abs{a(z)} \ge 0$ and $\abs{b(z)} \ge 0$, we have $1 \le 1 + \abs{a(z)} + \abs{b(z)}$, and the hypothesis $\abs{f(z)} \le 1$ gives $\abs{f(z)} \le 1 \le 1 + \abs{a(z)} + \abs{b(z)}$.
:::

:::

::: {.pf-step #s1-4}
If $\abs{f(z)} > 1$, then $\abs{b(z)} \le \abs{b(z)} \abs{f(z)}$, so:
$$
\abs{f(z)}^2 \le (\abs{a(z)} + \abs{b(z)}) \abs{f(z)} \implies \abs{f(z)} \le \abs{a(z)} + \abs{b(z)}.
$$

::: pf-proof
divide by $\abs{f(z)} > 0$.
:::

:::

::: pf-step
Therefore, for all $z \in \CC$:
$$
\abs{f(z)} \le 1 + \abs{a(z)} + \abs{b(z)}.
$$

::: pf-proof
step [](#s1-3){.pf-ref} and step [](#s1-4){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s2}
Proof of (i): $f$ has finite order:

::: pf-proof

::: pf-step
Let $\rho_a = \operatorname{order}(a) < \infty$ and $\rho_b = \operatorname{order}(b) < \infty$, and set $\rho = \max(\rho_a, \rho_b)$.

::: pf-proof
hypothesis that $a, b$ have finite order.
:::

:::

::: {.pf-step #s2-2}
For any $\varepsilon > 0$, there exists $R > 0$ such that for all $\abs{z} \ge R$:
$$
\abs{a(z)} \le \exp(\abs{z}^{\rho + \varepsilon}) \quad \text{and} \quad \abs{b(z)} \le \exp(\abs{z}^{\rho + \varepsilon}).
$$

::: pf-proof
definition of the order of an entire function.
:::

:::

::: pf-step
Combining with the bound from step [](#s1){.pf-ref}:
$$
\abs{f(z)} \le 1 + 2\exp(\abs{z}^{\rho + \varepsilon}) \le 3\exp(\abs{z}^{\rho + \varepsilon}) \quad \text{for all } \abs{z} \ge R.
$$

::: pf-proof
step [](#s1){.pf-ref} and step [](#s2-2){.pf-ref}.
:::

:::

::: pf-step
Taking logarithms yields $\limsup_{r \to \infty} \frac{\log \log M_f(r)}{\log r} \le \rho + \varepsilon$ for every $\varepsilon > 0$.

::: pf-proof
definition of order $\operatorname{order}(f) = \limsup_{r\to\infty} \frac{\log\log M(r)}{\log r}$.
:::

:::

::: pf-step
Thus $\operatorname{order}(f) \le \rho = \max(\operatorname{order}(a), \operatorname{order}(b)) < \infty$.

::: pf-proof
$\varepsilon > 0$ is arbitrary.
:::

:::

:::

:::

::: {.pf-step #s3}
Proof of (ii): If $a, b$ are polynomials, $f$ is a polynomial:

::: pf-proof

::: pf-step
Let $d = \max(\deg a, \deg b) \ge 0$.

::: pf-proof
polynomials have finite non-negative degrees.
:::

:::

::: pf-step
There exist constants $C > 0$ and $R > 0$ such that for all $\abs{z} \ge R$:
$$
\abs{a(z)} \le C \abs{z}^d \quad \text{and} \quad \abs{b(z)} \le C \abs{z}^d.
$$

::: pf-proof
asymptotic growth of polynomials.
:::

:::

::: pf-step
By step [](#s1){.pf-ref}, for all $\abs{z} \ge R$:
$$
\abs{f(z)} \le 1 + 2C \abs{z}^d \le (2C + 1) \abs{z}^d.
$$

::: pf-proof
$\abs{z} \ge R \ge 1 \implies 1 \le \abs{z}^d$.
:::

:::

::: {.pf-step #s3-4}
By the generalized Liouville Theorem / Cauchy estimates, an entire function satisfying $\abs{f(z)} \le M \abs{z}^d$ for all $\abs{z} \ge R$ is a polynomial of degree at most $d$.

::: pf-proof
Cauchy's differentiation formula shows $f^{(k)}(0) = 0$ for all $k > d$.
:::

:::

::: pf-step
Thus $f(z)$ is a polynomial.

::: pf-proof
step [](#s3-4){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion: Both claims (i) and (ii) hold.

::: pf-proof
step [](#s2){.pf-ref} and step [](#s3){.pf-ref}.
:::

:::

:::
:::
