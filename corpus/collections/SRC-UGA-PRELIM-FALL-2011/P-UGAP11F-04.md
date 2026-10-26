---
schema: qual/card@1
id: P-UGAP11F-04
kind: problem
title: Prove $1/(3-x)\to1$ at $x=2$ by an $\varepsilon$-$\delta$ argument
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give an $\varepsilon$-$\delta$ proof that
\[
\lim_{x\to2}\frac1{3-x}=1.
\]
:::

::: pf

::: pf-step

For every $x\ne3$,
$$
\left|
\frac1{3-x}-1
\right|
=
\frac{|x-2|}{|3-x|}.
$$


::: pf-proof

Compute
$$
\frac1{3-x}-1
=
\frac{1-(3-x)}{3-x}
=
\frac{x-2}{3-x},
$$
and take absolute values.

:::

:::

::: pf-step

If
$$
|x-2|<\frac12,
$$
then
$$
|3-x|>\frac12.
$$


::: pf-proof

By the reverse triangle inequality,
$$
|3-x|
=
|1-(x-2)|
\ge
1-|x-2|
>
\frac12.
$$

:::

:::

::: pf-step

Given $\varepsilon>0$, set
$$
\boxed{
\delta
=
\min\left\{
\frac12,
\frac\varepsilon2
\right\}}.
$$


::: pf-proof

This choice is positive for every $\varepsilon>0$.

:::

:::

::: pf-step

If
$$
0<|x-2|<\delta,
$$
then
$$
\left|
\frac1{3-x}-1
\right|
<\varepsilon.
$$


::: pf-proof

Because
$$
|x-2|<\delta\le\frac12,
$$
step <1>2 gives
$$
|3-x|>\frac12.
$$
Using step <1>1,
$$
\left|
\frac1{3-x}-1
\right|
=
\frac{|x-2|}{|3-x|}
<
2|x-2|
<
2\delta
\le
\varepsilon.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
\lim_{x\to2}\frac1{3-x}=1}.
$$


::: pf-proof

Step <1>4 verifies the definition of the limit for the arbitrary $\varepsilon>0$ chosen in step <1>3.

:::

:::

::: pf-qed

Step <1>5 is the required $\varepsilon$-$\delta$ conclusion.

:::

:::
