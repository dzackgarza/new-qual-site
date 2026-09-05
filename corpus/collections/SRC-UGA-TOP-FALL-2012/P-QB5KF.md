---
schema: qual/card@1
id: P-QB5KF
kind: problem
title: Two non-isomorphic index-$2$ subgroups of $\ZZ_2*\ZZ$, via covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 5 of the official UGA Fall 2012 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Constructed the two connected double covers of RP^2 wedge S^1 coming from
    the two coordinate monodromies and computed their groups as F_2 and
    Z_2 * Z_2 * Z, which are distinguished by torsion.
---

::: problem
Use covering space theory to show that $\ZZ_2 \ast \ZZ$  (that is, the free product of $\ZZ_2$ and $\ZZ$)  has two subgroups of index 2 which are not isomorphic to each other.
:::

::: {.solution}
<1>1. Let
\[
X=\RP^2\vee S^1.
\]
Then
\[
\pi_1(X,*)\cong\ZZ_2*\ZZ
=\langle a,b\mid a^2=1\rangle,
\]
where $a$ comes from $\RP^2$ and $b$ comes from $S^1$.
::: {.proof}
The fundamental groups of the two wedge summands are
\[
\pi_1(\RP^2)\cong\ZZ_2,
\qquad
\pi_1(S^1)\cong\ZZ.
\]
The intersection in the wedge model is the single basepoint, so van Kampen gives their free product.
:::

<1>2. There is a connected two-sheeted cover
\[
p_1:Y_1\longrightarrow X
\]
whose monodromy sends $a$ to the nontrivial transposition of the two sheets and sends $b$ to the identity.
Its total space is a copy of $S^2$ with one circle attached at each of the two points lying over the wedge point.
::: {.proof}
Consider the surjective homomorphism
\[
\rho_1:\pi_1(X,*)\longrightarrow\ZZ_2,
\qquad
\rho_1(a)=1,
\qquad
\rho_1(b)=0.
\]
Interpreting $\ZZ_2$ as the permutation group of a two-point fiber gives a transitive monodromy action, hence a connected double cover.

Over the $\RP^2$ summand the monodromy is nontrivial, so the restricted cover is the universal double cover
\[
S^2\longrightarrow\RP^2.
\]
Over the $S^1$ summand the monodromy is trivial, so its inverse image consists of two separate copies of $S^1$, one attached at each point of the fiber over the wedge point.
This gives the stated description of $Y_1$.
:::

<1>3. One has
\[
\pi_1(Y_1)\cong F_2,
\]
the free group on two generators.
::: {.proof}
The sphere is simply connected, and the two attached circles meet it only at their respective attaching points.
Applying van Kampen, or joining the two attaching points by an arc in $S^2$ and using a maximal tree, gives one free generator for each attached circle and no relations.
Thus
\[
\pi_1(Y_1)\cong\ZZ*\ZZ=F_2.
\]
:::

<1>4. There is a second connected two-sheeted cover
\[
p_2:Y_2\longrightarrow X
\]
whose monodromy fixes the sheets along $a$ and interchanges them along $b$.
Its total space consists of a connected double cover of the $S^1$ summand, with one copy of $\RP^2$ attached at each of the two points over the wedge point.
::: {.proof}
Use the surjection
\[
\rho_2:\pi_1(X,*)\longrightarrow\ZZ_2,
\qquad
\rho_2(a)=0,
\qquad
\rho_2(b)=1.
\]
Again the monodromy action is transitive, so the associated double cover is connected.

Since $a$ acts trivially on the fiber, the inverse image of the $\RP^2$ summand is two disjoint copies of $\RP^2$.
Since $b$ interchanges the two sheets, the inverse image of the $S^1$ summand is its connected two-sheeted cover, itself a circle.
The two copies of $\RP^2$ attach at the two points of this covering circle lying over the wedge point.
:::

<1>5. The second covering space has
\[
\pi_1(Y_2)\cong\ZZ_2*\ZZ_2*\ZZ.
\]
::: {.proof}
Give the covering circle a CW structure with the two points over the wedge point as vertices and two edges between them.
At each vertex attach the standard CW structure on a copy of $\RP^2$, with a loop $a_i$ and a $2$-cell imposing $a_i^2=1$.

Choose one of the two edges of the covering circle as a maximal tree.
The other edge contributes one free generator $t$.
Van Kampen therefore gives
\[
\pi_1(Y_2)
\cong
\langle a_0,a_1,t\mid a_0^2=1,\ a_1^2=1\rangle
\cong
\ZZ_2*\ZZ_2*\ZZ.
\]
:::

<1>6. The images
\[
H_i=(p_i)_*\pi_1(Y_i)
\subseteq
\pi_1(X)\cong\ZZ_2*\ZZ
\qquad(i=1,2)
\]
are subgroups of index $2$.
::: {.proof}
For a connected covering space, the induced homomorphism on fundamental groups is injective, and the index of its image equals the number of sheets.
Both $p_1$ and $p_2$ are connected two-sheeted covers, so
\[
[\pi_1(X):H_i]=2.
\]
Moreover
\[
H_1\cong\pi_1(Y_1)\cong F_2,
\qquad
H_2\cong\pi_1(Y_2)\cong\ZZ_2*\ZZ_2*\ZZ.
\]
:::

<1>7. The two index-$2$ subgroups $H_1$ and $H_2$ are not isomorphic.
::: {.proof}
The group $H_2$ contains nontrivial elements of order $2$, namely the two displayed $\ZZ_2$ factor generators.

The free group $F_2$ is torsion-free.
Indeed, every nontrivial free-group element is conjugate to a nonempty cyclically reduced word, and every positive power of such a word remains a nonempty reduced word.
Hence no nontrivial element can have finite order.

Therefore $H_1\not\cong H_2$.
:::
:::
