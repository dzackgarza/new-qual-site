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
For class functions $\chi,\psi\colon G\to\CC$, let
$$
\inner{\chi}{\psi}=\frac1{\abs{G}}\sum_{g\in G}\chi(g)\overline{\psi(g)},
$$
and let $\chi_1,\ldots,\chi_r$ be the irreducible characters of $G$, the characters of the irreducible representations $V_1,\ldots,V_r$.

::: pf

::: {.pf-step #row}

(Row orthogonality) $\inner{\chi_i}{\chi_j}=\delta_{ij}$, and $\chi_1,\ldots,\chi_r$ form an orthonormal basis of the space of complex class functions on $G$.

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

:::

::: pf-step

If $V$ is a representation with character $\chi_V$, then $V_i$ occurs in $V$ with multiplicity $\inner{\chi_V}{\chi_i}$; in particular $V_i$ is a constituent of $V$ exactly when $\inner{\chi_V}{\chi_i}>0$.

::: pf-proof

By Maschke's theorem, $V\cong\bigoplus_j V_j^{\oplus m_j}$ for some multiplicities $m_j\ge0$. Characters are additive on direct sums, so $\chi_V=\sum_j m_j\chi_j$, and step [](#row){.pf-ref} gives $\inner{\chi_V}{\chi_i}=\sum_j m_j\delta_{ji}=m_i$.

:::

:::

:::

:::
