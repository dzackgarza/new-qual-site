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

::: {.solution}
<1>1. For every $x\ne3$,
$$
\left|
\frac1{3-x}-1
\right|
=
\frac{|x-2|}{|3-x|}.
$$

::: {.proof}
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

<1>2. If
$$
|x-2|<\frac12,
$$
then
$$
|3-x|>\frac12.
$$

::: {.proof}
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

<1>3. Given $\varepsilon>0$, set
$$
\boxed{
\delta
=
\min\left\{
\frac12,
\frac\varepsilon2
\right\}}.
$$

::: {.proof}
This choice is positive for every $\varepsilon>0$.
:::

<1>4. If
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

::: {.proof}
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

<1>5. Therefore
$$
\boxed{
\lim_{x\to2}\frac1{3-x}=1}.
$$

::: {.proof}
Step <1>4 verifies the definition of the limit for the arbitrary $\varepsilon>0$ chosen in step <1>3.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required $\varepsilon$-$\delta$ conclusion.
:::
:::
