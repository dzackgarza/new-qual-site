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

::: problem
Let $a, b : \mathbb{C} \to \mathbb{C}$ be entire functions.
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function such that
$$
f(z)^2 + a(z)f(z) + b(z) = 0.
$$

(i) Show that if $a, b$ have finite order, then $f$ is also of finite order.

(ii) Show that if $a, b$ are polynomials, then $f$ is also a polynomial.
:::

::: {.solution}
<1>1. Establish a pointwise bound on $|f(z)|$ in terms of $|a(z)|$ and $|b(z)|$: <2>1. By the given relation, $f(z)^2 = -a(z)f(z) - b(z)$.
::: {.proof}
rearrange $f(z)^2 + a(z)f(z) + b(z) = 0$.
:::
<2>2. Applying the triangle inequality:
\[
|f(z)|^2 \le |a(z)| |f(z)| + |b(z)|.
\]
::: {.proof}
$|-w| = |w|$ and triangle inequality.
:::
<2>3. If $|f(z)| \le 1$, then $|f(z)| \le 1 + |a(z)| + |b(z)|$.
::: {.proof}
since $|a(z)| \ge 0$ and $|b(z)| \ge 0$, we have $1 \le 1 + |a(z)| + |b(z)|$, and the hypothesis $|f(z)| \le 1$ gives $|f(z)| \le 1 \le 1 + |a(z)| + |b(z)|$.
:::
<2>4. If $|f(z)| > 1$, then $|b(z)| \le |b(z)| |f(z)|$, so:
\[
|f(z)|^2 \le (|a(z)| + |b(z)|) |f(z)| \implies |f(z)| \le |a(z)| + |b(z)|.
\]
::: {.proof}
divide by $|f(z)| > 0$.
:::
<2>5. Therefore, for all $z \in \mathbb{C}$:
\[
|f(z)| \le 1 + |a(z)| + |b(z)|.
\]
::: {.proof}
<2>3 and <2>4.
:::

<1>2. Proof of (i): $f$ has finite order: <2>1. Let $\rho_a = \operatorname{order}(a) < \infty$ and $\rho_b = \operatorname{order}(b) < \infty$, and set $\rho = \max(\rho_a, \rho_b)$.
::: {.proof}
hypothesis that $a, b$ have finite order.
:::
<2>2. For any $\varepsilon > 0$, there exists $R > 0$ such that for all $|z| \ge R$:
\[
|a(z)| \le \exp(|z|^{\rho + \varepsilon}) \quad \text{and} \quad |b(z)| \le \exp(|z|^{\rho + \varepsilon}).
\]
::: {.proof}
definition of the order of an entire function.
:::
<2>3. Combining with the bound from <1>1:
\[
|f(z)| \le 1 + 2\exp(|z|^{\rho + \varepsilon}) \le 3\exp(|z|^{\rho + \varepsilon}) \quad \text{for all } |z| \ge R.
\]
::: {.proof}
<1>1 and <2>2. <2>4. Taking logarithms yields $\limsup_{r \to \infty} \frac{\log \log M_f(r)}{\log r} \le \rho + \varepsilon$ for every $\varepsilon > 0$.
::: {.proof}
definition of order $\operatorname{order}(f) = \limsup_{r\to\infty} \frac{\log\log M(r)}{\log r}$.
:::
:::
<2>5. Thus $\operatorname{order}(f) \le \rho = \max(\operatorname{order}(a), \operatorname{order}(b)) < \infty$.
::: {.proof}
$\varepsilon > 0$ is arbitrary.
:::

<1>3. Proof of (ii): If $a, b$ are polynomials, $f$ is a polynomial: <2>1. Let $d = \max(\deg a, \deg b) \ge 0$.
::: {.proof}
polynomials have finite non-negative degrees.
:::
<2>2. There exist constants $C > 0$ and $R > 0$ such that for all $|z| \ge R$:
\[
|a(z)| \le C |z|^d \quad \text{and} \quad |b(z)| \le C |z|^d.
\]
::: {.proof}
asymptotic growth of polynomials.
:::
<2>3. By <1>1, for all $|z| \ge R$:
\[
|f(z)| \le 1 + 2C |z|^d \le (2C + 1) |z|^d.
\]
::: {.proof}
$|z| \ge R \ge 1 \implies 1 \le |z|^d$.
:::
<2>4. By the generalized Liouville Theorem / Cauchy estimates, an entire function satisfying $|f(z)| \le M |z|^d$ for all $|z| \ge R$ is a polynomial of degree at most $d$.
::: {.proof}
Cauchy's differentiation formula shows $f^{(k)}(0) = 0$ for all $k > d$.
:::
<2>5. Thus $f(z)$ is a polynomial.
::: {.proof}
<2>4.
:::

<1>4. Conclusion: Both claims (i) and (ii) hold.
::: {.proof}
<1>2 and <1>3.
:::
Q.E.D.
:::
