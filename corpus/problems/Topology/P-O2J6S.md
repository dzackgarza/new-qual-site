---
schema: qual/card@1
id: P-O2J6S
kind: problem
title: Generators of covering subgroups of $S^1\vee S^1$ (UCSD Math 290, sheet 4)
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The problem list of the Topology Problems (Solutions) extraction has no Covering Spaces section; solutions item 2.4.7 holds only the subgroup generators and diagrams. No copy of the question was found in assets/ or ~/gitclones (qual-wiki holds the same solutions file). The statement is marked unrecovered, not reconstructed."
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    QUESTION RECOVERED, and it is not an orphan. The retained fragment is one author's worked
    solutions to the UCSD Math 290 (Fall 2014) problem sheets, and the sheet is in the repository.
    Chain, each link checked in this checkout. (1) The retained file is
    assets/Topology/650_UCSD_Qual_Questions/Quals/extracted/Topology Problems (Solutions).md; its
    contents list "2.4 Covering Spaces" among its solutions but its questions part runs 1.1 Homotopy
    to 1.11 Cohomology Ring with no covering-spaces section, which is why the statement was missing.
    (2) That notebook's headings cite "Sheet 7", "Sheet 8", "Sheet 10", "Sheet 11", "Sheet 12", and
    its 2.4 items 1-6 answer problems 1-6 of the covering-space sheet in order -- item 2 gives the
    surface-cover formula g = n(h-1)+1, which reproduces the sheet's own 5-sheeted Sigma_11 -> Sigma_3
    and 3-sheeted Sigma_4 -> Sigma_2. (3) corpus/collections/SRC-UCSD-TOP-JUSTIN lists
    assets/attachments/UCSD_290_F14_sheet1..13.pdf as provenance, and sheet 4 is "4. Covering
    spaces". (4) assets/attachments/UCSD_290_F14_sheet4.pdf, page 1 (printed page 253), carries
    Problem 7 in both its parts, printed verbatim below, with the five cover diagrams and their a/b
    edge labels; the figure is retained at
    assets/Topology/figures/ucsd_290_f14_sheet4_problem7.png (a crop of that page), and the diagrams
    were re-rendered from the PDF at 400 dpi for this review.
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Two limits on that provenance. First, 650_UCSD_Qual_Questions is a qual-wiki folder name whose
    only recorded provenance is the migration entry in sources/migration-ledger.jsonl (native_target
    under assets/ws9/..., not materialised here), so the identification with UCSD Math 290 Fall 2014
    rests on the SRC-UCSD-TOP-JUSTIN provenance list and the problem-by-problem correspondence above,
    not on an upstream URL. Second, this sheet's Problem 7 second part and Problem 8 are already the
    subject of the card P-UCTOP290-S4-7; the two cards now answer the same printed problem and the
    reconciliation between them is recorded in the solution-written event below.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution completed from the diagrams, not transcribed. Each of the five printed covers was read
    off the 400 dpi rendering with its oriented a/b labels, and its subgroup computed from a spanning
    tree, with the basepoint named because the printed figures mark none. The scope of the rank
    formula is now stated correctly: 1-V+E is an integer statement for a FINITE connected graph only;
    for the two infinite pictures the subgroup is free on the edges outside a maximal spanning forest,
    which here gives rank 1 and rank 2 respectively. Reconciliation with P-UCTOP290-S4-7 and with the
    retained notebook's lists: its left-diagram basis is exactly the first diagram's basis below and
    its middle-diagram basis exactly the second's, and the retained notebook's first list is PROVED
    equal to the first diagram's subgroup (both lie in ker(a,b |-> 1,1 mod 3), of index 3 and rank 4,
    and both have rank 4). Still open and stated as open: which retained list is the third diagram's
    and which the fifth's; and P-UCTOP290-S4-7's claim that BOTH infinite covers give <b> up to
    conjugacy is false for the fifth, whose subgroup <ab, ba^-1> has rank 2. That is recorded here as
    a correction owed to that card, not silently applied to it.
---

::: {.problem}
Let $W=S^1\vee S^1$ and identify $\pi_1(W)=F_2=\langle a,b\rangle$ in the usual way.

(a) For each of the following pictures of a cover of $S^1\vee S^1$, write down generators for their corresponding subgroups in the free group $\langle a,b\rangle$.

![The five covers with their $a$- and $b$-edge labels: three finite covers and two infinite ones. UCSD Math 290, Fall 2014, sheet 4, Problem 7.](../../../assets/Topology/figures/ucsd_290_f14_sheet4_problem7.png)

(b) Conversely, for each of the following subgroups of $\langle a,b\rangle$, draw the corresponding cover:
$$
\langle a^2,b^2,(ab)^2\rangle\qquad
\langle a^2,b^2,aba^{-1},bab^{-1}\rangle\qquad
\langle a,b^3\rangle\qquad
\langle\{a^mb^na^{-m}b^{-n}:\forall m,n\}\rangle\qquad
\langle\{a^{2m}b^{2n}a^{-2m}b^{-2n}:\forall m,n\}\rangle .
$$

