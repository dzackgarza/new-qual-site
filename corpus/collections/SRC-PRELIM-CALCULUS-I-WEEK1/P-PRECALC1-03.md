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

::: {.solution}
<1>1. Use the identity
\[
\boxed{
\cos u-1=-2\sin^2\frac u2}.
\]

::: {.proof}
From
\[
\cos u=1-2\sin^2\frac u2,
\]
subtract \(1\).
:::

<1>2. Therefore
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

::: {.proof}
Apply step <1>1 with
\[
u=\beta x.
\]
:::

<1>3. Rewrite the quotient as
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

::: {.proof}
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

<1>4. The standard limit gives
\[
\boxed{
\lim_{y\to0}\frac{\sin y}{y}=1}.
\]

::: {.proof}
This is the basic trigonometric limit.
:::

<1>5. If \(\beta\ne0\), then as \(x\to0\),
\[
\frac{
\sin(\beta x/2)
}{
\beta x/2
}
\longrightarrow1.
\]

::: {.proof}
Set
\[
y=\frac{\beta x}{2}.
\]
Then \(y\to0\), so apply step <1>4.
:::

<1>6. Hence for \(\beta\ne0\),
\[
\boxed{
\lim_{x\to0}
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}}.
\]

::: {.proof}
Take limits in step <1>3 and use step <1>5.
:::

<1>7. If \(\beta=0\), the quotient is identically \(0\), and the same
formula gives
\[
-\frac{\beta^2}{2}=0.
\]

::: {.proof}
When \(\beta=0\),
\[
\cos(\beta x)-1
=
\cos0-1
=
0.
\]
:::

<1>8. Therefore for every \(\beta\in\mathbb R\),
\[
\boxed{
\lim_{x\to0}
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}}.
\]

::: {.proof}
Combine steps <1>6--<1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested limit.
:::
:::
