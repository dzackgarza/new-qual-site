---
schema: qual/card@1
id: P-TRIV-DE06
kind: problem
title: Repeated-root equation $y''-6y'+9y=0$ with boundary conditions
classification:
  areas: [prelim]
  topics:
  - Constant-Coefficient ODEs
  - Boundary Value Problems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y'' - 6y' + 9y = 0$ with $y(1) = 1$ and $y'(3) = 0$.
:::

::: {.solution}

::: pf

::: pf-step

The characteristic polynomial is
$$
\lambda^2-6\lambda+9
=
(\lambda-3)^2.
$$


::: pf-proof

Substitute the exponential trial function $y=e^{\lambda x}$ into the differential equation.

:::

:::

::: {.pf-step #s1-2}

Hence the general solution is
$$
y(x)
=
(C_1+C_2x)e^{3x}.
$$


::: pf-proof

A repeated characteristic root $\lambda=3$ of multiplicity two gives the independent solutions $e^{3x}$ and $xe^{3x}$.

:::

:::

::: {.pf-step #s1-3}

The condition $y(1)=1$ gives
$$
C_1+C_2=e^{-3}.
$$


::: pf-proof

Substitute $x=1$ into step [](#s1-2){.pf-ref}:
$$
(C_1+C_2)e^3=1.
$$

:::

:::

::: {.pf-step #s1-4}

The derivative is
$$
y'(x)
=
\left(
3C_1+C_2+3C_2x
\right)e^{3x}.
$$


::: pf-proof

Differentiate step [](#s1-2){.pf-ref} using the product rule.

:::

:::

::: {.pf-step #s1-5}

The condition $y'(3)=0$ gives
$$
3C_1+10C_2=0.
$$


::: pf-proof

Substitute $x=3$ into step [](#s1-4){.pf-ref}. Since $e^9\neq0$, only the coefficient in parentheses must vanish.

:::

:::

::: {.pf-step #s1-6}

Solving steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref} gives
$$
C_1
=
\frac{10}{7}e^{-3},
\qquad
C_2
=
-\frac{3}{7}e^{-3}.
$$


::: pf-proof

From step [](#s1-5){.pf-ref},
$$
C_1=-\frac{10}{3}C_2.
$$
Substitute into step [](#s1-3){.pf-ref}:
$$
-\frac73C_2=e^{-3}.
$$
Thus
$$
C_2=-\frac37e^{-3},
$$
and then $C_1=10e^{-3}/7$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
y(x)
=
\frac{10-3x}{7}
e^{3x-3}.
}
$$


::: pf-proof

Substitute the constants from step [](#s1-6){.pf-ref} into step [](#s1-2){.pf-ref} and factor out $e^{-3}/7$.

:::

:::

::: {.pf-step #s1-8}

The derivative of the solution is
$$
y'(x)
=
\frac{9(3-x)}7e^{3x-3}.
$$


::: pf-proof

Differentiate the formula in step [](#s1-7){.pf-ref}.

:::

:::

::: pf-step

Hence
$$
y(1)=1,
\qquad
y'(3)=0.
$$


::: pf-proof

Substitute $x=1$ into step [](#s1-7){.pf-ref} and $x=3$ into step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the unique solution satisfying both boundary conditions.

:::

:::

:::
