---
schema: qual/card@1
id: P-TRIV-DE13
kind: problem
title: Initial value problem $y''-3y'+2y=e^{3t}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime \prime } - 3 y ^ { \prime } + 2 y = e ^ { 3 t } \mathrm { w i t h } y ( 0 ) = 1 , y ^ { \prime } ( 0 ) = 0$
:::

::: pf

::: pf-step

The associated homogeneous equation has characteristic polynomial
$$
\lambda^2-3\lambda+2
=
(\lambda-1)(\lambda-2).
$$


::: pf-proof

Substitute $y=e^{\lambda t}$ into the homogeneous equation.

:::

:::

::: pf-step

Hence
$$
y_h
=
C_1e^t
+
C_2e^{2t}.
$$


::: pf-proof

The distinct characteristic roots are $1$ and $2$.

:::

:::

::: pf-step

Seek a particular solution of the form
$$
y_p=Ae^{3t}.
$$


::: pf-proof

The forcing is $e^{3t}$, and $3$ is not a root of the characteristic polynomial, so no resonance factor is needed.

:::

:::

::: pf-step

Substitution gives
$$
2A e^{3t}
=
e^{3t}.
$$


::: pf-proof

For $y_p=Ae^{3t}$,
$$
y_p'=3Ae^{3t},
\qquad
y_p''=9Ae^{3t}.
$$
Thus
$$
y_p''-3y_p'+2y_p
=
(9-9+2)Ae^{3t}.
$$

:::

:::

::: pf-step

Therefore
$$
A=\frac12,
$$
and
$$
y(t)
=
C_1e^t
+
C_2e^{2t}
+
\frac12e^{3t}.
$$


::: pf-proof

Solve step <1>4 for $A$ and add the particular solution to the homogeneous solution from step <1>2.

:::

:::

::: pf-step

The condition $y(0)=1$ gives
$$
C_1+C_2=\frac12.
$$


::: pf-proof

Substitute $t=0$ into step <1>5.

:::

:::

::: pf-step

The derivative is
$$
y'(t)
=
C_1e^t
+
2C_2e^{2t}
+
\frac32e^{3t}.
$$


::: pf-proof

Differentiate step <1>5.

:::

:::

::: pf-step

The condition $y'(0)=0$ gives
$$
C_1+2C_2=-\frac32.
$$


::: pf-proof

Substitute $t=0$ into step <1>7.

:::

:::

::: pf-step

Solving steps <1>6 and <1>8 gives
$$
C_1=\frac52,
\qquad
C_2=-2.
$$


::: pf-proof

Subtract step <1>6 from step <1>8 to get $C_2=-2$, then substitute back to get $C_1=5/2$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
y(t)
=
\frac52e^t
-
2e^{2t}
+
\frac12e^{3t}.
}
$$


::: pf-proof

Substitute the constants from step <1>9 into step <1>5.

:::

:::

::: pf-qed

Step <1>10 satisfies both the differential equation and the two initial conditions.

:::

:::
