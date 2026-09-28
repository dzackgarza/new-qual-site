---
schema: qual/card@1
id: P-APASP08D
kind: problem
title: "Garnir polynomial expansion for a tableau"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
  - Tableaux
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Give the expansion of the Garnir polynomial $G_T(x)$ corresponding to the tableau
$$
T = \begin{array}{ccc}
7 & & \\
2 & 3 & 5 \\
1 & 4 & 6
\end{array}
$$
in terms of the Garnir polynomials of the standard tableaux of the same shape.
:::

::: {.solution}
For a tableau $T$, the Garnir (Specht) polynomial is alternating in the entries of each column. In particular, interchanging two entries in one column changes the sign of the polynomial.

Starting from
\[
T=
\begin{array}{ccc}
7&&\\
2&3&5\\
1&4&6
\end{array},
\]
interchange $3$ and $4$ in the second column, and interchange $5$ and $6$ in the third column. This gives
\[
S=
\begin{array}{ccc}
7&&\\
2&4&6\\
1&3&5
\end{array}.
\]
The rows of $S$ increase from left to right and its columns increase from bottom to top, so $S$ is standard.

Each of the two column transpositions contributes a factor of $-1$. Hence
\[
G_T=(-1)^2G_S=G_S.
\]
Therefore the expansion in the standard Garnir basis consists of a single term:
\[
\boxed{
G_T(x)=
G_{\left[\begin{smallmatrix}
7&&\\
2&4&6\\
1&3&5
\end{smallmatrix}\right]}(x).
}
\]

Equivalently, writing the column factors explicitly, both polynomials equal
\[
(x_1-x_2)(x_1-x_7)(x_2-x_7)(x_3-x_4)(x_5-x_6),
\]
up to the common global sign determined by the convention for ordering entries inside each column.
:::
