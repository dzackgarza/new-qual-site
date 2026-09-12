---
schema: qual/card@1
id: P-3DGMZ
kind: problem
title: The Sylow theorems
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked June 2010 Groups 1 on PDF page 13, including the existence, order, conjugacy, divisibility, and congruence requests; corrected the area to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the full theorem statement, stabilizer formula, divisibility by the prime-to-p factor, uniqueness of the fixed Sylow subgroup, and the normality criterion."
---

::: {.problem}
State the Sylow Theorems.
Include information about the existence, order, and number $n_p$ of Sylow $p$-subgroups of a finite group, and mention additional divisibility and congruence properties of $n_p$.
:::

::: solution
Let $G$ be finite, let $p$ be prime, and write
$|G|=p^a m$ with $a\geq0$ and $p\nmid m$.

<1>1. Existence, containment, and conjugacy.

A Sylow $p$-subgroup is a subgroup of order $p^a$.
Such subgroups exist. Every subgroup of $G$ whose order
is a power of $p$ is contained in a Sylow $p$-subgroup.
Any two Sylow $p$-subgroups are conjugate by an element
of $G$ [@DF04, sec. 4.5].

<1>2. The number $n_p$ of Sylow $p$-subgroups satisfies
$$
n_p=[G:N_G(P)],\qquad n_p\mid m,\qquad
n_p\equiv1\pmod p
$$
for any Sylow $p$-subgroup $P$.

::: proof
Conjugation is transitive on the Sylow subgroups by step
<1>1, and the stabilizer of $P$ is its normalizer
$N_G(P)=\{g\in G:gPg^{-1}=P\}$. Orbit-stabilizer gives
the index formula [@DF04]. Since $P\leq N_G(P)$,
$$
m=[G:P]=[G:N_G(P)]\,[N_G(P):P],
$$
so $n_p\mid m$.

For the congruence, restrict the conjugation action to $P$.
Every orbit has power-of-$p$ size by orbit-stabilizer; hence
all non-singleton orbits have size divisible by $p$.
The subgroup $P$ itself is a fixed point. If another Sylow
subgroup $Q$ is fixed, then $P$ normalizes $Q$. Consequently
$PQ$ is a subgroup, of order $|P||Q|/|P\cap Q|$, a power
of $p$. Its order divides $|G|$ and hence is at most $p^a$.
But it contains both order-$p^a$ groups $P,Q$, forcing
$P=PQ=Q$. Thus there is exactly one fixed point, and
counting orbits gives $n_p\equiv1\pmod p$.
:::

<1>3. A Sylow $p$-subgroup $P$ is normal exactly when $n_p=1$.

::: proof
If $P$ is normal, its conjugacy orbit has one member;
conjugacy in step <1>1 then implies that it is the only
Sylow subgroup. Conversely, if it is unique, each conjugate
has the same order and must equal $P$, which is normality.
For $a=0$, the unique Sylow subgroup is the trivial group,
so all statements above also cover primes not dividing $|G|$.
:::
:::
