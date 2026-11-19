---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-03B
kind: problem
title: Projection from a product with a compact factor is closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood: the tube lemma is isolated as its own step, with the finite subcover of the V_y and
    the intersection U of the U_y; the fibre over a point outside the image is shown to lie in
    the complement of C; and the neighbourhood U is shown disjoint from pi(C) elementwise. Not
    claimed: a retained solution set; the workshop collection is a problem list with no
    solution sheet. Statement unchanged.
---

::: {.problem}
Suppose that $X$ is an arbitrary topological space and $Y$ is a compact space.
Consider the projection map $\pi:X\times Y\to X$ defined by $\pi(x,y)=x$.
Prove that if $X\times Y$ has the product topology, then $\pi$ is a closed map.
:::

::: {.solution}
The statement is the one printed on this card, from the Day 4 workshop list; no retained solution set covers it — the collection is a problem list with no solution sheet — so the argument below is the card's own, and it is the card's previous prose with the tube lemma stated and the verification of the union completed.

Throughout $X$ is an arbitrary topological space, $Y$ is compact, $\pi:X\times Y\to X$ is the projection, and $X\times Y$ carries the product topology.

::: pf

::: {.pf-step #tube}
(Tube lemma.) If $x_0\in X$ and $N\subseteq X\times Y$ is an open set containing $\theset{x_0}\times Y$, then there is an open neighbourhood $U$ of $x_0$ with $U\times Y\subseteq N$.

::: pf-proof
For each $y\in Y$ the point $(x_0,y)$ lies in $N$, which is open, so there are open sets $U_y\ni x_0$ and $V_y\ni y$ with $U_y\times V_y\subseteq N$ — basic open sets of the product topology. The family $\theset{V_y}_{y\in Y}$ is an open cover of the compact $Y$, so there are $y_1,\dots,y_n$ with $Y=V_{y_1}\cup\cdots\cup V_{y_n}$. Put $U=U_{y_1}\cap\cdots\cap U_{y_n}$, an open neighbourhood of $x_0$. For $x\in U$ and any $y\in Y$ there is $i$ with $y\in V_{y_i}$; since $x\in U\subseteq U_{y_i}$, $(x,y)\in U_{y_i}\times V_{y_i}\subseteq N$. Hence $U\times Y\subseteq N$.

:::

:::

::: {.pf-step #complement}
For $C\subseteq X\times Y$ closed and $x_0\notin\pi(C)$, the open set $N=(X\times Y)\setminus C$ contains $\theset{x_0}\times Y$.

::: pf-proof
If $y\in Y$ then $(x_0,y)\in C$ would give $x_0=\pi(x_0,y)\in\pi(C)$, contrary to hypothesis; so $(x_0,y)\notin C$, i.e. $(x_0,y)\in N$. Thus the whole fibre over $x_0$ lies in $N$.

:::

:::

::: {.pf-step #neighbourhood}
There is an open neighbourhood $U$ of $x_0$ with $U\subseteq X\setminus\pi(C)$.

::: pf-proof
By steps [](#complement){.pf-ref} and [](#tube){.pf-ref} there is an open $U\ni x_0$ with $U\times Y\subseteq(X\times Y)\setminus C$. If $x\in U$ and $x=\pi(x,y)$ for some $(x,y)\in C$, then $(x,y)\in U\times Y\subseteq(X\times Y)\setminus C$, contradicting $(x,y)\in C$. So $U\cap\pi(C)=\varnothing$, that is $U\subseteq X\setminus\pi(C)$.

:::

:::

::: {.pf-step #conclusion}
$\pi$ is a closed map.

::: pf-proof
Let $C\subseteq X\times Y$ be closed and $x_0\notin\pi(C)$. Step [](#neighbourhood){.pf-ref} produces an open neighbourhood of $x_0$ disjoint from $\pi(C)$, so $X\setminus\pi(C)$ is open, i.e. $\pi(C)$ is closed. $C$ was arbitrary, so $\pi$ takes closed sets to closed sets.

:::

:::

:::
:::
