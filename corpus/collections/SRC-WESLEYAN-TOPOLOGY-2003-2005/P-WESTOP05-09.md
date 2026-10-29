---
schema: qual/card@1
id: P-WESTOP05-09
kind: problem
title: The suspension of a path-connected space is simply connected
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For a space $X$, define its suspension $\Sigma X$ as the quotient of $X\times I$ obtained by collapsing $X\times\{0\}$ to one point and $X\times\{1\}$ to another point. Assuming $X$ is path-connected, compute with proof
$$
\pi_1(\Sigma X).
$$
:::

::: {.solution}

Let
$$
q:X\times I\to\Sigma X
$$
be the quotient map. Denote the two suspension points by
$$
S=q(X\times\{0\}),
\qquad
N=q(X\times\{1\}).
$$

::: pf

::: {.pf-step #s1-1}

Define
$$
U=q\bigl(X\times[0,2/3)\bigr)
$$
and
$$
V=q\bigl(X\times(1/3,1]\bigr).
$$


::: pf-proof

These are saturated subsets for the quotient relation because the entire
collapsed end $X\times\{0\}$ lies in the first set and the entire collapsed
end $X\times\{1\}$ lies in the second.

:::

:::

::: {.pf-step #s1-2}

The sets $U$ and $V$ are open in $\Sigma X$.


::: pf-proof

The subsets
$$
X\times[0,2/3)
$$
and
$$
X\times(1/3,1]
$$
are open in the product $X\times I$, using the subspace topology on
$I=[0,1]$. Since they are saturated, their quotient images are open.

:::

:::

::: pf-step

One has
$$
\boxed{
\Sigma X=U\cup V}.
$$


::: pf-proof

The intervals
$$
[0,2/3)
\qquad\text{and}\qquad
(1/3,1]
$$
cover $I$.

:::

:::

::: {.pf-step #s1-4}

The space $U$ is contractible.


::: pf-proof

It is a truncated cone on $X$ with cone point $S$. Define
$$
H_U(q(x,t),s)
=
q(x,(1-s)t).
$$
This is well defined because all points with $t=0$ are already identified.
At $s=1$, every point is sent to $S$.

:::

:::

::: {.pf-step #s1-5}

The space $V$ is contractible.


::: pf-proof

It is a truncated cone on $X$ with cone point $N$. Define
$$
H_V(q(x,t),s)
=
q(x,t+s(1-t)).
$$
At $s=1$, every point is sent to $N$.

:::

:::

::: pf-step

The intersection is
$$
\boxed{
U\cap V
=
q\bigl(X\times(1/3,2/3)\bigr)}.
$$


::: pf-proof

This is the overlap of the two interval factors from step [](#s1-1){.pf-ref}.
No quotient identifications occur in the open middle interval.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
U\cap V
\cong
X\times(1/3,2/3)}.
$$


::: pf-proof

The quotient map is injective on
$$
X\times(1/3,2/3),
$$
since only the two endpoint slices of $X\times I$ are collapsed.

:::

:::

::: pf-step

Therefore
$$
\boxed{
U\cap V\simeq X}.
$$


::: pf-proof

The interval
$$
(1/3,2/3)
$$
is contractible, so projection onto $X$ is a homotopy equivalence.

:::

:::

::: {.pf-step #s1-9}

Since $X$ is path connected,
$$
\boxed{
U\cap V
\text{ is path connected}}.
$$


::: pf-proof

A product of path-connected spaces is path connected. Use step [](#s1-7){.pf-ref} and the
fact that the interval is path connected.

:::

:::

::: {.pf-step #s1-10}

The spaces $U$ and $V$ are path connected.


::: pf-proof

Each is contractible by steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}, hence path connected.

:::

:::

::: {.pf-step #s1-11}

The Seifert--van Kampen theorem gives
$$
\pi_1(\Sigma X)
\cong
\pi_1(U)
*_{\pi_1(U\cap V)}
\pi_1(V).
$$


::: pf-proof

The cover
$$
\Sigma X=U\cup V
$$
is by open path-connected sets with path-connected intersection by steps
[](#s1-2){.pf-ref} and [](#s1-9){.pf-ref}, and [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\boxed{
\pi_1(U)=0}
$$
and
$$
\boxed{
\pi_1(V)=0}.
$$


::: pf-proof

Both spaces are contractible by steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
\pi_1(\Sigma X)=0}.
$$


::: pf-proof

The amalgamated free product of the two trivial groups is trivial,
regardless of the maps from $\pi_1(U\cap V)$. Apply step [](#s1-11){.pf-ref} and step
[](#s1-12){.pf-ref}.

:::

:::

::: pf-step

Thus the suspension of every path-connected space is simply
connected.


::: pf-proof

The suspension is path connected because $U$ and $V$ are path connected
and intersect nontrivially, and step [](#s1-13){.pf-ref} gives trivial fundamental group.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the requested computation.

:::

:::

:::
