---
schema: qual/card@1
id: P-PRECALC1-03
kind: problem
title: Limit of $\frac{\cos(\beta x)-1}{x^2}$ as $x\to0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate $\operatorname* { l i m } _ { x \to 0 } { \frac { \cos ( \beta x ) - 1 } { x ^ { 2 } } }$ for $\beta \in \mathbb { R }$
:::

::: pf

::: pf-step

Use the identity
\[
\boxed{
\cos u-1=-2\sin^2\frac u2}.
\]


::: pf-proof

From
\[
\cos u=1-2\sin^2\frac u2,
\]
subtract \(1\).

:::

:::

::: pf-step

Therefore
\[
\frac{\cos(\beta x)-1}{x^2}
=
-2
\frac{
\sin^2(\beta x/2)
}{
x^2
}.
\]


::: pf-proof

Apply step <1>1 with
\[
u=\beta x.
\]

:::

:::

::: pf-step

Rewrite the quotient as
\[
\boxed{
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}
\left(
\frac{
\sin(\beta x/2)
}{
\beta x/2
}
\right)^2}
\]
when \(\beta x\ne0\).


::: pf-proof

Factor
\[
\sin^2(\beta x/2)
=
\left(
\frac{\beta x}{2}
\right)^2
\left(
\frac{
\sin(\beta x/2)
}{
\beta x/2
}
\right)^2.
\]
Then
\[
-2\frac{(\beta x/2)^2}{x^2}
=
-\frac{\beta^2}{2}.
\]

:::

:::

::: pf-step

The standard limit gives
\[
\boxed{
\lim_{y\to0}\frac{\sin y}{y}=1}.
\]


::: pf-proof

This is the basic trigonometric limit.

:::

:::

::: pf-step

If \(\beta\ne0\), then as \(x\to0\),
\[
\frac{
\sin(\beta x/2)
}{
\beta x/2
}
\longrightarrow1.
\]


::: pf-proof

Set
\[
y=\frac{\beta x}{2}.
\]
Then \(y\to0\), so apply step <1>4.

:::

:::

::: pf-step

Hence for \(\beta\ne0\),
\[
\boxed{
\lim_{x\to0}
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}}.
\]


::: pf-proof

Take limits in step <1>3 and use step <1>5.

:::

:::

::: pf-step

If \(\beta=0\), the quotient is identically \(0\), and the same
formula gives
\[
-\frac{\beta^2}{2}=0.
\]


::: pf-proof

When \(\beta=0\),
\[
\cos(\beta x)-1
=
\cos0-1
=
0.
\]

:::

:::

::: pf-step

Therefore for every \(\beta\in\mathbb R\),
\[
\boxed{
\lim_{x\to0}
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}}.
\]


::: pf-proof

Combine steps <1>6--<1>7.

:::

:::

::: pf-qed

Step <1>8 is the requested limit.

:::

:::
