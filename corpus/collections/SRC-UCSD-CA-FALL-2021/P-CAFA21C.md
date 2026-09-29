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
Let $a, b : \mathbb{C} \to \mathbb{C}$ be entire functions.
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function such that
$$
f(z)^2 + a(z)f(z) + b(z) = 0.
$$

(i) Show that if $a, b$ have finite order, then $f$ is also of finite order.

(ii) Show that if $a, b$ are polynomials, then $f$ is also a polynomial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Establish a pointwise bound on $|f(z)|$ in terms of $|a(z)|$ and $|b(z)|$:

::: pf-proof

::: pf-step
By the given relation, $f(z)^2 = -a(z)f(z) - b(z)$.

::: pf-proof
rearrange $f(z)^2 + a(z)f(z) + b(z) = 0$.
:::

:::

::: pf-step
Applying the triangle inequality:
\[
|f(z)|^2 \le |a(z)| |f(z)| + |b(z)|.
\]

::: pf-proof
$|-w| = |w|$ and triangle inequality.
:::

:::

::: {.pf-step #s1-3}
If $|f(z)| \le 1$, then $|f(z)| \le 1 + |a(z)| + |b(z)|$.

::: pf-proof
since $|a(z)| \ge 0$ and $|b(z)| \ge 0$, we have $1 \le 1 + |a(z)| + |b(z)|$, and the hypothesis $|f(z)| \le 1$ gives $|f(z)| \le 1 \le 1 + |a(z)| + |b(z)|$.
:::

:::

::: {.pf-step #s1-4}
If $|f(z)| > 1$, then $|b(z)| \le |b(z)| |f(z)|$, so:
\[
|f(z)|^2 \le (|a(z)| + |b(z)|) |f(z)| \implies |f(z)| \le |a(z)| + |b(z)|.
\]

::: pf-proof
divide by $|f(z)| > 0$.
:::

:::

::: pf-step
Therefore, for all $z \in \mathbb{C}$:
\[
|f(z)| \le 1 + |a(z)| + |b(z)|.
\]

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
For any $\varepsilon > 0$, there exists $R > 0$ such that for all $|z| \ge R$:
\[
|a(z)| \le \exp(|z|^{\rho + \varepsilon}) \quad \text{and} \quad |b(z)| \le \exp(|z|^{\rho + \varepsilon}).
\]

::: pf-proof
definition of the order of an entire function.
:::

:::

::: pf-step
Combining with the bound from step [](#s1){.pf-ref}:
\[
|f(z)| \le 1 + 2\exp(|z|^{\rho + \varepsilon}) \le 3\exp(|z|^{\rho + \varepsilon}) \quad \text{for all } |z| \ge R.
\]

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
There exist constants $C > 0$ and $R > 0$ such that for all $|z| \ge R$:
\[
|a(z)| \le C |z|^d \quad \text{and} \quad |b(z)| \le C |z|^d.
\]

::: pf-proof
asymptotic growth of polynomials.
:::

:::

::: pf-step
By step [](#s1){.pf-ref}, for all $|z| \ge R$:
\[
|f(z)| \le 1 + 2C |z|^d \le (2C + 1) |z|^d.
\]

::: pf-proof
$|z| \ge R \ge 1 \implies 1 \le |z|^d$.
:::

:::

::: {.pf-step #s3-4}
By the generalized Liouville Theorem / Cauchy estimates, an entire function satisfying $|f(z)| \le M |z|^d$ for all $|z| \ge R$ is a polynomial of degree at most $d$.

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
