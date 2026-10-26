---
schema: qual/card@1
id: P-PRECALC1-18
kind: problem
title: Derivative of $g\circ g$ at $0$ for $g(x)=e^{2x+1}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $g ( x ) = e ^ { 2 x + 1 }$ . Compute $\operatorname* { l i m } _ { x \to 0 } { \frac { g ( g ( x ) ) - g ( e ) } { x } }$
:::

Let
\[
h(x)=g(g(x)).
\]

::: pf

::: pf-step

One has
\[
\boxed{
g(0)=e}.
\]


::: pf-proof

\[
g(0)
=
e^{2\cdot0+1}
=
e.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
h(0)=g(e)}.
\]


::: pf-proof

By definition,
\[
h(0)=g(g(0)).
\]
Apply step <1>1.

:::

:::

::: pf-step

The given limit is
\[
\boxed{
\lim_{x\to0}
\frac{h(x)-h(0)}{x}
=
h'(0)}.
\]


::: pf-proof

Step <1>2 identifies the numerator as the standard difference quotient for
\(h\) at \(0\).

:::

:::

::: pf-step

The derivative of \(g\) is
\[
\boxed{
g'(x)=2e^{2x+1}}.
\]


::: pf-proof

Apply the chain rule to
\[
g(x)=e^{2x+1}.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
g'(0)=2e}.
\]


::: pf-proof

Substitute \(x=0\) into step <1>4.

:::

:::

::: pf-step

Also,
\[
\boxed{
g'(e)=2e^{2e+1}}.
\]


::: pf-proof

Substitute \(x=e\) into step <1>4.

:::

:::

::: pf-step

By the chain rule,
\[
h'(0)
=
g'(g(0))\,g'(0).
\]


::: pf-proof

Since
\[
h=g\circ g,
\]
the chain rule gives
\[
h'(x)=g'(g(x))g'(x).
\]
Set \(x=0\).

:::

:::

::: pf-step

Therefore
\[
h'(0)
=
\left(
2e^{2e+1}
\right)
(2e).
\]


::: pf-proof

Use steps <1>1, <1>5, <1>6, and <1>7.

:::

:::

::: pf-step

Simplifying,
\[
\boxed{
h'(0)
=
4e^{2e+2}}.
\]


::: pf-proof

\[
2e^{2e+1}\cdot2e
=
4e^{2e+1+1}
=
4e^{2e+2}.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\lim_{x\to0}
\frac{g(g(x))-g(e)}{x}
=
4e^{2e+2}}.
\]


::: pf-proof

Combine steps <1>3 and <1>9.

:::

:::

::: pf-qed

Step <1>10 is the requested limit.

:::

:::
