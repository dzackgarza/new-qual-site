---
schema: qual/card@1
id: P-WESTOP09-II3
kind: problem
title: Covering spaces of $S^1\vee S^1$, including regularity and universal covers
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $X=S^1\vee S^1$.

1. Classify all connected $2$-sheeted covering spaces of $X$ up to covering equivalence. For each, calculate the associated subgroup of $\pi_1(X)$ and its deck group.
2. Construct a covering space of $X$ that is not regular.
3. Describe the universal cover of $X$.
4. Describe the universal abelian cover of $X$, corresponding to the commutator subgroup of $\pi_1(X)$.
:::

::: {.solution}

Fix the wedge point as basepoint and write
\[
\pi_1(X)=F(a,b),
\]
where $a$ and $b$ are the two circle generators.

::: pf

::: {.pf-step #s1-1}

Up to covering equivalence, there are exactly three connected
$2$-sheeted covers of $X$.


::: pf-proof

Connected $2$-sheeted covers correspond to transitive actions of $F(a,b)$ on
a two-element fiber, equivalently to homomorphisms
\[
\rho:F(a,b)\to S_2\cong\ZZ/2
\]
with nontrivial image. A homomorphism from the free group is determined by
the images of $a$ and $b$. There are exactly three nonzero choices:
\[
(\rho(a),\rho(b))=(1,0),\qquad(0,1),\qquad(1,1)
\]
in $\ZZ/2\times\ZZ/2$.

Geometrically, in the first cover the $a$-loop interchanges the two sheets
and the $b$-loop fixes them; in the second the roles are reversed; in the
third both loops interchange the sheets. These monodromies are distinct over
the labeled base $X$, so the three covers are inequivalent.

:::

:::

::: pf-step

For the cover with
\[
\rho(a)=1,\qquad \rho(b)=0,
\]
the associated subgroup and deck group are
\[
\boxed{
H_a=\ker\rho
=\langle a^2,b,aba^{-1}\rangle,
\qquad
\operatorname{Deck}\cong\ZZ/2 }.
\]


::: pf-proof

The kernel consists exactly of words whose total exponent sum in $a$ is even.
Using Schreier representatives $\{1,a\}$ for the two cosets gives the
generators
\[
b,\qquad a^2,\qquad aba^{-1}.
\]
Because $H_a$ has index $2$, it is normal. Hence the deck group is
\[
F(a,b)/H_a\cong\ZZ/2.
\]

:::

:::

::: pf-step

For the cover with
\[
\rho(a)=0,\qquad \rho(b)=1,
\]
the associated subgroup and deck group are
\[
\boxed{
H_b=\ker\rho
=\langle a,b^2,bab^{-1}\rangle,
\qquad
\operatorname{Deck}\cong\ZZ/2 }.
\]


::: pf-proof

Here the kernel consists of words whose total exponent sum in $b$ is even.
Schreier representatives $\{1,b\}$ give the displayed generators. Again the
subgroup has index $2$, hence is normal, and the quotient is $\ZZ/2$.

:::

:::

::: {.pf-step #s1-4}

For the cover with
\[
\rho(a)=1,\qquad \rho(b)=1,
\]
the associated subgroup and deck group are
\[
\boxed{
H_{a+b}=\ker\rho
=\langle a^2,ab,ba^{-1}\rangle,
\qquad
\operatorname{Deck}\cong\ZZ/2 }.
\]


::: pf-proof

The kernel consists of words for which the sum of the exponent sums of $a$
and $b$ is even. Using the Schreier representatives $\{1,a\}$ gives
\[
a^2,\qquad ab,\qquad ba^{-1}
\]
as generators. This is again an index-$2$ normal subgroup, so its deck group
is $\ZZ/2$.

:::

:::

::: {.pf-step #s1-5}

There exists a connected covering of $X$ that is not regular.


::: pf-proof

Define a monodromy homomorphism
\[
\rho:F(a,b)\to S_3
\]
by
\[
\rho(a)=(12),
\qquad
\rho(b)=(123).
\]
These two permutations generate $S_3$, so the action on
$\{1,2,3\}$ is transitive and determines a connected $3$-sheeted covering.
The subgroup corresponding to the sheet labeled $1$ is
\[
H=\rho^{-1}(\operatorname{Stab}_{S_3}(1)).
\]
The stabilizer of $1$ is not normal in $S_3$. Since $\rho$ is surjective,
$H$ is not normal in $F(a,b)$. A connected covering is regular exactly when
its associated subgroup is normal, so this covering is not regular.

:::

:::

::: {.pf-step #s1-6}

The universal cover of $X$ is the $4$-regular tree.


::: pf-proof

Take the Cayley graph of the free group $F(a,b)$ with respect to
$a^{\pm1},b^{\pm1}$. Its vertices are the elements $g\in F(a,b)$, with an
$a$-edge from $g$ to $ga$ and a $b$-edge from $g$ to $gb$. Map every vertex
to the wedge point of $X$, every $a$-edge to the first circle, and every
$b$-edge to the second circle.

This graph is a covering of $X$. A reduced nonempty word in a free group is
not the identity, so the Cayley graph contains no nontrivial reduced cycles;
hence it is a tree. It is therefore simply connected and is the universal
cover. Each vertex has one incident edge in each of the four directions
$a,a^{-1},b,b^{-1}$, so the tree is $4$-regular.

:::

:::

::: {.pf-step #s1-7}

The universal abelian cover is the square grid with vertex set
$\ZZ^2$.


::: pf-proof

The abelianization map is
\[
F(a,b)\longrightarrow F(a,b)^{\mathrm{ab}}\cong\ZZ^2,
\qquad
a\longmapsto(1,0),
\qquad
b\longmapsto(0,1),
\]
and its kernel is the commutator subgroup $[F(a,b),F(a,b)]$.

The covering graph associated to this kernel is the Cayley graph of
$\ZZ^2$ with these two generators: its vertices are
\[
(m,n)\in\ZZ^2,
\]
with a horizontal $a$-edge from $(m,n)$ to $(m+1,n)$ and a vertical $b$-edge
from $(m,n)$ to $(m,n+1)$. Thus it is the infinite square grid, with all
vertices mapping to the wedge point and the two edge directions mapping to
the two circles. Its deck group is
\[
\ZZ^2.
\]

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} classify the connected two-sheeted covers and compute
their subgroups and deck groups; step [](#s1-5){.pf-ref} gives a nonregular cover; steps
[](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} describe the universal and universal-abelian covers.

:::

:::

:::
