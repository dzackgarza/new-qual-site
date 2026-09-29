---
schema: qual/card@1
id: P-RASP16B
kind: problem
title: Lebesgue-Stieltjes measure of a piecewise distribution function
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue-Stieltjes Measures
  - Distribution Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing Lebesgue-Stieltjes computation reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $\mu$ be the Lebesgue-Stieltjes measure associated to the increasing and right-continuous function $F : \mathbb{R} \to \mathbb{R}$:
$$
F(x) = \begin{cases} 0 & \text{if } x < 0, \\ x + 2 & \text{if } 0 \leq x < 1, \\ 4x^2 & \text{if } 1 \leq x < \infty. \end{cases}
$$

Calculate $\mu((-\infty, 0])$, $\mu(\{1\})$, and $\mu([1, 2])$.
:::

::: {.solution}

::: pf

::: pf-step

For a Lebesgue–Stieltjes measure $\mu$ associated to a right-continuous increasing $F$, $\mu((a, b]) = F(b) - F(a)$ and $\mu(\{x\}) = F(x) - F(x^-)$.

::: pf-proof

standard properties of the Lebesgue–Stieltjes measure.

:::

:::

::: {.pf-step #s2}

$\mu((-\infty, 0]) = F(0) - \lim_{x \to -\infty} F(x) = (0 + 2) - 0 = 2$.

::: pf-proof

$F(0) = 2$ (using the $0 \le x < 1$ branch) and $F(x) \to 0$ as $x \to -\infty$.

:::

:::

::: {.pf-step #s3}

$\mu(\{1\}) = F(1) - F(1^-)$.

::: pf-proof

::: {.pf-step #s3-1}

$F(1) = 4(1)^2 = 4$.

::: pf-proof

the $1 \le x < \infty$ branch.

:::

:::

::: {.pf-step #s3-2}

$F(1^-) = \lim_{x \to 1^-} (x + 2) = 3$.

::: pf-proof

the $0 \le x < 1$ branch.

:::

:::

::: pf-step

Hence $\mu(\{1\}) = 4 - 3 = 1$.

::: pf-proof

Steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s4}

$\mu([1, 2]) = \mu(\{1\}) + \mu((1, 2]) = 1 + (F(2) - F(1))$.

::: pf-proof

split $[1,2]$ into $\{1\}$ and $(1,2]$.

:::

:::

::: {.pf-step #s5}

$F(2) = 4(2)^2 = 16$ and $F(1) = 4$, so $\mu((1,2]) = 16 - 4 = 12$.

::: pf-proof

the $1 \le x < \infty$ branch.

:::

:::

::: {.pf-step #s6}

Hence $\mu([1,2]) = 1 + 12 = 13$.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

$\mu((-\infty,0]) = 2$, $\mu(\{1\}) = 1$, $\mu([1,2]) = 13$ (steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s6){.pf-ref}).

:::

:::

:::
