---
schema: qual/card@1
id: P-BKS77-9
kind: problem
title: Initial value problem $y''-2y'+y=0$, $y(0)=y'(0)=1$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Solve
\[
y''-2y'+y=0
\]
subject to
\[
y(0)=1,
\qquad
y'(0)=1.
\]
:::

::: {.solution}
<1>1. The characteristic polynomial of the differential equation is
$$
r^2-2r+1=(r-1)^2.
$$

::: {.proof}
Substituting a trial solution $y=e^{rx}$ gives
$$
(r^2-2r+1)e^{rx}=0.
$$
Since $e^{rx}\neq0$, the characteristic equation is the displayed polynomial equation.
:::

<1>2. Every solution has the form
$$
y(x)=(C_1+C_2x)e^x.
$$

::: {.proof}
The characteristic root $r=1$ has multiplicity $2$. For a repeated root of multiplicity $2$, the two linearly independent solutions are
$$
e^x
\qquad\text{and}\qquad
xe^x.
$$
Their linear combinations give the displayed general solution.
:::

<1>3. The condition $y(0)=1$ forces
$$
C_1=1.
$$

::: {.proof}
From step <1>2,
$$
y(0)=C_1.
$$
Apply the initial condition.
:::

<1>4. The condition $y'(0)=1$ forces
$$
C_2=0.
$$

::: {.proof}
Differentiating step <1>2 gives
$$
y'(x)
=
(C_1+C_2x+C_2)e^x.
$$
Hence
$$
y'(0)=C_1+C_2.
$$
By step <1>3 and the initial condition,
$$
1+C_2=1,
$$
so $C_2=0$.
:::

<1>5. The unique solution is
$$
\boxed{y(x)=e^x}.
$$

::: {.proof}
Substitute the constants from steps <1>3--<1>4 into the general solution from step <1>2.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the required solution.
:::
:::
