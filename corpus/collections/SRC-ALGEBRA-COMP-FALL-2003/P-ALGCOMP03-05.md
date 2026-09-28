---
schema: qual/card@1
id: P-ALGCOMP03-05
kind: problem
title: Characterizations of nilpotent matrices
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the nilpotence-index argument, characteristic-polynomial conclusion, and the converse trace criterion via Newton identities.
---

::: {.problem}
Recall that a square matrix is nilpotent if $A^p=0$ for some $p>0$.

(a) If $A$ is an $n\times n$ complex nilpotent matrix, prove that $A^n=0$.

(b) Prove that the characteristic polynomial of a nilpotent matrix $A$ of order $n$ is $\lambda^n$.

(c) Let $A$ be a matrix of order $n$.
Prove that $A$ is nilpotent if and only if
\[
\operatorname{tr}(A^p)=0\qquad (p=1,\ldots,n).
\]
:::


::: {.solution}
<1>1. If \(A\) is nilpotent, then \(A^n=0\).
::: {.proof}
Let \(r>0\) be the least integer such that
\[
A^r=0.
\]
Then \(A^{r-1}\ne0\), so there exists \(v\in\mathbb C^n\) with
\[
A^{r-1}v\ne0.
\]
We claim that
\[
v,Av,A^2v,\dots,A^{r-1}v
\]
are linearly independent.

Suppose
\[
\sum_{j=0}^{r-1}c_jA^jv=0
\]
with not all \(c_j\) zero, and let \(j_0\) be the least index with \(c_{j_0}\ne0\). Multiply by \(A^{r-1-j_0}\). Every term with \(j>j_0\) then contains a power \(A^m\) with \(m\ge r\), hence vanishes. We obtain
\[
c_{j_0}A^{r-1}v=0,
\]
contradicting \(A^{r-1}v\ne0\).

Thus there are \(r\) linearly independent vectors in \(\mathbb C^n\), so
\[
r\le n.
\]
Since \(A^r=0\), it follows that
\[
\boxed{A^n=0}.
\]
:::

<1>2. A nilpotent \(n\times n\) matrix has characteristic polynomial \(\lambda^n\).
::: {.proof}
Let \(\mu\) be any eigenvalue of \(A\), with eigenvector \(w\ne0\). Since \(A\) is nilpotent, \(A^m=0\) for some \(m>0\). Therefore
\[
0=A^mw=\mu^m w.
\]
Because \(w\ne0\), we get
\[
\mu=0.
\]
Thus every eigenvalue of \(A\) is \(0\). Over \(\mathbb C\), the characteristic polynomial splits and has degree \(n\), so
\[
\boxed{\chi_A(\lambda)=\lambda^n}.
\]
:::

<1>3. \(A\) is nilpotent if and only if \(\operatorname{tr}(A^p)=0\) for \(1\le p\le n\).
::: {.proof}
If \(A\) is nilpotent, then by <1>2 all eigenvalues are zero. Hence every \(A^p\) has all eigenvalues zero, and therefore
\[
\operatorname{tr}(A^p)=0
\]
for every \(p\ge1\).

Conversely, assume
\[
\operatorname{tr}(A^p)=0
\qquad (p=1,\dots,n).
\]
Let the eigenvalues of \(A\), counted with algebraic multiplicity, be
\[
\lambda_1,\dots,\lambda_n.
\]
Triangularizing \(A\) over \(\mathbb C\) shows that the diagonal entries of \(A^p\) are \(\lambda_1^p,\dots,\lambda_n^p\). Thus
\[
s_p:=\sum_{i=1}^n\lambda_i^p
=\operatorname{tr}(A^p)=0
\qquad (1\le p\le n).
\]

Write \(e_k\) for the \(k\)-th elementary symmetric polynomial in the \(\lambda_i\), with \(e_0=1\). Newton's identities give, for \(1\le k\le n\),
\[
k e_k=\sum_{j=1}^k(-1)^{j-1}e_{k-j}s_j.
\]
Since every \(s_j=0\), induction on \(k\) yields
\[
e_1=e_2=\cdots=e_n=0.
\]
Hence
\[
\chi_A(t)
=t^n-e_1t^{n-1}+e_2t^{n-2}-\cdots+(-1)^ne_n
=t^n.
\]
By the Cayley--Hamilton theorem,
\[
A^n=0.
\]
Therefore \(A\) is nilpotent.

Thus
\[
\boxed{A\text{ is nilpotent}\iff \operatorname{tr}(A^p)=0\text{ for }p=1,\dots,n}.
\]
:::
:::
