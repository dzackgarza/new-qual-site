---
schema: qual/card@1
id: E-TK5YY
kind: exercise
title: Cayley-Hamilton theorem, cokernels of integer matrices, and diagonalizability
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Diagonalization
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
- Prove the Cayley-Hamilton theorem.

- Prove that the minimal polynomial divides the characteristic polynomial.

- Prove that the cokernel of $A\in \mat(n\times n, \ZZ)$ is finite $\iff \det A \neq 0$, and show that in this case $\abs{\coker(A)} = \abs{\det(A)}$.

- Show that a nilpotent operator is diagonalizable.

- Show that if $A,B$ are diagonalizable and $[A, B] = 0$ then $A,B$ are simultaneously diagonalizable.

- Does diagonalizable imply invertible?
  The converse?

- Does diagonalizable imply distinct eigenvalues?

- Show that if a matrix is diagonalizable, its minimal polynomial is squarefree.

- Show that a matrix representing a linear map $T:V\to V$ is diagonalizable iff $V$ is a direct sum of eigenspaces $V = \bigoplus_i \ker(T -\lambda_i I)$.

- Show that if $\theset{\vector v_i}$ is a basis for $V$ where $\dim(V) = n$ and $T(\vector v_i) = \vector v_{i+1 \mod n}$ then $T$ is diagonalizable with minimal polynomial $x^n-1$.

- Show that if the minimal polynomial of a linear map $T$ is irreducible, then every $T\dash$invariant subspace has a $T\dash$invariant complement.
:::

::: {.solution}
<1>1. Proof of the Cayley–Hamilton Theorem and minimal polynomial divisibility:
<2>1. Let $p(t) = \det(tI - A) = \sum_{j=0}^n c_j t^j \in F[t]$ be the characteristic polynomial of $A \in M_n(F)$.
::: {.proof}
definition of characteristic polynomial.
:::
<2>2. Consider the adjugate matrix $B(t) = \operatorname{adj}(tI - A) \in M_n(F[t])$. Its entries are polynomials in $t$ of degree $\le n - 1$, so write $B(t) = \sum_{j=0}^{n-1} B_j t^j$ with $B_j \in M_n(F)$.
::: {.proof}
adjugate formula for matrix inverse.
:::
<2>3. By Cramer’s rule, $(tI - A) B(t) = \det(tI - A) I = p(t) I$.
::: {.proof}
fundamental property of the adjugate matrix.
:::
<2>4. Expanding $(tI - A) \sum_{j=0}^{n-1} B_j t^j = \sum_{j=0}^n c_j I t^j$ and equating powers of $t$:
\[
B_{n-1} = c_n I, \quad B_{j-1} - A B_j = c_j I \ (1 \le j \le n-1), \quad -A B_0 = c_0 I.
\]
::: {.proof}
equating coefficients of polynomials with matrix coefficients.
:::
<2>5. Multiply each equation on the left by $A^j$ and sum over $j = 0, \dots, n$:
\[
p(A) = c_0 I + c_1 A + \cdots + c_n A^n = -A B_0 + A(B_0 - A B_1) + \cdots + A^n B_{n-1} = 0.
\]
Thus $p(A) = 0$ (Cayley–Hamilton Theorem).
::: {.proof}
telescoping sum of matrix equations.
:::
<2>6. Since the minimal polynomial $m_A(x)$ generates the ideal $\{f \in F[x] : f(A) = 0\}$, $p(A) = 0$ implies $m_A(x) \mid p(x)$.
::: {.proof}
$F[x]$ is a PID.
:::

<1>2. Cokernel of integer matrices via Smith Normal Form:
<2>1. By the Smith Normal Form theorem, there exist $P, Q \in \operatorname{GL}_n(\mathbb{Z})$ such that $P A Q = D = \operatorname{diag}(d_1, \dots, d_n)$ with $d_i \in \mathbb{Z}_{\ge 0}$.
::: {.proof}
Smith Normal Form over the PID $\mathbb{Z}$.
:::
<2>2. Since $P, Q$ are isomorphisms of $\mathbb{Z}^n$, $\operatorname{coker}(A) \cong \operatorname{coker}(D) \cong \bigoplus_{i=1}^n \mathbb{Z}/d_i\mathbb{Z}$.
::: {.proof}
isomorphic presentation of quotients.
:::
<2>3. $\operatorname{coker}(A)$ is finite if and only if all $d_i \neq 0$, which holds if and only if $\det(D) = \prod d_i \neq 0 \iff \det(A) = (\det P)^{-1} \det(D) (\det Q)^{-1} \neq 0$.
::: {.proof}
$\mathbb{Z}/0\mathbb{Z} \cong \mathbb{Z}$ is infinite.
:::
<2>4. When $\det(A) \neq 0$, $|\operatorname{coker}(A)| = \prod_{i=1}^n |d_i| = |\det(D)| = |\det(A)|$ since $\det P, \det Q \in \{\pm 1\}$.
::: {.proof}
product of orders of cyclic groups.
:::

