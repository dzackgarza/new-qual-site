---
schema: qual/card@1
id: P-UMNCP-F12-08C
kind: problem
title: Count zeros using Schwarz and Rouche
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
  note: Checked against Fall 2012, 8c as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f\) be holomorphic on the unit disk \(\mathbb D\), with \(f(0)=0\) and \(|f(z)|\le1\). Prove that for every integer \(m\ge1\),
\[
f(z)-2^m z^m
\]
has exactly \(m\) zeros, counted with multiplicity, in \(|z|<\frac12\).
:::

Fix
$$
m\ge1
$$
and set
$$
F_m(z)
\coloneqq
f(z)-2^mz^m.
$$

::: pf

::: pf-step

Schwarz's lemma gives
$$
\boxed{|f(z)|\le|z|}
$$
for every
$$
z\in\mathbb D.
$$


::: pf-proof

The function $f$ is holomorphic on the unit disk, satisfies
$$
f(0)=0,
$$
and has
$$
|f(z)|\le1.
$$
These are the hypotheses of Schwarz's lemma.

:::

:::

::: pf-step

On the circle
$$
|z|=\frac12,
$$
one has
$$
|f(z)|
<
|2^mz^m|.
$$


::: pf-proof

By step <1>1,
$$
|f(z)|
\le
|z|
=
\frac12.
$$
On the other hand,
$$
|2^mz^m|
=
2^m
\left(
\frac12
\right)^m
=1.
$$
Thus
$$
|f(z)|
\le
\frac12
<1
=
|2^mz^m|.
$$

:::

:::

::: pf-step

The functions
$$
F_m(z)
=
-2^mz^m+f(z)
$$
and
$$
-2^mz^m
$$
have the same number of zeros in
$$
|z|<\frac12,
$$
counted with multiplicity.


::: pf-proof

Step <1>2 gives the strict Rouché inequality on the boundary circle. Both functions are holomorphic on a neighborhood of the closed disk, so Rouché's theorem applies.

:::

:::

::: pf-step

The function $F_m$ has exactly
$$
\boxed{m}
$$
zeros in
$$
|z|<\frac12,
$$
counted with multiplicity.


::: pf-proof

The comparison function
$$
-2^mz^m
$$
has a zero of multiplicity $m$ at the origin and no other zeros. Step <1>3 transfers this zero count to $F_m$.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
