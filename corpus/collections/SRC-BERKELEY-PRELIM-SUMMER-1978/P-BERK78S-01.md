---
schema: qual/card@1
id: P-BERK78S-01
kind: problem
title: Examples and nonexamples for basic subgroup and quotient phenomena
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Supplied explicit examples for parts 1--7, using S_3, C_2×C_2, Z with
    5Z, C_4 versus C_2×C_2, a transposition subgroup of S_3, the simple
    group A_5, and Z/2Z as a quotient of Z. Proved A_5 simple from its
    conjugacy-class sizes and proved that every index-two subgroup is
    normal, so part 8 is impossible.
---

::: {.problem}
For each of the following, either give an example or prove that no such example is possible.

1. A nonabelian group.
2. A finite abelian group that is not cyclic.
3. An infinite group with a subgroup of index $5$.
4. Two finite groups of the same order that are not isomorphic.
5. A group $G$ with a subgroup $H$ that is not normal.
6. A nonabelian group with no normal subgroups except the whole group and the identity subgroup.
7. A group $G$ with a normal subgroup $H$ such that $G/H$ is not isomorphic to any subgroup of $G$.
8. A group $G$ with a subgroup $H$ of index $2$ that is not normal.
:::

::: {.solution}
<1>1. For part (1), the symmetric group
$$
\boxed{S_3}
$$
is nonabelian.

::: {.proof}
For example,
$$
(12)(23)=(123)
$$
while
$$
(23)(12)=(132).
$$
Thus multiplication in $S_3$ is not commutative.
:::

<1>2. For part (2), the group
$$
\boxed{C_2\times C_2}
$$
is finite abelian and not cyclic.

::: {.proof}
It is abelian because it is a direct product of abelian groups. It has four
elements, but every nonidentity element has order $2$. A cyclic group of
order $4$ would contain an element of order $4$, so $C_2\times C_2$ is not
cyclic.
:::

<1>3. For part (3), the additive group
$$
\boxed{\ZZ}
$$
has the subgroup
$$
\boxed{5\ZZ}
$$
of index $5$.

::: {.proof}
The five cosets are
$$
5\ZZ,\quad
1+5\ZZ,\quad
2+5\ZZ,\quad
3+5\ZZ,\quad
4+5\ZZ.
$$
Thus
$$
[\ZZ:5\ZZ]=5,
$$
and $\ZZ$ is infinite.
:::

<1>4. For part (4), the groups
$$
\boxed{C_4\quad\text{and}\quad C_2\times C_2}
$$
have the same finite order but are not isomorphic.

::: {.proof}
Both groups have order $4$. The first contains an element of order $4$,
whereas the second has no such element by step <1>2. Since isomorphisms
preserve element orders, the groups are not isomorphic.
:::

<1>5. For part (5), take
$$
\boxed{
G=S_3,
\qquad
H=\langle(12)\rangle.
}
$$
Then $H$ is not normal in $G$.

::: {.proof}
Conjugating the generator by $(123)$ gives
$$
(123)(12)(123)^{-1}=(23),
$$
which does not lie in
$$
H=\{e,(12)\}.
$$
Hence
$$
(123)H(123)^{-1}\neq H,
$$
so $H$ is not normal.
:::

<1>6. For part (6), the alternating group
$$
\boxed{A_5}
$$
is nonabelian and has no normal subgroups other than
$$
\{e\}
\quad\text{and}\quad
A_5.
$$

::: {.proof}
The group $A_5$ is nonabelian; for instance the $3$-cycles $(123)$ and
$(345)$ do not commute.

The nonidentity elements of $A_5$ have exactly the following cycle types:
$3$-cycles, products of two disjoint transpositions, and $5$-cycles.
Their conjugacy-class sizes in $A_5$ are respectively
$$
20,\qquad15,\qquad12,\qquad12.
$$
Indeed, a $3$-cycle has centralizer of order $3$ in $A_5$, so its class
has size $60/3=20$; a double transposition has centralizer of order $4$,
so its class has size $60/4=15$; and a $5$-cycle has centralizer of order
$5$, so its class has size $60/5=12$. Since there are $24$ five-cycles,
they form two classes of size $12$.

Any normal subgroup is a union of conjugacy classes containing the
identity, and its order must divide $60$. The possible orders obtained by
adding $1$ to a proper nonempty selection from
$$
20,\ 15,\ 12,\ 12
$$
are
$$
13,16,21,25,28,28,33,33,36,40,45,48,
$$
none of which divides $60$. Thus a normal subgroup has order either $1$ or
$60$. Therefore $A_5$ is simple.
:::

<1>7. For part (7), take
$$
\boxed{
G=\ZZ,
\qquad
H=2\ZZ.
}
$$
Then $H\trianglelefteq G$, but $G/H$ is not isomorphic to any subgroup of
$G$.

::: {.proof}
The group $\ZZ$ is abelian, so every subgroup is normal. Moreover,
$$
\ZZ/2\ZZ\cong C_2.
$$
Every nonzero subgroup of $\ZZ$ is of the form $m\ZZ$ and is infinite
cyclic; the zero subgroup is trivial. Thus $\ZZ$ has no subgroup
isomorphic to the finite nontrivial group $C_2$.
:::

<1>8. Part (8) is impossible: every subgroup of index $2$ is normal.

::: {.proof}
Let $H\leq G$ with $[G:H]=2$. If $g\in H$, then
$$
gH=H=Hg.
$$
If $g\notin H$, there are exactly two left cosets, so
$$
gH=G\sm H.
$$
There are also exactly two right cosets, hence
$$
Hg=G\sm H.
$$
Thus
$$
gH=Hg
$$
for every $g\in G$. Therefore $H\trianglelefteq G$, and no example of the
requested kind exists.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 give the requested examples, and step <1>8 proves the
nonexistence assertion for part (8).
:::
:::
