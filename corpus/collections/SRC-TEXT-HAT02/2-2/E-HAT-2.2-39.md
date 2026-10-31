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
---

::: {.problem}
Use the preceding exercise to derive relative Mayer–Vietoris sequences for CW pairs $(X, Y) = (A \cup B, C \cup D)$ with $A = B$ or $C = D$.
:::

::: {.solution}
Give $X$ a CW structure for which $A$, $B$, $C$, and $D$ are subcomplexes, with $C\subset A$ and $D\subset B$. The cellular relative chain groups fit into
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

The long exact homology sequence of this short exact sequence is
$$
\cdots\longrightarrow H_n(A\cap B,C\cap D)
\longrightarrow H_n(A,C)\oplus H_n(B,D)
\longrightarrow H_n(X,Y)
\longrightarrow H_{n-1}(A\cap B,C\cap D)
\longrightarrow\cdots .
$$
The signs are the same difference and sum signs as in Exercise 38. In particular this is the required relative Mayer--Vietoris sequence when $A=B$ or $C=D$.
:::
