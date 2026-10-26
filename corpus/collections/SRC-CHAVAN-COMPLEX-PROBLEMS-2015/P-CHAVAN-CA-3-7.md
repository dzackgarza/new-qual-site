---
schema: qual/card@1
id: P-CHAVAN-CA-3-7
kind: problem
title: Count zeros of $3e^z-z$ in the closed unit disk
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Find the number of zeros of
\[
3e^z-z
\]
in the closed unit disk centered at the origin.
:::

::: pf

::: pf-step

On the unit circle,
$$
|3e^z|>|z|.
$$


::: pf-proof

If $|z|=1$, then $\operatorname{Re}z\ge-1$, so
$$
|3e^z|=3e^{\operatorname{Re}z}
\ge\frac3e.
$$
Moreover,
$$
e=\sum_{n=0}^{\infty}\frac1{n!}
<2+\sum_{n=2}^{\infty}\frac1{2^{n-1}}
=3,
$$
since $n!\ge2^{n-1}$ for $n\ge2$, with strict inequality for
$n\ge3$. Thus $3/e>1=|z|$, proving the strict inequality on the whole
unit circle.

:::

:::

::: pf-step

The functions $3e^z$ and $3e^z-z$ have the same number of zeros in the open unit disk, counted with multiplicity.


::: pf-proof

Step <1>1 gives
$$
|-z|=|z|<|3e^z|
$$
on the unit circle. Rouché's theorem applied to $3e^z$ and $-z$
therefore gives the claim.

:::

:::

::: pf-step

The function $3e^z-z$ has no zero in the open unit disk.


::: pf-proof

The exponential function never vanishes, so $3e^z$ has no zeros.
By step <1>2, $3e^z-z$ has the same zero count in the open unit disk,
namely zero.

:::

:::

::: pf-step

The function $3e^z-z$ has no zero on the unit circle.


::: pf-proof

If $|z|=1$ and $3e^z-z=0$, then $|3e^z|=|z|$, contradicting the
strict inequality in step <1>1.

:::

:::

::: pf-step

The number of zeros in the closed unit disk is
$$
\boxed{0}.
$$


::: pf-proof

Step <1>3 excludes zeros in the open unit disk, and step <1>4 excludes
zeros on its boundary.

:::

:::

::: pf-qed

Step <1>5 gives the requested zero count.

:::

:::
