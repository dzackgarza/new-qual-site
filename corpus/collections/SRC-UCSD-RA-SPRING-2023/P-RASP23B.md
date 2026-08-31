---
schema: qual/card@1
id: P-RASP23B
kind: problem
title: "Uniform convergence and integration on finite measure spaces"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Assume that $\mu(X) < \infty$.
Let $\{f_n\}$ be a bounded sequence of complex functions.
Assume that $f_n \to f$ uniformly as $n \to \infty$.
Prove that $\int_X f_n\,d\mu \to \int_X f\,d\mu$.
Show by an example that the assumption $\mu(X) < \infty$ cannot be dropped.
:::

::: {.solution}
<1>1. Convergence of integrals under uniform convergence on finite measure spaces:
<2>1. Let $\varepsilon > 0$ be given.
If $\mu(X) = 0$, the integrals are identically zero.
Otherwise, assume $\mu(X) \in (0, \infty)$.
<2>2. Since $f_n \to f$ uniformly on $X$, there exists an integer $N \in \mathbb{N}$ such that for all $n \ge N$:
\[
\sup_{x \in X} |f_n(x) - f(x)| < \frac{\varepsilon}{\mu(X)}.
\]
<2>3. By the integral triangle inequality and monotonicity of the Lebesgue integral:
\[
\left| \int_X f_n \, d\mu - \int_X f \, d\mu \right| \le \int_X |f_n - f| \, d\mu \le \left( \sup_{x \in X} |f_n(x) - f(x)| \right) \mu(X).
\]
<2>4. For all $n \ge N$:
\[
\left| \int_X f_n \, d\mu - \int_X f \, d\mu \right| < \frac{\varepsilon}{\mu(X)} \cdot \mu(X) = \varepsilon.
\]
Since $\varepsilon > 0$ was arbitrary, $\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu$.

<1>2. Counterexample showing $\mu(X) < \infty$ is necessary:
<2>1. Let $X = [0, \infty)$ equipped with the standard Lebesgue measure $m$, so $m(X) = \infty$.
Define the sequence of functions:
\[
f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x) \quad \text{for } n \ge 1.
\]
<2>2. For every $n \ge 1$, $\sup_{x \in [0, \infty)} |f_n(x) - 0| = \frac{1}{n}$.
As $n \to \infty$, $\frac{1}{n} \to 0$, so $f_n \to 0$ uniformly on $[0, \infty)$.
<2>3. For every $n \ge 1$, compute the integral:
\[
\int_{[0, \infty)} f_n \, dm = \int_0^n \frac{1}{n} \, dx = \frac{1}{n} \cdot n = 1.
\]
Thus:
\[
\lim_{n \to \infty} \int_{[0, \infty)} f_n \, dm = 1 \neq 0 = \int_{[0, \infty)} 0 \, dm.
\]

<1>3. Conclusion:
The convergence holds when $\mu(X) < \infty$, and the sequence $f_n = \frac{1}{n}\mathbf{1}_{[0, n]}$ provides a counterexample when $\mu(X) = \infty$. Q.E.D.
:::
