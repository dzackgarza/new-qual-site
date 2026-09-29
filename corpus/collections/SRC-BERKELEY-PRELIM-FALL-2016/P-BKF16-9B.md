---
schema: qual/card@1
id: P-BKF16-9B
kind: problem
title: Classification of groups of order $12$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: the Sylow
    3-subgroup count is 1 or 4, giving four semidirect products in the normal
    C3 case and A4 in the four-Sylow-3 case.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Sylow counts, both normal-complement decompositions, the
    classification of actions through Aut(C3) and Aut(V4), identification of
    the five groups, and invariants separating their isomorphism classes.
---

::: {.problem}
Find (with proof) the number of groups of order $12$ up to isomorphism.
You may assume the Sylow theorems: if a prime power $p^n$ is the largest power of $p$ dividing the order of a group, then the group has subgroups of order $p^n$ and the number of them is $1 \pmod p$.
:::

::: {.solution}
Let $n_3$ denote the number of Sylow $3$-subgroups of $G$.

::: pf

::: pf-step

One has
$$
n_3\in\{1,4\}.
$$

::: pf-proof

By the Sylow theorems,
$$
n_3\equiv1\pmod3
$$
and
$$
n_3\mid4.
$$
The only divisors of $4$ congruent to $1$ modulo $3$ are $1$ and $4$.

:::

:::

