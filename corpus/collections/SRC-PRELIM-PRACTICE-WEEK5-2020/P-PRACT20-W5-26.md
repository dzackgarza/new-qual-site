---
schema: qual/card@1
id: P-PRACT20-W5-26
kind: problem
title: Contour integral of a polynomial around a circle
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 26).
---

::: {.problem}
Let $r > 0$ and let $P : \CC \to \CC$ be a polynomial. What is $\oint_{\{\abs{z} = r\}} P(z)\,dz$?
:::

::: {.solution}

::: pf

::: pf-step

The polynomial $P$ is holomorphic on all of $\CC$.


::: pf-proof

Every complex polynomial is entire.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{\oint_{\abs{z}=r}P(z)\,dz=0}.
$$


::: pf-proof

The circle $\abs{z}=r$ is a closed contour whose interior lies in the domain
$\CC$ on which $P$ is holomorphic. Cauchy's integral theorem therefore
gives zero.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} is the requested value.

:::

:::

:::
