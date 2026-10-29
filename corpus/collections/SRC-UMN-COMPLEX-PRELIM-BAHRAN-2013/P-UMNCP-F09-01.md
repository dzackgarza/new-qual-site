---
schema: qual/card@1
id: P-UMNCP-F09-01
kind: problem
title: Count zeros of six z cubed plus exponential z plus one
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
  note: Checked against Fall 2009, 1 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
How many roots, counted with multiplicity, does
$$
g(z)=6z^3+e^z+1
$$
have in the unit disk $|z|<1$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

On the unit circle,
$$
|e^z+1|<|6z^3|.
$$


::: pf-proof

If
$$
|z|=1,
$$
then
$$
|6z^3|=6.
$$
Also
$$
|e^z|
=
e^{\operatorname{Re}z}
\le
e,
$$
because
$$
\operatorname{Re}z\le|z|=1.
$$
Hence
$$
|e^z+1|
\le
|e^z|+1
\le
e+1
<6.
$$

:::

:::

::: {.pf-step #s1-2}

The functions
$$
g(z)=6z^3+e^z+1
$$
and
$$
6z^3
$$
have the same number of zeros in
$$
|z|<1,
$$
counted with multiplicity.


::: pf-proof

Step [](#s1-1){.pf-ref} gives the strict Rouché inequality
$$
|e^z+1|<|6z^3|
$$
on the boundary circle. Rouché's theorem therefore applies.

:::

:::

::: {.pf-step #s1-3}

The function $g$ has exactly
$$
\boxed{3}
$$
zeros in the unit disk, counted with multiplicity.


::: pf-proof

The comparison function
$$
6z^3
$$
has a zero of multiplicity $3$ at $z=0$ and no other zeros. By step [](#s1-2){.pf-ref}, $g$ has the same zero count in $|z|<1$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required number of roots.

:::

:::

:::
