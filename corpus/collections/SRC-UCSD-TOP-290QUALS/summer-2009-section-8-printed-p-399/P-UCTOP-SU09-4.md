---
schema: qual/card@1
id: P-UCTOP-SU09-4
kind: problem
title: Coverings of bouquets of circles
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

Let $X_n$ be the bouquet of $n$ circles, whose fundamental group (based at the vertex of the bouquet) is the free group $F_n$ on $n$ generators.

(a) Construct a basepointed covering of $X_3$ corresponding to the subgroup $\langle b^3, a^2, b^2ab^{-1} \rangle$ of the free group $\langle a, b, c \rangle$.

(b) Find the subgroup of $F_2$ corresponding to the basepointed cover of $X_2$ depicted in the source.

::: {.solution}
<1>1. For part (a), let $H=\langle b^3,a^2,b^2ab^{-1}\rangle\le F(a,b,c)$. The Stallings core of the corresponding based cover has four vertices $v_0,v_1,v_2,v_3$, based at $v_0$, and directed edges
$$
v_0\xrightarrow{a}v_1\xrightarrow{a}v_0,
\qquad
v_0\xrightarrow{b}v_2\xrightarrow{b}v_3\xrightarrow{b}v_0,
\qquad
v_3\xrightarrow{a}v_2.
$$
::: {.proof}
Start with based loops spelling the three generators $b^3$, $a^2$, and $b^2ab^{-1}$ and fold equally labelled oriented edges with common initial or terminal vertex. The $a^2$ loop gives the $a$-bigon $v_0\leftrightarrows v_1$; the $b^3$ loop gives the directed $b$-triangle $v_0\to v_2\to v_3\to v_0$; and the last word follows
$$
v_0\xrightarrow b v_2\xrightarrow b v_3\xrightarrow a v_2\xrightarrow{b^{-1}}v_0,
$$
so it contributes exactly the edge $v_3\xrightarrow a v_2$. No further fold is possible. Since this finite folded graph has rank $6-4+1=3$, and the three displayed generators are represented by its three independent based loops, its based fundamental group is exactly $H$.
:::

<1>2. Complete this core to a covering of $X_3$ by attaching trees along every missing $a$-, $b$-, and $c$-direction, so that at every vertex there is exactly one incoming and one outgoing edge of each label $a,b,c$.
::: {.proof}
A labelled graph maps to the rose $X_3$ as a covering exactly when the star of every vertex contains one incoming and one outgoing edge for each label. The finite core in <1>1 is folded but not complete. Attach fresh tree edges recursively at each missing labelled direction; because only trees are added, no new based cycles are introduced. The resulting connected labelled graph therefore covers $X_3$ and has based fundamental group equal to the core group $H$.
:::

<1>3. For part (b), the depicted cover has four vertices arranged cyclically. The $a$-edges form the clockwise directed $4$-cycle, while the $b$-edges form the counterclockwise directed $4$-cycle.
::: {.proof}
This is read directly from the arrows in the retained source figure: on the outer square all four $a$-arrows run clockwise, and on the four inner parallel arcs all $b$-arrows run counterclockwise.
:::

<1>4. Number the vertices by $\mathbb Z/4$, with the base vertex $0$, in clockwise order. Then traversing $a$ adds $1$ and traversing $b$ subtracts $1$ modulo $4$.
::: {.proof}
This is exactly the monodromy described in <1>3.
:::

<1>5. Hence the subgroup represented by the depicted based cover is
$$
K=\ker\!\left(F(a,b)\longrightarrow\mathbb Z/4\right),
\qquad a\longmapsto1,\quad b\longmapsto-1.
$$
::: {.proof}
A based word lifts to a closed loop precisely when its monodromy returns the base vertex to itself, i.e. when the total exponent sum of $a$ minus the total exponent sum of $b$ is $0$ modulo $4$.
:::

<1>6. Equivalently, one free basis for $K$ is
$$
a^4,\quad ba^{-3},\quad ab,\quad a^2ba^{-1},\quad a^3ba^{-2}.
$$
::: {.proof}
Use the Schreier transversal $\{1,a,a^2,a^3\}$ for the index-$4$ kernel in <1>5$. The Reidemeister--Schreier generators from the letter $a$ are trivial except for $a^4$, while those from $b$ are respectively
$$
ba^{-3},\quad ab,\quad a^2ba^{-1},\quad a^3ba^{-2}.
$$
Thus $K$ is free of rank $1+4(2-1)=5$ with the displayed basis.
:::
:::
