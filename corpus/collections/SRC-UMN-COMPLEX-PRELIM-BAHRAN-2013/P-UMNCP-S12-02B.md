---
schema: qual/card@1
id: P-UMNCP-S12-02B
kind: problem
title: Count zeros of a quartic in an annulus by Rouche
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
  note: Checked against Spring 2012, 2b as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Use Rouché's theorem to find the number of zeros of
$$
z^4+5z+3
$$
in the annulus
$$
1<|z|<2.
$$
:::

::: {.solution}

Let
$$
p(z)=z^4+5z+3.
$$

::: pf

::: {.pf-step #s1-1}

The polynomial $p$ has exactly four zeros in
$$
|z|<2,
$$
counted with multiplicity.


::: pf-proof

On the circle
$$
|z|=2,
$$
one has
$$
|z^4|=16,
$$
while
$$
|5z+3|
\le
5|z|+3
=
13.
$$
Thus
$$
|5z+3|<|z^4|
$$
on $|z|=2$. By Rouché's theorem,
$$
p(z)=z^4+(5z+3)
$$
and
$$
z^4
$$
have the same number of zeros in $|z|<2$. The function $z^4$ has four zeros there, counted with multiplicity.

:::

:::

::: {.pf-step #s1-2}

The polynomial $p$ has exactly one zero in
$$
|z|<1,
$$
counted with multiplicity.


::: pf-proof

On the circle
$$
|z|=1,
$$
one has
$$
|5z|=5,
$$
while
$$
|z^4+3|
\le
|z|^4+3
=
4.
$$
Thus
$$
|z^4+3|<|5z|
$$
on $|z|=1$. By Rouché's theorem,
$$
p(z)=5z+(z^4+3)
$$
and
$$
5z
$$
have the same number of zeros in $|z|<1$. The function $5z$ has exactly one zero there.

:::

:::

::: {.pf-step #s1-3}

The polynomial $p$ has no zeros on either boundary circle
$$
|z|=1
\quad\text{or}\quad
|z|=2.
$$


::: pf-proof

The strict Rouché inequalities in steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} imply that $p$ cannot vanish on either contour: if $p(z)=0$, then the two compared terms would have equal modulus, contradicting the strict inequality.

:::

:::

::: {.pf-step #s1-4}

Hence the number of zeros in
$$
1<|z|<2
$$
is
$$
\boxed{3}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} there are four zeros in $|z|<2$, while by step [](#s1-2){.pf-ref} there is one zero in $|z|<1$. Step [](#s1-3){.pf-ref} ensures that no zero lies on either boundary. Therefore the annulus contains
$$
4-1=3
$$
zeros, counted with multiplicity.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required zero count.

:::

:::

:::
