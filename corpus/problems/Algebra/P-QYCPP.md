---
schema: qual/card@1
id: P-QYCPP
kind: problem
title: Sylow $p$-subgroups of $\GL_3(\FF_p)$, their conjugates, and their normalizers
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $G = \operatorname{GL}_3(\mathbb{F}_p)$ for $p$ prime.
(1) What is the order of $G$, and what is the order of a Sylow $p$-subgroup?
(2) Give the standard matrix form for the canonical Sylow $p$-subgroup $P \le G$.
(3) Give the matrix form for the normalizer $N_G(P)$ and compute the number of conjugates (Sylow $p$-subgroups) $n_p$.
(4) Explain conjugacy of Sylow $p$-subgroups in terms of complete flags / eigenspaces.
:::

::: solution
We have
\[
|\operatorname{GL}_3(\mathbb F_p)|=(p^3-1)(p^3-p)(p^3-p^2)
=p^3(p-1)^3(p+1)(p^2+p+1).
\]
Thus a Sylow $p$-subgroup has order $p^3$. The standard one is
\[
P=\left\{\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}:a,b,c\in\mathbb F_p\right\}.
\]
Its normalizer is the upper-triangular Borel subgroup
\[
B=\left\{\begin{pmatrix}d_1&a&b\\0&d_2&c\\0&0&d_3\end{pmatrix}:d_i\in\mathbb F_p^\times\right\},
\]
so
\[
|B|=p^3(p-1)^3,\qquad
n_p=[G:B]=(p+1)(p^2+p+1).
\]

The subgroup $P$ is the unipotent radical of the stabilizer of the standard complete flag
\[
0<\langle e_1\rangle<\langle e_1,e_2\rangle<\mathbb F_p^3.
\]
Conjugating $P$ corresponds to conjugating this flag. Hence Sylow $p$-subgroups are in bijection with complete flags. Their number is
\[
(p^2+p+1)(p+1),
\]
matching the index calculation.
:::
