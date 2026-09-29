---
schema: qual/card@1
id: P-TOPS05D
kind: problem
title: "All covering spaces of S^1 x RP^3"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Determine all covering spaces of $S^1 \times \mathbb{RP}^3$.
(This includes determining the covering projections.)
:::

::: {.solution}

::: pf

::: pf-step

We have
$$
\pi_1(S^1\times\mathbb{RP}^3)\cong \mathbb Z\times\mathbb Z/2
=\langle a,b\mid [a,b]=1,\ b^2=1\rangle.
$$

::: pf-proof

Use the product formula for fundamental groups, $\pi_1(S^1)=\mathbb Z$, and $\pi_1(\mathbb{RP}^3)=\mathbb Z/2$.

:::

:::

::: pf-step

Connected covering spaces are classified by subgroups $H\le G:=\mathbb Z\times\mathbb Z/2$; conjugacy is irrelevant because $G$ is abelian.

::: pf-proof

This is the classification theorem for connected coverings of a connected, locally path-connected, semilocally simply connected space.

:::

:::

::: {.pf-step #s3}

Every subgroup $H\le G$ is one of the following:
$$
0,\quad \langle b\rangle,\quad
\langle a^d\rangle,\quad
\langle a^db\rangle,\quad
\langle a^d,b\rangle\qquad(d\ge1).
$$

::: pf-proof

Project $H$ to the $\mathbb Z$ factor. Its image is either $0$ or $d\mathbb Z$. If it is $0$, then $H\le\langle b\rangle$, giving the first two cases. If the image is $d\mathbb Z$, choose an element $a^db^\epsilon\in H$. The kernel of the projection $H\to d\mathbb Z$ is either $0$ or $\langle b\rangle$. In the first case $H=\langle a^db^\epsilon\rangle$, giving $\langle a^d\rangle$ or $\langle a^db\rangle$; in the second, $H=\langle a^d,b\rangle$.

:::

:::

::: pf-step

Using the universal cover $\mathbb R\times S^3$ with deck actions
$$
a(t,u)=(t+1,u),\qquad b(t,u)=(t,-u),
$$
the connected cover corresponding to $H$ is
$$
(\mathbb R\times S^3)/H\longrightarrow
(\mathbb R\times S^3)/G=S^1\times\mathbb{RP}^3.
$$

::: pf-proof

This is the standard subgroup construction for coverings from the universal cover.

:::

:::

::: {.pf-step #s5}

Concretely:
- $H=0$ gives the universal cover $\mathbb R\times S^3$;
- $H=\langle b\rangle$ gives $\mathbb R\times\mathbb{RP}^3$;
- $H=\langle a^d\rangle$ gives $S^1\times S^3$ with projection $(z,u)\mapsto(z^d,[u])$;
- $H=\langle a^d,b\rangle$ gives $S^1\times\mathbb{RP}^3$ with projection $(z,[u])\mapsto(z^d,[u])$;
- $H=\langle a^db\rangle$ gives $(\mathbb R\times S^3)/((t,u)\sim(t+d,-u))$ with the quotient projection induced by $(t,u)\mapsto(e^{2\pi it},[u])$.

::: pf-proof

Each description is obtained by quotienting the universal cover by the indicated subgroup from step [](#s3){.pf-ref}. The formulas are invariant under that subgroup and have the required deck subgroup.

:::

:::

::: pf-step

Every (not necessarily connected) covering is a disjoint union of connected coverings from step [](#s5){.pf-ref}.

::: pf-proof

Each connected component of a covering is itself a connected covering of the connected base, and the whole covering is their disjoint union.

:::

:::

:::

:::
