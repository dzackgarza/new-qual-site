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
Solve $y ^ { \prime \prime } - y ^ { \prime } - 2 y = 0$
:::

::: {.solution}
<1>1. Seek a solution of the form
$$
y=e^{\lambda x}.
$$

::: {.proof}
For a linear differential equation with constant coefficients, exponential trial functions reduce the equation to its characteristic polynomial.
:::

<1>2. Substitution gives
$$
\lambda^2-\lambda-2=0.
$$

::: {.proof}
One has
$$
y'=\lambda e^{\lambda x},
\qquad
y''=\lambda^2e^{\lambda x}.
$$
Substitute into the differential equation and divide by the nonzero factor $e^{\lambda x}$.
:::

<1>3. The characteristic polynomial factors as
$$
(\lambda-2)(\lambda+1)=0.
$$

::: {.proof}
Expand the product:
$$
(\lambda-2)(\lambda+1)
=
\lambda^2-\lambda-2.
$$
:::

<1>4. Hence the two distinct characteristic roots are
$$
\lambda_1=2,
\qquad
\lambda_2=-1.
$$

::: {.proof}
Solve the two linear factors from step <1>3.
:::

<1>5. Therefore two independent solutions are
$$
e^{2x}
$$
and
$$
e^{-x}.
$$

::: {.proof}
Each exponential corresponds to one characteristic root. Distinct roots give linearly independent solutions.
:::

<1>6. Thus the general solution is
$$
\boxed{
y(x)=C_1e^{2x}+C_2e^{-x},
}
$$
with arbitrary constants $C_1,C_2\in\mathbb R$.

::: {.proof}
A second-order homogeneous linear equation has a two-dimensional solution space, and step <1>5 provides a basis.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the complete solution family.
:::
:::
