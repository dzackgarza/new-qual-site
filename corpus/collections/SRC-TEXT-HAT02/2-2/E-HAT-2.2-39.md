---
schema: qual/card@1
id: E-HAT-2.2-39
kind: problem
title: Relative Mayer–Vietoris sequences for CW pairs from algebraic lemma
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - CW Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 39.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the degreewise exactness: a cell outside $Y$ lying in both $A$ and $B$ contributes
    $0\to\ZZ\xrightarrow{(1,-1)}\ZZ^2\xrightarrow{(1,1)}\ZZ\to0$, a cell in exactly one of them
    contributes an isomorphism, and cells lying in $Y$ contribute the corresponding copy of the
    intersection group or nothing, so the cellular sequence is short exact and its homology
    sequence is the relative Mayer-Vietoris sequence. The printed hypothesis reads "with $A=B$ or
    $C=D$"; the chain-level argument in the card uses $C\subset A$ and $D\subset B$ and does not
    use the printed alternative, which is the condition under which the sequence is exact.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement checked against the printed p. 159, which does read "with A = B or C = D"; the card
    reproduces it and no repair of the statement was needed. The proof is a degreewise cell count
    and is correct: with C contained in A and D contained in B the quotient of cells gives the
    short exact sequence, exactness being checked cell by cell, and Theorem 2.16 p. 117 then gives
    the sequence. Results now cited: Exercise 18 p. 157 for the relative cellular complex and the
    identification of its homology with H_*(X,Y), Theorem 2.16 p. 117 for the long exact sequence,
    and p. 153 for the case C = D. The card now says that C contained in A and D contained in B is
    the situation used and that the printed hypotheses are special cases of it. What is not
    covered: no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the cell-by-cell exactness
    argument, which is the whole content: a cell of A cap B outside Y contributes
    0 -> Z -> Z^2 -> Z -> 0 with maps (1,-1) and (1,1); a cell in exactly one of A, B contributes
    0 -> 0 -> Z -> Z -> 0; and cells in Y contribute only through the C and D memberships, where
    the surviving middle copy is the image of the intersection copy. Added the point the prose
    left implicit: that the maps commute with cellular boundary because membership in a
    subcomplex passes to boundary cells, which is what makes the sequence one of chain complexes
    rather than just of graded groups. The card's general hypotheses C contained in A, D contained
    in B are stated as such and the printed cases A = B and C = D are recorded as special cases,
    so the printed statement is what is proved. Statement unchanged; no retained solution set
    covers this exercise.
---

::: {.problem}
Use the preceding exercise to derive relative Mayer–Vietoris sequences for CW pairs $(X, Y) = (A \cup B, C \cup D)$ with $A = B$ or $C = D$.
:::

::: {.solution}
Filter the cube diagram of the preceding exercise, so that the relative cellular chains of $(X,Y)$ with $A,B,C,D$ subcomplexes and $C\subseteq A$, $D\subseteq B$ sit in a short exact sequence of complexes; the long exact homology sequence of that short exact sequence is the relative Mayer--Vietoris sequence. The printed hypotheses $A=B$ and $C=D$ are special cases of the hypotheses used, and the sequence for them is the one derived. The argument is this card's own: no retained solution set covers this exercise.

::: pf

