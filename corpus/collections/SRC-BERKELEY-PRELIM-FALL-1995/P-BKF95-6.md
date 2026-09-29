---
schema: qual/card@1
id: P-BKF95-6
kind: problem
title: Boundary lengths admitting a nonzero solution of an Euler equation
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Solved the Euler equation from its indicial roots
    (1 plus/minus i sqrt(3))/2; the two endpoint conditions quantize log L
    to positive integer multiples of 2 pi/sqrt(3).
---

::: {.problem}
Determine all real numbers $L>1$ for which
\[
x^2y''(x)+y(x)=0,
\qquad 1\le x\le L,
\]
with boundary conditions
\[
y(1)=y(L)=0
\]
has a nonzero solution.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The indicial equation for a solution of the form
$$
y=x^m
$$
is
$$
m(m-1)+1=0.
$$

::: pf-proof

For $y=x^m$,
$$
y''=m(m-1)x^{m-2}.
$$
Thus
$$
x^2y''+y
=
\bigl(m(m-1)+1\bigr)x^m.
$$
The differential equation holds for nonzero $x^m$ exactly when the
displayed coefficient vanishes.

:::

:::

::: {.pf-step #s2}

The roots of the indicial equation are
$$
m_\pm
=
\frac12
\pm
\frac{i\sqrt3}{2}.
$$

::: pf-proof

The equation in step [](#s1){.pf-ref} is
$$
m^2-m+1=0.
$$
Its discriminant is $-3$, so the quadratic formula gives the two displayed
roots.

:::

:::

::: {.pf-step #s3}

Every real solution on $(0,\infty)$ has the form
$$
y(x)
=
x^{1/2}
\left(
A\cos\left(\frac{\sqrt3}{2}\log x\right)
+B\sin\left(\frac{\sqrt3}{2}\log x\right)
\right),
$$
with $A,B\in\RR$.

::: pf-proof

The two complex solutions associated with step [](#s2){.pf-ref} are
$$
x^{m_\pm}
=
x^{1/2}
e^{\pm i(\sqrt3/2)\log x}.
$$
Taking their real and imaginary parts gives the displayed real basis.

:::

:::

::: {.pf-step #s4}

The boundary condition
$$
y(1)=0
$$
forces
$$
A=0.
$$

::: pf-proof

Since $\log1=0$, step [](#s3){.pf-ref} gives
$$
y(1)
=
A.
$$
Thus $y(1)=0$ is equivalent to $A=0$.

:::

:::

::: {.pf-step #s5}

After imposing $y(1)=0$, a nonzero solution satisfies $y(L)=0$ if
and only if
$$
\frac{\sqrt3}{2}\log L
=
k\pi
$$
for some positive integer $k$.

::: pf-proof

By step [](#s4){.pf-ref}, every solution satisfying the first boundary condition is
$$
y(x)
=
B x^{1/2}
\sin\left(\frac{\sqrt3}{2}\log x\right).
$$
It is nonzero exactly when $B\neq0$. Hence
$$
y(L)=0
$$
is equivalent to
$$
\sin\left(\frac{\sqrt3}{2}\log L\right)=0.
$$
Therefore
$$
\frac{\sqrt3}{2}\log L=k\pi
$$
for some integer $k$. Since $L>1$, the logarithm is positive, so
$k\geq1$.

:::

:::

::: {.pf-step #s6}

The complete set of admissible values is
$$
\boxed{
L
=
\exp\left(\frac{2\pi k}{\sqrt3}\right),
\qquad
k=1,2,3,\ldots
}.
$$

::: pf-proof

Solving the equation in step [](#s5){.pf-ref} for $L$ gives the displayed values.
Conversely, for any positive integer $k$, the function
$$
y(x)
=
x^{1/2}
\sin\left(\frac{\sqrt3}{2}\log x\right)
$$
is nonzero, solves the differential equation by step [](#s3){.pf-ref}, vanishes at
$x=1$, and vanishes at the displayed value of $L$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives all and only the required values of $L$.

:::

:::

:::
