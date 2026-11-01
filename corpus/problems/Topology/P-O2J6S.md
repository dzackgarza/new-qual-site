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
Let $\Gamma$ be a connected graph covering $W$, with its edges labelled $a$ or $b$ and oriented: the edge labelled $a$ and directed from $u$ to $v$ covers the $a$-loop of $W$ by a homeomorphism onto that loop, and at every vertex of $\Gamma$ there is exactly one incoming and one outgoing edge of each label.

**Basepoints and conjugacy.** A subgroup is an invariant of the cover together with a choice of vertex over the basepoint of $W$: the edges of $\Gamma$ then give a free basis of $\pi_1(\Gamma,v)\cong H\le F_2$, and moving $v$ replaces $H$ by a conjugate. The printed pictures mark no basepoint, so each picture determines its subgroup only up to conjugacy. Below, a basepoint is named for each picture and the basis is computed for it; where a picture is matched to a fixed list of generators, that list is the list for the named basepoint.

**Rank, and the scope of $1-V+E$.** A spanning forest of $\Gamma$ is contractible, so $\pi_1(\Gamma,v)$ is free on the edges outside it. When $\Gamma$ is **finite** with $V$ vertices and $E$ edges this is the integer
$$
\operatorname{rank}\pi_1(\Gamma)=1-V+E ,
$$
and a $k$-sheeted cover of a wedge of $r$ circles has $\operatorname{rank}=1+k(r-1)$. For the figure-eight $W$ of this problem $r=2$, so that formula specialises to $1+k$; the equality $1+k(r-1)=1+k$ is thus a statement about $r=2$ only, not about arbitrary $r$. When $\Gamma$ is **infinite** there is no integer formula: $\pi_1(\Gamma)$ is still free on the non-forest edges, but $1-V+E$ is not defined, and such a subgroup has infinite index however few non-forest edges there are. Both infinite pictures below are of this kind: in the order they are listed, the fourth has one non-forest edge and the fifth has two.

**The five covers.** For the first three pictures write $T,L,R$ for the top, lower-left and lower-right vertices.

1. $a$-edges $L\to R\to T\to L$ and $b$-edges $T\to L\to R\to T$: the same $3$-cycle, so $a$ and $b$ act by the same permutation. At $T$, with the spanning tree the $a$-edges $T\to L$, $L\to R$, the non-forest edges are $R\xrightarrow{a}T$, $T\xrightarrow{b}L$, $L\xrightarrow{b}R$, $R\xrightarrow{b}T$ and give
$$
\langle a^3,\ ba^{-1},\ aba^{-2},\ a^2b\rangle .
$$
2. $a$-edges the $3$-cycle $T\to L\to R\to T$, and a $b$-loop at each vertex. At $T$, the tree being $T\xrightarrow{a}L\xrightarrow{a}R$:
$$
\langle a^3,\ b,\ aba^{-1},\ a^2ba^{-2}\rangle .
$$
3. $a$-edges the $3$-cycle $P\to L\to R\to P$; $b$-edges $P\to L$, $L\to P$ and a $b$-loop at $R$. So $b$ interchanges $P$ and $L$ and fixes $R$. At $L$, with the tree $L\xrightarrow{a}R\xrightarrow{a}P$:
$$
\langle a^3,\ a^2b,\ ba^{-2},\ aba^{-1}\rangle .
$$
At the other natural choice, the $b$-fixed vertex $R$, the basis is $\langle a^3,\ aba^{-2},\ a^2ba^{-1},\ b\rangle$, which is a conjugate.
4. An infinite $a$-line with one $b$-loop at a vertex. At that vertex the line is a spanning tree and the loop is the only non-forest edge:
$$
\langle b\rangle .
$$
5. An infinite $a$-line, with two consecutive vertices $\alpha\to\beta$ of it joined by one $b$-edge in each direction. At $\beta$ the line is a spanning tree and the two $b$-edges are the only non-forest edges, giving the free basis
$$
a^{-1}b\quad\text{and}\quad ba ,
\qquad\text{that is}\qquad
\langle ba,\ b^{-1}a\rangle ,
$$
since $a^{-1}b=(b^{-1}a)^{-1}$.

