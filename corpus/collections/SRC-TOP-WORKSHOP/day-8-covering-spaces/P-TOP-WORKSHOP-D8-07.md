---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-07
kind: problem
title: Covering maps are open maps
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
    stood. Added: the construction of the sheet V_e containing e from the even covering; the
    chain that gives p(O cap V_e) open, including that an open subset of the evenly covered
    neighbourhood U_e is open in B; and the two inclusions proving p(O) is the union of the
    pieces. Not claimed: a retained solution set; the workshop collection is a problem list with
    no solution sheet.
---

::: {.problem}
(Purdue Jan ’07) Let $p:E\to B$ be a covering map.
Prove that $p$ takes open sets to open sets.
:::

::: {.solution}
The statement is the one printed on this card, from the Day 8 (covering spaces) workshop; no retained solution set covers it — the collection is a workshop problem list with no solution sheet — so the argument below is the card's own, and it is the card's previous prose with the two identifications it left implicit made explicit.

Throughout $p:E\to B$ is a covering map, $O\subseteq E$ is open, and for $e\in E$ a sheet over an evenly covered neighbourhood $U$ of $p(e)$ means a connected component $V$ of $p^{-1}(U)$ containing $e$, on which $p$ restricts to a homeomorphism onto $U$.

::: pf

::: {.pf-step #sheets}
For each $e\in O$ there is an evenly covered neighbourhood $U_e$ of $p(e)$ and a sheet $V_e$ containing $e$ with $e\in V_e$ and $p\restriction_{V_e}:V_e\to U_e$ a homeomorphism.

::: pf-proof
$p(e)$ has an evenly covered neighbourhood $U_e$, i.e. $p^{-1}(U_e)$ is a disjoint union of open sets each mapped homeomorphically onto $U_e$; the point $e$ lies in exactly one of them, which is $V_e$.

:::

:::

::: {.pf-step #piece}
$p(O\cap V_e)$ is open in $B$.

::: pf-proof
$V_e$ is open and $O$ is open, so $O\cap V_e$ is open in $E$, hence open in the subspace $V_e$. The restriction $p\restriction_{V_e}$ is a homeomorphism onto $U_e$, so it is an open map, and $p(O\cap V_e)=(p\restriction_{V_e})(O\cap V_e)$ is open in $U_e$. Since $U_e$ is open in $B$, an open subset of $U_e$ is open in $B$.

:::

:::

::: {.pf-step #union}
$p(O)=\bigcup_{e\in O}p(O\cap V_e)$.

::: pf-proof
One inclusion: $O\cap V_e\subseteq O$ gives $p(O\cap V_e)\subseteq p(O)$ for every $e$, hence the union is contained in $p(O)$. Other inclusion: if $y=p(x)$ with $x\in O$, then $x\in O\cap V_x$, so $y\in p(O\cap V_x)$ and $y$ lies in the union.
:::

:::

::: {.pf-step #conclusion}
$p(O)$ is open, so $p$ is an open map.

::: pf-proof
$p(O)$ is a union of the sets $p(O\cap V_e)$, each open in $B$ by step [](#piece){.pf-ref}, by step [](#union){.pf-ref}; an arbitrary union of open sets is open. $O$ was an arbitrary open subset of $E$.
:::

:::

:::
:::
