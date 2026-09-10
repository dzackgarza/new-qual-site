---
schema: qual/card@1
id: P-ARTALG-SU05-1
kind: problem
title: Sylow theorems, groups of order 35, simplicity of order 24
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
  note: "Compared all three parts with Summer 2005 problem 1 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the complete Sylow statements, both Sylow counts for order 35, and the kernel and faithful-image cases for order 24."
---

::: problem
(a) State Sylow's theorems.

(b) Classify up to isomorphism the groups of order 35.

(c) Show that there are no simple groups of order 24.
:::

::: solution
<1>1. The Sylow theorems have the following form.

Let $G$ be finite, let $p$ be prime, and write $|G|=p^am$ with
$p\nmid m$. A Sylow $p$-subgroup is a subgroup of order $p^a$.
Such subgroups exist. Every $p$-subgroup of $G$ is contained in a
Sylow $p$-subgroup, and all Sylow $p$-subgroups are conjugate.
For a Sylow $p$-subgroup $P$, their number is
$$
n_p=[G:N_G(P)],\qquad n_p\mid m,\qquad n_p\equiv1\pmod p,
$$
where $N_G(P)=\{g\in G:gPg^{-1}=P\}$.
In particular, $P$ is normal exactly when $n_p=1$ [@DF04].

<1>2. Every group of order $35$ is cyclic; hence $C_{35}$ is the
unique isomorphism class.

::: proof
Since $35=5\cdot7$, step <1>1 gives
$$
n_7\mid5,\quad n_7\equiv1\pmod7,
\qquad n_5\mid7,\quad n_5\equiv1\pmod5.
$$
The divisors of $5$ are $1,5$, and only $1$ is $1$ modulo $7$.
The divisors of $7$ are $1,7$, and only $1$ is $1$ modulo $5$.
Thus the subgroups $P$ and $Q$ of orders $5$ and $7$ are both
normal. Their intersection is trivial, since its order divides
both $5$ and $7$.

For $x\in P$ and $y\in Q$, the commutator $xyx^{-1}y^{-1}$
lies in both normal subgroups, hence is $1$. Thus they commute.
The multiplication map $P\times Q\to G$ is a homomorphism with
trivial kernel: $xy=1$ implies $x=y^{-1}\in P\cap Q$.
It is therefore injective and, since both groups have $35$
elements, surjective. Each prime-order group is cyclic by
Lagrange's theorem. Generators $x$ of $P$ and $y$ of $Q$ give
an element $(x,y)$ of order $35$, because an integer power is
the identity exactly when the exponent is divisible by both
$5$ and $7$. Therefore $G\cong C_{35}$, and $C_{35}$ realizes
the required order.
:::

<1>3. Every group of order $24$ has a nontrivial proper normal subgroup.

::: proof
Here $n_3$ divides $8$ and is $1$ modulo $3$. Of the divisors
$1,2,4,8$, exactly $1$ and $4$ satisfy that congruence.
If $n_3=1$, the unique subgroup of order $3$ is nontrivial,
proper, and normal.

Suppose $n_3=4$. Conjugation on the four Sylow $3$-subgroups
gives a homomorphism $\rho:G\to S_4$. The action is transitive
by Sylow conjugacy, so it is nontrivial and $\ker\rho\ne G$.
If $\ker\rho\ne\{1\}$, this kernel is the required subgroup.

In the remaining case $\rho$ is injective. Both $G$ and $S_4$
have order $24$, so $\rho$ is an isomorphism. The sign map
$S_4\to\{1,-1\}$ is onto, since a transposition has sign $-1$.
Its kernel $A_4$ is normal of order $12$, and
$\rho^{-1}(A_4)$ is a nontrivial proper normal subgroup of $G$.
All possibilities have been covered, so no group of order $24$
is simple.
:::
:::
