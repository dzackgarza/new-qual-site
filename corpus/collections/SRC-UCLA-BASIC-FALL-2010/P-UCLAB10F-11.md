---
schema: qual/card@1
id: P-UCLAB10F-11
kind: problem
title: Minimize the Dirichlet energy on an interval
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Problem 11. Find the function $g$ that minimizes
\[
\int_0^1 |f'(x)|^2\,dx
\]
among smooth functions $f:[0,1]\to\mathbb R$ satisfying $f(0)=0$ and $f(1)=1$.
Is the minimizing function unique?
:::

Let
\[
E(f)=\int_0^1|f'(x)|^2\,dx.
\]

::: pf

::: pf-step

Every admissible function satisfies
\[
1=\int_0^1 f'(x)\,dx.
\]


::: pf-proof

Since $f$ is smooth and
\[
f(0)=0,
\qquad
f(1)=1,
\]
the fundamental theorem of calculus gives
\[
\int_0^1f'(x)\,dx
=
f(1)-f(0)
=1.
\]

:::

:::

::: pf-step

Every admissible function satisfies
\[
E(f)\ge1.
\]


::: pf-proof

Apply the Cauchy--Schwarz inequality in $L^2[0,1]$ to the functions $f'$ and $1$:
\[
\left|
\int_0^1f'(x)\cdot1\,dx
\right|^2
\le
\left(\int_0^1|f'(x)|^2\,dx\right)
\left(\int_0^1 1^2\,dx\right).
\]
By step <1>1, the left side is $1$, while the second factor on the right is also $1$. Thus
\[
1\le E(f).
\]

:::

:::

::: pf-step

The function
\[
\boxed{g(x)=x}
\]
is admissible and satisfies
\[
E(g)=1.
\]


::: pf-proof

One has
\[
g(0)=0,
\qquad
g(1)=1,
\qquad
g'(x)=1.
\]
Therefore
\[
E(g)
=
\int_0^1 1\,dx
=1.
\]
By step <1>2, no admissible function can have smaller energy.

:::

:::

::: pf-step

If an admissible $f$ satisfies
\[
E(f)=1,
\]
then $f'(x)=1$ for every $x\in[0,1]$.


::: pf-proof

Equality holds in the Cauchy--Schwarz inequality used in step <1>2 exactly when $f'$ is a scalar multiple of the constant function $1$ in $L^2[0,1]$. Thus
\[
f'(x)=c
\]
for almost every $x$.

Because $f'$ is continuous, this equality holds everywhere. Step <1>1 then gives
\[
1
=
\int_0^1f'(x)\,dx
=
c,
\]
so $c=1$.

:::

:::

::: pf-step

The minimizing function is unique.


::: pf-proof

If $f$ is any minimizer, step <1>3 shows that the minimum value is $1$, so
\[
E(f)=1.
\]
By step <1>4,
\[
f'(x)=1.
\]
Since $f(0)=0$,
\[
f(x)=x.
\]
Thus every minimizer equals $g(x)=x$.

:::

:::

::: pf-qed

Step <1>3 identifies the minimizer, and step <1>5 proves its uniqueness.

:::

:::
