---
schema: qual/card@1
id: P-WESTOP09-II2
kind: problem
title: Fundamental groups of products, wedges, and a simplex skeleton
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Compute the fundamental group of each space:

1. $M\times\RP^{\infty}$, where $M$ is the Möbius band;
2. $\Sigma_2\times\CP^2$, where $\Sigma_2$ is the closed orientable surface of genus $2$;
3. $L(p,q)\vee K$, where $K$ is the Klein bottle;
4. the $1$-skeleton of the standard $3$-simplex $\Delta^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For the Möbius-band product,
\[
\boxed{\pi_1(M\times\RP^{\infty})
\cong \ZZ\times\ZZ/2}.
\]


::: pf-proof

The Möbius band deformation retracts onto its core circle, so
\[
\pi_1(M)\cong\pi_1(S^1)\cong\ZZ.
\]
The universal cover
\[
S^\infty\longrightarrow\RP^{\infty}
\]
has deck group $\ZZ/2$, and $S^\infty$ is contractible, so
\[
\pi_1(\RP^{\infty})\cong\ZZ/2.
\]
The fundamental group of a product of path-connected spaces is the direct
product of their fundamental groups. Therefore
\[
\pi_1(M\times\RP^{\infty})
\cong\ZZ\times\ZZ/2.
\]

:::

:::

::: pf-step

For the product with $\CP^2$,
\[
\boxed{
\pi_1(\Sigma_2\times\CP^2)
\cong
\left\langle
a_1,b_1,a_2,b_2
\ \middle|\
[a_1,b_1][a_2,b_2]=1
\right\rangle }.
\]


::: pf-proof

The standard CW decomposition of $\CP^2$ has one cell in dimensions
$0$, $2$, and $4$. Its $2$-skeleton is $S^2$, and attaching a $4$-cell does
not change the fundamental group. Hence
\[
\pi_1(\CP^2)=\{1\}.
\]
The product theorem gives
\[
\pi_1(\Sigma_2\times\CP^2)
\cong
\pi_1(\Sigma_2)\times \{1\}
\cong
\pi_1(\Sigma_2).
\]
The usual polygonal presentation of the closed orientable genus-$2$ surface
gives
\[
\pi_1(\Sigma_2)
\cong
\left\langle
a_1,b_1,a_2,b_2
\ \middle|\
[a_1,b_1][a_2,b_2]=1
\right\rangle.
\]

:::

:::

::: pf-step

For the wedge of the lens space and Klein bottle,
\[
\boxed{
\pi_1(L(p,q)\vee K)
\cong
\ZZ/p *
\left\langle a,b\mid aba^{-1}=b^{-1}\right\rangle }.
\]


::: pf-proof

The universal cover of the lens space $L(p,q)$ is $S^3$, with cyclic deck
group of order $p$, so
\[
\pi_1(L(p,q))\cong\ZZ/p.
\]
The Klein bottle has the standard presentation
\[
\pi_1(K)\cong
\left\langle a,b\mid aba^{-1}=b^{-1}\right\rangle.
\]
The wedge point has a contractible neighborhood in each CW complex, so the
Seifert--van Kampen theorem gives the free product
\[
\pi_1(L(p,q)\vee K)
\cong
\pi_1(L(p,q))*\pi_1(K),
\]
which is the displayed group.

:::

:::

::: {.pf-step #s1-4}

If $G$ is the $1$-skeleton of $\Delta^3$, then
\[
\boxed{\pi_1(G)\cong F_3},
\]
the free group on three generators.


::: pf-proof

The graph $G$ is the complete graph on the four vertices of the tetrahedron.
Thus it has
\[
V=4,\qquad E=6.
\]
Choose a spanning tree. It contains $V-1=3$ edges. Collapsing the tree to a
point is a homotopy equivalence of the graph and leaves
\[
E-(V-1)=6-3=3
\]
independent loop edges. Hence $G$ is homotopy equivalent to a wedge of three
circles, whose fundamental group is $F_3$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} compute the four requested fundamental groups.

:::

:::

:::
