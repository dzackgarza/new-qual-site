---
schema: qual/card@1
id: P-ALGF09F
kind: problem
title: "A matrix with A^3 = A decomposes C^n into a direct sum of three subspaces"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 6 of the official UCSD Algebra Qualifying Examination, Fall 2009; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that the minimal polynomial divides t(t-1)(t+1), hence is squarefree over C, and identified the three direct summands with the eigenspaces for 1, -1, and 0.
---

::: {.problem}
Let $n \geq 1$ and consider the ring $M_n(\mathbb{C})$ of $n \times n$ matrices with coefficients in $\mathbb{C}$.
Suppose that $A \in M_n(\mathbb{C})$ satisfies $A^3 = A$.
Let $V = \mathbb{C}^n$, an $n$-dimensional vector space over $\mathbb{C}$.
Thinking of the elements of $V$ as column vectors, consider the linear transformation $\phi: V \to V$ defined by left multiplication by the matrix $A$.
Prove that $V$ decomposes into a direct sum of three $\mathbb{C}$-linear subspaces, say $V = U_1 \oplus U_2 \oplus U_3$, such that given $v \in V$ with $v = u_1 + u_2 + u_3$ where $u_i \in U_i$, then $\phi(v) = u_1 - u_2$.
:::

::: {.solution}
The matrix identity
\[
A^3=A
\]
is equivalent to
\[
A(A-I)(A+I)=0.
\]

<1>1. The minimal polynomial of $A$ divides
\[
t(t-1)(t+1).
\]
::: {.proof}
Let $m_A(t)$ be the minimal polynomial of $A$.
Since
\[
A^3-A=0,
\]
the polynomial
\[
t^3-t=t(t-1)(t+1)
\]
annihilates $A$.
By the defining property of the minimal polynomial,
\[
m_A(t)\mid t(t-1)(t+1).
\]
:::

<1>2. The operator $A$ is diagonalizable over $\mathbb C$, with possible eigenvalues only $1,-1,0$.
::: {.proof}
The polynomial
\[
t(t-1)(t+1)
\]
splits over $\mathbb C$ into three distinct linear factors.
By <1>1, the minimal polynomial $m_A$ also splits into distinct linear factors.
A linear operator over a field is diagonalizable if and only if its minimal polynomial splits into distinct linear factors.
Therefore $A$ is diagonalizable.
Its eigenvalues are roots of $m_A$, hence belong to
\[
\{1,-1,0\}.
\]
:::

<1>3. Define
\[
U_1:=\ker(A-I),
\qquad
U_2:=\ker(A+I),
\qquad
U_3:=\ker A.
\]
Then
\[
V=U_1\oplus U_2\oplus U_3.
\]
::: {.proof}
By <1>2, $A$ is diagonalizable and its only possible eigenvalues are $1,-1,0$.
A diagonalizable operator is the direct sum of its eigenspaces.
The eigenspaces corresponding to $1,-1,0$ are exactly
\[
\ker(A-I),
\qquad
\ker(A+I),
\qquad
\ker A.
\]
If one of these eigenvalues does not occur, the corresponding eigenspace is simply $0$.
Hence
\[
V=U_1\oplus U_2\oplus U_3.
\]
:::

<1>4. For $v=u_1+u_2+u_3$ with $u_i\in U_i$, one has
\[
\phi(v)=u_1-u_2.
\]
::: {.proof}
By definition of the three eigenspaces,
\[
Au_1=u_1,
\qquad
Au_2=-u_2,
\qquad
Au_3=0.
\]
Since $\phi$ is left multiplication by $A$,
\[
\phi(v)
=A(u_1+u_2+u_3)
=Au_1+Au_2+Au_3
=u_1-u_2.
\]
This is exactly the required decomposition and action formula.
:::
:::
