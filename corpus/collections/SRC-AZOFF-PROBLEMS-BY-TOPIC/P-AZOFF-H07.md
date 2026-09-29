---
schema: qual/card@1
id: P-AZOFF-H07
kind: problem
title: Finite Blaschke products take each value in the disk $n$ times
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Each Blaschke factor has modulus one on the unit circle, while all of its
    denominator zeros lie outside the closed disk. Thus |f|=1>|b| on the
    boundary, and Rouché shows f-b has the same number of zeros as f. The
    latter has exactly the n numerator zeros a_k, counted with multiplicity.
---

::: {.problem}
Let $| a _ { k } | < 1 ( k = 1 , 2 , \ldots , n ) , | b | < 1$ and

$$
f ( z ) = { \frac { z - a _ { 1 } } { 1 - { \overline { { a } } } _ { 1 } z } } { \frac { z - a _ { 2 } } { 1 - { \overline { { a } } } _ { 2 } z } } \cdots { \frac { z - a _ { n } } { 1 - { \overline { { a } } } _ { n } z } } .
$$

Show that $f(z) = b$ has $n$ solutions in $\abs{z} < 1$.
:::

::: {.solution}
For $1\leq k\leq n$, set
$$
\phi_k(z)
=
\frac{z-a_k}{1-\overline{a_k}z},
$$
so that
$$
f(z)=\prod_{k=1}^{n}\phi_k(z).
$$

::: pf

::: {.pf-step #s1}

Every denominator
$$
1-\overline{a_k}z
$$
is nonzero on the closed unit disk.

::: pf-proof

If $\abs{z}\leq1$, then
$$
\abs{\overline{a_k}z}
\leq
\abs{a_k}
<
1.
$$
Hence $\overline{a_k}z\neq1$, so the denominator cannot vanish.

:::

:::

::: {.pf-step #s2}

If $\abs{z}=1$, then
$$
\abs{\phi_k(z)}=1
$$
for every $k$.

::: pf-proof

For $\abs{z}=1$,
$$
z-a_k
=
z(1-a_k\overline{z}).
$$
Taking moduli and using $\abs{z}=1$ gives
$$
\abs{z-a_k}
=
\abs{1-a_k\overline{z}}.
$$
But
$$
\abs{1-a_k\overline{z}}
=
\abs{\overline{1-\overline{a_k}z}}
=
\abs{1-\overline{a_k}z}.
$$
Therefore the numerator and denominator of $\phi_k$ have equal modulus.

:::

:::

::: {.pf-step #s3}

On the unit circle,
$$
\abs{f(z)}=1.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\abs{f(z)}
=
\prod_{k=1}^{n}\abs{\phi_k(z)}
=
1.
$$

:::

:::

::: {.pf-step #s4}

The function $f$ has exactly $n$ zeros in the open unit disk,
counting multiplicity.

::: pf-proof

By step [](#s1){.pf-ref}, none of the denominators vanishes in the closed unit disk.
Thus the zeros of $f$ there come exactly from the numerator factors
$$
z-a_1,\ldots,z-a_n.
$$
Each $a_k$ lies in the open unit disk by hypothesis. Counting repeated
values among the $a_k$ with their multiplicities gives exactly $n$ zeros.

:::

:::

::: {.pf-step #s5}

On the unit circle,
$$
\abs{b}<\abs{f(z)}.
$$

::: pf-proof

The hypothesis gives $\abs{b}<1$, while step [](#s3){.pf-ref} gives
$\abs{f(z)}=1$.

:::

:::

::: {.pf-step #s6}

The equation
$$
f(z)=b
$$
has exactly $n$ solutions in the open unit disk, counting multiplicity.

::: pf-proof

The functions $f$ and $f-b$ are holomorphic on a neighborhood of the closed
unit disk by step [](#s1){.pf-ref}. Step [](#s5){.pf-ref} is the strict Rouché inequality
$$
\abs{(f-b)-f}
=
\abs{b}
<
\abs{f}
$$
on the unit circle. Hence $f-b$ and $f$ have the same number of zeros in
the unit disk, counting multiplicity. Step [](#s4){.pf-ref} says that this number is
$n$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required conclusion.

:::

:::

:::
