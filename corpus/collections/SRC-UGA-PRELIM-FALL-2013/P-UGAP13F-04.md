---
schema: qual/card@1
id: P-UGAP13F-04
kind: problem
title: Prove $1/(x^2-1)\to1/3$ at $x=2$ from the definition of limit
classification:
  areas: [prelim]
  topics:
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Use the definition of a limit to show that
$$
\lim_{x\to2}\frac1{x^2-1}=\frac13.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
x\ne\pm1,
$$
one has
$$
\abs{
\frac1{x^2-1}
-
\frac13
}
=
\frac{\abs{x-2},\abs{x+2}}
{3\abs{x^2-1}}.
$$


::: pf-proof

Compute
$$
\begin{aligned}
\frac1{x^2-1}
-
\frac13
&=
\frac{3-(x^2-1)}
{3(x^2-1)}\\
&=
\frac{4-x^2}
{3(x^2-1)}\\
&=
-\frac{(x-2)(x+2)}
{3(x^2-1)}.
\end{aligned}
$$
Take absolute values.

:::

:::

::: {.pf-step #s1-2}

If
$$
\abs{x-2}<\frac12,
$$
then
$$
\abs{x+2}<\frac92
$$
and
$$
\abs{x^2-1}>\frac54.
$$


::: pf-proof

The inequality
$$
\abs{x-2}<\frac12
$$
gives
$$
\frac32<x<\frac52.
$$
Hence
$$
x+2<\frac92,
$$
so
$$
\abs{x+2}<\frac92.
$$

Also
$$
x>\frac32
$$
implies
$$
x^2-1
>
\frac94-1
=
\frac54.
$$
Since this quantity is positive,
$$
\abs{x^2-1}
>
\frac54.
$$

:::

:::

::: {.pf-step #s1-3}

Under the same restriction,
$$
\abs{
\frac1{x^2-1}
-
\frac13
}
<
\frac65\abs{x-2}.
$$


::: pf-proof

Insert the bounds from step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref}:
$$
\begin{aligned}
\abs{
\frac1{x^2-1}
-
\frac13
}
&=
\frac{\abs{x-2},\abs{x+2}}
{3\abs{x^2-1}}\\
&<
\frac{\abs{x-2}(9/2)}
{3(5/4)}\\
&=
\frac65\abs{x-2}.
\end{aligned}
$$

:::

:::

::: pf-step

Let
$$
\varepsilon>0
$$
be given.
Choose
$$
\boxed{
\delta
=
\min
\left\{
\frac12,
\frac{5\varepsilon}{6}
\right\}.
}
$$


::: pf-proof

This choice ensures both:

1. the denominator-control hypothesis
   $$
   \abs{x-2}<\frac12;
   $$
2. the final error bound
   $$
   \frac65\abs{x-2}
   <
   \varepsilon.
   $$

:::

:::

::: {.pf-step #s1-5}

If
$$
0<\abs{x-2}<\delta,
$$
then
$$
\abs{
\frac1{x^2-1}
-
\frac13
}
<
\varepsilon.
$$


::: pf-proof

Since
$$
\delta\le\frac12,
$$
step [](#s1-3){.pf-ref} applies:
$$
\abs{
\frac1{x^2-1}
-
\frac13
}
<
\frac65\abs{x-2}.
$$
Also
$$
\abs{x-2}
<
\delta
\le
\frac{5\varepsilon}{6},
$$
so
$$
\frac65\abs{x-2}
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\lim_{x\to2}
\frac1{x^2-1}
=
\frac13.
}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} is exactly the
$$
\varepsilon\text{--}\delta
$$
definition of the limit.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the desired conclusion.

:::

:::

:::
