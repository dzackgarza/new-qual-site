---
schema: qual/card@1
id: P-TRIV-DE08
kind: problem
title: Forced equation $y''-3y'+2y=\sin x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime \prime } - 3 y ^ { \prime } + 2 y = \sin x$
:::

::: {.solution}
<1>1. The associated homogeneous equation is
$$
y''-3y'+2y=0.
$$

::: {.proof}
Set the forcing term equal to zero.
:::

<1>2. Its characteristic polynomial is
$$
\lambda^2-3\lambda+2
=
(\lambda-1)(\lambda-2).
$$

::: {.proof}
Substitute $y=e^{\lambda x}$ into the homogeneous equation and factor the resulting polynomial.
:::

<1>3. Hence the homogeneous solution is
$$
y_h
=
C_1e^x
+
C_2e^{2x}.
$$

::: {.proof}
The two distinct characteristic roots are $1$ and $2$.
:::

<1>4. Seek a particular solution of the form
$$
y_p
=
A\sin x
+
B\cos x.
$$

::: {.proof}
The forcing is $\sin x$, and neither $\pm i$ is a characteristic root of the homogeneous equation, so no resonance factor is needed.
:::

<1>5. The derivatives are
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

::: {.proof}
Differentiate step <1>4 term by term.
:::

<1>6. Substitution into the differential equation gives
$$
(A+3B)\sin x
+
(B-3A)\cos x
=
\sin x.
$$

::: {.proof}
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

<1>7. Therefore
$$
A+3B=1,
\qquad
B-3A=0.
$$

::: {.proof}
Match the sine and cosine coefficients in step <1>6.
:::

<1>8. Solving gives
$$
A=\frac1{10},
\qquad
B=\frac3{10}.
$$

::: {.proof}
From the second equation, $B=3A$. Substitute into the first:
$$
10A=1.
$$
:::

<1>9. Hence
$$
y_p
=
\frac1{10}\sin x
+
\frac3{10}\cos x.
$$

::: {.proof}
Substitute step <1>8 into the ansatz from step <1>4.
:::

<1>10. Therefore the general solution is
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

::: {.proof}
Add the homogeneous solution from step <1>3 and one particular solution from step <1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the complete solution family.
:::
:::