::: {.pf-step #cw}
Give $X$ a CW structure in which $A$, $B$, $C$ and $D$ are subcomplexes, with $C\subseteq A$, $D\subseteq B$, $Y=C\cup D$ and $X=A\cup B$; this covers the printed case $A=B$ or $C=D$.

::: pf-proof
The exercise's pairs are $(X,Y)=(A\cup B,C\cup D)$, so the hypotheses $Y=C\cup D$ and $X=A\cup B$ are the statement's, and by the first part of the preceding exercise such a CW structure on $X$ with $A,B,C,D$ subcomplexes exists. The printed conditions $A=B$ or $C=D$ are particular choices of these subcomplexes, so a proof under the inclusions $C\subseteq A$, $D\subseteq B$ (which the printed cases satisfy, since then $C=A$ or $D=B$ is a subcomplex of the same set) gives the printed statement. What is needed of $C$ and $D$ in the proof below is only $C\subseteq A$ and $D\subseteq B$.
:::

:::


::: {.pf-step #chain}
There is a short exact sequence of chain complexes
$$
0\to C_*^{\mathrm{cell}}(A\cap B,C\cap D)\xrightarrow{(i_*,-j_*)}C_*^{\mathrm{cell}}(A,C)\oplus C_*^{\mathrm{cell}}(B,D)\xrightarrow{k_*+\ell_*}\to C_*^{\mathrm{cell}}(X,Y)\to0,
$$
where the maps are induced by the inclusions.

::: pf-proof
The relative cellular chain group is $H_n(X^n,X^{n-1}\cup Y^n)$, as computed in the preceding exercise, and it is the free abelian group on the $n$-cells of $X$ not in $Y$: each such cell contributes a $\ZZ$. Write a cell as a pair (cell of $X$, contained in which of $A,B,C,D$). A cell not in $Y=C\cup D$ contributes to the middle and top terms according to its membership, and the maps are the inclusion-induced ones with the signs displayed. The proof that the sequence is exact in each degree is step [](#exact){.pf-ref}.
:::

:::


::: {.pf-step #exact}
The sequence of step [](#chain){.pf-ref} is exact in each degree.

::: pf-proof
Check one cell $e\notin Y$ at a time. If $e\subseteq A\cap B$ it contributes $0\to\ZZ\xrightarrow{(1,-1)}\ZZ^2\xrightarrow{(1,1)}\ZZ\to0$, which is exact: the first map is injective, its image is the pairs $(x,-x)$ with $x\in\ZZ$, and those are exactly the pairs killed by the second map. If $e$ lies in exactly one of $A,B$, say $A$, it contributes $0\to0\to\ZZ\xrightarrow{\cong}\ZZ\to0$, exact since the last map is an isomorphism. A cell $e\in Y$ contributes nothing to the top term; if it lies in $A$ and in $C$, then it contributes to $C_*^{\mathrm{cell}}(A,C)$ as $0$, and similarly for $B$ and $D$; if it lies in $A\cap B$ and in $C\cap D$ it contributes $0$ everywhere; and if it lies in $A\cap B$ but in only one of $C$, $D$, then exactly one of the two middle summands survives, and it is the image of the single copy in the intersection term, so exactness holds. Every cell falls into one of these cases, and in each the three groups form an exact sequence; a direct sum of exact sequences is exact.
:::

:::


::: {.pf-step #boundary}
The maps of step [](#chain){.pf-ref} commute with the cellular boundary maps, so the sequence of chain complexes is short exact.

::: pf-proof
The cellular boundary of a cell is a signed sum of cells in its boundary, and membership in a subcomplex is inherited by boundary cells: the boundary of a cell in $A$ lies in $A^{n-1}$, of a cell in $C$ lies in $C^{n-1}$, and so on. Hence the boundary of a chain in $C_*^{\mathrm{cell}}(A,C)$ again lies there, and the induced maps are chain maps because they are induced by inclusions of pairs, which commute with $\partial$. With step [](#exact){.pf-ref} this makes the sequence short exact in each degree, hence a short exact sequence of chain complexes.
:::

:::


::: {.pf-step #les}
The long exact homology sequence of the short exact sequence of step [](#boundary){.pf-ref} is the relative Mayer--Vietoris sequence
$$
\cdots\to H_n(A\cap B,C\cap D)\to H_n(A,C)\oplus H_n(B,D)\to H_n(X,Y)\xrightarrow{\partial}H_{n-1}(A\cap B,C\cap D)\to\cdots
$$

::: pf-proof
A short exact sequence of chain complexes has a long exact homology sequence (Theorem 2.16, printed p.~117, in its algebraic form), and applying it to the sequence of step [](#boundary){.pf-ref} gives the displayed sequence with the stated connecting map. The relative cellular chain groups compute relative singular homology, so the terms are the singular homology groups of the pairs named.
:::

:::


::: {.pf-step #conclusion}
The relative Mayer--Vietoris sequence holds for $(X,Y)=(A\cup B,C\cup D)$ in the printed cases $A=B$ and $C=D$.

::: pf-proof
Steps [](#cw){.pf-ref} to [](#les){.pf-ref} derive the sequence for subcomplexes with $C\subseteq A$ and $D\subseteq B$; the printed hypotheses are the special cases of step [](#cw){.pf-ref}, so they are covered. The signs are the difference and sum signs of the preceding exercise, which are the ones used in step [](#chain){.pf-ref}.
:::

:::

:::
:::
