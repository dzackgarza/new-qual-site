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
2) Find all entire analytic functions satisfying $\abs{ f ( z ) } \leq \abs{ e ^ { z } }$ for all $z \in \CC$
:::

::: {.solution}
The functions are exactly $\boxed{f(z)=ce^z,\ \abs{c}\leq1}$.

::: pf

::: pf-step
The quotient by the exponential is a bounded entire function.

::: pf-proof
Since $e^{-z}$ is entire, $h(z)=f(z)e^{-z}$ is entire.
The given inequality implies
$$
\abs{h(z)}=\abs{f(z)}/\abs{e^z}\leq1
$$
for every $z$, using $e^z\ne0$. Liouville's theorem
therefore gives $h=c$ for a constant $c$ with $\abs{c}\leq1$
[@SS03]. Thus $f(z)=ce^z$.
:::

:::

::: pf-step
Every such constant gives an admissible function.

::: pf-proof
For $\abs{c}\leq1$, the function $ce^z$ is entire and
$\abs{ce^z}=\abs{c}\abs{e^z}\leq\abs{e^z}$ everywhere. Hence every
listed function satisfies the hypothesis, completing
both directions of the classification.
:::

:::

:::
:::
