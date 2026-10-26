---
schema: qual/card@1
id: P-UGAP08S-02
kind: problem
title: Prove $x^3$ is continuous at $2$ from the $\varepsilon$-$\delta$ definition
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Prove from the $\varepsilon$-$\delta$ definition that the function
\[
f:\mathbb R\to\mathbb R,\qquad f(x)=x^3,
\]
is continuous at $2$.
:::

::: pf

::: pf-step

Let
\[
\varepsilon>0
\]
be given.


::: pf-proof

To prove continuity at $2$, we must produce
\[
\delta>0
\]
such that
\[
|x-2|<\delta
\]
implies
\[
|x^3-8|<\varepsilon.
\]

:::

:::

::: pf-step

Factor the difference:
\[
|x^3-8|
=
|x-2|
\,|x^2+2x+4|.
\]


::: pf-proof

Use
\[
x^3-2^3
=
(x-2)(x^2+2x+4).
\]

:::

:::

::: pf-step

If
\[
|x-2|<1,
\]
then
\[
1<x<3.
\]


::: pf-proof

The inequality
\[
|x-2|<1
\]
is equivalent to
\[
-1<x-2<1,
\]
hence
\[
1<x<3.
\]

:::

:::

::: pf-step

Under the same restriction,
\[
|x^2+2x+4|<19.
\]


::: pf-proof

Since
\[
1<x<3,
\]
one has
\[
|x|<3.
\]
Therefore
\[
\begin{aligned}
|x^2+2x+4|
&\le
|x|^2+2|x|+4\\
&<
9+6+4\\
&=
19.
\end{aligned}
\]

:::

:::

::: pf-step

Choose
\[
\boxed{
\delta
=
\min
\left\{
1,
\frac{\varepsilon}{19}
\right\}.
}
\]


::: pf-proof

This choice guarantees both the bound in step <1>4 and the final
\[
\varepsilon
\]
estimate.

:::

:::

::: pf-step

If
\[
|x-2|<\delta,
\]
then
\[
|x^3-8|
<
\varepsilon.
\]


::: pf-proof

Because
\[
\delta\le1,
\]
step <1>4 applies.
Hence
\[
\begin{aligned}
|x^3-8|
&=
|x-2|
\,|x^2+2x+4|\\
&<
19|x-2|\\
&<
19\delta\\
&\le
\varepsilon.
\end{aligned}
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(x)=x^3
\text{ is continuous at }2.
}
\]


::: pf-proof

Step <1>6 is exactly the
\[
\varepsilon\text{--}\delta
\]
definition of continuity at $2$.

:::

:::

::: pf-qed

Step <1>7 is the desired conclusion.

:::

:::
