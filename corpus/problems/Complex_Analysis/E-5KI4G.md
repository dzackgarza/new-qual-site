---
schema: qual/card@1
id: E-5KI4G
kind: problem
title: Uniform convergence of $\sin(nx)/(1+nx)$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Counterexamples
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source gives no domain, and f_n is undefined at x = -1/n; the statement restricts to x >= 0, the domain the solution treats.
---

::: {.exercise}
Determine where on $[0,\infty)$ the following sequence of real-valued functions is or is not uniformly convergent:
$$
f_n(x) \definedas \frac{\sin(nx)}{1+nx}.
$$

:::

::: {.solution}

::: pf

::: {.pf-step #pointwise}
$f_n\to0$ pointwise on $[0,\infty)$.

::: pf-proof
$f_n(0)=0$, and for $x>0$, $\abs{f_n(x)}\le 1/(1+nx)\to0$.
:::

:::

::: pf-step
The convergence is uniform on $[a, \infty)$ for every $a>0$.

::: pf-proof
$\sup_{x\geq a}\abs{f_n(x)} \leq \frac{1}{1 + na}\to 0$ as $n\to\infty$.
:::

:::

::: pf-step
The convergence is not uniform on $(0, \infty)$, nor on $[0,\infty)$ or any interval $(0,a)$ with $a>0$.

::: pf-proof
With $x_n = 1/n$, which lies in $(0,a)$ for large $n$, $\abs{f_n(x_n)} = \sin(1)/2$ for every $n$, so $\sup\abs{f_n}\not\to0$ while the pointwise limit of step [](#pointwise){.pf-ref} is $0$.
:::

:::

:::

:::
