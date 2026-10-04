---
schema: qual/card@1
id: P-KSRING17-071
kind: problem
title: A unit plus a nilpotent is a unit
classification:
  areas: [algebra]
  topics: []
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

<1>1. The element
$$
m
\coloneqq
u^{-1}n
$$
is nilpotent.

::: {.proof}
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

<1>2. The element
$$
1+m
$$
is a unit.

::: {.proof}
With
$$
m^N=0
$$
from step <1>1, define
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

<1>3. One has
$$
u+n
=
u(1+m).
$$

::: {.proof}
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

<1>4. Therefore
$$
\boxed{u+n\text{ is a unit}.}
$$

::: {.proof}
The element $u$ is a unit by hypothesis, and $1+m$ is a unit by step <1>2.
The product of two units is a unit.
By step <1>3,
$$
u+n=u(1+m),
$$
so $u+n$ is invertible.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
