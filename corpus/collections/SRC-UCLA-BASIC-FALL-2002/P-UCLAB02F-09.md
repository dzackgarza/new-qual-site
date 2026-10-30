---
schema: qual/card@1
id: P-UCLAB02F-09
kind: problem
title: Cauchy--Schwarz inequality in a complex inner product space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Let $V$ be a complex inner product space.
State and prove the Cauchy--Schwarz inequality.
:::

::: {.solution}

Use the convention that the inner product is linear in its first argument and conjugate-linear in its second.

::: pf

::: {.pf-step #s1-1}

The Cauchy--Schwarz inequality states that for all $x,y\in V$,
$$
\boxed{\abs{\langle x,y\rangle}\le \norm{x}\,\norm{y}}.
$$


::: pf-proof

This is the assertion to be proved.

:::

:::

::: {.pf-step #s1-2}

If $y=0$, then the inequality in step [](#s1-1){.pf-ref} holds with equality.


::: pf-proof

One has
$$
\langle x,0\rangle=0
$$
and
$$
\norm{0}=0,
$$
so both sides of the inequality are zero.

:::

:::

::: {.pf-step #s1-3}

Suppose $y\ne0$ and set
$$
\lambda=\frac{\langle x,y\rangle}{\langle y,y\rangle}.
$$
Then
$$
x-\lambda y
$$
is orthogonal to $y$.


::: pf-proof

Since the inner product is linear in the first argument,
$$
\langle x-\lambda y,y\rangle
=
\langle x,y\rangle-\lambda\langle y,y\rangle
=0.
$$

:::

:::

::: {.pf-step #s1-4}

If $y\ne0$, then
$$
\norm{x}^2
=
\norm{x-\lambda y}^2
+
\frac{\abs{\langle x,y\rangle}^2}{\norm{y}^2}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
x=(x-\lambda y)+\lambda y
$$
is an orthogonal decomposition. Hence the Pythagorean identity gives
$$
\norm{x}^2
=
\norm{x-\lambda y}^2
+
\norm{\lambda y}^2.
$$
Also
$$
\norm{\lambda y}^2
=
\abs{\lambda}^2\norm{y}^2
=
\frac{\abs{\langle x,y\rangle}^2}{\norm{y}^4}\norm{y}^2
=
\frac{\abs{\langle x,y\rangle}^2}{\norm{y}^2}.
$$

:::

:::

::: {.pf-step #s1-5}

If $y\ne0$, then
$$
\abs{\langle x,y\rangle}^2
\le
\norm{x}^2\norm{y}^2.
$$


::: pf-proof

The first term on the right side of step [](#s1-4){.pf-ref} is nonnegative. Therefore
$$
\norm{x}^2
\ge
\frac{\abs{\langle x,y\rangle}^2}{\norm{y}^2}.
$$
Multiplying by $\norm{y}^2>0$ gives the claim.

:::

:::

::: {.pf-step #s1-6}

For all $x,y\in V$,
$$
\abs{\langle x,y\rangle}
\le
\norm{x}\,\norm{y}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} handles $y=0$. If $y\ne0$, step [](#s1-5){.pf-ref} gives the squared inequality. Both sides are nonnegative, so taking square roots gives the desired inequality.

:::

:::

::: {.pf-step #s1-7}

Equality holds if and only if $x$ and $y$ are linearly dependent.


::: pf-proof

If $y=0$, the vectors are linearly dependent and equality holds by step [](#s1-2){.pf-ref}. Suppose $y\ne0$. By step [](#s1-4){.pf-ref}, equality in Cauchy--Schwarz holds exactly when
$$
\norm{x-\lambda y}^2=0,
$$
equivalently when
$$
x=\lambda y.
$$
Thus equality is equivalent to linear dependence.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the Cauchy--Schwarz inequality, and step [](#s1-7){.pf-ref} gives its equality criterion.

:::

:::

:::
