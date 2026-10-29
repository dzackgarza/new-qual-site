---
schema: qual/card@1
id: P-6LWY3
kind: problem
title: Pointwise convergence of $n^\beta x(1-x^2)^n$ on $[0,1]$, uniform if and only
  if $\beta<\frac12$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 5 of the preserved UNL May 2016 qualifying-exam source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $f_n(x) = n^\beta x(1-x^2)^n$, $x \in [0,1]$, $n \in \NN$.

(a) Prove that $\{f_n\}_{n=1}^\infty$ converges pointwise on $[0,1]$ for every $\beta \in \RR$.

(b) Show that the convergence in part (a) is uniform for all $\beta < \frac{1}{2}$, but not uniform for any $\beta \geq \frac{1}{2}$.
:::

::: {.solution}

::: pf

::: pf-step

(a) $f_n \to 0$ pointwise on $[0,1]$ for every $\beta \in \RR$.

::: pf-proof

::: pf-step

$f_n(0) = 0$ for all $n$.

::: pf-proof

The factor $x$ vanishes at $x = 0$.

:::

:::

::: pf-step

For $0 < x \le 1$, $f_n(x) \to 0$.

::: pf-proof

Here $1 - x^2 \in [0,1)$. If $x = 1$, then $f_n(1) = 0$. Otherwise $\ln(1-x^2) < 0$, so $n^\beta(1-x^2)^n = n^\beta e^{n\ln(1-x^2)} \to 0$, because exponential decay dominates the power $n^\beta$.

:::

:::

:::

:::

::: {.pf-step #sup-norm}

$\sup_{x \in [0,1]}\abs{f_n(x)} = \frac{n^\beta}{\sqrt{2n+1}}\left(\frac{2n}{2n+1}\right)^n$.

::: pf-proof

Let $g(x) = x(1 - x^2)^n$. Then $g'(x) = (1 - x^2)^{n-1}(1 - (2n+1)x^2)$, so $g' > 0$ on $(0, x_n)$ and $g' < 0$ on $(x_n, 1)$ for $x_n = 1/\sqrt{2n+1}$. Since $g \geq 0$ on $[0,1]$ and $g(0) = g(1) = 0$, the maximum of $g$ is $g(x_n) = \frac{1}{\sqrt{2n+1}}\left(1 - \frac{1}{2n+1}\right)^n = \frac{1}{\sqrt{2n+1}}\left(\frac{2n}{2n+1}\right)^n$. Multiply by $n^\beta$.

:::

:::

::: pf-step

(b) The convergence is uniform if and only if $\beta < \frac{1}{2}$.

::: pf-proof

By (a), uniform convergence on $[0,1]$ means $\sup_{x\in[0,1]}\abs{f_n(x)} \to 0$. As $n \to \infty$, $\frac{1}{\sqrt{2n+1}} \sim \frac{1}{\sqrt 2}n^{-1/2}$ and $\left(\frac{2n}{2n+1}\right)^n = \left(1 - \frac{1}{2n+1}\right)^n \to e^{-1/2} > 0$. By step [](#sup-norm){.pf-ref}, the supremum is therefore asymptotic to $\frac{e^{-1/2}}{\sqrt 2}\, n^{\beta - 1/2}$. This tends to $0$ when $\beta < \frac12$, tends to $\frac{e^{-1/2}}{\sqrt 2} \neq 0$ when $\beta = \frac12$, and diverges when $\beta > \frac12$.

:::

:::

:::

:::