The first three covers are $3$-sheeted, so their subgroups have index $3$ and rank $1+3=4$, matching the four-element bases. The last two have infinite index and rank $1$ and $2$ respectively, as computed for the fourth and fifth covers.

**Matching the five lists in the retained solutions.** The retained notebook gives five lists under "Generators of the subgroups", and the sheet's own solutions pair them with these five pictures in this order. Each pairing is now an identity of subgroups at the basepoint named above, not a resemblance.

Picture 1: the subgroup $K=\langle a^3,ba^{-1},aba^{-2},a^2b\rangle$ equals the retained first list $R_1=\langle ab^{-1},\,aba^{-2},\,a^3b^{-1}a^{-2},\,a^3\rangle$. Both containments are witnessed by exact word identities:
$$
a^3\in R_1,\qquad
aba^{-2}\in R_1,\qquad
ba^{-1}=(ab^{-1})^{-1}\in R_1,\qquad
a^2b=(a^3b^{-1}a^{-2})^{-1}a^3\in R_1,
$$
so $K\subseteq R_1$; and
$$
a^3\in K,\qquad
aba^{-2}\in K,\qquad
ab^{-1}=(ba^{-1})^{-1}\in K,\qquad
a^3b^{-1}a^{-2}=a^3\,(a^2b)^{-1}\in K,
$$
so $R_1\subseteq K$. Hence $K=R_1$. (The last identity is immediate: $a^3(a^2b)^{-1}=a^3b^{-1}a^{-2}$.)

Picture 2: the retained second list is $\langle b,\ aba^{-1},\ a^2ba^{-2},\ a^3\rangle$, the same four generators as above in a different order, so the subgroups are equal by inspection.

Picture 3: the subgroup $S=\langle a^3,\,a^2b,\,ba^{-2},\,aba^{-1}\rangle$ equals the retained third list $R_3=\langle b^2,\,ba,\,a^3,\,aba^{-1}\rangle$. Writing $g_1=a^3$, $g_2=a^2b$, $g_3=ba^{-2}$, $g_4=aba^{-1}$ and $h_1=b^2$, $h_2=ba$, $h_3=a^3$, $h_4=aba^{-1}$, the identities
$$
b^2=g_3g_2,\qquad ba=g_3g_1,\qquad a^3=g_1,\qquad aba^{-1}=g_4
$$
give $R_3\subseteq S$, and
$$
g_3=h_2h_3^{-1},\qquad g_2=h_3h_2^{-1}h_1,\qquad g_1=h_3,\qquad g_4=h_4
$$
give $S\subseteq R_3$. Hence $S=R_3$.

Picture 4: the retained fourth list is $\langle b\rangle$, the basis computed above.

Picture 5: the retained fifth list is $\langle ba,\,b^{-1}a\rangle$, and the basis computed at $\beta$ is $\langle ba,\,a^{-1}b\rangle$; these are equal because $a^{-1}b=(b^{-1}a)^{-1}$.

So the five pictures correspond to the five retained lists in order, and the correspondence is proved at the stated basepoints. Consequently the fifth picture's subgroup has rank $2$ and is not conjugate to $\langle b\rangle$.

**The other card on this problem.** `P-UCTOP290-S4-7` answers the same printed Problem 7, and its first three bases agree with pictures 1, 2 and 3 above at the basepoints named there. Its treatment of the fifth picture was wrong — it assigned $\langle b\rangle$ up to conjugacy to both infinite pictures, which holds only for the fourth, since the fifth's subgroup has rank $2$ and rank is a conjugacy invariant. That card has been corrected in the same pass, so nothing here rests on it in its uncorrected state.

For part (b), the five printed subgroups are as displayed; the covers corresponding to them are drawn on `P-UCTOP290-S4-7`, which solves that half. They are not re-derived here, and no index or rank is asserted for them on this card.
:::
