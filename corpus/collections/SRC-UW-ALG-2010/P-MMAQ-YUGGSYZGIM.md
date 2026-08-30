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

::: problem
Let $f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_0\in\mathbb Z[x]$ (where $a_n\neq 0$) and let $R=\mathbb Z[x]/(f)$.
Prove that $R$ is a finitely generated module over $\mathbb Z$ if and only if $a_n=\pm 1$.
:::

::: {.solution}
**($\Leftarrow$) If $a_n = \pm 1$, then $R$ is a finitely generated $\mathbb{Z}$-module:**

<1>1. Since $a_n = \pm 1$, the polynomial $f_0(x) = a_n^{-1} f(x) = x^n + a_n a_{n-1} x^{n-1} + \dots + a_n a_0$ is a monic polynomial in $\mathbb{Z}[x]$ of degree $n$, with $(f) = (f_0)$.
Proof: $a_n \in \{1, -1\}$ is a unit in $\mathbb{Z}$, so $(f) = (f_0)$ as ideals in $\mathbb{Z}[x]$.

<1>2. By the polynomial division algorithm over $\mathbb{Z}$ for monic polynomials, for every $g(x) \in \mathbb{Z}[x]$, there exist $q(x), r(x) \in \mathbb{Z}[x]$ such that:
\[
g(x) = q(x)f_0(x) + r(x), \quad \text{with } \deg(r) < n \text{ (or } r = 0\text{)}.
\]
Proof: division algorithm in $\mathbb{Z}[x]$ with monic divisor.

<1>3. Passing to the quotient $R = \mathbb{Z}[x]/(f)$:
\[
g(x) + (f) = r(x) + (f) = c_0 \cdot 1 + c_1 \bar{x} + \dots + c_{n-1} \bar{x}^{n-1}, \quad c_i \in \mathbb{Z}.
\]
Proof: $q(x)f_0(x) \in (f)$ and $r(x) = \sum_{i=0}^{n-1} c_i x^i$.

<1>4. Thus $\{1, \bar{x}, \bar{x}^2, \dots, \bar{x}^{n-1}\}$ spans $R$ as a $\mathbb{Z}$-module, so $R$ is finitely generated over $\mathbb{Z}$.
Proof: <1>3.

**($\Rightarrow$) If $R$ is a finitely generated $\mathbb{Z}$-module, then $a_n = \pm 1$:**

<1>5. Suppose $R$ is generated as a $\mathbb{Z}$-module by finitely many elements $\{g_1(\bar{x}), \dots, g_m(\bar{x})\}$.
Proof: hypothesis.

<1>6. Let $d = \max_{1 \le i \le m} \deg(g_i) \ge 0$.
Proof: maximum degree among the finitely many polynomial generators.

<1>7. Every element of $R$ can be represented by a polynomial in $\mathbb{Z}[x]$ of degree at most $d$.
<2>1. Any element $u \in R$ is a $\mathbb{Z}$-linear combination $u = \sum_{i=1}^m k_i g_i(\bar{x})$ with $k_i \in \mathbb{Z}$.
Proof: $\{g_i(\bar{x})\}$ is a $\mathbb{Z}$-generating set.
<2>2. The polynomial $h(x) = \sum_{i=1}^m k_i g_i(x) \in \mathbb{Z}[x]$ satisfies $\deg(h) \le \max_i \deg(g_i) = d$.
Proof: degree of a sum of polynomials.
<2>3. Thus $u = h(\bar{x})$ with $\deg(h) \le d$.
Proof: <2>1 and <2>2.

<1>8. For $k = d + 1$, the element $\bar{x}^k \in R$ satisfies $\bar{x}^k = h(\bar{x})$ for some $h(x) \in \mathbb{Z}[x]$ with $\deg(h) \le d$.
Proof: <1>7 applied to $u = \bar{x}^k$.

<1>9. The difference $x^k - h(x)$ belongs to the ideal $(f(x)) = f(x)\mathbb{Z}[x]$.
Proof: $x^k + (f) = h(x) + (f) \iff x^k - h(x) \in (f)$.

<1>10. There exists a polynomial $q(x) \in \mathbb{Z}[x]$ such that $x^k - h(x) = q(x)f(x)$.
Proof: definition of the principal ideal $(f(x))$ in $\mathbb{Z}[x]$.

<1>11. Equating leading coefficients: <2>1. Since $k = d + 1 > d \ge \deg(h)$, the leading term of the left-hand side $x^k - h(x)$ is $1 \cdot x^k$.
Proof: $h(x)$ has degree $\le d < k$, so it cannot cancel the $x^k$ term.
<2>2. The leading term of the right-hand side $q(x)f(x)$ is $\operatorname{LC}(q) \cdot a_n \cdot x^{\deg(q) + n}$.
Proof: multiplication of polynomials over the integral domain $\mathbb{Z}$.
<2>3. Equating degrees gives $\deg(q) + n = k$, and equating leading coefficients gives:
\[
1 = \operatorname{LC}(q) \cdot a_n.
\]
Proof: coefficients of polynomials in $\mathbb{Z}[x]$.
<2>4. Since $\operatorname{LC}(q), a_n \in \mathbb{Z}$, $a_n$ is a unit in $\mathbb{Z}$, which implies $a_n = \pm 1$.
Proof: the only units in the ring of integers $\mathbb{Z}$ are $1$ and $-1$.

<1>12. Conclusion: $R = \mathbb{Z}[x]/(f)$ is a finitely generated $\mathbb{Z}$-module if and only if $a_n = \pm 1$.
Q.E.D. Proof: <1>4 and <1>11.
:::
