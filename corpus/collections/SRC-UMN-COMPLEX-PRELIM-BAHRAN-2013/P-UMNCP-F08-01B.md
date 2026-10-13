---
schema: qual/card@1
id: P-UMNCP-F08-01B
kind: problem
title: Count zeros of z seventh plus z cubed plus one sixteenth
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
  note: Checked against Fall 2008, 1b as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Determine the number of zeros of
\[
P(z)=z^7+z^3+\frac1{16}
\]
in the closed disk \(|z|\le\frac12\).
:::

::: {.solution}
<1>1. On the circle
$$
|z|=\frac12,
$$
one has
$$
\left|
z^7+\frac1{16}
\right|
<
|z^3|.
$$

::: {.proof}
If
$$
|z|=\frac12,
$$
then
$$
|z^3|
=
\frac18.
$$
Also,
$$
\left|
z^7+\frac1{16}
\right|
\le
|z|^7+\frac1{16}
=
\frac1{128}
+\frac8{128}
=
\frac9{128}.
$$
Since
$$
\frac9{128}
<
\frac{16}{128}
=
\frac18,
$$
the desired strict inequality follows.
:::

<1>2. The polynomial $P$ and the monomial
$$
z^3
$$
have the same number of zeros in
$$
|z|<\frac12,
$$
counted with multiplicity.

::: {.proof}
Write
$$
P(z)
=
z^3
+
\left(
z^7+\frac1{16}
\right).
$$
Step <1>1 gives the strict Rouché inequality on the boundary circle. Hence Rouché's theorem applies.
:::

<1>3. The polynomial $P$ has exactly three zeros in
$$
|z|<\frac12,
$$
counted with multiplicity.

::: {.proof}
The function
$$
z^3
$$
has a zero of multiplicity $3$ at the origin and no other zeros. Step <1>2 transfers this zero count to $P$.
:::

<1>4. The polynomial $P$ has no zeros on
$$
|z|=\frac12.
$$

::: {.proof}
If
$$
P(z)=0
$$
on the boundary circle, then
$$
z^3
=
-\left(
z^7+\frac1{16}
\right),
$$
so the two sides would have equal modulus. This contradicts the strict inequality in step <1>1.
:::

<1>5. Therefore the number of zeros in the closed disk
$$
|z|\le\frac12
$$
is
$$
\boxed{3}.
$$

::: {.proof}
Step <1>3 counts the interior zeros and step <1>4 shows that no additional zeros lie on the boundary.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required answer.
:::
:::
