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

::: {.solution}
<1>1. Combine the two fractions:
\[
\boxed{
x^{-2}-\sin(x)^{-2}
=
\frac{\sin^2x-x^2}{x^2\sin^2x}}.
\]

::: {.proof}
Use a common denominator:
\[
\frac1{x^2}-\frac1{\sin^2x}
=
\frac{\sin^2x-x^2}{x^2\sin^2x}.
\]
:::

<1>2. Factor the numerator:
\[
\sin^2x-x^2
=
(\sin x-x)(\sin x+x).
\]

::: {.proof}
Apply the difference-of-squares identity.
:::

<1>3. Therefore
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

::: {.proof}
Multiply the three factors on the right:
\[
\frac{x^2(\sin x+x)(\sin x-x)}
{\sin^2x\cdot x\cdot x^3}
=
\frac{\sin^2x-x^2}{x^2\sin^2x}.
\]
:::

<1>4. The first factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{x^2}{\sin^2x}
=
1}.
\]

::: {.proof}
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

<1>5. The second factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{\sin x+x}{x}
=
2}.
\]

::: {.proof}
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

<1>6. For the third factor,
\[
\lim_{x\to0}
\frac{\sin x-x}{x^3}
=
\lim_{x\to0}
\frac{\cos x-1}{3x^2}.
\]

::: {.proof}
Both numerator and denominator tend to \(0\). Apply l’Hôpital’s rule once.
:::

<1>7. Applying l’Hôpital’s rule again,
\[
\lim_{x\to0}
\frac{\cos x-1}{3x^2}
=
\lim_{x\to0}
\frac{-\sin x}{6x}.
\]

::: {.proof}
Again both numerator and denominator tend to \(0\).
:::

<1>8. Hence
\[
\boxed{
\lim_{x\to0}
\frac{\sin x-x}{x^3}
=
-\frac16}.
\]

::: {.proof}
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

<1>9. Combining the three factor limits,
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

::: {.proof}
Use steps <1>1, <1>3, <1>4, <1>5, and <1>8.
:::

<1>10. Therefore
\[
\boxed{
\lim_{x\to0}
\left(
x^{-2}-\sin(x)^{-2}
\right)
=
-\frac13}.
\]

::: {.proof}
This is step <1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the requested limit.
:::
:::
