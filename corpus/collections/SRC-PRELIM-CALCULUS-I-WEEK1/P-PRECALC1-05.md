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
Let $f(x) = |x| + 3x^2$ for $x \in \RR$. What is $f'(-1)$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In a neighborhood of
\[
x=-1,
\]
one has
\[
\boxed{|x|=-x}.
\]


::: pf-proof

Every \(x\) sufficiently close to \(-1\) is negative, and for \(x<0\),
\[
|x|=-x.
\]

:::

:::

::: {.pf-step #s1-2}

Therefore, near \(x=-1\),
\[
f(x)
=
-x+3x^2.
\]


::: pf-proof

Substitute step [](#s1-1){.pf-ref} into
\[
f(x)=|x|+3x^2.
\]

:::

:::

::: {.pf-step #s1-3}

Hence
\[
\boxed{
f'(x)=-1+6x}
\]
for \(x\) near \(-1\).


::: pf-proof

Differentiate the polynomial expression from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Evaluating at \(-1\),
\[
\boxed{
f'(-1)=-1+6(-1)=-7}.
\]


::: pf-proof

Substitute \(x=-1\) into step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested derivative.

:::

:::

:::
