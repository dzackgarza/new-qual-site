---
schema: qual/card@1
id: P-PRECALC1-23
kind: problem
title: Real roots of $2x^5+8x-7$
classification:
  areas:
  - prelim
  topics:
  - Polynomials
  - Mean Value Theorem
relations: []
review: draft
---

::: {.problem}
How many real roots does $2x^{5} + 8x - 7$ have?
:::

::: {.solution}

Let
$$
p(x)=2x^5+8x-7.
$$

::: pf

::: pf-step

The derivative is
$$
\boxed{
p'(x)=10x^4+8}.
$$


::: pf-proof

Differentiate term by term.

:::

:::

::: pf-step

For every real $x$,
$$
\boxed{
p'(x)>0}.
$$


::: pf-proof

Since
$$
x^4\ge0,
$$
one has
$$
10x^4+8\ge8>0.
$$

:::

:::

::: pf-step

Hence $p$ is strictly increasing on $\RR$.


::: pf-proof

A differentiable function whose derivative is everywhere positive is
strictly increasing.

:::

:::

::: {.pf-step #s1-4}

Therefore $p$ has at most one real root.


::: pf-proof

A strictly increasing function cannot take the same value, in particular the
value $0$, at two distinct points.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{
p(0)=-7<0}.
$$


::: pf-proof

Substitute $x=0$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
p(1)=3>0}.
$$


::: pf-proof

$$
p(1)
=
2+8-7
=
3.
$$

:::

:::

::: {.pf-step #s1-7}

By the intermediate value theorem, $p$ has a real root in
$$
(0,1).
$$


::: pf-proof

The polynomial $p$ is continuous, and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} show a sign
change between $0$ and $1$.

:::

:::

::: {.pf-step #s1-8}

Combining existence and uniqueness,
$$
\boxed{
p(x)=2x^5+8x-7
\text{ has exactly one real root}.}
$$


::: pf-proof

Existence is step [](#s1-7){.pf-ref} and uniqueness is step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives the requested number of real roots.

:::

:::

:::
