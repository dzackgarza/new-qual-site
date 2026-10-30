---
schema: qual/card@1
id: P-TRIV-DE05
kind: problem
title: Constant-coefficient equation $y''-y'-2y=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y'' - y' - 2y = 0$.
:::

::: {.solution}

::: pf

::: pf-step

Seek a solution of the form
$$
y=e^{\lambda x}.
$$


::: pf-proof

For a linear differential equation with constant coefficients, exponential trial functions reduce the equation to its characteristic polynomial.

:::

:::

::: pf-step

Substitution gives
$$
\lambda^2-\lambda-2=0.
$$


::: pf-proof

One has
$$
y'=\lambda e^{\lambda x},
\qquad
y''=\lambda^2e^{\lambda x}.
$$
Substitute into the differential equation and divide by the nonzero factor $e^{\lambda x}$.

:::

:::

::: {.pf-step #s1-3}

The characteristic polynomial factors as
$$
(\lambda-2)(\lambda+1)=0.
$$


::: pf-proof

Expand the product:
$$
(\lambda-2)(\lambda+1)
=
\lambda^2-\lambda-2.
$$

:::

:::

::: pf-step

Hence the two distinct characteristic roots are
$$
\lambda_1=2,
\qquad
\lambda_2=-1.
$$


::: pf-proof

Solve the two linear factors from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore two independent solutions are
$$
e^{2x}
$$
and
$$
e^{-x}.
$$


::: pf-proof

Each exponential corresponds to one characteristic root. Distinct roots give linearly independent solutions.

:::

:::

::: {.pf-step #s1-6}

Thus the general solution is
$$
\boxed{
y(x)=C_1e^{2x}+C_2e^{-x},
}
$$
with arbitrary constants $C_1,C_2\in\RR$.


::: pf-proof

A second-order homogeneous linear equation has a two-dimensional solution space, and step [](#s1-5){.pf-ref} provides a basis.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the complete solution family.

:::

:::

:::
