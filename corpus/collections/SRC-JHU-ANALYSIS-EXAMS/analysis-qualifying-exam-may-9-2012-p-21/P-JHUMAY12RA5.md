---
schema: qual/card@1
id: P-JHUMAY12RA5
kind: problem
title: Weak and strong convergence of squares in L2
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Justify or give a counterexample to the following assertions:

a. If $\{f_i\}$ is a sequence in $L^2([0,1])$ converging weakly to $f$ in $L^2([0,1])$ then $f_i^2$ converges weakly to $f^2$ in $L^1([0,1])$.

b. If $\{f_i\}$ is a sequence in $L^2([0,1])$ converging strongly to $f$ in $L^2([0,1])$, then $f_i^2$ converges strongly to $f^2$ in $L^1([0,1])$.

::: {.solution}
<1>1. Part (a): Weak convergence in $L^2$ does not imply weak convergence of squares in $L^1$:
<2>1. **The assertion is FALSE.**
Proof: statement of falsity.
<2>2. **Counterexample:**
Let $f_n(x) = \sin(2\pi n x)$ on $[0, 1]$.
By the Riemann–Lebesgue Lemma, for any test function $g \in L^2([0, 1])$:
\[
\lim_{n \to \infty} \int_0^1 f_n(x) g(x) \, dx = \lim_{n \to \infty} \int_0^1 \sin(2\pi n x) g(x) \, dx = 0.
\]
Thus $f_n \rightharpoonup f = 0$ weakly in $L^2([0, 1])$, so $f^2 = 0$.
Proof: Riemann–Lebesgue Lemma.
<2>3. Compute $f_n(x)^2$ using the trigonometric identity $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:
\[
f_n(x)^2 = \sin^2(2\pi n x) = \frac{1}{2} - \frac{1}{2}\cos(4\pi n x).
\]
Proof: trigonometric half-angle identity.
<2>4. For any test function $h \in L^\infty([0, 1]) \cong (L^1([0, 1]))^*$, the Riemann–Lebesgue Lemma gives:
\[
\lim_{n \to \infty} \int_0^1 f_n(x)^2 h(x) \, dx = \lim_{n \to \infty} \left[ \frac{1}{2}\int_0^1 h(x) \, dx - \frac{1}{2}\int_0^1 \cos(4\pi n x) h(x) \, dx \right] = \frac{1}{2}\int_0^1 h(x) \, dx.
\]
In particular, for the constant function $h(x) = 1 \in L^\infty([0, 1])$:
\[
\int_0^1 f_n(x)^2 \, dx = \frac{1}{2} \to \frac{1}{2} \neq 0 = \int_0^1 f(x)^2 \, dx.
\]
Thus $f_n^2 \rightharpoonup \frac{1}{2} \neq 0$ weakly in $L^1([0, 1])$.
Proof: weak limit in $L^1$ against $L^\infty$ functionals.

<1>2. Part (b): Strong convergence in $L^2$ implies strong convergence of squares in $L^1$:
<2>1. **The assertion is TRUE.**
Proof: statement of truth.
<2>2. Let $\{f_i\}$ be a sequence converging strongly to $f$ in $L^2([0, 1])$, so $\|f_i - f\|_{L^2} \to 0$.
Since convergent sequences in normed spaces are bounded, there exists $M < \infty$ such that $\|f_i\|_{L^2} \le M$ for all $i \ge 1$.
Proof: boundedness of convergent sequences.
<2>3. By difference of squares, $|f_i(x)^2 - f(x)^2| = |f_i(x) - f(x)| \cdot |f_i(x) + f(x)|$.
Applying the Cauchy–Schwarz inequality:
\[
\|f_i^2 - f^2\|_{L^1} = \int_0^1 |f_i(x) - f(x)| \cdot |f_i(x) + f(x)| \, dx \le \|f_i - f\|_{L^2} \cdot \|f_i + f\|_{L^2}.
\]
Proof: Cauchy–Schwarz inequality on $L^2([0, 1])$.
<2>4. By the triangle inequality:
\[
\|f_i + f\|_{L^2} \le \|f_i\|_{L^2} + \|f\|_{L^2} \le M + \|f\|_{L^2} < \infty.
\]
Therefore:
\[
\|f_i^2 - f^2\|_{L^1} \le (M + \|f\|_{L^2}) \|f_i - f\|_{L^2} \to 0 \quad \text{as } i \to \infty.
\]
Thus $f_i^2 \to f^2$ strongly in $L^1([0, 1])$.
Proof: squeeze theorem.

<1>3. Conclusion:
(a) is False (with counterexample $f_n = \sin(2\pi n x)$) and (b) is True (by Cauchy–Schwarz). Q.E.D.
Proof: <1>1 and <1>2.
:::
