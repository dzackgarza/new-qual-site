---
schema: qual/card@1
id: P-UCLAB02W-11
kind: problem
title: Triangularization in an orthonormal basis
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 11 of the official UCLA Basic Examination, Winter 2002 PDF. The source calls the matrix "upper triangular" but then specifies $A_{ij}=0$ for $i<j$, which is the standard lower-triangular index condition.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Records the terminology/index mismatch. Standard Schur triangularization gives the upper-triangular convention $A_{ij}=0$ for $i>j$; reversing an orthonormal basis converts it to the printed lower-triangular convention.
---

::: {.problem}
Let $V$ be a finite-dimensional complex inner-product space and let $T:V\to V$ be linear.
Prove that there exists an ordered orthonormal basis of $V$ such that the matrix $A=(A_{ij})$ of $T$ in this basis is, in the wording of the source, "upper triangular," with
\[
A_{ij}=0
\qquad\text{if }i<j.
\]

Hint: first show that if $S:V\to V$ is linear and $W\subset V$ is a subspace, then $W$ is $S$-invariant if and only if $W^\perp$ is $S^*$-invariant.
:::

::: {.solution}
The source calls the requested matrix upper triangular while imposing $A_{ij}=0$ for $i<j$, which is the standard lower-triangular index condition. The proof first constructs the standard upper-triangular form and then reverses the basis order.

<1>1. For a linear map $S:V\to V$ and a subspace $W\subseteq V$, one has
$$
W\text{ is }S\text{-invariant}
\quad\Longleftrightarrow\quad
W^\perp\text{ is }S^*\text{-invariant}.
$$

::: {.proof}
Assume first that $S(W)\subseteq W$. If $y\in W^\perp$ and $w\in W$, then
$$
\langle w,S^*y\rangle
=
\langle Sw,y\rangle
=0,
$$
because $Sw\in W$. Hence $S^*y\in W^\perp$, so $W^\perp$ is $S^*$-invariant.

Conversely, assume $W^\perp$ is $S^*$-invariant. Applying the implication just proved to $S^*$ and the subspace $W^\perp$ shows that
$$
(W^\perp)^\perp
$$
is $(S^*)^*$-invariant. In finite dimension,
$$
(W^\perp)^\perp=W,
\qquad
(S^*)^*=S.
$$
Thus $W$ is $S$-invariant.
:::

<1>2. Every linear map on a nonzero finite-dimensional complex vector space has an eigenvector.

::: {.proof}
Let $R:V\to V$ be linear and let $n=\dim V>0$. The characteristic polynomial
$$
\det(\lambda I-R)
$$
has degree $n$ and therefore has a root $\lambda\in\CC$ by the fundamental theorem of algebra. Hence
$$
\det(\lambda I-R)=0,
$$
so $\lambda I-R$ has nontrivial kernel. Any nonzero vector in that kernel is an eigenvector of $R$.
:::

<1>3. Every linear map $T$ on a finite-dimensional complex inner-product space admits an ordered orthonormal basis in which its matrix is upper triangular in the standard sense, namely
$$
A_{ij}=0\qquad(i>j).
$$

::: {.proof}
Proceed by induction on $n=\dim V$.

If $n=0$ or $n=1$, the assertion is immediate.

Assume $n\ge2$ and the result is known in dimension $n-1$. By step <1>2, the adjoint $T^*$ has a unit eigenvector $e_n$. Let
$$
W=\CC e_n.
$$
Then $W$ is $T^*$-invariant. Apply step <1>1 with $S=T^*$: the orthogonal complement
$$
W^\perp
$$
is $T$-invariant. It has dimension $n-1$.

By the induction hypothesis, there is an ordered orthonormal basis
$$
e_1,\ldots,e_{n-1}
$$
of $W^\perp$ in which the matrix of $T|_{W^\perp}$ is upper triangular. Since $e_n$ is a unit vector orthogonal to $W^\perp$,
$$
e_1,\ldots,e_{n-1},e_n
$$
is an orthonormal basis of $V$.

For $j<n$, invariance of $W^\perp$ gives
$$
T(e_j)\in W^\perp=\operatorname{span}\{e_1,\ldots,e_{n-1}\},
$$
so the coefficient of $e_n$ in $T(e_j)$ is zero. Thus the last row has zero entries in columns $1,\ldots,n-1$. Together with upper triangularity of the restriction to $W^\perp$, this shows that the full matrix is upper triangular in the standard sense.
:::

<1>4. Reversing the basis in step <1>3 produces an orthonormal basis whose matrix satisfies the source's index condition
$$
A_{ij}=0\qquad(i<j).
$$

::: {.proof}
Let
$$
e_1,\ldots,e_n
$$
be the orthonormal basis from step <1>3, and let $A$ be the corresponding standard upper-triangular matrix. Consider the reversed ordered basis
$$
e_n,e_{n-1},\ldots,e_1.
$$
It remains orthonormal. If $P$ is the permutation matrix reversing the coordinate order, the matrix of $T$ in the reversed basis is
$$
P^{-1}AP=PAP.
$$
Reversing both row and column order carries entries below the diagonal to entries above the diagonal. Since $A_{ij}=0$ for $i>j$, the new matrix has zero entries for $i<j$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives an ordered orthonormal basis satisfying exactly the index condition printed in the source. Step <1>1 proves the auxiliary invariant-subspace criterion requested in the hint.
:::
:::
