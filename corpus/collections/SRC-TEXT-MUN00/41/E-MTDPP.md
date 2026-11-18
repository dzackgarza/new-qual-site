---
schema: qual/card@1
id: E-MTDPP
kind: problem
title: The expansion lemma for locally finite families
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 41 Exercise 5, printed p. 260, with the definition of paracompactness, the definition of local finiteness and the passage from a cover to a locally finite open refinement. No correction was needed; the card's proof takes the locally finite open refinement $\mathcal V$ of the cover by the neighbourhoods $N_x$ and sets $U_\alpha$ to be the union of the members of $\mathcal V$ that meet $B_\alpha$.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; the mathematics is the card's own and was re-read
    against the book. Pages added where the prose had none: the definition of local
    finiteness (printed p. 244), the definition of paracompactness (printed p. 254) and the
    exercise (printed p. 260). Each step checked: the neighbourhood N_x meeting finitely
    many B_alpha is taken open because a neighbourhood contains an open set; paracompactness
    gives an open locally finite refinement of the cover by the N_x, and a member of the
    refinement meets only the sets its N_x meets; U_alpha is open as a union of members of
    the open family, and contains B_alpha because the member of the refinement through a
    point of B_alpha meets B_alpha; local finiteness at x uses the neighbourhood W meeting
    only V_1,...,V_k and the fact that a set meeting W and U_alpha must be one of the V_i,
    since it contains a point of W and lies in the refinement. A hypothesis noted and not
    used: the lemma's Hausdorff assumption plays no part in this argument, and the card now
    says so. No repair to the statement.
---

::: {.exercise}

Let $X$ be paracompact.
We proved a "shrinking lemma" for arbitrary indexed open coverings of $X$.
Here is an "expansion lemma" for arbitrary locally finite indexed families in $X$.

Lemma.
Let $\theset{B_\alpha}_{\alpha \in J}$ be a locally finite indexed family of subsets of the paracompact Hausdorff space $X$.
Then there is a locally finite indexed family $\theset{U_\alpha}_{\alpha \in J}$ of open sets in $X$ such that $B_\alpha \subset U_\alpha$ for each $\alpha$.
:::

::: {.solution}
The argument is the card's own: no retained set solves this exercise, as the audit and the COMPLAINTS.md entry for §39--§42 record.

Throughout, $X$ is paracompact and Hausdorff, $\{B_\alpha\}_{\alpha\in J}$ is a locally finite indexed family of subsets of $X$, and $\mathcal{V}$ will be a locally finite open refinement of a given open cover. A family of subsets is locally finite when each point has a neighbourhood meeting only finitely many of its members (§39, printed p. 244), and $X$ is paracompact when every open cover has an open locally finite refinement that covers $X$ (§41, printed p. 254); the exercise is §41 Exercise 5 (printed p. 260). The Hausdorff hypothesis is not used below.

::: pf

::: {.pf-step #local}
For each $x\in X$ there is an open neighbourhood $N_x$ of $x$ meeting only finitely many of the sets $B_\alpha$.

::: pf-proof
Local finiteness of $\{B_\alpha\}$ at $x$ says that some neighbourhood $M$ of $x$ meets only finitely many of the sets $B_\alpha$, and $M$ contains an open set $N_x$ containing $x$, which then meets no more of them.
:::

:::

::: {.pf-step #refinement}
There is a locally finite open cover $\mathcal{V}$ of $X$ such that each $V\in\mathcal{V}$ is contained in some $N_x$, and then each $V\in\mathcal{V}$ meets only finitely many of the sets $B_\alpha$.

::: pf-proof
The family $\{N_x\}_{x\in X}$ of step [](#local){.pf-ref} is an open cover of $X$, so paracompactness gives an open locally finite refinement $\mathcal{V}$ that covers $X$ and each of whose members is contained in some member $N_x$ of the cover. A subset of $N_x$ meets only sets that $N_x$ meets, so each $V$ meets only finitely many of the $B_\alpha$.
:::

:::

::: {.pf-step #U}
The sets $U_\alpha=\bigcup\{V\in\mathcal{V} \mid V\cap B_\alpha\ne\emptyset\}$ are open and satisfy $B_\alpha\subset U_\alpha$.

::: pf-proof
A union of members of $\mathcal{V}$ is open because $\mathcal{V}$ is an open family. If $b\in B_\alpha$, then $b$ lies in some $V\in\mathcal{V}$ because $\mathcal{V}$ covers $X$, and that $V$ meets $B_\alpha$ in $b$, so it occurs in the union defining $U_\alpha$ and $b\in U_\alpha$.
:::

:::

::: {.pf-step #lfinite}
The family $\{U_\alpha\}_{\alpha\in J}$ is locally finite.

::: pf-proof
Let $x\in X$. Since $\mathcal{V}$ is locally finite, there is an open neighbourhood $W$ of $x$ meeting only finitely many members of $\mathcal{V}$; call them $V_1,\ldots,V_k$. Suppose $W\cap U_\alpha\ne\emptyset$ and pick $y$ in that intersection. By the definition of $U_\alpha$ there is $V\in\mathcal{V}$ with $y\in V$ and $V\cap B_\alpha\ne\emptyset$; since $y\in W$, the set $V$ meets $W$, so $V=V_i$ for some $i\le k$. Hence $\alpha$ is an index with $B_\alpha\cap V_i\ne\emptyset$ for some $i\le k$, and each $V_i$ meets only finitely many of the sets $B_\alpha$ by step [](#refinement){.pf-ref}; a finite union of finite sets being finite, only finitely many $\alpha$ occur. So the neighbourhood $W$ of $x$ meets only finitely many of the sets $U_\alpha$.
:::

:::

::: {.pf-step}
$\{U_\alpha\}_{\alpha\in J}$ is a locally finite indexed family of open sets with $B_\alpha\subset U_\alpha$ for every $\alpha$.

::: pf-proof
Openness and the containments are step [](#U){.pf-ref}, and local finiteness is step [](#lfinite){.pf-ref}.
:::

:::

:::
:::
