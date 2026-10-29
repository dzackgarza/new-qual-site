---
schema: qual/card@1
id: P-UMNCP-F11-01
kind: problem
title: All zeros of z fifth plus three z cubed plus seven lie in radius two
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
  note: Checked against Fall 2011, 1 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Show that
$$
z^5+3z^3+7
$$
has all of its zeros in the disk $|z|<2$.
:::

::: {.solution}

Let
$$
p(z)=z^5+3z^3+7.
$$

::: pf

::: {.pf-step #s1-1}

On the circle
$$
|z|=2,
$$
one has
$$
|3z^3+7|<|z^5|.
$$


::: pf-proof

If
$$
|z|=2,
$$
then
$$
|z^5|=2^5=32.
$$
By the triangle inequality,
$$
|3z^3+7|
\le
3|z|^3+7
=
3\cdot8+7
=31.
$$
Hence
$$
|3z^3+7|
\le31
<32
=
|z^5|.
$$

:::

:::

::: {.pf-step #s1-2}

The polynomial $p$ and the monomial $z^5$ have the same number of zeros in
$$
|z|<2,
$$
counted with multiplicity.


::: pf-proof

Write
$$
p(z)=z^5+(3z^3+7).
$$
The strict inequality from step [](#s1-1){.pf-ref} holds on the boundary circle
$$
|z|=2.
$$
Rouché's theorem therefore gives the same number of zeros inside the circle for $p$ and $z^5$.

:::

:::

::: {.pf-step #s1-3}

The polynomial $p$ has exactly five zeros in
$$
|z|<2,
$$
counted with multiplicity.


::: pf-proof

The function
$$
z^5
$$
has a zero of multiplicity $5$ at the origin and no other zeros. By step [](#s1-2){.pf-ref}, $p$ also has five zeros in the disk.

:::

:::

::: {.pf-step #s1-4}

Therefore every zero of $p$ lies in
$$
\boxed{|z|<2}.
$$


::: pf-proof

The polynomial $p$ has degree $5$, so by the fundamental theorem of algebra it has exactly five zeros in $\CC$, counted with multiplicity. Step [](#s1-3){.pf-ref} places all five of them in $|z|<2$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
