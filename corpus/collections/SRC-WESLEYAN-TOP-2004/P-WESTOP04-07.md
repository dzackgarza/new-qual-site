---
schema: qual/card@1
id: P-WESTOP04-07
kind: problem
title: Lindelöfness of products with and without metrizability
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove or disprove each statement:

1. The product of two Lindelöf spaces is Lindelöf.
2. The product of two metrizable Lindelöf spaces is Lindelöf.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (1) is false.


::: pf-proof

Use the Sorgenfrey line
$$
\mathbb S,
$$
whose topology has basis
$$
\{
[a,b):
a<b
\}.
$$
Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} show that
$$
\mathbb S
$$
is Lindelöf but
$$
\mathbb S\times\mathbb S
$$
is not.

:::

:::

::: {.pf-step #s1-2}

The Sorgenfrey line
$$
\mathbb S
$$
is Lindelöf.


::: pf-proof

Let
$$
\mathcal U
$$
be an open cover of
$$
\mathbb S.
$$
Refining if necessary, for each
$$
x\in\RR
$$
choose a basic interval
$$
[x,b_x)
$$
contained in some member of
$$
\mathcal U.
$$

Define
$$
V
\coloneqq
\bigcup_{x\in\RR}
(x,b_x),
$$
where the intervals on the right are ordinary Euclidean-open intervals. The set
$$
V
$$
is Euclidean open, hence Lindelöf in the usual topology. Therefore the Euclidean-open cover
$$
\{
(x,b_x):
x\in\RR
\}
$$
of $V$ has a countable subcover
$$
\{
(x_n,b_{x_n})
\}_{n\ge1}.
$$

Let
$$
D
\coloneqq
\RR\setminus V.
$$
If
$$
x<y
$$
are points of $D$, then
$$
y\notin(x,b_x),
$$
so
$$
b_x\le y.
$$
Hence the intervals
$$
(x,b_x),
\qquad
x\in D,
$$
are pairwise disjoint. Choose one rational number
$$
q_x\in(x,b_x)
$$
for each
$$
x\in D.
$$
Disjointness makes the map
$$
x\longmapsto q_x
$$
injective into
$$
\QQ,
$$
so
$$
D
$$
is countable.

Now the countably many basic intervals
$$
[x_n,b_{x_n})
$$
cover
$$
V,
$$
and the countably many intervals
$$
[x,b_x),
\qquad
x\in D,
$$
cover the remaining points. Thus a countable collection of the chosen basic intervals covers
$$
\mathbb S.
$$
Replacing each basic interval by the original member of
$$
\mathcal U
$$
that contained it gives a countable subcover of
$$
\mathcal U.
$$

:::

:::

::: {.pf-step #s1-3}

The anti-diagonal
$$
A
\coloneqq
\{
(x,-x):
x\in\RR
\}
$$
is a closed discrete subspace of
$$
\mathbb S\times\mathbb S.
$$


::: pf-proof

For discreteness, fix
$$
x\in\RR.
$$
Then
$$
\left(
[x,x+1)
\times
[-x,-x+1)
\right)
\cap A
=
\{(x,-x)\}.
$$
Indeed, if
$$
(t,-t)
$$
lies in the rectangle, then
$$
t\ge x
$$
and
$$
-t\ge-x,
$$
so
$$
t=x.
$$

For closedness, let
$$
(u,v)\notin A,
$$
so
$$
u+v\ne0.
$$
If
$$
u+v>0,
$$
then every point of a sufficiently small rectangle
$$
[u,u+\varepsilon)
\times
[v,v+\varepsilon)
$$
has positive coordinate sum. If
$$
u+v<0,
$$
choose
$$
0<\varepsilon<-\frac{u+v}{2};
$$
then every point of that rectangle has negative coordinate sum. In either case the rectangle misses
$$
A.
$$
Thus the complement of
$$
A
$$
is open.

:::

:::

::: {.pf-step #s1-4}

The product
$$
\mathbb S\times\mathbb S
$$
is not Lindelöf.


::: pf-proof

The closed subspace
$$
A
$$
from step [](#s1-3){.pf-ref} is an uncountable discrete space. It is not Lindelöf, because the open cover by singleton sets
$$
\{
\{a\}:
a\in A
\}
$$
has no countable subcover.

Every closed subspace of a Lindelöf space is Lindelöf: if
$$
F\subseteq X
$$
is closed and
$$
\mathcal V
$$
is an open cover of
$$
F,
$$
then adjoining
$$
X\setminus F
$$
gives an open cover of
$$
X;
$$
a countable subcover restricts to one of
$$
F.
$$
Therefore
$$
\mathbb S\times\mathbb S
$$
cannot be Lindelöf.

:::

:::

::: {.pf-step #s1-5}

Every metrizable Lindelöf space is second countable.


::: pf-proof

Let
$$
(X,d)
$$
be metrizable and Lindelöf. For each
$$
n\ge1,
$$
the family
$$
\{
B(x,1/n):
x\in X
\}
$$
is an open cover. Choose a countable subcover
$$
\mathcal B_n.
$$
Set
$$
\mathcal B
\coloneqq
\bigcup_{n=1}^{\infty}\mathcal B_n.
$$
This family is countable.

To see that it is a base, let
$$
U
$$
be open and
$$
x\in U.
$$
Choose
$$
\varepsilon>0
$$
with
$$
B(x,\varepsilon)\subseteq U.
$$
Choose
$$
n
$$
so large that
$$
2/n<\varepsilon.
$$
Since
$$
\mathcal B_n
$$
covers
$$
X,
$$
there is
$$
B(c,1/n)\in\mathcal B_n
$$
containing
$$
x.
$$
If
$$
y\in B(c,1/n),
$$
then
$$
d(y,x)
\le
d(y,c)+d(c,x)
<
2/n
<
\varepsilon.
$$
Thus
$$
x
\in
B(c,1/n)
\subseteq
U.
$$
So
$$
\mathcal B
$$
is a countable base.

:::

:::

::: {.pf-step #s1-6}

The product of two second-countable spaces is second countable.


::: pf-proof

Let
$$
\mathcal B_X
$$
and
$$
\mathcal B_Y
$$
be countable bases for
$$
X
$$
and
$$
Y.
$$
Then
$$
\{
B\times C:
B\in\mathcal B_X,
\ C\in\mathcal B_Y
\}
$$
is a countable base for the product topology on
$$
X\times Y.
$$

:::

:::

::: {.pf-step #s1-7}

Every second-countable space is Lindelöf.


::: pf-proof

Let
$$
\mathcal B
$$
be a countable base and
$$
\mathcal U
$$
an open cover. For each basic set
$$
B\in\mathcal B
$$
that is contained in some member of
$$
\mathcal U,
$$
choose one such member
$$
U_B\in\mathcal U.
$$
The chosen family is countable.

For every
$$
x\in X,
$$
choose
$$
U\in\mathcal U
$$
with
$$
x\in U.
$$
By the base property, some
$$
B\in\mathcal B
$$
satisfies
$$
x\in B\subseteq U.
$$
Then the chosen
$$
U_B
$$
contains
$$
B
$$
and hence
$$
x.
$$
Thus the chosen family is a countable subcover.

:::

:::

::: {.pf-step #s1-8}

Statement (2) is true:
$$
\boxed{
X,Y\text{ metrizable and Lindelöf}
\Longrightarrow
X\times Y\text{ Lindelöf}.}
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
X
$$
and
$$
Y
$$
are second countable. Step [](#s1-6){.pf-ref} makes
$$
X\times Y
$$
second countable, and step [](#s1-7){.pf-ref} makes it Lindelöf.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} disprove statement (1), and steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} prove statement (2).

:::

:::

:::
