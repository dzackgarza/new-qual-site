---
schema: qual/card@1
id: E-SMI-8000E-SY7
kind: problem
title: Fixed points of p-groups and conjugacy of Sylow subgroups
classification:
  areas:
  - algebra
  topics:
  - Sylow Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both parts with Smith 8000e Sylow problem 7."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved the fixed-point congruence by orbit decomposition and deduced Sylow conjugacy from the P'-action on G/P without invoking the conjugacy part of Sylow's theorem."
---

::: {.exercise}
(i) Prove that the number of fixed points for the action of a $p$-group on a finite set is congruent mod $p$ to the cardinality of the set.

(ii) If $P$, $P'$ are any two Sylow subgroups of a group $G$, using only part (i) — and nothing else except that $P$ and $P'$ exist — prove $P$ is conjugate to $P'$, by looking at the action of $P'$ on the set $G/P$ of cosets of $P$ in $G$.
:::

::: {.solution}
<1>1. For a finite $p$-group action, the number of fixed points is congruent to the size of the set modulo $p$.
::: {.proof}
Let a finite $p$-group $Q$ act on a finite set $X$. Decompose $X$ into
$Q$-orbits. For $x\in X$, the orbit-stabilizer theorem gives
$$
|Qx|=[Q:Q_x].
$$
Since $|Q|$ is a power of $p$, every orbit size is a power of $p$. An orbit
has size $1$ exactly when its point is fixed by all of $Q$; every other orbit
therefore has cardinality divisible by $p$.

If $X^Q$ denotes the fixed-point set, summing the orbit sizes yields
$$
|X|=|X^Q|+pN
$$
for some integer $N$. Hence
$$
\boxed{|X^Q|\equiv |X|\pmod p.}
$$
:::

<1>2. Let $P'$ act on the left cosets $G/P$ by left multiplication.
::: {.proof}
Define
$$
x\cdot(gP)=(xg)P
\qquad(x\in P').
$$
This is a well-defined action of the $p$-group $P'$ on the finite set $G/P$.
Because $P$ is Sylow,
$$
|G/P|=[G:P]
$$
is not divisible by $p$. By step <1>1,
$$
|(G/P)^{P'}|\equiv [G:P]\not\equiv0\pmod p.
$$
Therefore the action has at least one fixed coset, say
$$
gP.
$$
:::

<1>3. A fixed coset forces $P$ and $P'$ to be conjugate.
::: {.proof}
The coset $gP$ is fixed by $P'$ precisely when, for every $x\in P'$,
$$
xgP=gP.
$$
Equivalently,
$$
g^{-1}xg\in P
$$
for every $x\in P'$. Thus
$$
g^{-1}P'g\le P.
$$
Both $P$ and $P'$ are Sylow $p$-subgroups of $G$, so they have the same
order. Conjugation preserves order, hence
$$
|g^{-1}P'g|=|P'|=|P|.
$$
The displayed inclusion is therefore an equality:
$$
g^{-1}P'g=P.
$$
Equivalently,
$$
\boxed{P'=gPg^{-1}.}
$$
Thus any two Sylow $p$-subgroups are conjugate, using only the fixed-point
congruence and the existence/equal order of Sylow subgroups.
:::
:::
