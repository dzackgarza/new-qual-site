---
schema: qual/card@1
id: P-WESRA14-6
kind: problem
title: 'An integral inequality from $fg\ge1$ on a probability space'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Suppose $\mu(\Omega)=1$ and $f,g$ are positive functions on $\Omega$ satisfying $fg\ge1$.
Prove
$$
\left(\int_\Omega f\,d\mu\right)
\left(\int_\Omega g\,d\mu\right)\ge1.
$$
:::

::: {.solution}

Assume $f$ and $g$ are measurable and positive.

::: pf

::: {.pf-step #s1-1}

If either
$$
\int_\Omega f\,d\mu
$$
or
$$
\int_\Omega g\,d\mu
$$
is infinite, then the desired inequality is immediate.


::: pf-proof

The other integral is nonnegative, so the product is
$$
+\infty
$$
unless the other integral is zero.
But a positive function has positive integral on a probability space unless
it vanishes almost everywhere, which is impossible here because
$$
fg\ge1.
$$
Thus the product is infinite and hence at least $1$.

:::

:::

::: pf-step

Hence it suffices to consider the case
$$
f,g\in L^1(\mu).
$$


::: pf-proof

This is the complementary case to step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Since
$$
fg\ge1,
$$
one has
$$
\sqrt{fg}\ge1.
$$


::: pf-proof

The square-root function is increasing on
$$
[0,\infty).
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_\Omega \sqrt{fg}\,d\mu
\ge
\int_\Omega 1\,d\mu
=
\mu(\Omega)
=
1.
$$


::: pf-proof

Integrate the pointwise inequality from step [](#s1-3){.pf-ref} and use
$$
\mu(\Omega)=1.
$$

:::

:::

::: {.pf-step #s1-5}

By the Cauchy--Schwarz inequality,
$$
\left(
\int_\Omega \sqrt{fg}\,d\mu
\right)^2
\le
\left(
\int_\Omega f\,d\mu
\right)
\left(
\int_\Omega g\,d\mu
\right).
$$


::: pf-proof

Apply Cauchy--Schwarz to the functions
$$
\sqrt f
\qquad\text{and}\qquad
\sqrt g.
$$
Since
$$
\int_\Omega (\sqrt f)^2\,d\mu
=
\int_\Omega f\,d\mu
<
\infty
$$
and similarly for $g$, both square roots lie in
$$
L^2(\mu).
$$
Thus
$$
\left|
\int_\Omega
\sqrt f\sqrt g
\,d\mu
\right|^2
\le
\left(
\int_\Omega f\,d\mu
\right)
\left(
\int_\Omega g\,d\mu
\right).
$$

:::

:::

::: {.pf-step #s1-6}

Combining steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} gives
$$
\boxed{
\left(
\int_\Omega f\,d\mu
\right)
\left(
\int_\Omega g\,d\mu
\right)
\ge
1.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives
$$
1
\le
\int_\Omega\sqrt{fg}\,d\mu.
$$
Squaring and applying step [](#s1-5){.pf-ref} yields the conclusion.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required inequality.

:::

:::

:::
