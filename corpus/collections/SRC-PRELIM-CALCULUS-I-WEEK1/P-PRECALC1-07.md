---
schema: qual/card@1
id: P-PRECALC1-07
kind: problem
title: Quadratic $3x^2+bx+c$ with a double root at $2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that $f ( x ) = 3 x ^ { 2 } + b x + c$ has a non-simple root at $x = 2$ . What is $f ( 5 ) ?$
:::

::: {.solution}

::: pf

::: pf-step

Since $x=2$ is a non-simple root of the quadratic $f$, it is a
double root.


::: pf-proof

A quadratic polynomial has total root multiplicity $2$. Thus any root of
multiplicity greater than $1$ has multiplicity exactly $2$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
f(x)
=
A(x-2)^2
$$
for some constant $A$.


::: pf-proof

A quadratic with a double root at $2$ is a scalar multiple of
$$
(x-2)^2.
$$

:::

:::

::: {.pf-step #s1-3}

Comparing leading coefficients gives
$$
\boxed{A=3}.
$$


::: pf-proof

The leading coefficient of
$$
A(x-2)^2
$$
is $A$, while the given polynomial
$$
3x^2+bx+c
$$
has leading coefficient $3$.

:::

:::

::: pf-step

Hence
$$
\boxed{
f(x)=3(x-2)^2}.
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Evaluating at $x=5$,
$$
\boxed{
f(5)=3(5-2)^2=27}.
$$


::: pf-proof

$$
5-2=3,
\qquad
3\cdot3^2
=
27.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested value.

:::

:::

:::
