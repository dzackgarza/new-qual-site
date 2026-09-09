---
schema: qual/card@1
id: P-NAGQY
kind: problem
title: Character table
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
For a finite group $G$, what is its complex character table? In what fields do its entries lie?
:::

::: {.solution}
Choose representatives
\[
g_1,\ldots,g_r
\]
of the conjugacy classes of $G$, and choose the irreducible complex characters
\[
\chi_1,\ldots,\chi_r.
\]
The **character table** is the matrix
\[
(\chi_i(g_j))_{i,j}.
\]
Rows are indexed by irreducible complex representations and columns by conjugacy classes.

If $g\in G$ has order $m$, then in any finite-dimensional complex representation the eigenvalues of $\rho(g)$ are $m$-th roots of unity. Hence
\[
\chi(g)=\operatorname{tr}(\rho(g))
\]
is a sum of $m$-th roots of unity. Therefore every character value is an algebraic integer lying in a cyclotomic field.

If $e$ is the exponent of $G$, then every element order divides $e$, so the entire character table has entries in
\[
\QQ(\zeta_e).
\]
Since $e\mid |G|$ for finite groups, one may also use the larger field
\[
\QQ(\zeta_{|G|}).
\]
The entries need not be rational or real in general.
:::
