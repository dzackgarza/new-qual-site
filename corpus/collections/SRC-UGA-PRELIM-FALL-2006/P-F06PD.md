---
schema: qual/card@1
id: P-F06PD
kind: problem
title: Dimension of $\operatorname{span}\{x^2+x+1,\,x^2+2x,\,x^2+2,\,x-1\}$ over $\mathbb{Q}$
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Consider the vector space of polynomials over $\mathbb{Q}$ spanned by $p_1(x) = x^2 + x + 1$, $p_2(x) = x^2 + 2x$, $p_3(x) = x^2 + 2$, $p_4(x) = x - 1$.
Find the dimension of this vector space.
:::

::: {.solution}
<1>1. Coordinate representation in standard basis:
<2>1. Represent polynomials in the standard basis $\{x^2, x, 1\}$ of the polynomial subspace $\mathbb{Q}_{\le 2}[x]$:
\[
p_1(x) = (1, 1, 1), \quad p_2(x) = (1, 2, 0), \quad p_3(x) = (1, 0, 2), \quad p_4(x) = (0, 1, -1).
\]
Proof: coordinate isomorphism $\mathbb{Q}_{\le 2}[x] \cong \mathbb{Q}^3$.
<2>2. Form the $4 \times 3$ matrix $A$ whose rows are the coordinate vectors of $p_1, p_2, p_3, p_4$:
\[
A = \begin{pmatrix}
1 & 1 & 1 \\
1 & 2 & 0 \\
1 & 0 & 2 \\
0 & 1 & -1
\end{pmatrix}.
\]
Proof: definition of row space.

<1>2. Row reduction and rank computation:
<2>1. Perform elementary row operations on $A$:
- $R_2 \leftarrow R_2 - R_1$: row becomes $(0, 1, -1)$.
- $R_3 \leftarrow R_3 - R_1$: row becomes $(0, -1, 1)$.
- $R_4$: $(0, 1, -1)$.
Proof: row operations preserve row space.
<2>2. Further reduce:
- $R_3 \leftarrow R_3 + R_2$: row becomes $(0, 0, 0)$.
- $R_4 \leftarrow R_4 - R_2$: row becomes $(0, 0, 0)$.
The row echelon form of $A$ is:
\[
\begin{pmatrix}
1 & 1 & 1 \\
0 & 1 & -1 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}.
\]
Proof: Gaussian elimination.
<2>3. There are exactly 2 non-zero pivot rows in the row echelon form, so $\operatorname{rank}(A) = 2$.
Explicitly:
\[
p_2(x) = p_1(x) + p_4(x), \qquad p_3(x) = p_1(x) - p_4(x).
\]
Proof: $(x^2 + x + 1) + (x - 1) = x^2 + 2x$ and $(x^2 + x + 1) - (x - 1) = x^2 + 2$.

<1>3. Conclusion:
The spanning set $\{p_1, p_2, p_3, p_4\}$ reduces to the linearly independent basis $\{x^2 + x + 1, x - 1\}$.
Thus the dimension of the subspace is $\dim(\operatorname{span}\{p_1, p_2, p_3, p_4\}) = 2$. Q.E.D.
Proof: <1>1 and <1>2.
:::
