---
schema: qual/card@1
id: P-JHUSP05AND
kind: problem
title: "Weak and strong convergence of an orthonormal basis and its Cesàro means"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Weak Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Let $\{e_n\}$ be an orthonormal basis for a Hilbert space $H$.

a) Show that $e_n \to 0$ weakly.
(Explain what weak convergence means.)

b) Show that $e_n$ does not tend to zero strongly.
(Explain what strong convergence means.)

c) Let $v_n = \frac{1}{n} \sum_{j=1}^{n} e_j$.
Show that $v_n \to 0$ strongly.

::: {.solution}
<1>1. Part (a): Weak convergence $e_n \rightharpoonup 0$:
<2>1. **Definition of weak convergence:**
A sequence $\{x_n\}$ in a Hilbert space $H$ converges weakly to $x \in H$ (denoted $x_n \rightharpoonup x$) if for every bounded linear functional $\phi \in H^*$, $\lim_{n \to \infty} \phi(x_n) = \phi(x)$.
By the Riesz Representation Theorem, every bounded linear functional is of the form $\phi(z) = \langle z, y \rangle$ for some unique $y \in H$, so weak convergence to $0$ is equivalent to:
\[
\lim_{n \to \infty} \langle x_n, y \rangle = 0 \quad \text{for every } y \in H.
\]
::: {.proof}
Riesz Representation Theorem.
:::
<2>2. Let $y \in H$ be arbitrary.
By Bessel’s inequality (or Parseval’s identity) for the orthonormal set $\{e_n\}$:
\[
\sum_{n=1}^\infty |\langle y, e_n \rangle|^2 \le \|y\|^2 < \infty.
\]
::: {.proof}
Bessel's inequality.
:::
<2>3. Because the series converges, its individual terms must tend to zero:
\[
\lim_{n \to \infty} |\langle e_n, y \rangle| = \lim_{n \to \infty} |\langle y, e_n \rangle| = 0.
\]
Since this holds for every $y \in H$, $e_n \rightharpoonup 0$ weakly.
::: {.proof}
term divergence criterion for convergent series.
:::

<1>2. Part (b): Strong convergence failure:
<2>1. **Definition of strong convergence:**
A sequence $\{x_n\}$ converges strongly (or in norm) to $x \in H$ (denoted $x_n \to x$) if:
\[
\lim_{n \to \infty} \|x_n - x\| = 0.
\]
::: {.proof}
definition of norm convergence in a normed space.
:::
<2>2. Since $\{e_n\}$ is orthonormal, $\|e_n\| = 1$ for all $n \ge 1$.
Therefore:
\[
\|e_n - 0\| = \|e_n\| = 1 \quad \text{for all } n \ge 1.
\]
Because $\lim_{n \to \infty} \|e_n - 0\| = 1 \neq 0$, $e_n$ does not converge strongly to $0$.
::: {.proof}
calculation of the norm.
:::

<1>3. Part (c): Strong convergence of the Cesàro means $v_n \to 0$:
<2>1. Let $v_n = \frac{1}{n} \sum_{j=1}^n e_j$.
Expanding the squared norm using orthonormality $\langle e_j, e_k \rangle = \delta_{jk}$:
\[
\|v_n\|^2 = \left\langle \frac{1}{n} \sum_{j=1}^n e_j, \, \frac{1}{n} \sum_{k=1}^n e_k \right\rangle = \frac{1}{n^2} \sum_{j=1}^n \sum_{k=1}^n \langle e_j, e_k \rangle = \frac{1}{n^2} \sum_{j=1}^n 1 = \frac{n}{n^2} = \frac{1}{n}.
\]
::: {.proof}
bilinearity of inner product and orthonormality.
:::
<2>2. Taking square roots and the limit as $n \to \infty$:
\[
\|v_n - 0\| = \|v_n\| = \frac{1}{\sqrt{n}} \xrightarrow{n \to \infty} 0.
\]
Thus $v_n \to 0$ strongly in $H$.
::: {.proof}
limit of $\frac{1}{\sqrt{n}}$.
:::

<1>4. Conclusion:
$e_n \rightharpoonup 0$ weakly, $e_n \not\to 0$ strongly, and $v_n \to 0$ strongly. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
