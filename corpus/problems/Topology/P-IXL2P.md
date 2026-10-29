---
schema: qual/card@1
id: P-IXL2P
kind: problem
title: Cayley graph of $\ZZ \times \ZZ$ as a covering space
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source text was only an answer: 'This is just the Cayley graph over Z x Z, or essentially the integer lattice', with a sketch of the lattice with edges labelled x and y. The question was not retained. The statement is reconstructed as the covering of the figure eight whose total space is that graph, namely the cover for the commutator subgroup; the original question is unconfirmed."
---

::: {.problem}
Let $X=S^1\vee S^1$, with $\pi_1(X)$ the free group on the loops $x$ and $y$. Describe the connected covering space of $X$ corresponding to the commutator subgroup $[\pi_1(X),\pi_1(X)]$.
:::

::: {.solution}

Let $\widetilde X\subset\RR^2$ be the integer lattice graph: its vertices are $\ZZ^2$, and its edges are the horizontal segments $[(m,n),(m+1,n)]$, labelled $x$, and the vertical segments $[(m,n),(m,n+1)]$, labelled $y$. This is the Cayley graph of $\ZZ\times\ZZ$ with respect to the generators $(1,0)$ and $(0,1)$.

![](../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1512966445331.png)

::: pf

::: pf-step

The map $p:\widetilde X\to X$ that sends every vertex to the wedge point and wraps each $x$-edge (resp. $y$-edge) once around the $x$-circle (resp. $y$-circle), in the positive direction, is a covering map.

::: pf-proof

Every vertex of $\widetilde X$ has exactly one incoming and one outgoing edge of each label, matching the four edge germs at the wedge point of $X$. Hence $p$ maps a small star of each vertex homeomorphically onto a small star of the wedge point, and the interior of each edge homeomorphically onto the interior of a circle. These neighbourhoods are evenly covered.

:::

:::

::: {.pf-step #image}

With basepoint $(0,0)$, the subgroup $p_*\pi_1(\widetilde X)$ is the set of words in $x,y$ whose exponent sums in $x$ and in $y$ are both $0$.

::: pf-proof

A word $w$ in $x,y$ lifts to the path from $(0,0)$ that moves one unit right or left for each $x^{\pm1}$ and one unit up or down for each $y^{\pm1}$. The lift ends at the point whose coordinates are the exponent sums of $x$ and of $y$ in $w$. The loop $w$ lies in $p_*\pi_1(\widetilde X)$ exactly when its lift is closed, that is, when both exponent sums are $0$.

:::

:::

::: pf-step

The covering $p:\widetilde X\to X$ corresponds to the commutator subgroup, so the requested cover is $\boxed{\text{the Cayley graph of }\ZZ\times\ZZ}$, the integer lattice graph above.

::: pf-proof

The exponent-sum map $\pi_1(X)\to\ZZ\times\ZZ$ is the abelianization of the free group on $x,y$, so its kernel is the commutator subgroup. By step [](#image){.pf-ref} this kernel is $p_*\pi_1(\widetilde X)$, and connected covers are classified by these subgroups up to conjugacy.

:::

:::

:::

:::
