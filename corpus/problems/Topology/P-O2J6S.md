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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    SUPERSEDES the justification given in the solution-written event above, which was invalid, and
    settles the two items that event left open. (i) The invalid step: that event argued the first
    picture's subgroup equals the retained first list because both lie in ker(a,b |-> 1,1 mod 3), which
    has index 3 and rank 4, and both bases have four elements. That does not follow -- a subgroup of a
    free group of rank 4 contained in it may have rank 4 and infinite index, so containment plus equal
    generator counts proves nothing. It is replaced by mutual containment with explicit word witnesses:
    a^3, aba^-2, ba^-1 = (ab^-1)^-1 and a^2b = (a^3 b^-1 a^-2)^-1 a^3 all lie in the retained list, and
    conversely a^3, aba^-2, ab^-1 = (ba^-1)^-1 and a^3 b^-1 a^-2 = a^3 (a^2 b)^-1 all lie in the
    computed basis. Each is an exact identity in F_2, checkable by cancellation. (ii) Pictures 3 and 5
    are now assigned rather than left open. Picture 3 at the vertex L has basis (a^3, a^2 b, ba^-2,
    aba^-1), and it equals the retained third list (b^2, ba, a^3, aba^-1) by the six identities
    b^2 = g3 g2, ba = g3 g1, a^3 = g1, aba^-1 = g4 and g3 = h2 h3^-1, g2 = h3 h2^-1 h1, g1 = h3,
    g4 = h4. Picture 5 at the right-hand vertex beta of the pair has basis (ba, a^-1 b), and
    a^-1 b = (b^-1 a)^-1 makes it exactly the retained fifth list (ba, b^-1 a). So the five pictures
    correspond to the five retained lists in order, at the basepoints named on the card. (iii) The
    consequence for the fifth picture -- rank 2, hence not conjugate to <b> -- is the correction owed to
    P-UCTOP290-S4-7, and it has been applied to that card in this same pass, so this card's delegation
    of part (b) to it does not rest on an uncorrected statement. Not checked: the five part (b) covers
    are not re-derived here; the basepoints are the ones named, and the other conjugates of pictures 1
    and 3 are not written out.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. What was checked this turn: the dictionary between a labelled graph cover and a subgroup of F_2 up to conjugacy, with the spanning-tree recipe stated explicitly and then applied edge by edge to each picture; the rank formula 1 - V + E for finite covers (rank 4 for the three 3-sheeted ones) and its inapplicability to the two infinite ones (rank 1 and rank 2, being the number of edges outside a maximal forest); and every word identity by which the computed bases are matched to the five retained lists, each an exact cancellation (for picture 1: a^3, aba^{-2}, ba^{-1} = (ab^{-1})^{-1} and a^2 b = (a^3 b^{-1} a^{-2})^{-1} a^3; for picture 3: b^2 = g_3 g_2, ba = g_3 g_1, g_3 = h_2 h_3^{-1}, g_2 = h_3 h_2^{-1} h_1). Two things were repaired in the course of the restructuring: an arithmetic slip in the first draft's picture-1 paragraph (the b-edge T -> L returns along the tree path L -> T, giving b a^{-1}, not b a^{-2}), and, as a cross-check, the picture-3 basis was confirmed independently against the four generators the tree gives (ba, a^2 b^{-1}, b^2, aba^{-1}), each expressed in the card's four (a^2 b^{-1} = g_3^{-1}). The reading of the five figures is carried from the card's earlier pass on the 400 dpi rendering; this turn re-examined the figure at reduced resolution only, which confirms the shapes (three finite 3-sheeted covers, two infinite ones) but not every edge arrow, so the edge structures used in the steps are as recorded by that earlier reading. The fifth picture's rank-2 conclusion, and the correction owed to P-UCTOP290-S4-7, are as on the card. Part (b) remains delegated to P-UCTOP290-S4-7 and is not re-derived here.
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
The collection's provenance is the retained UCSD Math 290 sheet 4 (Problem 7), whose figures are the statement, plus the retained worked notebook whose five lists are matched below. The reading of the five figures is the card's own, taken from the rendering at `assets/Topology/figures/ucsd_290_f14_sheet4_problem7.png`; the group theory below is checked word by word in $F_2=\langle a,b\rangle$, and every identity used is an exact cancellation, not a resemblance.

::: pf

