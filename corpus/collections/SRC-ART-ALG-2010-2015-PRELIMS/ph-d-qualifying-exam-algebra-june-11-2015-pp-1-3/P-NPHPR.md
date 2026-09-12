---
schema: qual/card@1
id: P-NPHPR
kind: problem
title: A proper subgroup of a finite $p$-group is proper in its normalizer
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the finite p-group and strict-subgroup hypotheses with June 2015 Groups 4 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the identification of fixed cosets with normalizer cosets, the divisibility of every nontrivial orbit, and the case of the trivial acting subgroup."
---

::: problem
Let $p$ be a prime number, and $P$ a finite $p$-group.
Suppose $H$ is a proper subgroup of $P$.
Prove that $H$ is also a proper subgroup of $N_P(H)$, the normalizer of $H$ in $P$.
:::

::: solution
Let $X$ be the set of left cosets $P/H$. The subgroup $H$ acts
on $X$ by left multiplication, $h\cdot(aH)=haH$.

<1>1. The fixed cosets are exactly the cosets represented by
elements of $N_P(H)$.

::: proof
A coset $aH$ is fixed by every $h\in H$ exactly when
$$
haH=aH\quad\text{for every }h\in H,
$$
or equivalently $a^{-1}Ha\subseteq H$. Both finite subgroups
have order $|H|$, so this containment is equality. That equality
is equivalent to $a\in N_P(H)$. Consequently the fixed-point
set $X^H$ is the coset set $N_P(H)/H$, and
$$
|X^H|=[N_P(H):H].
$$
:::

<1>2. The number of fixed cosets is a positive multiple of $p$.

::: proof
Every orbit of the $H$-action has size the index of its stabilizer
in $H$, by orbit-stabilizer [@DF04]. Since $H$ is a subgroup
of a finite $p$-group, its order is a power of $p$. Thus every
orbit has power-of-$p$ size. Orbits of size one are the fixed
points; every other orbit has size divisible by $p$. The orbit
partition therefore gives
$$
|X|\equiv |X^H|\pmod p.
$$
The proper-subgroup hypothesis makes $|X|=[P:H]$ a power of
$p$ greater than one, hence divisible by $p$. Thus $p\mid|X^H|$.
The coset $H$ itself is fixed, so $|X^H|>0$ and $|X^H|\geq p$.
The argument also covers $H=1$: then every orbit is a singleton,
and the same count applies.
:::

<1>3. The containment $H\subseteq N_P(H)$ is strict.

::: proof
Every subgroup normalizes itself. Steps <1>1 and <1>2 give
$[N_P(H):H]=|X^H|\geq p>1$, so $H\ne N_P(H)$.
:::
:::