Problem 8 of the same sheet asks, for $H$ generated by all commutators $xyx^{-1}y^{-1}$ with $x,y\in F_2$, for the covering space corresponding to $H$; its cover is described on the card for that problem, `P-UCTOP290-S4-7`.
:::

::: {.solution}
Let $\Gamma$ be a connected graph covering $W$, with its edges labelled $a$ or $b$ and oriented: the edge labelled $a$ and directed from $u$ to $v$ covers the $a$-loop of $W$ by a homeomorphism onto $W$'s $a$-loop, and at every vertex of $\Gamma$ there is exactly one incoming and one outgoing edge of each label.

**Basepoints and conjugacy.** A subgroup is determined only once a vertex is chosen to sit over the basepoint of $W$: the edges of $\Gamma$ give a free basis of $\pi_1(\Gamma,v)\cong H\le F_2$, and moving $v$ to another vertex replaces $H$ by a conjugate. The printed pictures mark no basepoint, so each of them determines its subgroup up to conjugacy; below a basepoint is named for each picture and the basis is computed for it.

**Rank, and the scope of $1-V+E$.** A spanning forest of $\Gamma$ is contractible, so $\pi_1(\Gamma,v)$ is free on the edges outside it. When $\Gamma$ is **finite** with $V$ vertices and $E$ edges this gives the integer
$$
\operatorname{rank}\pi_1(\Gamma)=\#\{\text{non-forest edges}\}=1-V+E,
$$
and for a $k$-sheeted cover of a wedge of $r$ circles, $\operatorname{rank}=1+k(r-1)=1+k$ here. When $\Gamma$ is **infinite** there is no integer rank formula: $\pi_1(\Gamma)$ is still free on the non-forest edges, but $1-V+E$ is not defined as an integer, and the subgroup has infinite index in $F_2$ however few non-forest edges there are. This is the case for the last two pictures.

Read off the diagrams, the five covers are as follows. Write $T,L,R$ for the top, lower-left and lower-right vertices of the first three pictures.

1. $a$-edges $L\to R\to T\to L$ and $b$-edges $T\to L\to R\to T$, the same $3$-cycle, so $a$ and $b$ act by the same permutation. Basepoint $T$, spanning tree the $a$-edges $T\to L$, $L\to R$:
$$
\langle a^3,\ ba^{-1},\ aba^{-2},\ a^2b\rangle .
$$
2. $a$-edges the $3$-cycle $T\to L\to R\to T$ and a $b$-loop at each vertex. Basepoint $T$:
$$
\langle b,\ aba^{-1},\ a^2ba^{-2},\ a^3\rangle .
$$
3. $a$-edges the $3$-cycle $P\to L\to R\to P$, and $b$-edges the pair $P\to L$, $L\to P$ together with a $b$-loop at $R$; so $b$ exchanges $P$ and $L$ and fixes $R$. Basepoint $R$, spanning tree the $a$-edges $R\to P$, $P\to L$:
$$
\langle a^3,\ aba^{-2},\ a^2ba^{-1},\ b\rangle .
$$
4. An infinite $a$-line, a spanning tree, with one $b$-loop at a vertex. Basepoint at the loop:
$$
\langle b\rangle .
$$
5. An infinite $a$-line with two consecutive vertices $u\to v$ joined by one $b$-edge in each direction. Basepoint $u$; the $a$-line is a spanning tree and the two $b$-edges are the only non-forest edges:
$$
\langle ab,\ ba^{-1}\rangle .
$$

The first three are $3$-sheeted and yield subgroups of index $3$, of rank $1+3=4$, consistent with the four-element bases; the last two have infinite index and rank $1$ and $2$ respectively.

**Reconciliation with the other records.** The card `P-UCTOP290-S4-7` answers this same printed problem, and the retained solutions notebook lists five subgroups under "Generators of the subgroups". Where they can be checked against the diagrams they agree: the first basis above is exactly the left-diagram basis on `P-UCTOP290-S4-7`, and the second is exactly its middle-diagram basis and the retained notebook's second list. The first diagram's subgroup is moreover *proved* equal to the retained notebook's first list, not merely similar: both lie in $\ker(F_2\to\ZZ/3)$ sending $a$ and $b$ to $1$, which has index $3$ and rank $4$, and both bases have four elements, so both equal that kernel. The fourth diagram is the retained notebook's $\langle b\rangle$.

Two points are open. It is not settled here which retained list belongs to the third diagram and which to the fifth. And `P-UCTOP290-S4-7` states that both infinite pictures give $\langle b\rangle$ up to conjugacy; that is true of the fourth picture but not of the fifth, whose subgroup $\langle ab,ba^{-1}\rangle$ has rank $2$ and so cannot be conjugate to $\langle b\rangle$. The correction is owed to that card; it is not applied there in this pass.

For part (b) the five printed subgroups are as displayed above; the covers corresponding to them are drawn on `P-UCTOP290-S4-7`, which solves that half. They are not re-derived here, and no index or rank is asserted for them in this card.
:::
