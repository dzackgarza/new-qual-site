---
schema: qual/card@1
id: P-BERK85SU-05
kind: problem
title: Sum of cubes of the roots of $x^3+2x^2+7x+1$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Vieta gives sum alpha_i=-2 and sum_{i<j} alpha_i alpha_j=7.
    Hence sum alpha_i^2=(-2)^2-2(7)=-10. Summing
    alpha_i^3=-2alpha_i^2-7alpha_i-1 over the three roots gives 31.
---

::: {.problem}
By the Fundamental Theorem of Algebra, the polynomial
\[
x^3+2x^2+7x+1
\]
has three complex roots $\alpha_1,\alpha_2,\alpha_3$, counted with multiplicity. Compute
\[
\alpha_1^3+\alpha_2^3+\alpha_3^3.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The roots satisfy
$$
\alpha_1+\alpha_2+\alpha_3=-2
$$
and
$$
\alpha_1\alpha_2
+\alpha_1\alpha_3
+\alpha_2\alpha_3
=
7.
$$

::: pf-proof

These are Vieta's formulas for
$$
x^3+2x^2+7x+1
=
(x-\alpha_1)(x-\alpha_2)(x-\alpha_3).
$$

:::

:::

::: {.pf-step #s2}

One has
$$
\alpha_1^2+\alpha_2^2+\alpha_3^2=-10.
$$

::: pf-proof

Squaring the first identity in step [](#s1){.pf-ref} gives
$$
(\alpha_1+\alpha_2+\alpha_3)^2
=
\alpha_1^2+\alpha_2^2+\alpha_3^2
+2(\alpha_1\alpha_2+\alpha_1\alpha_3+\alpha_2\alpha_3).
$$
Using both identities from step [](#s1){.pf-ref},
$$
4
=
\alpha_1^2+\alpha_2^2+\alpha_3^2+14,
$$
which proves the claim.

:::

:::

::: {.pf-step #s3}

Each root $\alpha_i$ satisfies
$$
\alpha_i^3
=
-2\alpha_i^2-7\alpha_i-1.
$$

::: pf-proof

Since $\alpha_i$ is a root of
$$
x^3+2x^2+7x+1,
$$
one has
$$
\alpha_i^3+2\alpha_i^2+7\alpha_i+1=0.
$$
Rearranging gives the displayed identity.

:::

:::

::: {.pf-step #s4}

The required sum is
$$
\boxed{
\alpha_1^3+\alpha_2^3+\alpha_3^3=31
}.
$$

::: pf-proof

Summing the identity in step [](#s3){.pf-ref} over $i=1,2,3$ gives
$$
\begin{aligned}
\alpha_1^3+\alpha_2^3+\alpha_3^3
&=
-2(\alpha_1^2+\alpha_2^2+\alpha_3^2)
-7(\alpha_1+\alpha_2+\alpha_3)
-3\\
&=
-2(-10)-7(-2)-3\\
&=
31,
\end{aligned}
$$
using steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested value.

:::

:::

:::
