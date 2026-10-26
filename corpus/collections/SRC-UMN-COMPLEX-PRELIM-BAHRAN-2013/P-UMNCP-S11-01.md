---
schema: qual/card@1
id: P-UMNCP-S11-01
kind: problem
title: A polynomial az to n plus z plus one has a root in radius two
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2011, 1 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Prove that for every \(a\in\mathbb C\) and every integer \(n\ge2\), the polynomial
\[
az^n+z+1
\]
has at least one root in \(|z|\le2\).
:::

Let
$$
p(z)=az^n+z+1.
$$

::: pf

::: pf-step

If $a=0$, then $p$ has the root
$$
z=-1,
$$
which lies in $|z|\le2$.


::: pf-proof

If $a=0$, then
$$
p(z)=z+1.
$$
Its unique root is $-1$.

:::

:::

::: pf-step

Assume $a\ne0$ and, toward a contradiction, suppose every root
$$
r_1,\ldots,r_n
$$
of $p$ satisfies
$$
|r_j|>2.
$$
Then
$$
\boxed{|a|<2^{-n}}.
$$


::: pf-proof

Since $a\ne0$, the polynomial has degree $n$. By Viète's formula,
$$
r_1r_2\cdots r_n
=
(-1)^n\frac1a.
$$
Taking absolute values gives
$$
\frac1{|a|}
=
\prod_{j=1}^n|r_j|
>
2^n.
$$
Hence
$$
|a|<2^{-n}.
$$

:::

:::

::: pf-step

On the circle
$$
|z|=2,
$$
one has
$$
|az^n|<|z+1|.
$$


::: pf-proof

By step <1>2,
$$
|az^n|
=
|a|2^n
<1.
$$
On the other hand, the reverse triangle inequality gives
$$
|z+1|
\ge
||z|-1|
=1.
$$
Therefore
$$
|az^n|<|z+1|
$$
on the whole circle.

:::

:::

::: pf-step

The polynomial $p$ has exactly one zero in
$$
|z|<2,
$$
counted with multiplicity.


::: pf-proof

Write
$$
p(z)
=(z+1)+az^n.
$$
By step <1>3, Rouché's theorem shows that $p$ and $z+1$ have the same number of zeros in $|z|<2$. The function $z+1$ has exactly one such zero, namely $-1$.

:::

:::

::: pf-step

The assumption in step <1>2 is impossible.


::: pf-proof

Step <1>2 assumed that every root of $p$ satisfies
$$
|r_j|>2,
$$
so $p$ would have no root in $|z|<2$. Step <1>4 gives one root there, a contradiction.

:::

:::

::: pf-step

Therefore $p$ has at least one root in
$$
\boxed{|z|\le2}.
$$


::: pf-proof

Step <1>1 handles $a=0$, and steps <1>2--<1>5 handle $a\ne0$.

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
