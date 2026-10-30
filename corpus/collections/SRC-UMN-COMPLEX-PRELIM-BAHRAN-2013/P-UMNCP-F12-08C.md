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
Let $f$ be holomorphic on the unit disk $\DD$, with $f(0)=0$ and $\abs{f(z)}\le1$. Prove that for every integer $m\ge1$,
$$
f(z)-2^m z^m
$$
has exactly $m$ zeros, counted with multiplicity, in $\abs{z}<\frac12$.
:::

::: {.solution}

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

::: {.pf-step #s1-1}

Schwarz's lemma gives
$$
\boxed{\abs{f(z)}\le\abs{z}}
$$
for every
$$
z\in\DD.
$$


::: pf-proof

The function $f$ is holomorphic on the unit disk, satisfies
$$
f(0)=0,
$$
and has
$$
\abs{f(z)}\le1.
$$
These are the hypotheses of Schwarz's lemma.

:::

:::

::: {.pf-step #s1-2}

On the circle
$$
\abs{z}=\frac12,
$$
one has
$$
\abs{f(z)}
<
\abs{2^mz^m}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{f(z)}
\le
\abs{z}
=
\frac12.
$$
On the other hand,
$$
\abs{2^mz^m}
=
2^m
\left(
\frac12
\right)^m
=1.
$$
Thus
$$
\abs{f(z)}
\le
\frac12
<1
=
\abs{2^mz^m}.
$$

:::

:::

::: {.pf-step #s1-3}

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
\abs{z}<\frac12,
$$
counted with multiplicity.


::: pf-proof

Step [](#s1-2){.pf-ref} gives the strict Rouché inequality on the boundary circle. Both functions are holomorphic on a neighborhood of the closed disk, so Rouché's theorem applies.

:::

:::

::: {.pf-step #s1-4}

The function $F_m$ has exactly
$$
\boxed{m}
$$
zeros in
$$
\abs{z}<\frac12,
$$
counted with multiplicity.


::: pf-proof

The comparison function
$$
-2^mz^m
$$
has a zero of multiplicity $m$ at the origin and no other zeros. Step [](#s1-3){.pf-ref} transfers this zero count to $F_m$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
