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
<1>1. The roots satisfy
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

::: {.proof}
These are Vieta's formulas for
$$
x^3+2x^2+7x+1
=
(x-\alpha_1)(x-\alpha_2)(x-\alpha_3).
$$
:::

<1>2. One has
$$
\alpha_1^2+\alpha_2^2+\alpha_3^2=-10.
$$

::: {.proof}
Squaring the first identity in step <1>1 gives
$$
(\alpha_1+\alpha_2+\alpha_3)^2
=
\alpha_1^2+\alpha_2^2+\alpha_3^2
+2(\alpha_1\alpha_2+\alpha_1\alpha_3+\alpha_2\alpha_3).
$$
Using both identities from step <1>1,
$$
4
=
\alpha_1^2+\alpha_2^2+\alpha_3^2+14,
$$
which proves the claim.
:::

<1>3. Each root $\alpha_i$ satisfies
$$
\alpha_i^3
=
-2\alpha_i^2-7\alpha_i-1.
$$

::: {.proof}
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

<1>4. The required sum is
$$
\boxed{
\alpha_1^3+\alpha_2^3+\alpha_3^3=31
}.
$$

::: {.proof}
Summing the identity in step <1>3 over $i=1,2,3$ gives
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
using steps <1>1 and <1>2.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
