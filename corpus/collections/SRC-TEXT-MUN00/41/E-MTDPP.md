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
For each $x\in X$, local finiteness of $\{B_\alpha\}$ gives an open neighborhood $N_x$ meeting only finitely many $B_\alpha$'s. The family $\{N_x:x\in X\}$ is an open cover of the paracompact space $X$, so choose a locally finite open refinement $\mathcal V$ covering $X$, with each $V\in\mathcal V$ contained in some $N_x$. In particular, each $V\in\mathcal V$ meets only finitely many $B_\alpha$'s.

For each $\alpha$, define
$$
U_\alpha=\bigcup\{V\in\mathcal V:V\cap B_\alpha\ne\varnothing\}.
$$
Then $U_\alpha$ is open. It contains $B_\alpha$: if $b\in B_\alpha$, some $V\in\mathcal V$ contains $b$, and that $V$ occurs in the displayed union.

It remains to prove local finiteness of $\{U_\alpha\}$. Fix $x\in X$. Since $\mathcal V$ is locally finite, choose an open neighborhood $W$ of $x$ meeting only $V_1,\ldots,V_k\in\mathcal V$. If $W\cap U_\alpha\ne\varnothing$, then some $V_i$ meeting $W$ also meets $B_\alpha$. Each $V_i$ meets only finitely many $B_\alpha$'s, so only finitely many indices $\alpha$ can occur. Thus $W$ meets only finitely many $U_\alpha$'s.

Hence $\{U_\alpha\}_{\alpha\in J}$ is a locally finite indexed family of open sets with $B_\alpha\subset U_\alpha$ for every $\alpha$.
:::
