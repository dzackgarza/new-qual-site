---
schema: qual/card@1
id: P-BKF93-5
kind: problem
title: Zeros at $0$ and $1$ force zeros at every integer for a constant-coefficient ODE
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used uniqueness for the second-order linear ODE to show that the translated
    solution x(t+1) is a nonzero scalar multiple of x(t), then propagated the
    zero at t=0 through all integer translates.
---

::: {.problem}
Let $x(t)$ solve
\[
x''-2b x'+cx=0
\]
for all real $t$, where $b,c\in\mathbb R$, and suppose
\[
x(0)=x(1)=0.
\]
Prove that
\[
x(n)=0
\]
for every integer $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $x'(0)=0$, then $x$ is identically zero.

::: pf-proof

The function $x$ satisfies the second-order linear initial-value problem
$$
x''-2bx'+cx=0,
\qquad
x(0)=0,
\qquad
x'(0)=0.
$$
The zero function satisfies the same initial-value problem. Uniqueness for
linear ordinary differential equations therefore gives $x\equiv0$.

:::

:::

::: {.pf-step #s2}

Suppose $x$ is not identically zero. Then there is a nonzero scalar
$\lambda\in\RR$ such that
$$
x(t+1)=\lambda x(t)
\qquad\text{for every }t\in\RR.
$$

::: pf-proof

By step [](#s1){.pf-ref}, $x'(0)\neq0$. Define
$$
y(t)\coloneqq x(t+1).
$$
Because the differential equation has constant coefficients, $y$ satisfies
the same equation as $x$. Also
$$
y(0)=x(1)=0.
$$
Set
$$
\lambda\coloneqq\frac{y'(0)}{x'(0)}
=
\frac{x'(1)}{x'(0)}.
$$
Then
$$
h\coloneqq y-\lambda x
$$
satisfies the same differential equation and has
$$
h(0)=0,
\qquad
h'(0)=0.
$$
By uniqueness, $h\equiv0$, so
$$
x(t+1)=y(t)=\lambda x(t)
$$
for every real $t$.

If $\lambda=0$, then $x(t+1)=0$ for every $t$, hence $x\equiv0$, contrary
to the present assumption. Therefore $\lambda\neq0$.

:::

:::

::: {.pf-step #s3}

One has
$$
x(n)=0
$$
for every integer $n$.

::: pf-proof

If $x\equiv0$, the conclusion follows from step [](#s1){.pf-ref}. Otherwise, step [](#s2){.pf-ref}
gives
$$
x(t+1)=\lambda x(t)
$$
with $\lambda\neq0$. Starting from $x(0)=0$ and iterating forward gives
$x(n)=0$ for every positive integer $n$. Since
$$
x(t)=\lambda^{-1}x(t+1),
$$
iterating backward from $x(0)=0$ gives $x(n)=0$ for every negative integer
$n$ as well.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