::: {.pf-step #dictionary}
Let $\Gamma$ be a connected graph whose edges are labelled $a$ or $b$ and oriented, with exactly one incoming and one outgoing edge of each label at every vertex. Then $\Gamma\to W=S^1\vee S^1$ is a covering, and for a vertex $v$ the image $\pi_1(\Gamma,v)\le F_2$ is generated by the words read along the edges outside a spanning tree; changing $v$ replaces the subgroup by a conjugate.

::: pf-proof
The label-and-orientation condition is exactly the covering condition for the standard cover $W$ with one vertex and one $a$-loop and one $b$-loop: lifting a small neighbourhood of the base point means choosing, at each vertex, the incoming and outgoing $a$-edge and the incoming and outgoing $b$-edge. A spanning tree $T$ of $\Gamma$ is contractible, so $\Gamma$ deformation retracts onto the quotient with one vertex and one loop per edge outside $T$; the words these loops spell, read from $v$ along $T$, generate $\pi_1(\Gamma,v)$, and their images generate the subgroup. A different basepoint gives the conjugate by the word of the path between the two vertices.
:::

:::

::: {.pf-step #rank}
If $\Gamma$ is finite, connected, with $V$ vertices and $E$ edges, then $\operatorname{rank}\pi_1(\Gamma)=1-V+E$; for a $k$-sheeted cover of $W$ this is $1+k$. If $\Gamma$ is infinite this integer is not defined, and the rank is the number of edges outside a maximal forest.

::: pf-proof
A spanning tree has $V-1$ edges, and the remaining $E-V+1$ edges give a free basis of $\pi_1(\Gamma)$. For a $k$-sheeted cover $E=2k$ (two edges at each of the $k$ vertices) and $V=k$, so the rank is $1-k+2k=1+k$. On an infinite graph a maximal forest still exists (Zorn) and the remaining edges still form a free basis, but $V$ and $E$ are not finite, so no integer formula applies.
:::

:::

::: {.pf-step #p1}
Picture 1 has three vertices $T,L,R$ with $a$-edges $L\to R\to T\to L$ and $b$-edges $T\to L\to R\to T$; at $T$ it gives $\langle a^3,\ ba^{-1},\ aba^{-2},\ a^2b\rangle$.

::: pf-proof
Both labels act by the same $3$-cycle, so the covering is $3$-sheeted and its subgroup has index $3$ and, by step [](#rank){.pf-ref}, rank $1+3=4$. Take the tree to be the $a$-edges $T\to L$, $L\to R$; the four non-tree edges are $R\xrightarrow{a}T$, $T\xrightarrow{b}L$, $L\xrightarrow{b}R$, $R\xrightarrow{b}T$. Reading each as a loop based at $T$ through the tree gives $a^3$, $ba^{-1}$, $aba^{-2}$ and $a^2b$ respectively. Explicitly, with tree paths $T\to L$ labelled $a$ and $L\to R$ labelled $a$, so that $t(T)=\epsilon$, $t(L)=a$, $t(R)=a^2$: the $a$-edge $R\to T$ gives $t(R)a\,t(T)^{-1}=a^3$; the $b$-edge $T\to L$ gives $t(T)b\,t(L)^{-1}=ba^{-1}$; the $b$-edge $L\to R$ gives $t(L)b\,t(R)^{-1}=aba^{-2}$; and the $b$-edge $R\to T$ gives $t(R)b\,t(T)^{-1}=a^2b$. Each is a loop at $T$, as it must be.
:::

:::

::: {.pf-step #p2}
Picture 2 has $a$-edges the $3$-cycle $T\to L\to R\to T$ and a $b$-loop at each vertex; at $T$ it gives $\langle a^3,\ b,\ aba^{-1},\ a^2ba^{-2}\rangle$.

::: pf-proof
Again $3$-sheeted, so index $3$ and rank $4$. With the tree $T\xrightarrow{a}L\xrightarrow{a}R$, the non-tree edges are $R\xrightarrow{a}T$ (giving $a^3$), the three $b$-loops (giving $b$ at $T$, $aba^{-1}$ at $L$ and $a^2ba^{-2}$ at $R$), each read from $T$ along the tree.
:::

:::

::: {.pf-step #p3}
Picture 3 has $a$-edges the $3$-cycle $P\to L\to R\to P$ and $b$-edges $P\to L$, $L\to P$, together with a $b$-loop at $R$; at $L$ it gives $\langle a^3,\ a^2b,\ ba^{-2},\ aba^{-1}\rangle$.

::: pf-proof
Here $b$ interchanges $P$ and $L$ and fixes $R$, so again $3$-sheeted, index $3$, rank $4$. With the tree $L\xrightarrow{a}R\xrightarrow{a}P$ the non-tree edges give $a^3$ (the $a$-edge $P\to L$), $a^2b$ (the $b$-edge $P\to L$), $ba^{-2}$ (the $b$-edge $L\to P$, whose return along the tree spells $a^{-2}$) and $aba^{-1}$ (the $b$-loop at $R$: out along $L\to R$, round the loop, back along $R\to L$).
:::

:::

::: {.pf-step #p4}
Picture 4 is an infinite $a$-line with a single $b$-loop at one vertex, and its subgroup is $\langle b\rangle$.

::: pf-proof
The $a$-line is a maximal forest (it contains every vertex), so the only non-forest edge is the $b$-loop, and by step [](#dictionary){.pf-ref} the subgroup is generated by $b$ alone. Its rank is $1$ and its index in $F_2$ is infinite, as step [](#rank){.pf-ref} says must happen for an infinite cover.
:::

:::

::: {.pf-step #p5}
Picture 5 is an infinite $a$-line with two consecutive vertices $\alpha\to\beta$ joined by a $b$-edge in each direction, and at $\beta$ its subgroup is $\langle ba,\ b^{-1}a\rangle=\langle ba,\ a^{-1}b\rangle$.

::: pf-proof
The $a$-line is a maximal forest, and the two $b$-edges are the non-forest edges. Read from $\beta$: the $b$-edge $\beta\to\alpha$ followed by the tree path $\alpha\to\beta$ (one $a$-edge) gives $ba$; the $b$-edge $\alpha\to\beta$ preceded by the tree path $\beta\to\alpha$ gives $a^{-1}b$. Since $a^{-1}b=(b^{-1}a)^{-1}$, the subgroup is $\langle ba,\ b^{-1}a\rangle$, free of rank $2$.
:::

:::

::: {.pf-step #match}
The five computed subgroups equal the five lists of the retained notebook, in order: $\langle ab^{-1},aba^{-2},a^3b^{-1}a^{-2},a^3\rangle$, $\langle b,aba^{-1},a^2ba^{-2},a^3\rangle$, $\langle b^2,ba,a^3,aba^{-1}\rangle$, $\langle b\rangle$ and $\langle ba,b^{-1}a\rangle$.

::: pf-proof
Picture 1: writing $K=\langle a^3,ba^{-1},aba^{-2},a^2b\rangle$ and $R_1=\langle ab^{-1},aba^{-2},a^3b^{-1}a^{-2},a^3\rangle$, the identities $a^3\in R_1$, $aba^{-2}\in R_1$, $ba^{-1}=(ab^{-1})^{-1}\in R_1$ and $a^2b=(a^3b^{-1}a^{-2})^{-1}a^3\in R_1$ give $K\subseteq R_1$, while $a^3,aba^{-2},ab^{-1}=(ba^{-1})^{-1},a^3b^{-1}a^{-2}=a^3(a^2b)^{-1}$ all lie in $K$, giving $R_1\subseteq K$.
Picture 2: the four generators $a^3,b,aba^{-1},a^2ba^{-2}$ are those of the retained second list, listed in another order.
Picture 3: with $g_1=a^3$, $g_2=a^2b$, $g_3=ba^{-2}$, $g_4=aba^{-1}$ and $h_1=b^2$, $h_2=ba$, $h_3=a^3$, $h_4=aba^{-1}$, the identities $b^2=g_3g_2$, $ba=g_3g_1$, $a^3=g_1$, $aba^{-1}=g_4$ give $R_3\subseteq S$ and $g_3=h_2h_3^{-1}$, $g_2=h_3h_2^{-1}h_1$, $g_1=h_3$, $g_4=h_4$ give $S\subseteq R_3$. As a check on the tree computation, the four tree-based generators of this cover are $ba$, $a^2b^{-1}$, $b^2$ and $aba^{-1}$, and each is a word in the card's four: $ba=g_3g_1$, $b^2=g_3g_2$, $aba^{-1}=g_4$ and $a^2b^{-1}=a^2b\,(b^2)^{-1}=g_2(g_3g_2)^{-1}=g_3^{-1}$.
Pictures 4 and 5: the retained fourth list is $\langle b\rangle$ and the fifth is $\langle ba,b^{-1}a\rangle$, identical to steps [](#p4){.pf-ref} and [](#p5){.pf-ref}.
:::

:::

::: {.pf-step}
The fifth picture's subgroup has rank $2$ and is therefore not conjugate to $\langle b\rangle$, which has rank $1$; and part (b) is not re-derived here.

::: pf-proof
Conjugacy preserves the rank of a free subgroup, so picture 5 is not a conjugate of picture 4: the retained notebook's assignment of $\langle b\rangle$ to both infinite pictures is corrected here, and the corresponding correction on `P-UCTOP290-S4-7` is recorded there. For part (b), the five printed subgroups are as displayed in the statement; the covers they correspond to are drawn on `P-UCTOP290-S4-7`, which solves that half, and no index or rank for them is asserted on this card.
:::

:::

:::
:::
