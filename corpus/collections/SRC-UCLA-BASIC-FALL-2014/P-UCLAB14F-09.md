---
schema: qual/card@1
id: P-UCLAB14F-09
kind: problem
title: Separating the spectra of $B$ and $A+B$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 9. Let $A\neq0$ be an $n\times n$ complex matrix. Prove that there is a matrix $B$ such that $B$ and $A+B$ have no eigenvalues in common.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $A$ is invertible, the choice
$$
\boxed{B=0}
$$
works.


::: pf-proof

The zero matrix has only the eigenvalue $0$.
If $A$ is invertible, then $0$ is not an eigenvalue of
$$
A+B=A.
$$
Thus the spectra are disjoint.

:::

:::

::: {.pf-step #s1-2}

Assume henceforth that $A$ is singular and nonzero.
Then there exists a vector $v$ such that
$$
Av\ne0
$$
and $Av$ is not a scalar multiple of $v$.


::: pf-proof

Suppose no such vector existed.
Then every nonzero vector $v$ with $Av\ne0$ would satisfy
$$
Av=\lambda_v v.
$$
Vectors in $\ker A$ also satisfy
$$
Av=0\cdot v.
$$
Thus every vector would be an eigenvector of $A$.
A linear map for which every vector is an eigenvector must be a scalar multiple of the identity: for linearly independent $u,w$ with
$$
Au=\lambda u,
\qquad
Aw=\mu w,
$$
the vector $u+w$ must also be an eigenvector, and comparing coefficients forces
$$
\lambda=\mu.
$$
Hence
$$
A=\lambda I.
$$
Since $A$ is singular, $\lambda=0$, contradicting $A\ne0$.
Therefore the required $v$ exists.

:::

:::

::: {.pf-step #s1-3}

Choose a basis
$$
e_1,\ldots,e_n
$$
such that
$$
e_1=v
$$
and the coefficient of $e_n$ in $Ae_1$ is nonzero.


::: pf-proof

By step [](#s1-2){.pf-ref}, the vectors
$$
v,\ Av
$$
are linearly independent.
Choose
$$
e_1=v,
\qquad
e_n=Av,
$$
and extend them to a basis of $\CC^n$.
In this basis,
$$
Ae_1=e_n,
$$
so the matrix entry in row $n$, column $1$ is
$$
a_{n1}=1\ne0.
$$

:::

:::

::: {.pf-step #s1-4}

In the basis from step [](#s1-3){.pf-ref}, let
$$
N=
\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&0&1\\
0&\cdots&\cdots&0&0
\end{pmatrix}.
$$
Then $N$ is nilpotent and has only the eigenvalue $0$.


::: pf-proof

The matrix $N$ is strictly upper triangular.
Hence
$$
N^n=0.
$$
Any eigenvalue $\lambda$ satisfies
$$
\lambda^n=0,
$$
so $\lambda=0$.

:::

:::

::: {.pf-step #s1-5}

The polynomial
$$
p(t)=\det(A+tN)
$$
is not identically zero.


::: pf-proof

Consider the coefficient of
$$
t^{n-1}
$$
in the determinant expansion.
To obtain a term of degree $n-1$ in $t$, select the $tN$ entries
$$
(1,2),(2,3),\ldots,(n-1,n)
$$
from the first $n-1$ rows.
These use columns
$$
2,3,\ldots,n.
$$
The remaining row $n$ must then use column $1$, contributing the entry
$$
a_{n1}.
$$
There is exactly one such permutation.
Thus the coefficient of $t^{n-1}$ is
$$
\pm a_{n1}.
$$
By step [](#s1-3){.pf-ref},
$$
a_{n1}\ne0.
$$
Hence $p(t)$ is a nonzero polynomial.

:::

:::

::: {.pf-step #s1-6}

There exists $t\in\CC$ such that
$$
A+tN
$$
is invertible.


::: pf-proof

The nonzero polynomial $p(t)$ from step [](#s1-5){.pf-ref} has only finitely many roots.
Choose $t$ that is not one of them.
Then
$$
\det(A+tN)
=
p(t)
\ne0.
$$
Thus $A+tN$ is invertible.

:::

:::

::: {.pf-step #s1-7}

For such a $t$, set
$$
\boxed{B=tN}.
$$
Then $B$ and $A+B$ have no eigenvalues in common.


::: pf-proof

By step [](#s1-4){.pf-ref}, $B=tN$ is nilpotent and therefore has only the eigenvalue $0$.
By step [](#s1-6){.pf-ref},
$$
A+B=A+tN
$$
is invertible, so it does not have eigenvalue $0$.
Hence
$$
\operatorname{spec}(B)
\cap
\operatorname{spec}(A+B)
=
\varnothing.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} handles the invertible case, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} handle the singular nonzero case.

:::

:::

:::
