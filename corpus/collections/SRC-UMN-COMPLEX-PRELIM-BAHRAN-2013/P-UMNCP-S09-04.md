---
schema: qual/card@1
id: P-UMNCP-S09-04
kind: problem
title: Zeros of $z^6+4z^2e^{z+1}-3$ in the unit disk
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
  note: Checked against Spring 2009, 4 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
How many zeros does
$$
f(z)=z^6+4z^2e^{z+1}-3
$$
have in the unit disk $|z|<1$?
:::

::: {.solution}

Let
$$
g(z)=4z^2e^{z+1}.
$$

::: pf

::: {.pf-step #s1-1}

On the unit circle,
$$
|f(z)-g(z)|
\le4.
$$


::: pf-proof

If
$$
|z|=1,
$$
then
$$
f(z)-g(z)=z^6-3.
$$
Hence
$$
|f(z)-g(z)|
=
|z^6-3|
\le
|z|^6+3
=4.
$$

:::

:::

::: {.pf-step #s1-2}

On the unit circle,
$$
|g(z)|\ge4.
$$


::: pf-proof

For
$$
|z|=1,
$$
one has
$$
\begin{aligned}
|g(z)|
&=
4|z|^2|e^{z+1}|\\
&=
4e^{\operatorname{Re}z+1}.
\end{aligned}
$$
Since
$$
\operatorname{Re}z\ge-1
$$
on the unit circle,
$$
|g(z)|
\ge
4e^0
=4.
$$

:::

:::

::: {.pf-step #s1-3}

In fact,
$$
\boxed{
|f(z)-g(z)|
<
|g(z)|}
$$
for every
$$
|z|=1.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, failure of strict inequality could occur only if
$$
|f(z)-g(z)|=4
$$
and
$$
|g(z)|=4.
$$
The second equality forces
$$
\operatorname{Re}z=-1.
$$
Together with
$$
|z|=1,
$$
this gives
$$
z=-1.
$$
But at $z=-1$,
$$
|f(-1)-g(-1)|
=
|(-1)^6-3|
=
2
<4
=
|g(-1)|.
$$
Thus equality never occurs.

:::

:::

::: {.pf-step #s1-4}

The functions $f$ and $g$ have the same number of zeros in
$$
|z|<1,
$$
counted with multiplicity.


::: pf-proof

Step [](#s1-3){.pf-ref} gives the strict Rouché inequality on the boundary circle. Rouché's theorem therefore applies.

:::

:::

::: {.pf-step #s1-5}

The function $g$ has exactly two zeros in the unit disk, counted with multiplicity.


::: pf-proof

Since
$$
g(z)=4z^2e^{z+1}
$$
and the exponential function never vanishes, the only zero is
$$
z=0,
$$
with multiplicity $2$.

:::

:::

::: {.pf-step #s1-6}

Therefore $f$ has exactly
$$
\boxed{2}
$$
zeros in the unit disk, counted with multiplicity.


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required zero count.

:::

:::

:::
