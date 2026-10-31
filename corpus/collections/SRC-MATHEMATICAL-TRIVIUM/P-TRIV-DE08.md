---
schema: qual/card@1
id: P-TRIV-DE08
kind: problem
title: Forced equation $y''-3y'+2y=\sin x$
classification:
  areas: [prelim]
  topics:
  - Constant-Coefficient ODEs
  - Undetermined Coefficients
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y'' - 3y' + 2y = \sin x$.
:::

::: {.solution}

::: pf

::: pf-step

The associated homogeneous equation is
$$
y''-3y'+2y=0.
$$


::: pf-proof

Set the forcing term equal to zero.

:::

:::

::: pf-step

Its characteristic polynomial is
$$
\lambda^2-3\lambda+2
=
(\lambda-1)(\lambda-2).
$$


::: pf-proof

Substitute $y=e^{\lambda x}$ into the homogeneous equation and factor the resulting polynomial.

:::

:::

::: {.pf-step #s1-3}

Hence the homogeneous solution is
$$
y_h
=
C_1e^x
+
C_2e^{2x}.
$$


::: pf-proof

The two distinct characteristic roots are $1$ and $2$.

:::

:::

::: {.pf-step #s1-4}

Seek a particular solution of the form
$$
y_p
=
A\sin x
+
B\cos x.
$$


::: pf-proof

The forcing is $\sin x$, and neither $\pm i$ is a characteristic root of the homogeneous equation, so no resonance factor is needed.

:::

:::

::: pf-step

The derivatives are
$$
y_p'
=
A\cos x
-
B\sin x,
$$
and
$$
y_p''
=
-A\sin x
-
B\cos x.
$$


::: pf-proof

Differentiate step [](#s1-4){.pf-ref} term by term.

:::

:::

::: {.pf-step #s1-6}

Substitution into the differential equation gives
$$
(A+3B)\sin x
+
(B-3A)\cos x
=
\sin x.
$$


::: pf-proof

Combine the coefficients from
$$
y_p''-3y_p'+2y_p.
$$
For the sine term the coefficient is
$$
-A+3B+2A=A+3B,
$$
and for the cosine term it is
$$
-B-3A+2B=B-3A.
$$

:::

:::

::: pf-step

Therefore
$$
A+3B=1,
\qquad
B-3A=0.
$$


::: pf-proof

Match the sine and cosine coefficients in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Solving gives
$$
A=\frac1{10},
\qquad
B=\frac3{10}.
$$


::: pf-proof

From the second equation, $B=3A$. Substitute into the first:
$$
10A=1.
$$

:::

:::

::: {.pf-step #s1-9}

Hence
$$
y_p
=
\frac1{10}\sin x
+
\frac3{10}\cos x.
$$


::: pf-proof

Substitute step [](#s1-8){.pf-ref} into the ansatz from step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore the general solution is
$$
\boxed{
y(x)
=
C_1e^x
+
C_2e^{2x}
+
\frac1{10}\sin x
+
\frac3{10}\cos x.
}
$$


::: pf-proof

Add the homogeneous solution from step [](#s1-3){.pf-ref} and one particular solution from step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the complete solution family.

:::

:::

:::
