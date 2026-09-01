---
schema: qual/card@1
id: P-4QQGN
kind: problem
title: Measurability of $f'$ and of the differentiability set of a continuous function
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Measure Theory
relations: []
review: draft
---

::: {.problem}
(1) Let $f(x)$ be a real valued function on the real line that is differentiable almost everywhere.
Prove that $f'(x)$ is a Lebesgue measurable function.

(2) If $f$ is continuous real values function on the real line, then the set of points at which $f$ is differentiable is measurable.
:::

::: {.solution}
$f'(x) = \lim_{n\to\infty} n(f(x+1/n) - f(x))$ if the limit exists.
Then Module a null set, $f'$ is measurable.
Thus, it is measurable.

For the second part, By the similar argument, We know that $D^+f$, $D^-f$, $D_+f$ and $D_-f$ are measurable.
Then $\{x : f'(x) \text{ exsits}\} = \{x : D^+f(x) = D^-f(x) = D_+f(x) = D_-f(x)\}$ is measurable.
:::
