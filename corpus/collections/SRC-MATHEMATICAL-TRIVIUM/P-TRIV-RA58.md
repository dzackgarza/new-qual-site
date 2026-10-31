---
schema: qual/card@1
id: P-TRIV-RA58
kind: problem
title: Ant on a stretching rubber rope
classification:
  areas: [real-analysis]
  topics:
  - Differential Equations
  - Harmonic Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 58, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the rubber cord with one end attached to a tree and another - to a car moving away from the tree with the velocity $V = 10\ \mathrm{m/s}$. At some point an ant appears on the fixed end of the cord and starts running along it with the velocity $v = 10\ \mathrm{cm/s}$. Will it reach the car?
Assume the cord can be stretched up to arbitrary length.
:::

::: {.solution}

Let
$$
L(t)=L_0+Vt
$$
be the length of the cord after the ant starts, where $L_0>0$ is its length at
that instant.

::: pf

::: pf-step

Let $u(t)$ be the fraction of the cord's length that lies between the
tree and the ant.


::: pf-proof

Thus the ant's position measured from the tree is
$$
x(t)=u(t)L(t),
$$
with
$$
u(0)=0.
$$
The ant reaches the car exactly when $u(t)=1$.

:::

:::

::: {.pf-step #s1-2}

Uniform stretching of the cord carries the ant with velocity
$$
u(t)L'(t)=u(t)V
$$
in addition to its own running velocity $v$ relative to the cord.


::: pf-proof

A material point at fractional coordinate $u$ has position $uL(t)$. Holding
$u$ fixed and differentiating gives stretching velocity $uL'(t)=uV$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
x'(t)=u(t)V+v.
$$


::: pf-proof

The ant's velocity relative to the ground is the sum of the local stretching
velocity from step [](#s1-2){.pf-ref} and its velocity $v$ relative to the cord.

:::

:::

::: {.pf-step #s1-4}

Differentiating
$$
x(t)=u(t)L(t)
$$
also gives
$$
x'(t)=u'(t)L(t)+u(t)V.
$$


::: pf-proof

Apply the product rule and use $L'(t)=V$.

:::

:::

::: pf-step

Comparing steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} yields
$$
u'(t)=\frac{v}{L_0+Vt}.
$$


::: pf-proof

The terms $u(t)V$ cancel, leaving
$$
u'(t)L(t)=v.
$$
Substitute $L(t)=L_0+Vt$.

:::

:::

::: {.pf-step #s1-6}

Integrating from $0$ to $t$ gives
$$
u(t)
=
\frac vV
\log\left(
1+\frac{Vt}{L_0}
\right).
$$


::: pf-proof

Using $u(0)=0$,
$$
u(t)
=
\int_0^t
\frac{v}{L_0+Vs}
\,ds
=
\frac vV
\left[
\log(L_0+Vs)
\right]_0^t.
$$
This simplifies to the displayed expression.

:::

:::

::: {.pf-step #s1-7}

One has
$$
u(t)\longrightarrow\infty
$$
as $t\to\infty$.


::: pf-proof

The logarithm in step [](#s1-6){.pf-ref} tends to infinity, and $v/V>0$.

:::

:::

::: {.pf-step #s1-8}

Hence there is a finite time $t_*$ at which
$$
u(t_*)=1.
$$


::: pf-proof

The function $u$ is continuous, satisfies $u(0)=0$, and tends to infinity by
step [](#s1-7){.pf-ref}. The Intermediate Value Theorem therefore gives a finite point where
$u=1$.

:::

:::

::: {.pf-step #s1-9}

Solving for that time gives
$$
\boxed{
t_*
=
\frac{L_0}{V}
\left(
e^{V/v}-1
\right).
}
$$


::: pf-proof

Set $u(t_*)=1$ in step [](#s1-6){.pf-ref}:
$$
1
=
\frac vV
\log\left(
1+\frac{Vt_*}{L_0}
\right).
$$
Thus
$$
\log\left(
1+\frac{Vt_*}{L_0}
\right)
=
\frac Vv.
$$
Exponentiate and solve for $t_*$.

:::

:::

::: {.pf-step #s1-10}

Therefore the ant does reach the car.


::: pf-proof

Step [](#s1-8){.pf-ref} proves eventual arrival. The numerical speeds
$$
V=10\,\mathrm{m/s},
\qquad
v=10\,\mathrm{cm/s}=0.1\,\mathrm{m/s}
$$
make
$$
\frac Vv=100,
$$
so the time in step [](#s1-9){.pf-ref} is enormous but finite.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} answers the question.

:::

:::

:::
