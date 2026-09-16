---
schema: qual/card@1
id: P-APASP08I
kind: problem
title: "Schur function expansion via Littlewood-Richardson rule"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
  - Littlewood-Richardson Rule
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Compute the Schur function expansion of $s_{2,2} \times s_{2,1}$ by constructing the standard tableaux yielded by the Littlewood-Richardson rule.

**(a)** Check your result by means of the SF package.

**(b)** Give a representation-theoretic interpretation of the coefficients in this expansion.
:::

::: {.solution}
By the Littlewood--Richardson rule,
\[
s_{(2,2)}s_{(2,1)}
=
\sum_{\lambda\vdash7}c^{\lambda}_{(2,2),(2,1)}s_\lambda,
\]
where $c^{\lambda}_{(2,2),(2,1)}$ counts Littlewood--Richardson tableaux of skew shape $\lambda/(2,2)$ and content $(2,1)$, i.e. two entries $1$ and one entry $2$.

There is exactly one such tableau for each of the following six outer shapes. Listing only the three boxes of the skew diagram and their entries:
\[
\begin{array}{c|c}
\lambda & \text{entries in }\lambda/(2,2)\\ \hline
(4,3) & (1,3)\mapsto1,\ (1,4)\mapsto1,\ (2,3)\mapsto2\\
(4,2,1) & (1,3)\mapsto1,\ (1,4)\mapsto1,\ (3,1)\mapsto2\\
(3,3,1) & (1,3)\mapsto1,\ (2,3)\mapsto2,\ (3,1)\mapsto1\\
(3,2,2) & (1,3)\mapsto1,\ (3,1)\mapsto1,\ (3,2)\mapsto2\\
(3,2,1,1) & (1,3)\mapsto1,\ (3,1)\mapsto1,\ (4,1)\mapsto2\\
(2,2,2,1) & (3,1)\mapsto1,\ (3,2)\mapsto1,\ (4,1)\mapsto2.
\end{array}
\]
In each case rows are weakly increasing, columns are strictly increasing, and the reverse row-reading word is a lattice word. No other outer shape admits such a filling.

Hence
\[
\boxed{
\begin{aligned}
s_{(2,2)}s_{(2,1)}
={}&s_{(4,3)}+s_{(4,2,1)}+s_{(3,3,1)}\\
&+s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}.
\end{aligned}}
\]
Every coefficient is $1$.

A convenient independent check uses
\[
s_{(2,1)}=s_{(2)}s_{(1)}-s_{(3)}.
\]
Pieri gives
\[
s_{(2,2)}s_{(2)}
=s_{(4,2)}+s_{(3,2,1)}+s_{(2,2,2)}.
\]
Multiplying by $s_{(1)}$ gives
\[
\begin{aligned}
s_{(2,2)}s_{(2)}s_{(1)}
={}&s_{(5,2)}+s_{(4,3)}+2s_{(4,2,1)}+s_{(3,3,1)}\\
&+2s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)},
\end{aligned}
\]
while
\[
s_{(2,2)}s_{(3)}
=s_{(5,2)}+s_{(4,2,1)}+s_{(3,2,2)}.
\]
Subtracting reproduces the boxed expansion.

For part (b), the coefficient
\[
c^\lambda_{(2,2),(2,1)}
\]
is the multiplicity of the irreducible $S_7$-module $V_\lambda$ in
\[
\operatorname{Ind}_{S_4\times S_3}^{S_7}
\bigl(V_{(2,2)}\boxtimes V_{(2,1)}\bigr).
\]
Thus the expansion says that this induced representation is multiplicity-free and decomposes as
\[
\boxed{
V_{(4,3)}\oplus V_{(4,2,1)}\oplus V_{(3,3,1)}\oplus
V_{(3,2,2)}\oplus V_{(3,2,1,1)}\oplus V_{(2,2,2,1)}.
}
\]
:::
