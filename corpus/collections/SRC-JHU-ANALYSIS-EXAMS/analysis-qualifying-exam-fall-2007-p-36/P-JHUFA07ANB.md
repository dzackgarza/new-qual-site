---
schema: qual/card@1
id: P-JHUFA07ANB
kind: problem
title: "Entire functions bounded by the exponential"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the pointwise coefficient-one exponential bound with Fall 2007 problem 2 on PDF page 36; removed the trailing opening-parenthesis fragment."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked holomorphy and boundedness of the quotient and necessity and sufficiency of the closed unit-disk restriction on the constant."
---

::: {.problem}
2) Find all entire analytic functions satisfying $| f ( z ) | \leq | e ^ { z } |$ for all $z \in \mathbb { C }$
:::

::: {.solution}
The functions are exactly $\boxed{f(z)=ce^z,\ |c|\leq1}$.

<1>1. The quotient by the exponential is a bounded entire function.

::: {.proof}
Since $e^{-z}$ is entire, $h(z)=f(z)e^{-z}$ is entire.
The given inequality implies
$$
|h(z)|=|f(z)|/|e^z|\leq1
$$
for every $z$, using $e^z\ne0$. Liouville's theorem
therefore gives $h=c$ for a constant $c$ with $|c|\leq1$
[@SS03]. Thus $f(z)=ce^z$.
:::

<1>2. Every such constant gives an admissible function.

::: {.proof}
For $|c|\leq1$, the function $ce^z$ is entire and
$|ce^z|=|c||e^z|\leq|e^z|$ everywhere. Hence every
listed function satisfies the hypothesis, completing
both directions of the classification.
:::
:::
