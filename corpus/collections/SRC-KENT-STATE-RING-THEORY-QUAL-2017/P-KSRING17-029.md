---
schema: qual/card@1
id: P-KSRING17-029
kind: problem
title: A right ideal quotient isomorphic to $R$ splits
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 29 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $I \subseteq J$ be right ideals of a ring R such that $J / I \cong R$ as right R-modules.
Prove that there exists a right ideal K such that $I \cap K = ( 0 )$ and $I + K = J$
:::

Let
$$
\pi:J\to J/I
$$
be the quotient map, and choose a right $R$-module isomorphism
$$
\theta:R\overset{\sim}{\longrightarrow}J/I.
$$

::: pf

::: pf-step

Choose
$$
y\in J
$$
such that
$$
\pi(y)=\theta(1).
$$


::: pf-proof

The quotient map
$$
\pi:J\to J/I
$$
is surjective. Hence the element
$$
\theta(1)\in J/I
$$
has a lift
$$
y\in J.
$$

:::

:::

::: pf-step

Define
$$
K
\coloneqq
yR.
$$
Then $K$ is a right ideal of $R$ contained in $J$.


::: pf-proof

Since
$$
y\in J
$$
and $J$ is a right ideal,
$$
yr\in J
$$
for every
$$
r\in R.
$$
Thus
$$
K\subseteq J.
$$

Moreover, $K$ is closed under subtraction because
$$
yr-ys
=
y(r-s)
\in
yR,
$$
and it is closed under right multiplication because
$$
(yr)t
=
y(rt)
\in
yR.
$$
Hence $K$ is a right ideal.

:::

:::

::: pf-step

For every
$$
r\in R,
$$
one has
$$
\pi(yr)=\theta(r).
$$


::: pf-proof

Because $\pi$ and $\theta$ are right $R$-module homomorphisms,
$$
\begin{aligned}
\pi(yr)
&=
\pi(y)r\\
&=
\theta(1)r\\
&=
\theta(r).
\end{aligned}
$$

:::

:::

::: pf-step

One has
$$
I\cap K=(0).
$$


::: pf-proof

Let
$$
x\in I\cap K.
$$
Since
$$
x\in K,
$$
write
$$
x=yr
$$
for some
$$
r\in R.
$$
Because
$$
x\in I,
$$
one has
$$
\pi(x)=0.
$$
By step <1>3,
$$
0
=
\pi(yr)
=
\theta(r).
$$
Since $\theta$ is injective,
$$
r=0.
$$
Hence
$$
x=y0=0.
$$
Therefore
$$
I\cap K=(0).
$$

:::

:::

::: pf-step

One has
$$
I+K=J.
$$


::: pf-proof

Since
$$
I,K\subseteq J,
$$
one has
$$
I+K\subseteq J.
$$

Conversely, let
$$
j\in J.
$$
Because $\theta$ is surjective, there exists
$$
r\in R
$$
such that
$$
\pi(j)=\theta(r).
$$
By step <1>3,
$$
\theta(r)=\pi(yr).
$$
Hence
$$
\pi(j-yr)=0,
$$
so
$$
j-yr\in I.
$$
Since
$$
yr\in K,
$$
we obtain
$$
j
=
(j-yr)+yr
\in
I+K.
$$
Thus
$$
J\subseteq I+K.
$$
Therefore
$$
I+K=J.
$$

:::

:::

::: pf-step

Consequently
$$
\boxed{
J
=
I\oplus K
}
$$
as right $R$-modules.


::: pf-proof

Step <1>4 gives
$$
I\cap K=(0),
$$
and step <1>5 gives
$$
I+K=J.
$$
These are exactly the conditions for the internal direct sum.

:::

:::

::: pf-qed

The right ideal $K=yR$ from step <1>2 satisfies both required properties by steps <1>4--<1>5.

:::

:::
