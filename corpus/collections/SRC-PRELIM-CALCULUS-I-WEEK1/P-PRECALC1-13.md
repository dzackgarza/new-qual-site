---
schema: qual/card@1
id: P-PRECALC1-13
kind: problem
title: Lower limit $c$ in $3x^5+96=\int_c^x g(t)\,dt$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the map from R to R of Problem 13 on page 3 of Week1_solns.pdf.
---

::: {.problem}
Find $c \in \RR$ such that $g : \RR \to \RR$ satisfies $3x^5 + 96 = \int_c^x g(t)\,dt$.
:::

::: {.solution}

Assume
$$
3x^5+96
=
\int_c^x g(t)\,dt
$$
for all $x\in\RR$.

::: pf

::: pf-step

Differentiate both sides with respect to $x$:
$$
\boxed{
15x^4=g(x)}.
$$


::: pf-proof

The derivative of
$$
3x^5+96
$$
is
$$
15x^4.
$$
By the fundamental theorem of calculus,
$$
\frac{d}{dx}
\int_c^x g(t)\,dt
=
g(x).
$$

:::

:::

::: pf-step

Set
$$
x=c
$$
in the original identity.


::: pf-proof

The identity is assumed to hold for every real $x$.

:::

:::

::: {.pf-step #s1-3}

Then
$$
3c^5+96
=
\int_c^c g(t)\,dt
=
0.
$$


::: pf-proof

An integral over an interval of zero length is zero.

:::

:::

::: pf-step

Hence
$$
c^5=-32.
$$


::: pf-proof

From step [](#s1-3){.pf-ref},
$$
3c^5=-96.
$$
Divide by $3$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{c=-2}.
$$


::: pf-proof

Since
$$
(-2)^5=-32,
$$
and the fifth-power function is strictly increasing on $\RR$, this
solution is unique.

:::

:::

::: {.pf-step #s1-6}

With
$$
g(t)=15t^4
$$
and
$$
c=-2,
$$
one indeed has
$$
\int_{-2}^x15t^4\,dt
=
3x^5+96.
$$


::: pf-proof

$$
\begin{aligned}
\int_{-2}^x15t^4\,dt
&=
\left[
3t^5
\right]_{-2}^x\\
&=
3x^5-3(-2)^5\\
&=
3x^5+96.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required lower limit, and step [](#s1-6){.pf-ref} verifies it.

:::

:::

:::
