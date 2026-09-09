---
schema: qual/card@1
id: P-ALGS04H
kind: problem
title: "Factorization of the third cyclotomic polynomial over Z_7 and rational canonical forms"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $\Phi = X^2 + X + 1$ be the third cyclotomic polynomial.

(a) Prove that $\Phi$ is reducible over $\mathbb{Z}_7$ and give a complete factorization.

(b) Determine the possible rational canonical forms for any element $A \in \operatorname{GL}(2, \mathbb{Z}_7)$ which satisfies $A^3 = I$.
:::

::: {.solution}
<1>1. Over \(\mathbf F_7\),
\[
\Phi_3(X)=X^2+X+1=(X-2)(X-4).
\]
::: {.proof}
One has \(2^2+2+1=7\equiv0\pmod7\) and \(4^2+4+1=21\equiv0\pmod7\). Since \(2\neq4\) in \(\mathbf F_7\) and \(\Phi_3\) is monic of degree \(2\), this gives the complete factorization.
:::

<1>2. Therefore
\[
X^3-1=(X-1)(X-2)(X-4)
\]
in \(\mathbf F_7[X]\), with three distinct roots.
::: {.proof}
Use \(X^3-1=(X-1)\Phi_3(X)\) and <1>1. The elements \(1,2,4\) are distinct modulo \(7\).
:::

<1>3. If \(A\in\operatorname{GL}_2(\mathbf F_7)\) satisfies \(A^3=I\), then its minimal polynomial \(m_A(X)\) divides \(X^3-1\). Hence \(A\) is diagonalizable over \(\mathbf F_7\), and its eigenvalues belong to \(\{1,2,4\}\).
::: {.proof}
The equality \(A^3-I=0\) implies \(m_A\mid X^3-1\). By <1>2, \(X^3-1\) is squarefree and splits over \(\mathbf F_7\), so the same is true of \(m_A\). A matrix whose minimal polynomial splits with no repeated root is diagonalizable.
:::

<1>4. If \(A\) has only one eigenvalue \(a\in\{1,2,4\}\), then \(A=aI_2\). These give the three rational canonical forms
\[
I_2,\qquad 2I_2,\qquad 4I_2.
\]
::: {.proof}
By <1>3, \(A\) is diagonalizable. A diagonalizable \(2\times2\) matrix with a single eigenvalue \(a\) is similar to \(\operatorname{diag}(a,a)=aI_2\), which is already its rational canonical form.
:::

<1>5. If \(A\) has two distinct eigenvalues \(a,b\in\{1,2,4\}\), then its characteristic and minimal polynomials are both
\[
(X-a)(X-b).
\]
Its rational canonical form is the single companion block \(C((X-a)(X-b))\).
::: {.proof}
A \(2\times2\) matrix with two distinct eigenvalues has characteristic polynomial \((X-a)(X-b)\). Both eigenvalues occur in the minimal polynomial, so the minimal polynomial is the same degree-\(2\) polynomial. Thus there is one invariant factor, equal to the characteristic polynomial, and rational canonical form is its companion matrix.
:::

<1>6. With the companion convention
\[
C(X^2+c_1X+c_0)=
\begin{pmatrix}
0&-c_0\\
1&-c_1
\end{pmatrix},
\]
the three remaining rational canonical forms are
\[
C((X-1)(X-2))=
\begin{pmatrix}0&5\\1&3\end{pmatrix},
\]
\[
C((X-1)(X-4))=
\begin{pmatrix}0&3\\1&5\end{pmatrix},
\]
and
\[
C((X-2)(X-4))=
\begin{pmatrix}0&6\\1&6\end{pmatrix}.
\]
::: {.proof}
Modulo \(7\),
\[
(X-1)(X-2)=X^2+4X+2,
\]
\[
(X-1)(X-4)=X^2+2X+4,
\]
and
\[
(X-2)(X-4)=X^2+X+1.
\]
Substitution into the displayed companion-matrix convention gives the three matrices.
:::

<1>7. These six forms exhaust all possibilities.
::: {.proof}
By <1>3, the multiset of two eigenvalues is a size-\(2\) multiset drawn from \(\{1,2,4\}\). There are exactly three repeated-eigenvalue cases, handled in <1>4, and three unordered distinct-eigenvalue cases, handled in <1>5--<1>6.
:::
:::

