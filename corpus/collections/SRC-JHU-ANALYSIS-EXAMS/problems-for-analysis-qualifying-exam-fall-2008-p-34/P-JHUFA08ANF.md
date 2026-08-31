---
schema: qual/card@1
id: P-JHUFA08ANF
kind: problem
title: "Entire functions of polynomial growth are polynomials"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

6) (10 points) Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Prove that if there exists some real number C and some positive integer k so that

$$
| f ( z ) | \leq C | z | ^ { k }
$$

for all z with $| z | > 1$ , then f is a polynomial in z of degree at most $k .$

::: {.solution}
<1>1. Power series expansion of the entire function:
<2>1. Since $f: \mathbb{C} \to \mathbb{C}$ is entire, it has a Taylor series expansion converging on the entire complex plane:
\[
f(z) = \sum_{n=0}^\infty a_n z^n, \quad \text{where } a_n = \frac{f^{(n)}(0)}{n!}.
\]
::: {.proof}
Taylor's theorem for entire functions.
:::
<2>2. By Cauchy’s Integral Formula for derivatives, for any radius $R > 0$:
\[
a_n = \frac{1}{2\pi i} \oint_{|w| = R} \frac{f(w)}{w^{n+1}} \, dw.
\]
::: {.proof}
Cauchy's Integral Formula.
:::

<1>2. Cauchy estimates on Taylor coefficients:
<2>1. Let $R > 1$. By the hypothesis $|f(w)| \le C |w|^k = C R^k$ for $|w| = R$:
\[
|a_n| \le \frac{1}{2\pi} \oint_{|w| = R} \frac{|f(w)|}{|w|^{n+1}} \, |dw| \le \frac{1}{2\pi} \cdot \frac{C R^k}{R^{n+1}} \cdot (2\pi R) = C R^{k - n}.
\]
::: {.proof}
standard ML-estimate on the circle of radius $R$.
:::
<2>2. Suppose $n > k$, so that $k - n \le -1 < 0$.
Since the inequality $|a_n| \le C R^{k - n}$ holds for all arbitrarily large $R > 1$, we take the limit as $R \to \infty$:
\[
|a_n| \le \lim_{R \to \infty} C R^{k - n} = 0 \implies a_n = 0.
\]
::: {.proof}
limit of negative powers of $R$ as $R \to \infty$.
:::

<1>3. Conclusion:
$a_n = 0$ for all $n \ge k + 1$, and therefore:
\[
f(z) = \sum_{n=0}^k a_n z^n,
\]
which is a polynomial of degree at most $k$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
