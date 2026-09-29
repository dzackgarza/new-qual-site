---
schema: qual/card@1
id: P-MMAQ-YUGGSYZGIM
kind: problem
title: $\ZZ[x]/(f)$ is a finitely generated $\ZZ$-module if and only if the leading
  coefficient of $f$ is $\pm 1$
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_0\in\mathbb Z[x]$ (where $a_n\neq 0$) and let $R=\mathbb Z[x]/(f)$.
Prove that $R$ is a finitely generated module over $\mathbb Z$ if and only if $a_n=\pm 1$.
:::

::: {.solution}

**($\Leftarrow$) If $a_n = \pm 1$, then $R$ is a finitely generated $\mathbb{Z}$-module:**

::: pf

::: pf-step
Since $a_n = \pm 1$, the polynomial $f_0(x) = a_n^{-1} f(x) = x^n + a_n a_{n-1} x^{n-1} + \dots + a_n a_0$ is a monic polynomial in $\mathbb{Z}[x]$ of degree $n$, with $(f) = (f_0)$.

::: pf-proof
$a_n \in \{1, -1\}$ is a unit in $\mathbb{Z}$, so $(f) = (f_0)$ as ideals in $\mathbb{Z}[x]$.
:::

:::

::: pf-step
By the polynomial division algorithm over $\mathbb{Z}$ for monic polynomials, for every $g(x) \in \mathbb{Z}[x]$, there exist $q(x), r(x) \in \mathbb{Z}[x]$ such that:
\[
g(x) = q(x)f_0(x) + r(x), \quad \text{with } \deg(r) < n \text{ (or } r = 0\text{)}.
\]

::: pf-proof
division algorithm in $\mathbb{Z}[x]$ with monic divisor.
:::

:::

::: {.pf-step #s3}
Passing to the quotient $R = \mathbb{Z}[x]/(f)$:
\[
g(x) + (f) = r(x) + (f) = c_0 \cdot 1 + c_1 \bar{x} + \dots + c_{n-1} \bar{x}^{n-1}, \quad c_i \in \mathbb{Z}.
\]

::: pf-proof
$q(x)f_0(x) \in (f)$ and $r(x) = \sum_{i=0}^{n-1} c_i x^i$.
:::

:::

::: {.pf-step #s4}
Thus $\{1, \bar{x}, \bar{x}^2, \dots, \bar{x}^{n-1}\}$ spans $R$ as a $\mathbb{Z}$-module, so $R$ is finitely generated over $\mathbb{Z}$.

::: pf-proof
step [](#s3){.pf-ref}.
:::

:::

:::

**($\Rightarrow$) If $R$ is a finitely generated $\mathbb{Z}$-module, then $a_n = \pm 1$:**

::: pf

::: pf-step
Suppose $R$ is generated as a $\mathbb{Z}$-module by finitely many elements $\{g_1(\bar{x}), \dots, g_m(\bar{x})\}$.

::: pf-proof
hypothesis.
:::

:::

::: pf-step
Let $d = \max_{1 \le i \le m} \deg(g_i) \ge 0$.

::: pf-proof
maximum degree among the finitely many polynomial generators.
:::

:::

::: {.pf-step #s7}
Every element of $R$ can be represented by a polynomial in $\mathbb{Z}[x]$ of degree at most $d$.

::: pf-proof

::: {.pf-step #s7-1}
Any element $u \in R$ is a $\mathbb{Z}$-linear combination $u = \sum_{i=1}^m k_i g_i(\bar{x})$ with $k_i \in \mathbb{Z}$.

::: pf-proof
$\{g_i(\bar{x})\}$ is a $\mathbb{Z}$-generating set.
:::

:::

::: {.pf-step #s7-2}
The polynomial $h(x) = \sum_{i=1}^m k_i g_i(x) \in \mathbb{Z}[x]$ satisfies $\deg(h) \le \max_i \deg(g_i) = d$.

::: pf-proof
degree of a sum of polynomials.
:::

:::

::: pf-step
Thus $u = h(\bar{x})$ with $\deg(h) \le d$.

::: pf-proof
step [](#s7-1){.pf-ref} and step [](#s7-2){.pf-ref}.
:::

:::

:::

:::

::: pf-step
For $k = d + 1$, the element $\bar{x}^k \in R$ satisfies $\bar{x}^k = h(\bar{x})$ for some $h(x) \in \mathbb{Z}[x]$ with $\deg(h) \le d$.

::: pf-proof
step [](#s7){.pf-ref} applied to $u = \bar{x}^k$.
:::

:::

::: pf-step
The difference $x^k - h(x)$ belongs to the ideal $(f(x)) = f(x)\mathbb{Z}[x]$.

::: pf-proof
$x^k + (f) = h(x) + (f) \iff x^k - h(x) \in (f)$.
:::

:::

::: pf-step
There exists a polynomial $q(x) \in \mathbb{Z}[x]$ such that $x^k - h(x) = q(x)f(x)$.

::: pf-proof
definition of the principal ideal $(f(x))$ in $\mathbb{Z}[x]$.
:::

:::

::: {.pf-step #s11}
Equating leading coefficients:

::: pf-proof

::: pf-step
Since $k = d + 1 > d \ge \deg(h)$, the leading term of the left-hand side $x^k - h(x)$ is $1 \cdot x^k$.

::: pf-proof
$h(x)$ has degree $\le d < k$, so it cannot cancel the $x^k$ term.
:::

:::

::: pf-step
The leading term of the right-hand side $q(x)f(x)$ is $\operatorname{LC}(q) \cdot a_n \cdot x^{\deg(q) + n}$.

::: pf-proof
multiplication of polynomials over the integral domain $\mathbb{Z}$.
:::

:::

::: pf-step
Equating degrees gives $\deg(q) + n = k$, and equating leading coefficients gives:
\[
1 = \operatorname{LC}(q) \cdot a_n.
\]

::: pf-proof
coefficients of polynomials in $\mathbb{Z}[x]$.
:::

:::

::: pf-step
Since $\operatorname{LC}(q), a_n \in \mathbb{Z}$, $a_n$ is a unit in $\mathbb{Z}$, which implies $a_n = \pm 1$.

::: pf-proof
the only units in the ring of integers $\mathbb{Z}$ are $1$ and $-1$.
:::

:::

:::

:::

::: pf-qed
Conclusion: $R = \mathbb{Z}[x]/(f)$ is a finitely generated $\mathbb{Z}$-module if and only if $a_n = \pm 1$.
step [](#s4){.pf-ref} and step [](#s11){.pf-ref}.
:::

:::

:::
