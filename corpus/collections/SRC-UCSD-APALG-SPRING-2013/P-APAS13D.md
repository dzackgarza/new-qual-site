---
schema: qual/card@1
id: P-APAS13D
kind: problem
title: Unique positive semidefinite square root; orthogonal projection via $\widehat{X}=X|X|^{-1}$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Singular Values
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
(a) Prove that if $A\in M_n$ is positive semidefinite, then there exists a unique positive semidefinite $X$ such that $A=X^2$.

(b) Let $X$ be a matrix whose columns define a basis for a subspace $\mathcal{X}\subset\mathbb{C}^n$.
Consider the matrix $\widehat{X}=X|X|^{-1}$, where $|X|$ denotes the modulus of $X$, i.e., $|X|=(X^HX)^{1/2}$.
Prove that $\widehat{X}$ exists and that $\widehat{X}\widehat{X}^H$ is an orthogonal projection onto $\mathcal{X}$.
:::

::: {.solution}
For part (a), since \(A\) is Hermitian positive semidefinite, the spectral theorem gives a unitary matrix \(U\) and nonnegative real numbers \(\lambda_1,\ldots,\lambda_n\) such that
\[
A=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^H.
\]
Define
\[
X=U\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})U^H.
\]
Then \(X\) is Hermitian positive semidefinite and \(X^2=A\), so existence holds.

For uniqueness, let \(Y\) be any positive semidefinite matrix with \(Y^2=A\). Since \(Y\) is Hermitian, it is unitarily diagonalizable, and every eigenvalue of \(Y\) is nonnegative. Moreover,
\[
AY=Y^2Y=Y^3=YY^2=YA,
\]
so \(Y\) preserves every eigenspace \(E_\lambda=\ker(A-\lambda I)\) of \(A\). On \(E_\lambda\),
\[
Y^2=\lambda I.
\]
The restriction \(Y|_{E_\lambda}\) is Hermitian positive semidefinite, hence all its eigenvalues are nonnegative square roots of \(\lambda\); therefore
\[
Y|_{E_\lambda}=\sqrt\lambda\,I.
\]
Thus \(Y\) agrees with the matrix \(X\) constructed above on every eigenspace of \(A\), and hence \(Y=X\). Therefore the positive semidefinite square root is unique.

For part (b), let \(X\in M_{n,r}(\mathbb C)\), where its \(r\) columns form a basis of \(\mathcal X\). Thus \(X\) has full column rank. For every nonzero \(v\in\mathbb C^r\),
\[
v^HX^HXv=\|Xv\|_2^2>0.
\]
Hence \(X^HX\) is positive definite. By part (a),
\[
|X|=(X^HX)^{1/2}
\]
is positive definite and therefore invertible. Thus \(\widehat X=X|X|^{-1}\) is well-defined.

Since \(|X|\) is Hermitian,
\[
\widehat X^H\widehat X
=|X|^{-1}X^HX|X|^{-1}
=|X|^{-1}|X|^2|X|^{-1}
=I_r.
\]
So the columns of \(\widehat X\) are orthonormal. Also right multiplication by the invertible matrix \(|X|^{-1}\) does not change the column space, hence
\[
\operatorname{col}(\widehat X)=\operatorname{col}(X)=\mathcal X.
\]
Set
\[
P=\widehat X\widehat X^H.
\]
Then
\[
P^H=P
\]
and
\[
P^2=\widehat X(\widehat X^H\widehat X)\widehat X^H
=\widehat X\widehat X^H=P.
\]
Thus \(P\) is a Hermitian idempotent. Its image is
\[
\operatorname{im}P=\operatorname{col}(\widehat X)=\mathcal X,
\]
because \(P\widehat X=\widehat X\). A Hermitian idempotent is the orthogonal projection onto its image. Therefore
\[
\boxed{\widehat X\widehat X^H}
\]
is the orthogonal projection onto \(\mathcal X\).
:::
