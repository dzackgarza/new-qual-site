---
schema: qual/card@1
id: P-PRECALC1-06
kind: problem
title: Limit of $x^{-2}-\sin(x)^{-2}$ as $x\to0$
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
  note: Restored the lost arrow in the limit of Problem 6 on page 1 of Week1_solns.pdf.
---

::: {.problem}
Compute the limit $\lim_{x \to 0} (x^{-2} - \sin(x)^{-2})$.
:::

::: pf

::: pf-step

Combine the two fractions:
\[
\boxed{
x^{-2}-\sin(x)^{-2}
=
\frac{\sin^2x-x^2}{x^2\sin^2x}}.
\]


::: pf-proof

Use a common denominator:
\[
\frac1{x^2}-\frac1{\sin^2x}
=
\frac{\sin^2x-x^2}{x^2\sin^2x}.
\]

:::

:::

::: pf-step

Factor the numerator:
\[
\sin^2x-x^2
=
(\sin x-x)(\sin x+x).
\]


::: pf-proof

Apply the difference-of-squares identity.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac{\sin^2x-x^2}{x^2\sin^2x}
=
\frac{x^2}{\sin^2x}
\cdot
\frac{\sin x+x}{x}
\cdot
\frac{\sin x-x}{x^3}}.
\]


::: pf-proof

Multiply the three factors on the right:
\[
\frac{x^2(\sin x+x)(\sin x-x)}
{\sin^2x\cdot x\cdot x^3}
=
\frac{\sin^2x-x^2}{x^2\sin^2x}.
\]

:::

:::

::: pf-step

The first factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{x^2}{\sin^2x}
=
1}.
\]


::: pf-proof

The standard limit
\[
\frac{\sin x}{x}\to1
\]
implies
\[
\frac{x}{\sin x}\to1.
\]
Square.

:::

:::

::: pf-step

The second factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{\sin x+x}{x}
=
2}.
\]


::: pf-proof

\[
\frac{\sin x+x}{x}
=
\frac{\sin x}{x}+1
\to
1+1
=
2.
\]

:::

:::

::: pf-step

For the third factor,
\[
\lim_{x\to0}
\frac{\sin x-x}{x^3}
=
\lim_{x\to0}
\frac{\cos x-1}{3x^2}.
\]


::: pf-proof

Both numerator and denominator tend to \(0\). Apply l’Hôpital’s rule once.

:::

:::

::: pf-step

Applying l’Hôpital’s rule again,
\[
\lim_{x\to0}
\frac{\cos x-1}{3x^2}
=
\lim_{x\to0}
\frac{-\sin x}{6x}.
\]


::: pf-proof

Again both numerator and denominator tend to \(0\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\lim_{x\to0}
\frac{\sin x-x}{x^3}
=
-\frac16}.
\]


::: pf-proof

Using
\[
\frac{\sin x}{x}\to1,
\]
step <1>7 gives
\[
\lim_{x\to0}
\frac{-\sin x}{6x}
=
-\frac16.
\]

:::

:::

::: pf-step

Combining the three factor limits,
\[
\begin{aligned}
\lim_{x\to0}
\left(
x^{-2}-\sin(x)^{-2}
\right)
&=
1\cdot2\cdot\left(-\frac16\right)\\
&=
-\frac13.
\end{aligned}
\]


::: pf-proof

Use steps <1>1, <1>3, <1>4, <1>5, and <1>8.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{x\to0}
\left(
x^{-2}-\sin(x)^{-2}
\right)
=
-\frac13}.
\]


::: pf-proof

This is step <1>9.

:::

:::

::: pf-qed

Step <1>10 is the requested limit.

:::

:::
