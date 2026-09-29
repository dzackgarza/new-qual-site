---
schema: qual/card@1
id: P-BKS84-4
kind: problem
title: $\pi^3$ versus $3^\pi$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the comparison by monotonicity of $\log x/x$ on $(e,\infty)$.
---

::: {.problem}
Which number is larger,
\[
\pi^3
\qquad\text{or}\qquad
3^\pi?
\]
Justify your answer.
:::

::: {.solution}
::: pf

::: {.pf-step #h-decreasing}
The function
$$
h(x)\coloneqq\frac{\log x}{x}
$$
is strictly decreasing for $x>e$.

::: pf-proof
Differentiation gives
$$
h'(x)
=
\frac{1-\log x}{x^2}.
$$
If $x>e$, then $\log x>1$, so $h'(x)<0$.
:::

:::

::: {.pf-step #h-comparison}
One has
$$
\frac{\log\pi}{\pi}
<
\frac{\log3}{3}.
$$

::: pf-proof
The standard inequalities
$$
e<3<\pi
$$
put both $3$ and $\pi$ in the interval on which step [](#h-decreasing){.pf-ref} shows that
$h$ is strictly decreasing. Since $3<\pi$,
$$
h(\pi)<h(3),
$$
which is the displayed inequality.
:::

:::

::: {.pf-step #larger-number-boxed}
The larger number is
$$
\boxed{3^\pi}.
$$

::: pf-proof
Multiplying the inequality in step [](#h-comparison){.pf-ref} by the positive number $3\pi$
gives
$$
3\log\pi<\pi\log3.
$$
Exponentiation, which is strictly increasing, yields
$$
\pi^3
=
e^{3\log\pi}
<
e^{\pi\log3}
=
3^\pi.
$$
:::

:::

::: pf-qed
Step [](#larger-number-boxed){.pf-ref} gives the requested comparison.
:::

:::
:::
