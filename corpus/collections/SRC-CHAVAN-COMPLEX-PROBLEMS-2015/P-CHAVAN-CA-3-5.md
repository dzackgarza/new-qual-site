---
schema: qual/card@1
id: P-CHAVAN-CA-3-5
kind: problem
title: A boundary-modulus-one holomorphic map covers the unit disk
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The extraction's first clause is normalized to existence of a zero in the open unit disk, as forced by the Maximum Modulus hint and the following Rouché step.
---

::: {.problem}
Let $f$ be nonconstant and holomorphic on an open set containing the closed unit disk, and suppose
$$
|f(z)|=1\qquad(|z|=1).
$$

1. Show that $f$ has a zero in the open unit disk.

2. Show that for every $|w_0|<1$, the equation $f(z)=w_0$ has a root in the open unit disk.

Thus the image of $f$ contains the unit disk.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $|z|\le1$,
$$
|f(z)|\le1.
$$


::: pf-proof

The function $f$ is holomorphic on an open neighborhood of the closed
unit disk, and $|f|=1$ on its boundary. The maximum modulus principle
therefore gives
$$
|f(z)|\le\max_{|w|=1}|f(w)|=1
$$
throughout the closed unit disk.

:::

:::

::: {.pf-step #s1-2}

The function $f$ has a zero in the open unit disk.


::: pf-proof

Suppose instead that $f$ has no zero in the open unit disk. Since
$|f|=1$ on the unit circle, $f$ is then nowhere zero on the closed
unit disk. Hence $1/f$ is holomorphic on a neighborhood of that compact
disk after shrinking the original neighborhood if necessary. On the
unit circle,
$$
\left|\frac1{f(z)}\right|=1.
$$
Applying the maximum modulus principle to $1/f$ gives
$$
\frac1{|f(z)|}\le1
$$
for $|z|\le1$, so $|f(z)|\ge1$. Combining this with step [](#s1-1){.pf-ref} yields
$$
|f(z)|=1
$$
throughout the unit disk. Thus $|f|$ attains its maximum at every
interior point. The strong maximum modulus principle then forces $f$
to be constant, contrary to the hypothesis. Therefore $f$ has a zero
in the open unit disk.

:::

:::

::: {.pf-step #s1-3}

For every $w_0$ with $|w_0|<1$, the functions $f$ and $f-w_0$ have the same number of zeros in the open unit disk, counted with multiplicity.


::: pf-proof

On the unit circle,
$$
|f(z)|=1>|w_0|=|-w_0|.
$$
Thus Rouché's theorem, applied to $f$ and the constant function
$-w_0$, shows that $f$ and $f-w_0$ have the same number of zeros in
the open unit disk, counted with multiplicity.

:::

:::

::: {.pf-step #s1-4}

For every $|w_0|<1$, there is a $z$ with $|z|<1$ such that
$$
f(z)=w_0.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $f$ has at least one zero in the open unit disk. By step
[](#s1-3){.pf-ref}, $f-w_0$ has the same number of zeros there, hence at least one.
Any such zero satisfies $f(z)=w_0$.

:::

:::

::: {.pf-step #s1-5}

The image of $f$ contains the open unit disk.


::: pf-proof

Step [](#s1-4){.pf-ref} applies to every $w_0$ with $|w_0|<1$, so every point of the
open unit disk lies in the image of $f$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part 1, steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} prove part 2, and step
[](#s1-5){.pf-ref} gives the stated image containment.

:::

:::

:::
