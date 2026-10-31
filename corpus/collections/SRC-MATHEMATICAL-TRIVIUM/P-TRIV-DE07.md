---
schema: qual/card@1
id: P-TRIV-DE07
kind: problem
title: Third-order equation $y'''-3y'+2y=0$
classification:
  areas: [prelim]
  topics:
  - Constant-Coefficient ODEs
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y''' - 3y' + 2y = 0$.
:::

::: {.solution}

::: pf

::: pf-step

Seek a solution of the form
$$
y=e^{\lambda x}.
$$


::: pf-proof

For a constant-coefficient linear equation, the exponential ansatz reduces the differential equation to its characteristic polynomial.

:::

:::

::: pf-step

Substitution gives
$$
\lambda^3-3\lambda+2=0.
$$


::: pf-proof

One has
$$
y'=\lambda e^{\lambda x},
\qquad
y'''=\lambda^3e^{\lambda x}.
$$
Substitute and divide by the nonzero factor $e^{\lambda x}$.

:::

:::

::: {.pf-step #s1-3}

The characteristic polynomial factors as
$$
\lambda^3-3\lambda+2
=
(\lambda-1)^2(\lambda+2).
$$


::: pf-proof

Factor once by the root $\lambda=1$:
$$
\lambda^3-3\lambda+2
=
(\lambda-1)(\lambda^2+\lambda-2),
$$
and then use
$$
\lambda^2+\lambda-2
=
(\lambda-1)(\lambda+2).
$$

:::

:::

::: pf-step

Thus the characteristic roots are $1$ with multiplicity $2$ and $-2$ with multiplicity $1$.


::: pf-proof

Read the roots and multiplicities from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

A basis of solutions is
$$
e^x,
\qquad
xe^x,
\qquad
e^{-2x}.
$$


::: pf-proof

A double root $1$ contributes $e^x$ and $xe^x$, while the simple root $-2$ contributes $e^{-2x}$.

:::

:::

::: {.pf-step #s1-6}

Therefore the general solution is
$$
\boxed{
y(x)
=
(C_1+C_2x)e^x
+
C_3e^{-2x},
}
$$
with arbitrary constants $C_1,C_2,C_3\in\RR$.


::: pf-proof

A third-order homogeneous linear equation has a three-dimensional solution space, and step [](#s1-5){.pf-ref} gives three independent solutions.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the complete solution family.

:::

:::

:::
