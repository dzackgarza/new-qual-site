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
<1>1. The polynomial $P$ is holomorphic on all of $\mathbb C$.

::: {.proof}
Every complex polynomial is entire.
:::

<1>2. Therefore
\[
\boxed{\oint_{|z|=r}P(z)\,dz=0}.
\]

::: {.proof}
The circle $|z|=r$ is a closed contour whose interior lies in the domain
$\mathbb C$ on which $P$ is holomorphic. Cauchy's integral theorem therefore
gives zero.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the requested value.
:::
:::
