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
Evaluate $\operatorname* { l i m } _ { x \to 0 } { \frac { \cos ( \beta x ) - 1 } { x ^ { 2 } } }$ for $\beta \in \RR$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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

Apply step [](#s1-1){.pf-ref} with
\[
u=\beta x.
\]

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

The standard limit gives
\[
\boxed{
\lim_{y\to0}\frac{\sin y}{y}=1}.
\]


::: pf-proof

This is the basic trigonometric limit.

:::

:::

::: {.pf-step #s1-5}

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
Then \(y\to0\), so apply step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Hence for \(\beta\ne0\),
\[
\boxed{
\lim_{x\to0}
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}}.
\]


::: pf-proof

Take limits in step [](#s1-3){.pf-ref} and use step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

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

::: {.pf-step #s1-8}

Therefore for every \(\beta\in\RR\),
\[
\boxed{
\lim_{x\to0}
\frac{\cos(\beta x)-1}{x^2}
=
-\frac{\beta^2}{2}}.
\]


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested limit.

:::

:::

:::
