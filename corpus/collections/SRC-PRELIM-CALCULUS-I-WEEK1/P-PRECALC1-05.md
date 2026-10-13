---
schema: qual/card@1
id: P-PRECALC1-05
kind: problem
title: Derivative of $|x|+3x^2$ at $x=-1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the extraction's \updownarrow with the question mark of Problem 5 on page 1 of Week1_solns.pdf.
---

::: {.problem}
Let $f(x) = |x| + 3x^2$ for $x \in \mathbb{R}$. What is $f'(-1)$?
:::

::: {.solution}
<1>1. In a neighborhood of
\[
x=-1,
\]
one has
\[
\boxed{|x|=-x}.
\]

::: {.proof}
Every \(x\) sufficiently close to \(-1\) is negative, and for \(x<0\),
\[
|x|=-x.
\]
:::

<1>2. Therefore, near \(x=-1\),
\[
f(x)
=
-x+3x^2.
\]

::: {.proof}
Substitute step <1>1 into
\[
f(x)=|x|+3x^2.
\]
:::

<1>3. Hence
\[
\boxed{
f'(x)=-1+6x}
\]
for \(x\) near \(-1\).

::: {.proof}
Differentiate the polynomial expression from step <1>2.
:::

<1>4. Evaluating at \(-1\),
\[
\boxed{
f'(-1)=-1+6(-1)=-7}.
\]

::: {.proof}
Substitute \(x=-1\) into step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested derivative.
:::
:::
