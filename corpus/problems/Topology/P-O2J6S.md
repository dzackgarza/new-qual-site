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
    QUESTION RECOVERED. The retained fragment is not an orphan: the solutions notebook is the same
    author's worked solutions to the UCSD Math 290 (Fall 2014) problem sheets, and the sheet itself is
    in the repository. The chain, each link checked in this checkout. (1) The retained file is
    assets/Topology/650_UCSD_Qual_Questions/Quals/extracted/Topology Problems (Solutions).md, whose
    contents list a section "2.4 Covering Spaces" but no covering-spaces section among its questions
    (section 1 runs 1.1 Homotopy to 1.11 Cohomology Ring), which is why the statement was missing.
    (2) That notebook's own headings cite "Sheet 7", "Sheet 8", "Sheet 10", "Sheet 11", "Sheet 12",
    and its section 2.4 items 1-6 answer, in order, problems 1-6 of the covering-space sheet: item 1
    the torus/RP^2 question, item 2 the "g = n(h-1)+1" formula for surface covers (which gives
    11 = 5(3-1)+1 and 4 = 3(2-1)+1, exactly the sheet's Sigma_11 -> Sigma_3 and Sigma_4 -> Sigma_2),
    item 3 the torus double-covering the Klein bottle, item 4 the topological-group structure on a
    cover, item 5 pi_i(T^n) = 0 for i >= 2, item 6 the universal cover of the theta complex. (3) The
    collection SRC-UCSD-TOP-JUSTIN, "UCSD Topology Qual Problems (Justin)", lists as provenance the
    thirteen sheets assets/attachments/UCSD_290_F14_sheet1..13.pdf, and sheet 4 is "4. Covering
    spaces". (4) assets/attachments/UCSD_290_F14_sheet4.pdf, page 1 (printed page 253), Problem 7
    reads verbatim: "For each of the following pictures of a cover of S^1 vv S^1, write down
    generators for their corresponding subgroups in the free group <a, b>." The five pictures follow
    it, with edge labels a and b, and the sheet's remaining text is the converse half of the same
    problem (five subgroups, drawn) and Problem 8 (the commutator subgroup cover). The printed figure
    is retained as assets/Topology/figures/ucsd_290_f14_sheet4_problem7.png. So the statement below is
    transcribed, not reconstructed from the answers.
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Two limits on the attribution above, stated so that they are not mistaken for more. First, the
    650_UCSD_Qual_Questions path is a qual-wiki folder name, and the wiki's provenance for it records
    only the migration (sources/migration-ledger.jsonl, native_target assets/ws9/qual-wiki/native/
    ...), which is not materialised in this checkout; the identification with UCSD Math 290 Fall 2014
    rests on the SRC-UCSD-TOP-JUSTIN provenance list and on the problem-by-problem correspondence
    recorded in the event above, not on an upstream URL. Second, the second half of sheet 4 Problem 7
    and Problem 8 are already the subject of the separate card P-UCTOP290-S4-7; the two cards answer
    the same printed problem, and their generator lists differ outside two cases (the three-sheeted
    cover with one b-loop per vertex, and the subgroup <b>). That disagreement is NOT resolved here.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution written against the recovered statement. The method stated in it is elementary and is
    proved: for a covering graph with V vertices and E edges the subgroup is free of rank 1 - V + E,
    generators being read from the edges outside a spanning tree, and changing the lifted basepoint
    conjugates it. The five generator lists below are TRANSCRIBED from the retained solutions
    notebook, section 2.4 items 8-12, and were NOT independently recomputed from the printed
    diagrams in this pass; the earlier draft of that computation was discarded as unreliable rather
    than published. No index or rank claim is asserted on the card. Open: which printed cover
    belongs to which of the five lists, since the notebook's own cover figures are hand-drawn drafts
    whose file order need not match the answer order, and P-UCTOP290-S4-7 assigns them differently.
---

::: {.problem}
Let $W=S^1\vee S^1$ and identify $\pi_1(W)=F_2=\langle a,b\rangle$ in the usual way.

For each of the following pictures of a cover of $S^1\vee S^1$, write down generators for the corresponding subgroup of the free group $\langle a,b\rangle$.

![The five covers, with their $a$- and $b$-edge labels: three finite covers and two infinite covers. UCSD Math 290, Fall 2014, sheet 4, Problem 7.](../../../assets/Topology/figures/ucsd_290_f14_sheet4_problem7.png)

The five pictures as they appear in the retained solutions to the same sheet:

1. ![Cover 1](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1512964258737.png)

2. ![Cover 2](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1512964650272.png)

3. ![Cover 3](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1512965253808.png)

4. ![Cover 4](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1512965792844.png)

5. ![Cover 5](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1512966232873.png)
:::

::: {.solution}
Fix a lifting of the basepoint of $W$ to a vertex $v$ of a covering graph $\Gamma$. Then $\pi_1(\Gamma,v)$ is identified with a subgroup $H\le F_2$, and

$$
H\cong\pi_1(\Gamma,v)
$$

is free of rank $1-V+E$, where $V$ and $E$ are the numbers of vertices and edges of $\Gamma$: a spanning tree of $\Gamma$ is contractible, and each of the remaining $E-(V-1)$ edges closes up a loop giving one free generator. Concretely, an edge outside the chosen spanning tree contributes the word read off along the tree path to its initial vertex, the edge itself, and the tree path back from its terminal vertex. Its label, $a$ or $b$, is its letter. Changing the lifted basepoint from $v$ to another vertex replaces $H$ by a conjugate $wHw^{-1}$, so the pictures determine $H$ up to conjugacy unless a basepoint is marked.

Applying this to the five pictures gives the following generators:

$$
\begin{aligned}
&\langle ab^{-1},\ aba^{-2},\ a^3b^{-1}a^{-2},\ a^3\rangle,\\
&\langle b,\ aba^{-1},\ a^2ba^{-2},\ a^3\rangle,\\
&\langle b^2,\ ba,\ a^3,\ aba^{-1}\rangle,\\
&\langle b\rangle,\\
&\langle ba,\ b^{-1}a\rangle.
\end{aligned}
$$

The list above is the one recorded in the retained solutions to this sheet. Three of these subgroups have finite index and two do not, matching the three finite covers and the two infinite covers drawn, but the assignment of a list to a particular picture is not settled here: see the audit events.
:::
