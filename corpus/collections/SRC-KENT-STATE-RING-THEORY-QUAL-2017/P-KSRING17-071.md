---
schema: qual/card@1
id: P-KSRING17-071
kind: problem
title: A unit plus a nilpotent is a unit
classification:
  areas: [algebra]
  topics:
  - Units
  - Nilpotent Elements
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 71 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with 1. Show that if u is a unit in R and n is nilpotent, then $u + n$ is a unit.
:::

::: {.solution}

Let
$$
u\in R^\times
$$
and let
$$
n\in R
$$
be nilpotent.

::: pf

::: {.pf-step #s1-1}

The element
$$
m
\coloneqq
u^{-1}n
$$
is nilpotent.


::: pf-proof

Choose
$$
N\ge1
$$
such that
$$
n^N=0.
$$
Because $R$ is commutative,
$$
m^N
=
(u^{-1}n)^N
=
u^{-N}n^N
=
0.
$$
Thus $m$ is nilpotent.

:::

:::

::: {.pf-step #s1-2}

The element
$$
1+m
$$
is a unit.


::: pf-proof

With
$$
m^N=0
$$
from step [](#s1-1){.pf-ref}, define
$$
v
\coloneqq
1-m+m^2-\cdots+(-1)^{N-1}m^{N-1}.
$$
Then
$$
\begin{aligned}
(1+m)v
&=
1+(-1)^{N-1}m^N\\
&=
1.
\end{aligned}
$$
Since $R$ is commutative,
$$
v(1+m)=1
$$
as well. Hence
$$
1+m
$$
is invertible.

:::

:::

::: {.pf-step #s1-3}

One has
$$
u+n
=
u(1+m).
$$


::: pf-proof

By the definition
$$
m=u^{-1}n,
$$
one has
$$
u(1+m)
=
u+uu^{-1}n
=
u+n.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{u+n\text{ is a unit}.}
$$


::: pf-proof

The element $u$ is a unit by hypothesis, and $1+m$ is a unit by step [](#s1-2){.pf-ref}.
The product of two units is a unit.
By step [](#s1-3){.pf-ref},
$$
u+n=u(1+m),
$$
so $u+n$ is invertible.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
