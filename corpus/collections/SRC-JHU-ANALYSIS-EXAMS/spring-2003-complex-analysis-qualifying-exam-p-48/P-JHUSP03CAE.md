---
schema: qual/card@1
id: P-JHUSP03CAE
kind: problem
title: Meromorphic on Riemann sphere implies rational (part a)
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Let $f : \mathbb{C} \to \mathbb{C}$ be meromorphic with a pole at infinity.
Show that $f$ must be a rational function.

::: {.solution}
<1>1. Finiteness of poles in $\mathbb{C}$:
<2>1. Since $f$ has a pole (or removable singularity) at $\infty$, the function $F(w) = f(1/w)$ has an isolated singularity at $w = 0$.
Thus there exists $R > 0$ such that $f$ has no poles in the region $\{z \in \mathbb{C} : |z| > R\}$.
::: {.proof}
isolated singularities.
:::
<2>2. Since $f$ is meromorphic on $\mathbb{C}$, its poles are isolated in the closed bounded disk $\overline{D}(0, R)$.
Because a compact set cannot contain an infinite discrete set with no limit point, $f$ has only finitely many poles in $\mathbb{C}$, say $\{z_1, \dots, z_k\}$.
::: {.proof}
Bolzano–Weierstrass Theorem.
:::

<1>2. Principal parts and polynomial part:
<2>1. For each pole $z_j \in \mathbb{C}$, let the principal part of $f$ at $z_j$ be the rational function:
\[
P_j(z) = \sum_{m=1}^{d_j} \frac{c_{j,m}}{(z - z_j)^m}.
\]
::: {.proof}
Laurent expansion around $z_j$.
:::
<2>2. The Laurent expansion of $f(z)$ in the annulus $\{|z| > R\}$ takes the form:
\[
f(z) = \sum_{m=1}^d a_m z^m + a_0 + \sum_{m=1}^\infty \frac{b_m}{z^m}.
\]
Define the polynomial $P_\infty(z) = \sum_{m=1}^d a_m z^m$.
::: {.proof}
Laurent expansion around $\infty$.
:::

<1>3. Liouville’s Theorem applied to the regularized difference:
<2>1. Define $g(z) = f(z) - \sum_{j=1}^k P_j(z) - P_\infty(z)$.
::: {.proof}
definition of $g$.
:::
<2>2. At each $z_j$, subtracting $P_j(z)$ removes the negative power terms in the Laurent series, so $g$ has a removable singularity at each $z_j$.
Therefore $g$ extends to an entire function on $\mathbb{C}$.
::: {.proof}
Riemann's theorem on removable singularities.
:::
<2>3. As $|z| \to \infty$, $P_j(z) \to 0$ for all $1 \le j \le k$, and $f(z) - P_\infty(z) \to a_0$.
Thus $\lim_{|z| \to \infty} g(z) = a_0 \in \mathbb{C}$.
::: {.proof}
<2>1 and <2>2.
:::
<2>4. Since $g$ is an entire function and $\lim_{|z| \to \infty} g(z) = a_0$, $g$ is bounded on $\mathbb{C}$.
By Liouville’s Theorem, $g(z) = a_0$ is a constant.
::: {.proof}
Liouville's Theorem.
:::

<1>4. Conclusion:
\[
f(z) = a_0 + P_\infty(z) + \sum_{j=1}^k P_j(z) = a_0 + \sum_{m=1}^d a_m z^m + \sum_{j=1}^k \sum_{m=1}^{d_j} \frac{c_{j,m}}{(z - z_j)^m},
\]
which is a finite sum of polynomials and rational functions, hence a rational function in $\mathbb{C}(z)$. Q.E.D.
::: {.proof}
<1>3.
:::
:::
