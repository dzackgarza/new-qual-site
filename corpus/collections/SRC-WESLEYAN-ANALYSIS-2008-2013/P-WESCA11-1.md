---
schema: qual/card@1
id: P-WESCA11-1
kind: problem
title: 'Square roots of $2-4i$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Find algebraic expressions involving real square roots, sums, and differences for the real and imaginary parts of both square roots of $2-4i$.
:::

::: {.solution}

Let
$$
w=a+ib
$$
be a square root of
$$
2-4i,
$$
with $a,b\in\RR$.

::: pf

::: pf-step

Expanding $w^2$,
$$
(a+ib)^2
=
a^2-b^2+2abi.
$$


::: pf-proof

Multiply out and use $i^2=-1$.

:::

:::

::: {.pf-step #s1-2}

Comparing real and imaginary parts with
$$
2-4i,
$$
one gets
$$
\boxed{a^2-b^2=2}
$$
and
$$
\boxed{2ab=-4}.
$$


::: pf-proof

Equality of complex numbers implies equality of their real and imaginary
parts.

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{ab=-2}.
$$


::: pf-proof

Divide the second equation in step [](#s1-2){.pf-ref} by $2$.

:::

:::

::: {.pf-step #s1-4}

The modulus of $2-4i$ is
$$
\boxed{\abs{2-4i}=2\sqrt5}.
$$


::: pf-proof

$$
\abs{2-4i}
=
\sqrt{2^2+(-4)^2}
=
\sqrt{20}
=
2\sqrt5.
$$

:::

:::

::: pf-step

Since
$$
\abs{w}^2=\abs{w^2},
$$
one has
$$
\boxed{a^2+b^2=2\sqrt5}.
$$


::: pf-proof

$$
\abs{w}^2=a^2+b^2,
$$
and
$$
\abs{w}^2=\abs{w^2}=\abs{2-4i}.
$$
Apply step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Adding the equations
$$
a^2-b^2=2
$$
and
$$
a^2+b^2=2\sqrt5
$$
gives
$$
2a^2=2+2\sqrt5.
$$


::: pf-proof

The $b^2$-terms cancel.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
a^2=1+\sqrt5}.
$$


::: pf-proof

Divide step [](#s1-6){.pf-ref} by $2$.

:::

:::

::: {.pf-step #s1-8}

Subtracting the first equation from the second gives
$$
2b^2=2\sqrt5-2.
$$


::: pf-proof

$$
(a^2+b^2)-(a^2-b^2)=2b^2.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
b^2=\sqrt5-1}.
$$


::: pf-proof

Divide step [](#s1-8){.pf-ref} by $2$.

:::

:::

::: {.pf-step #s1-10}

Thus
$$
\abs{a}
=
\sqrt{1+\sqrt5}
$$
and
$$
\abs{b}
=
\sqrt{\sqrt5-1}.
$$


::: pf-proof

Take nonnegative square roots in steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The signs of $a$ and $b$ must be opposite.


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
ab=-2<0.
$$

:::

:::

::: {.pf-step #s1-12}

Taking $a>0$ forces
$$
\boxed{
a=\sqrt{1+\sqrt5},
\qquad
b=-\sqrt{\sqrt5-1}}.
$$


::: pf-proof

Use step [](#s1-10){.pf-ref} and the opposite-sign condition from step [](#s1-11){.pf-ref}.

:::

:::

::: pf-step

The product of these two numbers is indeed
$$
ab=-2.
$$


::: pf-proof

$$
\begin{aligned}
ab
&=
-\sqrt{(1+\sqrt5)(\sqrt5-1)}\\
&=
-\sqrt{5-1}\\
&=
-2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-14}

Therefore one square root is
$$
\boxed{
\sqrt{1+\sqrt5}
-
i\sqrt{\sqrt5-1}}.
$$


::: pf-proof

Substitute step [](#s1-12){.pf-ref} into $w=a+ib$.

:::

:::

::: {.pf-step #s1-15}

The other square root is its negative:
$$
\boxed{
-\sqrt{1+\sqrt5}
+
i\sqrt{\sqrt5-1}}.
$$


::: pf-proof

If $w^2=z$, then $(-w)^2=z$. A nonzero complex number has exactly two
square roots, which are opposites.

:::

:::

::: pf-step

Hence the real and imaginary parts of the two roots are
$$
\boxed{
\left(
\sqrt{1+\sqrt5},
-\sqrt{\sqrt5-1}
\right)}
$$
and
$$
\boxed{
\left(
-\sqrt{1+\sqrt5},
\sqrt{\sqrt5-1}
\right)}.
$$


::: pf-proof

Read off the real and imaginary parts from steps [](#s1-14){.pf-ref} through [](#s1-15){.pf-ref}.

:::

:::

:::

:::
