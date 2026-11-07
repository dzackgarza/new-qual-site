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
---

::: {.problem}
Use the preceding exercise to derive relative Mayer–Vietoris sequences for CW pairs $(X, Y) = (A \cup B, C \cup D)$ with $A = B$ or $C = D$.
:::

::: {.solution}
Give $X$ a CW structure for which $A$, $B$, $C$, and $D$ are subcomplexes, with $C\subset A$ and $D\subset B$; this is the situation in which the printed conditions $A=B$ or $C=D$ are special cases. The relative cellular chain groups of Exercise 18 (p. 157), formed from the groups $H_i(X^i, X^{i-1}\cup Y^i)$ and computed there, fit into
$$
0\longrightarrow C_*^{\mathrm{cell}}(A\cap B,C\cap D)
\xrightarrow{(i_*,-j_*)}
C_*^{\mathrm{cell}}(A,C)\oplus C_*^{\mathrm{cell}}(B,D)
\xrightarrow{k_*+\ell_*}
C_*^{\mathrm{cell}}(X,Y)\longrightarrow0.
$$
These maps commute with the cellular boundary. They are exact in each degree: check one cell at a time. A cell outside $Y$ and in both $A$ and $B$ contributes the sequence
$$
0\longrightarrow\ZZ\xrightarrow{(1,-1)}\ZZ^2
\xrightarrow{(1,1)}\ZZ\longrightarrow0.
$$
A cell outside $Y$ and in only one of $A,B$ contributes $0\to0\to\ZZ\xrightarrow{\cong}\ZZ\to0$. If a cell is in $Y$ and in both $A,B$, it is in $C$, in $D$, or in both. In the first two cases the surviving copy in the middle is exactly the image of its copy in the intersection term; in the last case all three relative terms vanish. The remaining cells contribute zero. Hence the sequence is short exact.

The long exact homology sequence of this short exact sequence, that of Theorem 2.16 (p. 117), is
$$
\cdots\longrightarrow H_n(A\cap B,C\cap D)
\longrightarrow H_n(A,C)\oplus H_n(B,D)
\longrightarrow H_n(X,Y)
\longrightarrow H_{n-1}(A\cap B,C\cap D)
\longrightarrow\cdots .
$$
The relative cellular groups compute relative singular homology by Exercise 18 (p. 157), so this is a sequence in the homology of the pairs. The signs are the same difference and sum signs as in Exercise 38 (p. 158). In particular this gives the required relative Mayer--Vietoris sequence under the printed hypotheses $A=B$ or $C=D$, which are the cases in which the inclusion hypotheses $C\subset A$ and $D\subset B$ hold with the intersection of the two rows identified; the sequence of p. 153 is the case $C=D$.
:::
