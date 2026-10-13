---
schema: qual/card@1
id: P-BKS77-8
kind: problem
title: Similarity classes with characteristic polynomial $(x-1)^5(x+1)$ and minimal polynomial $(x-1)^2(x+1)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Find as long a list as possible of pairwise nonsimilar real matrices such that every matrix in the list has characteristic polynomial
\[
(x-1)^5(x+1)
\]
and minimal polynomial
\[
(x-1)^2(x+1).
\]
:::

::: {.solution}
Write
$$
J_2(1)\coloneqq
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
$$

<1>1. For any matrix satisfying the hypotheses, the generalized eigenspace for eigenvalue $-1$ is one-dimensional and contributes exactly one Jordan block
$$
[-1].
$$

::: {.proof}
The factor $(x+1)$ occurs to the first power in the characteristic polynomial, so the algebraic multiplicity of $-1$ is $1$. Hence its entire primary component has dimension $1$. The factor $(x+1)$ also occurs to the first power in the minimal polynomial, so the unique block has size $1$.
:::

<1>2. The Jordan blocks for eigenvalue $1$ have total size $5$, every block has size at most $2$, and at least one block has size $2$.

::: {.proof}
The factor $(x-1)^5$ in the characteristic polynomial gives algebraic multiplicity $5$, so the $1$-primary Jordan blocks have total size $5$. The exponent $2$ of $(x-1)$ in the minimal polynomial is the size of the largest Jordan block for eigenvalue $1$. Hence no block has size larger than $2$, and some block has size exactly $2$.
:::

<1>3. There are exactly two possible multisets of Jordan-block sizes for eigenvalue $1$:
$$
2+2+1
\qquad\text{or}\qquad
2+1+1+1.
$$

::: {.proof}
By step <1>2, the block sizes form a partition of $5$ using only parts $1$ and $2$, with at least one part $2$. If there are two parts of size $2$, the remaining size is $1$, giving $2+2+1$. If there is one part of size $2$, the remaining size $3$ must be three parts of size $1$, giving $2+1+1+1$. More than two parts of size $2$ would already have total size at least $6$.
:::

<1>4. The two matrices
$$
\boxed{
A_1=
\operatorname{diag}\bigl(J_2(1),J_2(1),[1],[-1]\bigr)
}
$$
and
$$
\boxed{
A_2=
\operatorname{diag}\bigl(J_2(1),[1],[1],[1],[-1]\bigr)
}
$$
both satisfy the required characteristic and minimal polynomials.

::: {.proof}
For $A_1$, the eigenvalue $1$ occurs in blocks of sizes $2,2,1$, so its contribution to the characteristic polynomial is $(x-1)^5$ and the largest such block has size $2$. For $A_2$, the corresponding block sizes are $2,1,1,1$, with the same conclusions. In both matrices the remaining block is $[-1]$, contributing $(x+1)$ to the characteristic polynomial and exponent $1$ to the minimal polynomial. Hence both matrices have
$$
\chi_A(x)=(x-1)^5(x+1)
$$
and
$$
m_A(x)=(x-1)^2(x+1).
$$
:::

<1>5. The matrices $A_1$ and $A_2$ are not similar.

::: {.proof}
Jordan form is unique up to permutation of Jordan blocks. The $1$-eigenspace Jordan block multisets are
$$
\{2,2,1\}
\qquad\text{and}\qquad
\{2,1,1,1\},
$$
which are different. Therefore the matrices are not similar.
:::

<1>6. Every real matrix satisfying the hypotheses is similar to exactly one of $A_1,A_2$.

::: {.proof}
All roots of the characteristic polynomial are real, so the Jordan form is defined over $\mathbb R$. Step <1>1 fixes the $-1$ block, and step <1>3 shows that the $1$-blocks have exactly one of the two listed shapes. Thus no other similarity class is possible. Uniqueness follows from uniqueness of Jordan form.
:::

<1>7. Hence a longest possible list has length
$$
\boxed{2},
$$
and one such list is $\{A_1,A_2\}$.

::: {.proof}
Step <1>4 gives two admissible matrices, step <1>5 shows they are pairwise nonsimilar, and step <1>6 shows the list is exhaustive.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 answers the problem.
:::
:::
