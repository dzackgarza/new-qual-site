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
$$
\lim_{x\to2}\frac1{3-x}=1.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\ne3$,
$$
\abs{
\frac1{3-x}-1
}
=
\frac{\abs{x-2}}{\abs{3-x}}.
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

::: {.pf-step #s1-2}

If
$$
\abs{x-2}<\frac12,
$$
then
$$
\abs{3-x}>\frac12.
$$


::: pf-proof

By the reverse triangle inequality,
$$
\abs{3-x}
=
\abs{1-(x-2)}
\ge
1-\abs{x-2}
>
\frac12.
$$

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

If
$$
0<\abs{x-2}<\delta,
$$
then
$$
\abs{
\frac1{3-x}-1
}
<\varepsilon.
$$


::: pf-proof

Because
$$
\abs{x-2}<\delta\le\frac12,
$$
step [](#s1-2){.pf-ref} gives
$$
\abs{3-x}>\frac12.
$$
Using step [](#s1-1){.pf-ref},
$$
\abs{
\frac1{3-x}-1
}
=
\frac{\abs{x-2}}{\abs{3-x}}
<
2\abs{x-2}
<
2\delta
\le
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\lim_{x\to2}\frac1{3-x}=1}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} verifies the definition of the limit for the arbitrary $\varepsilon>0$ chosen in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required $\varepsilon$-$\delta$ conclusion.

:::

:::

:::
