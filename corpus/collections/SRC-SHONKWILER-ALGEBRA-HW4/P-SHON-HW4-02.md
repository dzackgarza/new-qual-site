---
schema: qual/card@1
id: P-SHON-HW4-02
kind: problem
title: Composition series of $Q_8$ and $D_8$
classification:
  areas: [algebra]
  topics:
  - Composition Series
  - Quaternion Group
  - Dihedral Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against exercise 3.4.2 in the retained Algebra HW 4 solution packet.
---

::: {.problem}
Find all three composition series for $Q_8$ and all seven composition series for $D_8$.
List the composition factors in each case.
:::

::: {.solution}

Use
$$
Q_8=\{\pm1,\pm i,\pm j,\pm k\}
$$
and
$$
D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle.
$$

Every composition series of a group of order $8$ has subgroup orders
$$
1,\ 2,\ 4,\ 8,
$$
and every composition factor has order $2$, hence is isomorphic to $C_2$.

## The quaternion group $Q_8$

::: pf

::: {.pf-step #s1-1}

The unique subgroup of order $2$ in $Q_8$ is
$$
\boxed{Z=\{1,-1\}}.
$$


::: pf-proof

The element $-1$ has order $2$. The six elements $\pm i,\pm j,\pm k$ all have order $4$, since their squares equal $-1$. Thus there is no other element, hence no other subgroup, of order $2$.

:::

:::

::: {.pf-step #s1-2}

The subgroups of order $4$ in $Q_8$ are exactly
$$
\boxed{\langle i\rangle,\qquad \langle j\rangle,\qquad \langle k\rangle}.
$$


::: pf-proof

Every subgroup of order $4$ contains an element of order $4$, and each such element generates one of the displayed cyclic subgroups. The pairs $\pm i,\pm j,\pm k$ give exactly three such subgroups.

:::

:::

::: pf-step

Each subgroup in step [](#s1-2){.pf-ref} contains $Z$.


::: pf-proof

For example,
$$
i^2=-1,
$$
so
$$
\langle i\rangle=\{1,-1,i,-i\}
$$
contains $Z$. The same argument applies to $j$ and $k$.

:::

:::

::: {.pf-step #s1-4}

Hence the three composition series of $Q_8$ are
$$
\boxed{
1\triangleleft Z\triangleleft\langle i\rangle\triangleleft Q_8},
$$
$$
\boxed{
1\triangleleft Z\triangleleft\langle j\rangle\triangleleft Q_8},
$$
and
$$
\boxed{
1\triangleleft Z\triangleleft\langle k\rangle\triangleleft Q_8}.
$$


::: pf-proof

The subgroup orders are $1,2,4,8$. Every subgroup of index $2$ is normal, and $Z$ is central. Thus each chain is subnormal. The successive quotients all have order $2$, hence are simple.

:::

:::

::: {.pf-step #s1-5}

There are no other composition series for $Q_8$.


::: pf-proof

Any composition series must have an order-$2$ subgroup, which by step [](#s1-1){.pf-ref} must be $Z$, and then an order-$4$ subgroup containing $Z$, which by step [](#s1-2){.pf-ref} is one of the three displayed groups.

:::

:::

::: {.pf-step #s1-6}

In every $Q_8$ composition series, the composition factors are
$$
\boxed{C_2,\ C_2,\ C_2}.
$$


::: pf-proof

Each successive quotient has order $2$.

:::

:::

::: pf-step

The elements of $D_8$ are
$$
\boxed{
1,r,r^2,r^3,s,sr,sr^2,sr^3}.
$$


::: pf-proof

Every word reduces using
$$
r^4=s^2=1
$$
and
$$
sr=r^{-1}s
$$
to either $r^a$ or $sr^a$, with $0\le a<4$.

:::

:::

::: {.pf-step #s1-8}

The subgroups of order $4$ are exactly
$$
\boxed{
R=\langle r\rangle},
$$
$$
\boxed{
V_0=\langle r^2,s\rangle
=
\{1,r^2,s,sr^2\}},
$$
and
$$
\boxed{
V_1=\langle r^2,sr\rangle
=
\{1,r^2,sr,sr^3\}}.
$$


::: pf-proof

The cyclic subgroup $R$ has order $4$.

Any order-$4$ subgroup not equal to $R$ must contain a reflection $sr^a$. Its square is $1$, and closure with the central element $r^2$ gives
$$
\{1,r^2,sr^a,sr^{a+2}\}.
$$
For even $a$, this is $V_0$; for odd $a$, this is $V_1$. Thus there are no others.

:::

:::

::: {.pf-step #s1-9}

Each subgroup in step [](#s1-8){.pf-ref} is normal in $D_8$.


::: pf-proof

Each has index $2$, and every index-$2$ subgroup is normal.

:::

:::

::: {.pf-step #s1-10}

The cyclic group
$$
R=\langle r\rangle\cong C_4
$$
has the unique subgroup of order $2$
$$
\boxed{\langle r^2\rangle}.
$$


::: pf-proof

A cyclic group of order $4$ has exactly one subgroup of order $2$.

:::

:::

::: {.pf-step #s1-11}

Therefore the unique composition series passing through $R$ is
$$
\boxed{
1\triangleleft\langle r^2\rangle\triangleleft\langle r\rangle\triangleleft D_8}.
$$


::: pf-proof

Use steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref}. All quotient orders are $2$.

:::

:::

::: {.pf-step #s1-12}

The group
$$
V_0\cong C_2\times C_2
$$
has exactly three subgroups of order $2$:
$$
\boxed{
\langle r^2\rangle,\qquad
\langle s\rangle,\qquad
\langle sr^2\rangle}.
$$


::: pf-proof

The three nonidentity elements $r^2,s,sr^2$ all have order $2$, and in a Klein four group each generates a distinct subgroup of order $2$.

:::

:::

::: {.pf-step #s1-13}

Thus the three composition series through $V_0$ are
$$
\boxed{
1\triangleleft\langle r^2\rangle\triangleleft V_0\triangleleft D_8},
$$
$$
\boxed{
1\triangleleft\langle s\rangle\triangleleft V_0\triangleleft D_8},
$$
and
$$
\boxed{
1\triangleleft\langle sr^2\rangle\triangleleft V_0\triangleleft D_8}.
$$


::: pf-proof

Every subgroup of $V_0$ is normal because $V_0$ is abelian, and $V_0\triangleleft D_8$ by step [](#s1-9){.pf-ref}. The quotient orders are all $2$.

:::

:::

::: {.pf-step #s1-14}

The group
$$
V_1\cong C_2\times C_2
$$
has exactly three subgroups of order $2$:
$$
\boxed{
\langle r^2\rangle,\qquad
\langle sr\rangle,\qquad
\langle sr^3\rangle}.
$$


::: pf-proof

The three nonidentity elements $r^2,sr,sr^3$ all have order $2$.

:::

:::

::: {.pf-step #s1-15}

Thus the three composition series through $V_1$ are
$$
\boxed{
1\triangleleft\langle r^2\rangle\triangleleft V_1\triangleleft D_8},
$$
$$
\boxed{
1\triangleleft\langle sr\rangle\triangleleft V_1\triangleleft D_8},
$$
and
$$
\boxed{
1\triangleleft\langle sr^3\rangle\triangleleft V_1\triangleleft D_8}.
$$


::: pf-proof

As in step [](#s1-13){.pf-ref}, every order-$2$ subgroup is normal in the abelian group $V_1$, and $V_1\triangleleft D_8$.

:::

:::

::: {.pf-step #s1-16}

Altogether, $D_8$ has exactly
$$
\boxed{1+3+3=7}
$$
composition series.


::: pf-proof

Every composition series must pass through an order-$4$ subgroup. Step [](#s1-8){.pf-ref} lists all three such subgroups. Steps [](#s1-11){.pf-ref} and [](#s1-13){.pf-ref}, and [](#s1-15){.pf-ref} enumerate all choices of order-$2$ subgroup inside each.

:::

:::

::: {.pf-step #s1-17}

In every $D_8$ composition series, the composition factors are
$$
\boxed{C_2,\ C_2,\ C_2}.
$$


::: pf-proof

Every successive quotient has order $2$.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give all three composition series of $Q_8$, while steps [](#s1-11){.pf-ref} through [](#s1-17){.pf-ref} give all seven composition series of $D_8$ and their factors.

:::

:::

:::
