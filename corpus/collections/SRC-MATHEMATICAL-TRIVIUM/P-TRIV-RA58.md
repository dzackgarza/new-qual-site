---
schema: qual/card@1
id: P-TRIV-RA58
kind: problem
title: Ant on a stretching rubber rope
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 58, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the rubber cord with one end attached to a tree and another - to a car moving away from the tree with the velocity $V = 1 0 m / s$ At some point an ant appears on the fixed end of the cord and starts running along it with the velocity $v = 1 0 c m / s$ Will it reach the car?
Assume the cord can be stretched up to arbitrary length.
:::

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

::: pf-step

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

::: pf-step

Therefore
$$
x'(t)=u(t)V+v.
$$


::: pf-proof

The ant's velocity relative to the ground is the sum of the local stretching
velocity from step <1>2 and its velocity $v$ relative to the cord.

:::

:::

::: pf-step

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

Comparing steps <1>3--<1>4 yields
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

::: pf-step

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

::: pf-step

One has
$$
u(t)\longrightarrow\infty
$$
as $t\to\infty$.


::: pf-proof

The logarithm in step <1>6 tends to infinity, and $v/V>0$.

:::

:::

::: pf-step

Hence there is a finite time $t_*$ at which
$$
u(t_*)=1.
$$


::: pf-proof

The function $u$ is continuous, satisfies $u(0)=0$, and tends to infinity by
step <1>7. The Intermediate Value Theorem therefore gives a finite point where
$u=1$.

:::

:::

::: pf-step

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

Set $u(t_*)=1$ in step <1>6:
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

::: pf-step

Therefore the ant does reach the car.


::: pf-proof

Step <1>8 proves eventual arrival. The numerical speeds
$$
V=10\,\mathrm{m/s},
\qquad
v=10\,\mathrm{cm/s}=0.1\,\mathrm{m/s}
$$
make
$$
\frac Vv=100,
$$
so the time in step <1>9 is enormous but finite.

:::

:::

::: pf-qed

Step <1>10 answers the question.

:::

:::
