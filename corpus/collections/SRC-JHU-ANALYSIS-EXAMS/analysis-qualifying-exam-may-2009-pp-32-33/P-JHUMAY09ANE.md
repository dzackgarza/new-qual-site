---
schema: qual/card@1
id: P-JHUMAY09ANE
kind: problem
title: 'Convolution of two $L^2$ functions is bounded and continuous'
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, May 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f,g\in L^2(\mathbb R)$. Prove that
\[
(f*g)(x)=\int_{\mathbb R}f(y)g(x-y)\,dy
\]
defines a bounded continuous function on $\mathbb R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The convolution is bounded, with
$$
\|f*g\|_\infty\le\|f\|_2\|g\|_2.
$$

::: pf-proof

For each $x$, the [[FF-4XBYG|Cauchy--Schwarz inequality in $L^2$]] and translation invariance of the $L^2$ norm give
$$
|(f*g)(x)|\le \|f\|_2\,\|g(x-\cdot)\|_2=\|f\|_2\|g\|_2.
$$
Taking the supremum over $x$ proves the claim.

:::

:::

::: {.pf-step #s2}

The convolution is uniformly continuous.

::: pf-proof

For $h\in\mathbb R$,
$$
(f*g)(x+h)-(f*g)(x)
=\int_{\mathbb R}f(y)\bigl(g(x+h-y)-g(x-y)\bigr)\,dy.
$$
Applying Cauchy--Schwarz again gives, uniformly in $x$,
$$
|(f*g)(x+h)-(f*g)(x)|
\le\|f\|_2\,\|g(\cdot+h)-g\|_2.
$$
By [[PR-JX4YU|continuity of translation in $L^p$]], the final norm tends to $0$ as $h\to0$. The bound is independent of $x$, so $f*g$ is uniformly continuous, hence continuous.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves boundedness and step [](#s2){.pf-ref} proves continuity.

:::

:::

:::
