---
schema: qual/card@1
id: P-DEFYR
kind: problem
title: $nx(1-x)^n\to 0$ pointwise but not uniformly, and $\int n(1-x)^n\sin x\to 0$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
---

::: {.problem}
Let $f_n(x) = n x (1 - x)^n$ for $n \in \mathbb{N}$ on the interval $[0, 1]$.

(a) Show that $f_n \to 0$ pointwise but not uniformly on $[0, 1]$.

(b) Show that
$$
\lim_{n \to \infty} \int_0^1 n (1 - x)^n \sin x \, dx = 0.
$$
:::

::: {.solution}
**Goal:** Prove pointwise convergence to zero and failure of uniform convergence in (a) via the supremum of $f_n$, and evaluate the integral limit in (b) using the Squeeze Theorem.

::: pf

::: pf-step
Part (a): Pointwise convergence $f_n(x) \to 0$ on $[0, 1]$.

::: pf-proof

::: pf-step
For $x = 0$: $f_n(0) = n \cdot 0 \cdot (1 - 0)^n = 0 \to 0$ as $n \to \infty$.

:::

::: pf-step
For $x = 1$: $f_n(1) = n \cdot 1 \cdot (1 - 1)^n = 0 \to 0$ as $n \to \infty$.

:::

::: pf-step
For $x \in (0, 1)$: let $r = 1 - x \in (0, 1)$. Then $f_n(x) = x \cdot n r^n$.

:::

::: pf-step
By the ratio test for sequences (or L'Hôpital's Rule), since $0 < r < 1$:
$$\lim_{n \to \infty} n r^n = 0.$$

:::

::: pf-step
Thus for each fixed $x \in (0, 1)$, $\lim_{n \to \infty} f_n(x) = x \cdot 0 = 0$.

:::

::: pf-step
Therefore $f_n \to 0$ pointwise on $[0, 1]$.

:::

:::

:::

::: pf-step
Part (a): Convergence is not uniform on $[0, 1]$.

::: pf-proof

::: pf-step
Compute the derivative of $f_n$ on $(0, 1)$:
$$f_n'(x) = n (1 - x)^n - n^2 x (1 - x)^{n-1} = n (1 - x)^{n-1} \left( (1 - x) - n x \right) = n (1 - x)^{n-1} (1 - (n + 1)x).$$

:::

::: pf-step
On $[0, 1]$, $f_n'(x) = 0$ at the unique critical point $x_n = \frac{1}{n + 1} \in (0, 1)$.

:::

::: pf-step
Since $f_n(0) = f_n(1) = 0$ and $f_n(x) > 0$ on $(0, 1)$, the absolute maximum of $f_n$ on $[0, 1]$ is achieved at $x_n$:
$$\|f_n\|_\infty = \sup_{x \in [0, 1]} |f_n(x)| = f_n\left(\frac{1}{n+1}\right) = n \cdot \frac{1}{n+1} \left(1 - \frac{1}{n+1}\right)^n = \frac{n}{n+1} \left(1 - \frac{1}{n+1}\right)^n.$$

:::

::: pf-step
Take the limit as $n \to \infty$:
$$\lim_{n \to \infty} \|f_n\|_\infty = \lim_{n \to \infty} \frac{n}{n+1} \cdot \lim_{n \to \infty} \left(1 - \frac{1}{n+1}\right)^n = 1 \cdot e^{-1} = \frac{1}{e} > 0.$$

:::

::: pf-step
Since $\lim_{n \to \infty} \|f_n - 0\|_\infty = e^{-1} \ne 0$, $f_n$ does not converge uniformly to $0$ on $[0, 1]$.

:::

:::

:::

::: pf-step
Part (b): $\lim_{n \to \infty} \int_0^1 n (1 - x)^n \sin x \, dx = 0$.

::: pf-proof

::: pf-step
For all $x \in [0, 1]$, $0 \le \sin x \le x$.

:::

::: pf-step
Multiply by the non-negative kernel $n (1 - x)^n \ge 0$:
$$0 \le n (1 - x)^n \sin x \le n x (1 - x)^n = f_n(x) \quad \text{for all } x \in [0, 1].$$

:::

::: pf-step
Integrate the upper bound by parts, with $u = x$ and $d v = n (1 - x)^n d x$ (so $d u = d x$ and $v = -\frac{n}{n+1}(1 - x)^{n+1}$):
$$\int_0^1 n x (1 - x)^n \, dx = \left[ -\frac{n x (1 - x)^{n+1}}{n+1} \right]_0^1 + \frac{n}{n+1} \int_0^1 (1 - x)^{n+1} \, dx = 0 + \frac{n}{n+1} \left[ -\frac{(1 - x)^{n+2}}{n+2} \right]_0^1 = \frac{n}{(n+1)(n+2)}.$$

:::

::: pf-step
Therefore, by monotonicity of integration:
$$0 \le \int_0^1 n (1 - x)^n \sin x \, dx \le \frac{n}{(n+1)(n+2)}.$$

:::

::: pf-step
Since $\lim_{n \to \infty} \frac{n}{(n+1)(n+2)} = 0$, by the Squeeze Theorem:
$$\lim_{n \to \infty} \int_0^1 n (1 - x)^n \sin x \, dx = 0.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$f_n \to 0$ pointwise with $\|f_n\|_\infty \to 1/e$ (non-uniform), and the integral limit is 0 by the Squeeze Theorem.
:::

:::

:::

:::
