---
schema: qual/card@1
id: P-PRECALC1-20
kind: problem
title: Derivative of $\int_0^{x^2}e^{-t^2}\,dt$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute the derivative $\frac { d } { d x } \int _ { 0 } ^ { x ^ { 2 } } e ^ { - t ^ { 2 } } d t$
:::

Define
\[
F(u)
=
\int_0^u e^{-t^2}\,dt.
\]

::: pf

::: pf-step

By the fundamental theorem of calculus,
\[
\boxed{
F'(u)=e^{-u^2}}.
\]


::: pf-proof

The integrand \(e^{-t^2}\) is continuous on \(\mathbb R\).

:::

:::

::: pf-step

The given function is
\[
\boxed{
F(x^2)}.
\]


::: pf-proof

Substitute \(u=x^2\) into the definition of \(F\).

:::

:::

::: pf-step

By the chain rule,
\[
\frac{d}{dx}F(x^2)
=
F'(x^2)\cdot2x.
\]


::: pf-proof

Differentiate the composition \(F\circ(x\mapsto x^2)\).

:::

:::

::: pf-step

Using step <1>1,
\[
F'(x^2)
=
e^{-(x^2)^2}
=
e^{-x^4}.
\]


::: pf-proof

Substitute \(u=x^2\) into
\[
F'(u)=e^{-u^2}.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac{d}{dx}
\int_0^{x^2}e^{-t^2}\,dt
=
2x\,e^{-x^4}}.
\]


::: pf-proof

Combine steps <1>3--<1>4.

:::

:::

::: pf-qed

Step <1>5 is the requested derivative.

:::

:::
