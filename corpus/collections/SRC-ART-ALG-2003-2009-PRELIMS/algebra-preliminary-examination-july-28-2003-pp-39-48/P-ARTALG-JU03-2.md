---
schema: qual/card@1
id: P-ARTALG-JU03-2
kind: problem
title: 'A normal $D_8\times D_8$ in every Sylow $2$-subgroup of $S_8$'
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
  note: "Compared the order-eight dihedral convention and normality in every Sylow subgroup with July 2003 problem 2 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the explicit dihedral generators, disjoint-support direct product, block-swap conjugation, order 128, and transport to an arbitrary Sylow subgroup."
---

::: {.problem}
Let $D_8$ be the dihedral group with 8 elements.
Show that every Sylow 2-subgroup of $S_8$ contains a normal subgroup that is isomorphic to $D_8 \times D_8$.
:::

::: {.solution}
We first construct one Sylow subgroup with the required normal subgroup.
All permutations below act on $\{1,\ldots,8\}$ and fix unlisted points.

<1>1. The subgroup $H_1=\langle r,s\rangle$, where
$r=(1\,2\,3\,4)$ and $s=(2\,4)$, is isomorphic to $D_8$.

::: {.proof}
We have $r^4=s^2=1$ and
$$
srs=(1\,4\,3\,2)=r^{-1}.
$$
These relations put every word into the form $r^i s^e$ with
$0\leq i<4$ and $e\in\{0,1\}$. The four powers of $r$ are
distinct, and $s$ is none of them: the two nontrivial odd powers
are $4$-cycles and $r^2=(1\,3)(2\,4)$. Therefore the two cosets
$\langle r\rangle$ and $\langle r\rangle s$ are disjoint,
so the eight normal forms are distinct. The actions of $r$ and
$s$ on four cyclically ordered vertices are a quarter-turn and a
reflection of a square. They generate its dihedral group of order $8$.
:::

<1>2. There is a subgroup $H\cong D_8\times D_8$ of order $64$.

::: {.proof}
Let
$$
t=(1\,5)(2\,6)(3\,7)(4\,8),\qquad H_2=tH_1t^{-1}.
$$
Then $H_2=\langle(5\,6\,7\,8),(6\,8)\rangle\cong D_8$.
The groups $H_1,H_2$ have disjoint supports, so every element of
one commutes with every element of the other. Their intersection
is trivial: an element in both fixes each of the two four-point
blocks pointwise. Thus multiplication induces an injective
homomorphism
$$
H_1\times H_2\longrightarrow S_8,
\qquad (h_1,h_2)\longmapsto h_1h_2.
$$
Its image $H=H_1H_2$ has order $8\cdot8=64$ and the asserted
direct-product structure.
:::

<1>3. The group $P=\langle H,t\rangle$ is Sylow and $H\lhd P$.

::: {.proof}
The involution $t$ interchanges $H_1$ and $H_2$ under conjugation,
so it normalizes their product $H$. Also $t\notin H$, because
every element of $H$ preserves each four-point block, whereas
$t$ interchanges them. Consequently
$$
P=H\sqcup Ht,\qquad |P|=2|H|=128,
$$
and $H$ is normal in $P$: it is normalized by $H$ and by $t$,
which together generate $P$.

The exponent of $2$ in $8!$ is $4+2+1=7$, counting one factor
from every even integer, another from $4$ and $8$, and another
from $8$. Hence $128=2^7$ is the full power of $2$ dividing
$|S_8|=8!$, so $P$ is a Sylow $2$-subgroup.
:::

<1>4. Every Sylow $2$-subgroup has the asserted normal subgroup.

::: {.proof}
Let $P'$ be any Sylow $2$-subgroup of $S_8$. Sylow conjugacy
[@DF04] gives $g\in S_8$ with $P'=gPg^{-1}$.
Then $H'=gHg^{-1}$ is isomorphic to $H\cong D_8\times D_8$.
Conjugating the relation $H\lhd P$ gives $H'\lhd P'$, which
proves the statement for the arbitrary chosen $P'$.
:::
:::
