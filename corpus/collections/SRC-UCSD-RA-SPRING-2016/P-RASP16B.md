---
schema: qual/card@1
id: P-RASP16B
kind: problem
title: "Compute a Lebesgue-Stieltjes measure from its distribution function"
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
---

::: problem
Let $\mu$ be the Lebesgue-Stieltjes measure associated to the increasing and right-continuous function $F : \mathbb{R} \to \mathbb{R}$:
$$
F(x) = \begin{cases} 0 & \text{if } x < 0, \\ x + 2 & \text{if } 0 \leq x < 1, \\ 4x^2 & \text{if } 1 \leq x < \infty. \end{cases}
$$

Calculate $\mu((-\infty, 0])$, $\mu(\{1\})$, and $\mu([1, 2])$.
:::

::: {.solution}
<1>1. For a Lebesgue–Stieltjes measure $\mu$ associated to a right-continuous increasing $F$, $\mu((a, b]) = F(b) - F(a)$ and $\mu(\{x\}) = F(x) - F(x^-)$.
::: {.proof}
standard properties of the Lebesgue–Stieltjes measure.
:::

<1>2. $\mu((-\infty, 0]) = F(0) - \lim_{x \to -\infty} F(x) = (0 + 2) - 0 = 2$.
::: {.proof}
$F(0) = 2$ (using the $0 \le x < 1$ branch) and $F(x) \to 0$ as $x \to -\infty$.
:::

<1>3. $\mu(\{1\}) = F(1) - F(1^-)$.
<2>1. $F(1) = 4(1)^2 = 4$.
::: {.proof}
the $1 \le x < \infty$ branch.
:::
<2>2. $F(1^-) = \lim_{x \to 1^-} (x + 2) = 3$.
::: {.proof}
the $0 \le x < 1$ branch.
:::
<2>3. Hence $\mu(\{1\}) = 4 - 3 = 1$.
::: {.proof}
<2>1 and <2>2.
:::

<1>4. $\mu([1, 2]) = \mu(\{1\}) + \mu((1, 2]) = 1 + (F(2) - F(1))$.
::: {.proof}
split $[1,2]$ into $\{1\}$ and $(1,2]$.
:::

<1>5. $F(2) = 4(2)^2 = 16$ and $F(1) = 4$, so $\mu((1,2]) = 16 - 4 = 12$.
::: {.proof}
the $1 \le x < \infty$ branch.
:::

<1>6. Hence $\mu([1,2]) = 1 + 12 = 13$.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
$\mu((-\infty,0]) = 2$, $\mu(\{1\}) = 1$, $\mu([1,2]) = 13$ (<1>2, <1>3, <1>6).
:::
:::
