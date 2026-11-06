---
schema: qual/card@1
id: P-PRACT20-W6-15
kind: problem
title: Topology of the points of the unit square with an irrational coordinate
classification:
  areas:
  - prelim
  topics:
  - Connectedness
  - Path-Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the five assertions were checked: S is the complement of a countable dense set, which settles openness, closedness and compactness, and the path-connectedness was proved by avoiding countably many measure-zero bad choices
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The countable dense complement settling (A), (B), (E), a three-segment path construction through a point chosen outside countably many null sets for (C), and the existence of two points for the denial of (D)
---

::: {.problem}
Let $S \subset [0, 1] \times [0, 1]$ consist of all points $(x, y) \in [0, 1] \times [0, 1]$ such that $x$ or $y$ or both is irrational.
Which of the following is true (with respect to the standard topology on $\RR^{2}$)?

(A) $S$ is open

(B) $S$ is closed

(C) $S$ is connected

(D) $S$ is totally disconnected

(E) $S$ is compact
:::

::: {.solution}

Let $S=\{(x,y)\in[0,1]^2:\ x\notin\QQ\ \text{or}\ y\notin\QQ\}$, the
complement of $C=(\QQ\cap[0,1])^2$ in the square, with the usual topology.

::: pf

::: {.pf-step #notopen}

(A), (B) and (E) fail.

::: pf-proof

$C$ is countable, being a product of countable sets, hence $C=\bigcup_{c\in
C}\{c\}$ is a countable union of singleton closed sets and is an $F_\sigma$;
its closure is the whole square, since $C$ is dense. So $S$ is the complement
of a dense countable set: $S$ is not open, because no ball around a point of
$S$ misses $C$; $S$ is not closed, since its closure is the square and
$C\ne\emptyset$; and $S$ is not compact, because a compact subset of the
Hausdorff space $[0,1]^2$ is closed and $S$ is not.

:::

:::

::: {.pf-step #pathconnected}

(C) holds: $S$ is path-connected, hence connected.

::: pf-proof

Let $p,q\in S$ and let $R$ be the set of $r=(u,v)\in[0,1]^2$ such that the
three-segment path $p\to(u,p_2)\to(u,v)\to q$ meets $C$; the vertices
$(u,p_2),(u,v),(u,q_2)$ themselves are required to lie in $S$ as well. For a
fixed $c\in C$, the condition that $c$ lie on the path or be one of the
vertices forces $u=c_1$ or $v=c_2$ or $u=p_1$ or $u=q_1$ or $v=p_2$ or
$v=q_2$, a finite union of vertical and horizontal line segments, of planar
measure zero. Since $C$ is countable, the union over $c$ of these bad sets is
a countable union of null sets, hence null, and does not fill the square; so
some $r$ is available. The resulting three-segment path lies in $S$ and joins
$p$ to $q$, so $S$ is path-connected, and a path-connected space is connected.

:::

:::

::: {.pf-step #notdisconnected}

(D) fails.

::: pf-proof

A totally disconnected space has no connected subset with more than one point;
but $S$ is connected and contains more than one point, for instance
$(0,\frac12)$ and $(1,\frac12)$, both of whose second coordinate is
irrational. So $S$ is not totally disconnected, and the only true statement is
(C).

:::

:::

:::


:::
