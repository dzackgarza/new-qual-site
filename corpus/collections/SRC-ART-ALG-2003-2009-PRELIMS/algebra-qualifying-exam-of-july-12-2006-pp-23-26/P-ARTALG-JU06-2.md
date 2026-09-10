---
schema: qual/card@1
id: P-ARTALG-JU06-2
kind: problem
title: Sylow subgroups and simplicity
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the Sylow definition, theorem request, and order 132 with July 2006 Groups 2 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked every Sylow-count possibility and proved both nontriviality and properness of the action kernel."
---

::: problem
Let $G$ be a group of order $p^k m$, where $p$ is a prime not dividing $m$.

(a) What is a Sylow $p$-subgroup of $G$?

(b) State Sylow's theorem, including information about the number of Sylow $p$-subgroups of $G$ and about relationships between them.

(c) Show that there are no simple groups of order 132.
:::

::: solution
<1>1. A Sylow $p$-subgroup is a subgroup of order $p^k$.
Sylow's theorems assert that such subgroups exist, that every
$p$-subgroup is contained in one, and that all Sylow $p$-subgroups
are conjugate. Their number $n_p$ satisfies
$$
n_p\mid m,\qquad n_p\equiv1\pmod p.
$$
These are the Sylow theorems in their finite-group form [@DF04].
In particular, a unique Sylow subgroup is normal, because conjugation
preserves its order.

<1>2. A group of order $132=2^2\cdot3\cdot11$ has a nontrivial
proper normal subgroup.

::: proof
The number $n_{11}$ divides $12$ and is $1$ modulo $11$, so
$n_{11}=1$ or $12$. In the first case the unique subgroup of
order $11$ is the required normal subgroup.

Suppose $n_{11}=12$. Two different subgroups of order $11$ intersect
only in the identity, since a nonidentity element generates each
subgroup of prime order containing it. They therefore account for
$12\cdot10=120$ distinct elements of order $11$.
Of the $131$ nonidentity elements in $G$, only $11$ remain.
Different subgroups of order $3$ likewise have disjoint nonidentity
parts, and each contributes two elements of order $3$. Hence
$2n_3\leq11$, giving $n_3\leq5$.

By Sylow's theorem, $n_3$ divides $44$ and is $1$ modulo $3$.
The divisors of $44$ are $1,2,4,11,22,44$; the ones congruent to
$1$ modulo $3$ are $1,4,22$. The bound just obtained therefore
leaves $n_3=1$ or $4$.

If $n_3=1$, the unique subgroup of order $3$ is normal and is
nontrivial and proper. If $n_3=4$, conjugation on these four
subgroups gives a homomorphism $\varphi:G\to S_4$. It is not
injective, since $|G|=132>24=|S_4|$, so $\ker\varphi\ne\{1\}$.
Its image is not trivial: Sylow conjugacy makes the action
transitive on a set of four elements, whereas the trivial action
has singleton orbits. Thus $\ker\varphi\ne G$ as well.
Being the kernel of a homomorphism, it is a normal subgroup.
Every case has produced a nontrivial proper normal subgroup,
so no group of order $132$ is simple.
:::
:::
