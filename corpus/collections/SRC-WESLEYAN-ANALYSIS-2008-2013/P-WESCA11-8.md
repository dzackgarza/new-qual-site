---
schema: qual/card@1
id: P-WESCA11-8
kind: problem
title: 'Count roots of $z^4-6z+3$ in an annulus'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
How many roots of
$$
z^4-6z+3=0
$$
have absolute value strictly between $1$ and $2$?
:::

::: {.solution}

Let
$$
P(z)=z^4-6z+3.
$$

::: pf

::: {.pf-step #s1-1}

The polynomial $P$ has exactly one zero in the disk
$$
\abs{z}<1.
$$


::: pf-proof

On the circle
$$
\abs{z}=1,
$$
write
$$
P(z)
=
-6z+(z^4+3).
$$
Then
$$
\abs{-6z}
=
6,
$$
while
$$
\abs{z^4+3}
\le
\abs{z}^4+3
=
4.
$$
Thus
$$
\abs{z^4+3}
<
\abs{-6z}
$$
on the entire unit circle.

By Rouché's theorem, $P$ and
$$
-6z
$$
have the same number of zeros in
$$
\abs{z}<1,
$$
counted with multiplicity. The latter has exactly one zero there, namely
$$
z=0.
$$
Hence $P$ has exactly one zero in the unit disk.

:::

:::

::: {.pf-step #s1-2}

The polynomial $P$ has exactly four zeros in the disk
$$
\abs{z}<2.
$$


::: pf-proof

On the circle
$$
\abs{z}=2,
$$
write
$$
P(z)
=
z^4+(-6z+3).
$$
Then
$$
\abs{z^4}
=
16,
$$
while
$$
\abs{-6z+3}
\le
6\abs{z}+3
=
15.
$$
Thus
$$
\abs{-6z+3}
<
\abs{z^4}
$$
on the entire circle.

By Rouché's theorem, $P$ and
$$
z^4
$$
have the same number of zeros in
$$
\abs{z}<2,
$$
counted with multiplicity. The polynomial $z^4$ has four zeros there,
counted with multiplicity. Therefore $P$ has four zeros in the disk.

:::

:::

::: {.pf-step #s1-3}

The polynomial has no zero on either boundary circle
$$
\abs{z}=1
\qquad\text{or}\qquad
\abs{z}=2.
$$


::: pf-proof

The strict Rouché inequalities in steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} imply that on each
boundary circle the dominant term has strictly larger modulus than the
remaining terms. Hence their sum cannot vanish there.

:::

:::

::: {.pf-step #s1-4}

Exactly
$$
\boxed{3}
$$
roots of $P$ have modulus strictly between $1$ and $2$.


::: pf-proof

Step [](#s1-2){.pf-ref} gives four zeros in
$$
\abs{z}<2,
$$
and step [](#s1-1){.pf-ref} gives one zero in
$$
\abs{z}<1.
$$
By step [](#s1-3){.pf-ref}, no zero lies on either boundary circle. Therefore the annulus
$$
1<\abs{z}<2
$$
contains
$$
4-1=3
$$
zeros, counted with multiplicity.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested count.

:::

:::

:::
