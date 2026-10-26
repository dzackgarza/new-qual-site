---
schema: qual/card@1
id: P-UCLAB04S-02
kind: problem
title: Uniform continuity of the square-root function on the half-line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Exam Spring 2004 PDF.
---

::: {.problem}
Is
\[
f(x)=\sqrt{x}
\]
uniformly continuous on $[0,\infty)$?
Prove your assertion.
:::

Yes.

::: pf

::: pf-step

For all $x,y\ge0$,
\[
\boxed{
|\sqrt{x}-\sqrt{y}|
\le
\sqrt{|x-y|}
}.
\]


::: pf-proof

Assume without loss of generality that
\[
x\ge y.
\]
Then
\[
\sqrt{x}-\sqrt{y}\ge0.
\]
Squaring gives
\[
(\sqrt{x}-\sqrt{y})^2
=
x+y-2\sqrt{xy}.
\]
Since
\[
x\ge y,
\]
one has
\[
\sqrt{xy}\ge y.
\]
Therefore
\[
(\sqrt{x}-\sqrt{y})^2
\le
x+y-2y
=
x-y
=
|x-y|.
\]
Both sides are nonnegative, so taking square roots gives the desired inequality.

:::

:::

::: pf-step

Let $\varepsilon>0$ and choose
\[
\delta=\varepsilon^2.
\]
If
\[
|x-y|<\delta,
\]
then
\[
|\sqrt{x}-\sqrt{y}|<\varepsilon.
\]


::: pf-proof

By step <1>1,
\[
|\sqrt{x}-\sqrt{y}|
\le
\sqrt{|x-y|}
<
\sqrt{\delta}
=
\varepsilon.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{f(x)=\sqrt{x}\text{ is uniformly continuous on }[0,\infty).}
\]


::: pf-proof

The number
\[
\delta=\varepsilon^2
\]
in step <1>2 depends only on $\varepsilon$, not on the points $x,y$.
Thus step <1>2 is exactly the definition of uniform continuity.

:::

:::

::: pf-qed

Step <1>3 is the required assertion.

:::

:::
