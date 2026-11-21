---
schema: qual/card@1
id: P-ZCY6S
kind: problem
title: Character orthogonality and detecting irreducible constituents
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof. Two steps that stated the row and column orthogonality relations of
    the character table with no justification now derive them, the second from the first by the standard
    argument that a square matrix with $YY^*=I$ also satisfies $Y^*Y=I$. The mathematics is unchanged;
    the relations are standard consequences of Schur's lemma, which is named where it is used rather than
    proved. Nothing in the statement was changed.

---

::: {.problem}
Let $G$ be a finite group and work with finite-dimensional complex representations. State the character orthogonality relations and explain how characters detect irreducible constituents.
:::

::: {.solution}
For class functions $\chi,\psi\colon G\to\CC$, let
$$
\inner{\chi}{\psi}=\frac1{\abs{G}}\sum_{g\in G}\chi(g)\overline{\psi(g)},
$$
and let $\chi_1,\ldots,\chi_r$ be the irreducible characters of $G$, the characters of the irreducible representations $V_1,\ldots,V_r$.

::: pf

::: {.pf-step #row}

(Row orthogonality) $\inner{\chi_i}{\chi_j}=\delta_{ij}$, and $\chi_1,\ldots,\chi_r$ form an orthonormal basis of the space of complex class functions on $G$.


::: pf-proof
This is the orthogonality of irreducible characters: $\langle\chi_i,\chi_j\rangle=\delta_{ij}$ follows from Schur's lemma applied to the spaces of intertwining operators, and the irreducible characters span the class functions because their number equals the number of conjugacy classes.
:::

:::

::: pf-step

(Column orthogonality) For $g,h\in G$,
$$
\sum_{i=1}^r \chi_i(g)\overline{\chi_i(h)}
=
\begin{cases}
\abs{C_G(g)},&g\text{ and }h\text{ are conjugate},\\
0,&\text{otherwise}.
\end{cases}
$$


::: pf-proof
Row orthogonality says that the normalized character table $Y$, with entries $\chi_i(g)\sqrt{\abs{C(g)}/\abs{G}}$ indexed by conjugacy classes, satisfies $YY^*=I$; a square matrix with that property also satisfies $Y^*Y=I$, which is the displayed relation, and $\abs{G}/\abs{C(g)}=\abs{C_G(g)}$.
:::

:::

::: pf-step

If $V$ is a representation with character $\chi_V$, then $V_i$ occurs in $V$ with multiplicity $\inner{\chi_V}{\chi_i}$; in particular $V_i$ is a constituent of $V$ exactly when $\inner{\chi_V}{\chi_i}>0$.

::: pf-proof

By Maschke's theorem, $V\cong\bigoplus_j V_j^{\oplus m_j}$ for some multiplicities $m_j\ge0$. Characters are additive on direct sums, so $\chi_V=\sum_j m_j\chi_j$, and step [](#row){.pf-ref} gives $\inner{\chi_V}{\chi_i}=\sum_j m_j\delta_{ji}=m_i$.

:::

:::

:::

:::
