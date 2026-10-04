---
schema: qual/card@1
id: P-TRIV-DE06
kind: problem
title: Repeated-root equation $y''-6y'+9y=0$ with boundary conditions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime \prime } - 6 y ^ { \prime } + 9 y = 0 { \mathrm { ~ w i t h ~ } } y ( 1 ) = 1 { \mathrm { ~ a n d ~ } } y ^ { \prime } ( 3 ) = 0$
:::

::: {.solution}
<1>1. The characteristic polynomial is
$$
\lambda^2-6\lambda+9
=
(\lambda-3)^2.
$$

::: {.proof}
Substitute the exponential trial function $y=e^{\lambda x}$ into the differential equation.
:::

<1>2. Hence the general solution is
$$
y(x)
=
(C_1+C_2x)e^{3x}.
$$

::: {.proof}
A repeated characteristic root $\lambda=3$ of multiplicity two gives the independent solutions $e^{3x}$ and $xe^{3x}$.
:::

<1>3. The condition $y(1)=1$ gives
$$
C_1+C_2=e^{-3}.
$$

::: {.proof}
Substitute $x=1$ into step <1>2:
$$
(C_1+C_2)e^3=1.
$$
:::

<1>4. The derivative is
$$
y'(x)
=
\left(
3C_1+C_2+3C_2x
\right)e^{3x}.
$$

::: {.proof}
Differentiate step <1>2 using the product rule.
:::

<1>5. The condition $y'(3)=0$ gives
$$
3C_1+10C_2=0.
$$

::: {.proof}
Substitute $x=3$ into step <1>4. Since $e^9\neq0$, only the coefficient in parentheses must vanish.
:::

<1>6. Solving steps <1>3 and <1>5 gives
$$
C_1
=
\frac{10}{7}e^{-3},
\qquad
C_2
=
-\frac{3}{7}e^{-3}.
$$

::: {.proof}
From step <1>5,
$$
C_1=-\frac{10}{3}C_2.
$$
Substitute into step <1>3:
$$
-\frac73C_2=e^{-3}.
$$
Thus
$$
C_2=-\frac37e^{-3},
$$
and then $C_1=10e^{-3}/7$.
:::

<1>7. Therefore
$$
\boxed{
y(x)
=
\frac{10-3x}{7}
e^{3x-3}.
}
$$

::: {.proof}
Substitute the constants from step <1>6 into step <1>2 and factor out $e^{-3}/7$.
:::

<1>8. The derivative of the solution is
$$
y'(x)
=
\frac{9(3-x)}7e^{3x-3}.
$$

::: {.proof}
Differentiate the formula in step <1>7.
:::

<1>9. Hence
$$
y(1)=1,
\qquad
y'(3)=0.
$$

::: {.proof}
Substitute $x=1$ into step <1>7 and $x=3$ into step <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>7 gives the unique solution satisfying both boundary conditions.
:::
:::