<1>3. Nilpotent operators, invertibility, and distinct eigenvalues:
<2>1. A nilpotent operator $N$ satisfies $N^k = 0$. Its only eigenvalue is $0$.
If $N$ is diagonalizable, $N$ is similar to $\operatorname{diag}(0, \dots, 0) = 0$, so $N = 0$.
Thus the only diagonalizable nilpotent operator is the zero operator.
::: {.proof}
a matrix similar to the zero matrix is zero.
:::
<2>2. Diagonalizability does not imply invertibility (e.g. $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ is diagonalizable but singular).
Invertibility does not imply diagonalizability (e.g. $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is invertible with $m_A(x) = (x-1)^2$, hence non-diagonalizable).
::: {.proof}
counterexamples.
:::
<2>3. Diagonalizability does not imply distinct eigenvalues (e.g. $I_n$ is diagonal with single eigenvalue $1$ of multiplicity $n$).
::: {.proof}
identity matrix.
:::

<1>4. Commuting diagonalizable operators and eigenspace decomposition:
<2>1. A linear map $T: V \to V$ is diagonalizable if and only if $V$ has a basis of eigenvectors, which is equivalent to $V = \bigoplus_i \ker(T - \lambda_i I)$.
::: {.proof}
definition of diagonalizability and linear independence of eigenvectors.
:::
<2>2. If $T$ is diagonalizable, its minimal polynomial $m_T(x) = \prod_{i=1}^k (x - \lambda_i)$ has distinct linear factors, hence is squarefree.
::: {.proof}
$T$ is diagonalizable $\iff$ minimal polynomial splits with distinct roots.
:::
<2>3. If $A, B$ are diagonalizable and $AB = BA$, then for each eigenspace $E_\lambda(A) = \ker(A - \lambda I)$ and $v \in E_\lambda(A)$:
\[
A(Bv) = B(Av) = B(\lambda v) = \lambda (Bv) \implies Bv \in E_\lambda(A).
\]
Thus $E_\lambda(A)$ is $B$-invariant.
::: {.proof}
commuting operators preserve eigenspaces.
:::
<2>4. Since $B$ is diagonalizable, its restriction $B|_{E_\lambda(A)}$ is diagonalizable, providing a basis of simultaneous eigenvectors for $V = \bigoplus E_\lambda(A)$.
::: {.proof}
restriction of diagonalizable operators to invariant subspaces is diagonalizable.
:::

<1>5. Cyclic permutation operator and irreducible minimal polynomial:
<2>1. For the cyclic shift $T(v_i) = v_{i+1 \pmod n}$, $T^n = I$, so $m_T(x) \mid (x^n - 1)$.
Since $\{v_1, T(v_1), \dots, T^{n-1}(v_1)\}$ is a basis, $\deg(m_T) \ge n$, so $m_T(x) = x^n - 1$.
Over $\mathbb{C}$, $x^n - 1$ has $n$ distinct roots $e^{2\pi i k/n}$, so $T$ is diagonalizable.
::: {.proof}
distinct roots of unity.
:::
<2>2. If $m_T(x)$ is irreducible over $F$, then the ring $E = F[x]/(m_T(x))$ is a field.
$V$ is an $E$-vector space via $T$. Every subspace of a vector space over a field has a complement, so every $T$-invariant subspace $W \subseteq V$ has a $T$-invariant complement $W'$.
::: {.proof}
$F[x]$-submodules of $V$ are $E$-subspaces of $V$.
:::

<1>6. Conclusion:
All statements are established. Q.E.D.
::: {.proof}
<1>1 through <1>5.
:::
:::
