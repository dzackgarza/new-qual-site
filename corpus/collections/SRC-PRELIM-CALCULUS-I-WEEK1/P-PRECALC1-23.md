---
schema: qual/card@1
id: P-PRECALC1-23
kind: problem
title: Real roots of $2x^5+8x-7$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
How many real roots does $2 x ^ { 5 } + 8 x - 7$ have?
:::

::: {.solution}
Let
\[
p(x)=2x^5+8x-7.
\]

<1>1. The derivative is
\[
\boxed{
p'(x)=10x^4+8}.
\]

::: {.proof}
Differentiate term by term.
:::

<1>2. For every real \(x\),
\[
\boxed{
p'(x)>0}.
\]

::: {.proof}
Since
\[
x^4\ge0,
\]
one has
\[
10x^4+8\ge8>0.
\]
:::

<1>3. Hence \(p\) is strictly increasing on \(\mathbb R\).

::: {.proof}
A differentiable function whose derivative is everywhere positive is
strictly increasing.
:::

<1>4. Therefore \(p\) has at most one real root.

::: {.proof}
A strictly increasing function cannot take the same value, in particular the
value \(0\), at two distinct points.
:::

<1>5. One has
\[
\boxed{
p(0)=-7<0}.
\]

::: {.proof}
Substitute \(x=0\).
:::

<1>6. One has
\[
\boxed{
p(1)=3>0}.
\]

::: {.proof}
\[
p(1)
=
2+8-7
=
3.
\]
:::

<1>7. By the intermediate value theorem, \(p\) has a real root in
\[
(0,1).
\]

::: {.proof}
The polynomial \(p\) is continuous, and steps <1>5--<1>6 show a sign
change between \(0\) and \(1\).
:::

<1>8. Combining existence and uniqueness,
\[
\boxed{
p(x)=2x^5+8x-7
\text{ has exactly one real root}.}
\]

::: {.proof}
Existence is step <1>7 and uniqueness is step <1>4.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 gives the requested number of real roots.
:::
:::
