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
---

::: {.problem}
Let $G$ be a finite group and work with finite-dimensional complex representations. State the character orthogonality relations and explain how characters detect irreducible constituents.
:::

::: {.solution}
For class functions $\chi,\psi:G\to\CC$, define
\[
\langle\chi,\psi\rangle
=\frac1{|G|}\sum_{g\in G}\chi(g)\overline{\psi(g)}.
\]

If $\chi_1,\ldots,\chi_r$ are the irreducible characters of $G$, then the row orthogonality relations are
\[
\langle\chi_i,\chi_j\rangle=\delta_{ij}.
\]
Equivalently, irreducible characters form an orthonormal basis of the space of complex class functions.

The column orthogonality relation says that for $g,h\in G$,
\[
\sum_{i=1}^r \chi_i(g)\overline{\chi_i(h)}
=
\begin{cases}
|C_G(g)|,&g\text{ and }h\text{ are conjugate},\\
0,&\text{otherwise}.
\end{cases}
\]

Now let $V$ be a representation with character $\chi_V$. Complete reducibility gives
\[
V\cong\bigoplus_i m_i V_i,
\]
where $V_i$ has irreducible character $\chi_i$. Taking characters,
\[
\chi_V=\sum_i m_i\chi_i.
\]
By orthogonality,
\[
m_i=\langle\chi_V,\chi_i\rangle.
\]
Thus an irreducible representation $V_i$ occurs in $V$ exactly when
\[
\langle\chi_V,\chi_i\rangle>0,
\]
and the inner product gives its multiplicity.
:::
