---
schema: qual/card@1
id: E-SMI-8000E-SY1
kind: problem
title: Small p-subgroups lie in Sylow subgroups
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
  note: "Compared the card with the Sylow-subgroups section of the Smith 8000e packet."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used the conjugation action of Q on the Sylow p-subgroups, the mod-p fixed-point count, and maximality of a Sylow subgroup to pass from normalization to containment."
---

::: {.exercise}
Imitate the proof given in class for the number of Sylow subgroups to prove that if $\#G = m(p^r)$ where $p$ does not divide $m$, and if $Q$ is any subgroup of $G$ of order $p^s$ where $s < r$, then $Q$ is contained in some Sylow subgroup of order $p^r$.
[The case $s = r$ was proved in class. The point is to let $Q$ act on the set of Sylow subgroups by conjugation, prove there is a fixed point, and conclude that $Q$ is contained in the fixed Sylow group.]
:::

::: {.solution}
Let $\mathcal S$ be the set of Sylow $p$-subgroups of $G$.

<1>1. The $p$-group $Q$ acts on $\mathcal S$ by conjugation.
::: {.proof}
For $q\in Q$ and $P\in\mathcal S$, define
$$
q\cdot P=qPq^{-1}.
$$
Conjugation preserves subgroup order, so $qPq^{-1}$ is again a subgroup of
order $p^r$. Thus it is again Sylow, and the formula defines an action of
$Q$ on $\mathcal S$.
:::

<1>2. This action has a fixed point.
::: {.proof}
By Sylow's theorem,
$$
|\mathcal S|\equiv1\pmod p.
$$
Every $Q$-orbit has size
$$
[Q:\operatorname{Stab}_Q(P)],
$$
hence a power of $p$. Therefore every nontrivial orbit has cardinality
divisible by $p$. If $\mathcal S^Q$ denotes the set of fixed points, the orbit
decomposition gives
$$
|\mathcal S|\equiv |\mathcal S^Q|\pmod p.
$$
Since $|\mathcal S|\equiv1\pmod p$, we have
$$
|\mathcal S^Q|\equiv1\pmod p,
$$
so $\mathcal S^Q$ is nonempty. Choose
$$
P\in\mathcal S^Q.
$$
:::

<1>3. A fixed Sylow subgroup contains $Q$.
::: {.proof}
The fact that $P$ is fixed by the conjugation action of $Q$ means
$$
qPq^{-1}=P
$$
for every $q\in Q$. Hence $Q$ normalizes $P$, so the product
$$
PQ
$$
is a subgroup of $G$.

Both $P$ and $Q$ are $p$-groups. Therefore
$$
|PQ|=\frac{|P||Q|}{|P\cap Q|}
$$
is a power of $p$, so $PQ$ is a $p$-subgroup of $G$. But $P$ is Sylow and has
the largest possible $p$-power order, namely $p^r$. Since $P\le PQ$, maximality
forces
$$
PQ=P.
$$
Consequently
$$
\boxed{Q\le P.}
$$
Thus every subgroup of order $p^s$ with $s<r$ is contained in a Sylow
$p$-subgroup of $G$.
:::
:::
