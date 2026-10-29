---
schema: qual/card@1
id: P-BKS88-9
kind: problem
title: Convergence of the Fresnel integrals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
Prove that the integrals

$$
\int_0^\infty\cos x^2\,dx\quad\text{and}\quad\int_0^\infty\sin x^2\,dx
$$

converge.
:::

::: {.solution}
::: pf

::: {.pf-step #tail-bound}
For $0<A<B$,
$$
\left|\int_A^B e^{ix^2}\,dx\right|
\leq \frac1A+\frac1{2B}.
$$

::: pf-proof
Since
$$
d(e^{ix^2})=2ix e^{ix^2}\,dx,
$$
integration by parts gives
$$
\int_A^B e^{ix^2}\,dx
=\left[\frac{e^{ix^2}}{2ix}\right]_A^B
+\frac1{2i}\int_A^B\frac{e^{ix^2}}{x^2}\,dx.
$$
Taking absolute values and using $|e^{ix^2}|=1$ yields
$$
\left|\int_A^B e^{ix^2}\,dx\right|
\leq \frac1{2A}+\frac1{2B}
+\frac12\int_A^B\frac{dx}{x^2}
\leq \frac1A+\frac1{2B}.
$$
:::

:::

::: {.pf-step #complex-integral}
The improper integral $\int_0^\infty e^{ix^2}\,dx$ converges.

::: pf-proof
The integral over every finite interval exists because $e^{ix^2}$ is continuous. By [](#tail-bound){.pf-ref}, for $B>A>0$,
$$
\left|\int_A^B e^{ix^2}\,dx\right|
\leq \frac1A+\frac1{2B}
\leq \frac{3}{2A}.
$$
The right-hand side tends to $0$ as $A\to\infty$, uniformly in $B>A$. Thus the Cauchy criterion for improper integrals shows that $\int_0^\infty e^{ix^2}\,dx$ converges.
:::

:::

::: pf-step
Both $\int_0^\infty\cos x^2\,dx$ and $\int_0^\infty\sin x^2\,dx$ converge.

::: pf-proof
For every $R>0$,
$$
\int_0^R e^{ix^2}\,dx
=\int_0^R\cos x^2\,dx
+i\int_0^R\sin x^2\,dx.
$$
By [](#complex-integral){.pf-ref}, the left-hand side has a finite limit as $R\to\infty$. Its real and imaginary parts therefore have finite limits, which are precisely the two stated improper integrals.
:::

:::

:::

:::
