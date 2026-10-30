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
$$
f(x)=\sqrt{x}
$$
uniformly continuous on $[0,\infty)$?
Prove your assertion.
:::

::: {.solution}

Yes.

::: pf

::: {.pf-step #s1-1}

For all $x,y\ge0$,
$$
\boxed{
\abs{\sqrt{x}-\sqrt{y}}
\le
\sqrt{\abs{x-y}}
}.
$$


::: pf-proof

Assume without loss of generality that
$$
x\ge y.
$$
Then
$$
\sqrt{x}-\sqrt{y}\ge0.
$$
Squaring gives
$$
(\sqrt{x}-\sqrt{y})^2
=
x+y-2\sqrt{xy}.
$$
Since
$$
x\ge y,
$$
one has
$$
\sqrt{xy}\ge y.
$$
Therefore
$$
(\sqrt{x}-\sqrt{y})^2
\le
x+y-2y
=
x-y
=
\abs{x-y}.
$$
Both sides are nonnegative, so taking square roots gives the desired inequality.

:::

:::

::: {.pf-step #s1-2}

Let $\varepsilon>0$ and choose
$$
\delta=\varepsilon^2.
$$
If
$$
\abs{x-y}<\delta,
$$
then
$$
\abs{\sqrt{x}-\sqrt{y}}<\varepsilon.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{\sqrt{x}-\sqrt{y}}
\le
\sqrt{\abs{x-y}}
<
\sqrt{\delta}
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{f(x)=\sqrt{x}\text{ is uniformly continuous on }[0,\infty).}
$$


::: pf-proof

The number
$$
\delta=\varepsilon^2
$$
in step [](#s1-2){.pf-ref} depends only on $\varepsilon$, not on the points $x,y$.
Thus step [](#s1-2){.pf-ref} is exactly the definition of uniform continuity.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required assertion.

:::

:::

:::
