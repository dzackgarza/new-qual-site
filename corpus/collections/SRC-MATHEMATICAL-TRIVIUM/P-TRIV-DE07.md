---
schema: qual/card@1
id: P-TRIV-DE07
kind: problem
title: Third-order equation $y'''-3y'+2y=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime \prime \prime } - 3 y ^ { \prime } + 2 y = 0$
:::

::: {.solution}
<1>1. Seek a solution of the form
$$
y=e^{\lambda x}.
$$

::: {.proof}
For a constant-coefficient linear equation, the exponential ansatz reduces the differential equation to its characteristic polynomial.
:::

<1>2. Substitution gives
$$
\lambda^3-3\lambda+2=0.
$$

::: {.proof}
One has
$$
y'=\lambda e^{\lambda x},
\qquad
y'''=\lambda^3e^{\lambda x}.
$$
Substitute and divide by the nonzero factor $e^{\lambda x}$.
:::

<1>3. The characteristic polynomial factors as
$$
\lambda^3-3\lambda+2
=
(\lambda-1)^2(\lambda+2).
$$

::: {.proof}
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

<1>4. Thus the characteristic roots are $1$ with multiplicity $2$ and $-2$ with multiplicity $1$.

::: {.proof}
Read the roots and multiplicities from step <1>3.
:::

<1>5. A basis of solutions is
$$
e^x,
\qquad
xe^x,
\qquad
e^{-2x}.
$$

::: {.proof}
A double root $1$ contributes $e^x$ and $xe^x$, while the simple root $-2$ contributes $e^{-2x}$.
:::

<1>6. Therefore the general solution is
$$
\boxed{
y(x)
=
(C_1+C_2x)e^x
+
C_3e^{-2x},
}
$$
with arbitrary constants $C_1,C_2,C_3\in\mathbb R$.

::: {.proof}
A third-order homogeneous linear equation has a three-dimensional solution space, and step <1>5 gives three independent solutions.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the complete solution family.
:::
:::
