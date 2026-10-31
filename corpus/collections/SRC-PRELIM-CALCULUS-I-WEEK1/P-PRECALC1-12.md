---
schema: qual/card@1
id: P-PRECALC1-12
kind: problem
title: Comparing $\int_0^1\sqrt{1-x^4}\,dx$, $\int_0^1\sqrt{1+x^4}\,dx$ and $\int_0^1\sqrt{1-x^8}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
relations: []
review: draft
---

::: {.problem}
Let
$$
J = \int_{0}^{1} \sqrt{1 - x^{4}}\, dx, \qquad K = \int_{0}^{1} \sqrt{1 + x^{4}}\, dx, \qquad L = \int_{0}^{1} \sqrt{1 - x^{8}}\, dx.
$$
Order the numbers $J, K, L, 1$ in increasing order.
:::

::: {.solution}

For $0<x<1$, one has
$$
0<x^8<x^4<1.
$$

::: pf

::: {.pf-step #s1-1}

Therefore
$$
\boxed{
1-x^4<1-x^8<1}.
$$


::: pf-proof

Subtract the inequalities
$$
x^8<x^4
$$
and
$$
0<x^8
$$
from $1$.

:::

:::

::: {.pf-step #s1-2}

Since all quantities in step [](#s1-1){.pf-ref} are nonnegative,
$$
\boxed{
\sqrt{1-x^4}
<
\sqrt{1-x^8}
<
1}.
$$


::: pf-proof

The square-root function is strictly increasing on $[0,\infty)$.

:::

:::

::: {.pf-step #s1-3}

Also,
$$
1+x^4>1
$$
for $0<x<1$.


::: pf-proof

Because
$$
x^4>0.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
1<
\sqrt{1+x^4}}.
$$


::: pf-proof

Apply the strictly increasing square-root function to step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Combining steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref},
$$
\boxed{
\sqrt{1-x^4}
<
\sqrt{1-x^8}
<
1
<
\sqrt{1+x^4}}
$$
for every $0<x<1$.


::: pf-proof

This is exactly the conjunction of the two preceding comparisons.

:::

:::

::: {.pf-step #s1-6}

Integrating the first inequality in step [](#s1-5){.pf-ref} over $[0,1]$,
$$
\boxed{J<L}.
$$


::: pf-proof

The integrands are continuous, and the strict inequality holds on the whole
open interval $(0,1)$, which has positive length. Therefore the integral of
the difference is strictly positive.

:::

:::

::: {.pf-step #s1-7}

Integrating the second comparison,
$$
\boxed{L<1}.
$$


::: pf-proof

From step [](#s1-5){.pf-ref},
$$
\sqrt{1-x^8}<1
$$
for $0<x<1$. Hence
$$
L
=
\int_0^1\sqrt{1-x^8}\,dx
<
\int_0^1 1\,dx
=
1.
$$

:::

:::

::: {.pf-step #s1-8}

Integrating the final comparison,
$$
\boxed{1<K}.
$$


::: pf-proof

From step [](#s1-5){.pf-ref},
$$
1<\sqrt{1+x^4}
$$
for $0<x<1$. Thus
$$
1
=
\int_0^1 1\,dx
<
\int_0^1\sqrt{1+x^4}\,dx
=
K.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore the increasing order is
$$
\boxed{
J<L<1<K}.
$$


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the requested ordering.

:::

:::

:::
