---
schema: qual/card@1
id: P-K5JBF
kind: problem
title: Isomorphism type of $\mathbb{Z}^3/\langle(0,4,2),(-1,-4,-1),(0,0,-2)\rangle$
classification:
  areas:
  - prelim
  topics:
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Form an abelian group $M$ as the quotient of $\mathbb{Z}^3$ by the elements $(0,4,2)$, $(-1,-4,-1)$, and $(0,0,-2)$.
What abelian group is $M$?
(That is, find its isomorphism type).
:::

::: {.solution}
Let $A$ be the integer matrix whose rows are the three relations:
$$
A = \begin{pmatrix} 0 & 4 & 2 \\ -1 & -4 & -1 \\ 0 & 0 & -2 \end{pmatrix}.
$$
Then $M=\ZZ^3/\ZZ^3A$, where $\ZZ^3A$ is the row space of $A$.

<1>1. The Smith normal form of $A$ is $\operatorname{diag}(1, 2, 4)$.
::: {.proof}
Integer row operations replace the relations by another generating set of the same subgroup, and invertible integer column operations change the basis of $\ZZ^3$; neither changes the isomorphism type of $M$.
Subtract $4$ times the first column from the second and the first column from the third, then negate the second row. The rows become $(0,4,2)$, $(1,0,0)$, $(0,0,-2)$.
The remaining $2\times2$ block in the last two columns is $\begin{pmatrix}4&2\\0&-2\end{pmatrix}$. Subtracting twice its second column from its first gives $\begin{pmatrix}0&2\\4&-2\end{pmatrix}$; adding its first row to its second gives $\begin{pmatrix}0&2\\4&0\end{pmatrix}$; swapping its columns gives $\operatorname{diag}(2,4)$.
Since $1\mid2\mid4$, this is the Smith normal form. As a check, $\abs{\det A}=8=1\cdot2\cdot4$.
:::

<1>2. $M \cong \boxed{\ZZ/2 \oplus \ZZ/4}$.
::: {.proof}
By step <1>1, $M\cong\ZZ/1\oplus\ZZ/2\oplus\ZZ/4$, and $\ZZ/1=0$.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 gives the isomorphism type.
:::
:::