::: {.pf-step #s2}

Suppose first that $n_3=1$. If $P$ is the Sylow $3$-subgroup and
$H$ is any Sylow $2$-subgroup, then
$$
P\cong C_3,
\qquad
|H|=4,
\qquad
G\cong P\rtimes H.
$$

::: pf-proof

The unique Sylow $3$-subgroup $P$ is normal. Since $|P|=3$ and
$|H|=4$,
$$
P\cap H=1.
$$
Because $P$ is normal, $PH$ is a subgroup, and
$$
|PH|
=
\frac{|P||H|}{|P\cap H|}
=
12.
$$
Thus $PH=G$, giving the semidirect-product decomposition.

:::

:::

::: {.pf-step #s3}

In the case $n_3=1$, there are exactly four semidirect products
up to isomorphism.

::: pf-proof

Every group of order $4$ is isomorphic to either
$$
C_4
$$
or
$$
V_4\cong C_2\times C_2.
$$
The action in step [](#s2){.pf-ref} is a homomorphism
$$
H\to\Aut(C_3)\cong C_2.
$$

For $H=C_4$, there are exactly two homomorphisms to $C_2$: the trivial
one and the surjection whose kernel has order $2$.

For $H=V_4$, there is the trivial homomorphism and there are three
nontrivial homomorphisms. Each nontrivial homomorphism has an order-$2$
kernel, and $\Aut(V_4)$ acts transitively on the three order-$2$
subgroups. Hence those three nontrivial actions yield isomorphic
semidirect products.

Thus each of the two possibilities for $H$ gives one trivial and one
nontrivial action, for a total of four isomorphism types.

:::

:::

::: {.pf-step #s4}

The four groups from step [](#s3){.pf-ref} are
$$
C_{12},
\qquad
C_6\times C_2,
\qquad
C_3\rtimes C_4,
\qquad
S_3\times C_2,
$$
where in $C_3\rtimes C_4$ a generator of $C_4$ acts on $C_3$ by
inversion.

::: pf-proof

The trivial $C_4$-action gives
$$
C_3\times C_4\cong C_{12}.
$$
The trivial $V_4$-action gives
$$
C_3\times V_4
\cong
C_3\times C_2\times C_2
\cong
C_6\times C_2.
$$

For the nontrivial $C_4$-action, a generator maps to the nonidentity
element of
$$
\Aut(C_3)\cong C_2,
$$
which is inversion. This gives the displayed nontrivial semidirect
product $C_3\rtimes C_4$.

For the nontrivial $V_4$-action, write
$$
V_4=\langle x\rangle\times\langle y\rangle
$$
so that $x$ acts on $C_3$ by inversion and $y$ lies in the kernel of
the action. Then
$$
C_3\rtimes\langle x\rangle\cong S_3,
$$
while $\langle y\rangle$ centralizes both factors. Hence
$$
C_3\rtimes V_4
\cong
S_3\times C_2.
$$

:::

:::

::: {.pf-step #s5}

Suppose now that $n_3=4$. Then $G$ has a unique Sylow
$2$-subgroup $H$, so $H$ is normal.

::: pf-proof

Distinct subgroups of order $3$ intersect only in the identity. Hence
the four Sylow $3$-subgroups contribute
$$
4(3-1)=8
$$
distinct nonidentity elements of order $3$.

A Sylow $2$-subgroup has order $4$, and none of its three nonidentity
elements has order $3$. Thus all four of its elements lie in the set
consisting of the identity and the three elements not among those eight
order-$3$ elements. Since that set has exactly four elements, every
Sylow $2$-subgroup must equal it. Therefore the Sylow $2$-subgroup is
unique and normal.

:::

:::

::: {.pf-step #s6}

In the case $n_3=4$, one has
$$
H\cong V_4.
$$

::: pf-proof

Let $P$ be any Sylow $3$-subgroup. By step [](#s5){.pf-ref}, $H$ is normal, so as
in step [](#s2){.pf-ref},
$$
G\cong H\rtimes P.
$$

If $H\cong C_4$, then
$$
\Aut(H)\cong C_2.
$$
Every homomorphism
$$
C_3\to C_2
$$
is trivial, so the semidirect product would be the direct product
$$
C_4\times C_3\cong C_{12}.
$$
That group has a unique Sylow $3$-subgroup, contradicting $n_3=4$.
Hence $H\cong V_4$.

:::

:::

::: {.pf-step #s7}

The case $n_3=4$ yields exactly one isomorphism type, namely
$$
G\cong A_4.
$$

::: pf-proof

By step [](#s6){.pf-ref},
$$
G\cong V_4\rtimes C_3.
$$
The action
$$
C_3\to\Aut(V_4)\cong S_3
$$
cannot be trivial, since a trivial action would make the Sylow
$3$-subgroup normal. Therefore the action is injective and its image is
the unique subgroup of order $3$ in $S_3$. Hence there is only one
nontrivial action up to isomorphism.

The alternating group $A_4$ realizes this semidirect product: its
normal Klein four subgroup is
$$
\{1,(12)(34),(13)(24),(14)(23)\},
$$
and a $3$-cycle acts by conjugation as a $3$-cycle on the three
nonidentity elements of that subgroup. Thus the unique group in this
case is $A_4$.

:::

:::

::: {.pf-step #s8}

The five groups obtained in steps [](#s4){.pf-ref} and [](#s7){.pf-ref} are pairwise
nonisomorphic.

::: pf-proof

The group $A_4$ is separated from the other four by having four Sylow
$3$-subgroups; the groups in step [](#s4){.pf-ref} have a unique Sylow
$3$-subgroup.

Among the four groups in step [](#s4){.pf-ref}, the two groups from trivial actions
are abelian and the two groups from nontrivial actions are nonabelian.
The abelian groups are distinct because $C_{12}$ is cyclic, while
$C_6\times C_2$ has no element of order $12$.

Finally, the nontrivial product
$$
C_3\rtimes C_4
$$
contains an element of order $4$, namely a generator of its $C_4$
complement. The group
$$
S_3\times C_2
$$
has no element of order $4$, since element orders in $S_3$ are
$1$, $2$, or $3$. Thus these two groups are not isomorphic.

:::

:::

::: {.pf-step #s9}

The number of groups of order $12$ up to isomorphism is
$$
\boxed{5}.
$$

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} give four isomorphism types when $n_3=1$. Steps
[](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} give one isomorphism type when $n_3=4$. Step [](#s8){.pf-ref} shows that
all five are distinct.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref} is the requested count.

:::

:::

:::
