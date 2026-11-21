---
schema: qual/card@1
id: P-APAS13D
kind: problem
title: Unique positive semidefinite square root; orthogonal projection via $\widehat{X}=X\operatorabs{X}^{-1}$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Singular Values
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, four for part (a) and three for part (b), each carrying a `pf-proof`; the
    two statements and every displayed formula are unchanged. Cited by number only: the
    spectral theorem for Hermitian matrices, and part (a) itself for the existence of the
    square root in part (b). Checked: that positive semidefiniteness forces the eigenvalues to
    be nonnegative, that $U^HU=I$ gives $X^2=A$, that a Hermitian operator on $E_\lambda$ whose
    square is $\lambda I$ is $\sqrt\lambda I$, that the columns of $X$ being a basis makes
    $X^HX$ positive definite, and that the kernel of a Hermitian idempotent is the orthogonal
    complement of its image.
---

::: {.problem}
(a) Prove that if $A\in M_n$ is positive semidefinite, then there exists a unique positive semidefinite $X$ such that $A=X^2$.

(b) Let $X$ be a matrix whose columns define a basis for a subspace $\mathcal{X}\subset\CC^n$.
Consider the matrix $\widehat{X}=X\operatorabs{X}^{-1}$, where $\operatorabs{X}$ denotes the modulus of $X$, i.e., $\operatorabs{X}=(X^HX)^{1/2}$.
Prove that $\widehat{X}$ exists and that $\widehat{X}\widehat{X}^H$ is an orthogonal projection onto $\mathcal{X}$.
:::

::: {.solution}

::: pf

::: pf-step

(a) Since $A$ is Hermitian positive semidefinite, the spectral theorem gives a unitary $U$ and nonnegative reals $\lambda_1,\ldots,\lambda_n$ with
$$
A=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^H.
$$

::: pf-proof

A positive semidefinite matrix is by definition Hermitian, so the spectral theorem for Hermitian matrices gives an orthonormal basis of eigenvectors and real eigenvalues; arranging them in $U$ gives the displayed factorisation. Positive semidefiniteness says $v^HAv\ge0$ for every $v$, and with $v$ an eigenvector this reads $\lambda_i\norm{v}^2\ge0$, so each $\lambda_i\ge0$.

:::

:::

::: pf-step

(a) With
$$
X=U\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})U^H,
$$
the matrix $X$ is Hermitian positive semidefinite and $X^2=A$.

::: pf-proof

$X$ is Hermitian because $U^H$ is the conjugate transpose of $U$ and the middle factor is real diagonal. Its eigenvalues are the nonnegative numbers $\sqrt{\lambda_i}$, so $X$ is positive semidefinite. And $X^2=U\operatorname{diag}(\lambda_1,\dots,\lambda_n)U^HU\operatorname{diag}(\dots)U^H=U\operatorname{diag}(\lambda_1,\dots,\lambda_n)U^H=A$, using $U^HU=I$ and that a diagonal matrix commutes with itself.

:::

:::

::: pf-step

(a) If $Y$ is positive semidefinite with $Y^2=A$, then $AY=YA$, so $Y$ preserves every eigenspace $E_\lambda=\ker(A-\lambda I)$ of $A$.

::: pf-proof

$AY=Y^2Y=Y^3=YY^2=YA$ by associativity. If $v\in E_\lambda$ then $A(Yv)=YA v=\lambda Yv$, so $Yv\in E_\lambda$; that is $YE_\lambda\subseteq E_\lambda$.

:::

:::

::: pf-step

(a) On $E_\lambda$ one has $Y^2=\lambda I$, and $Y\restriction_{E_\lambda}=\sqrt\lambda\,I$; hence $Y=X$.

::: pf-proof

For $v\in E_\lambda$ we have $Y^2v=Av=\lambda v$, so the restriction of $Y$ to the invariant subspace $E_\lambda$ is a Hermitian operator whose square is $\lambda I$. Its eigenvalues are therefore nonnegative square roots of $\lambda$, that is $\sqrt\lambda$, and being Hermitian it is diagonalisable; a diagonalisable operator all of whose eigenvalues equal $\sqrt\lambda$ is $\sqrt\lambda I$. The eigenspaces $E_\lambda$ span $\CC^n$, so $Y$ agrees with $X$ — whose value on $E_\lambda$ is $\sqrt\lambda I$ by step 2 — on a basis, hence $Y=X$.

:::

:::

::: pf-step

(b) Let $X\in M_{n,r}(\CC)$ have columns forming a basis of $\mathcal X$. Then $X$ has full column rank, and for $v\ne0$,
$$
v^HX^HXv=\norm{Xv}_2^2>0,
$$
so $X^HX$ is positive definite and $\operatorabs{X}=(X^HX)^{1/2}$ is invertible; hence $\widehat X=X\operatorabs{X}^{-1}$ exists.

::: pf-proof

Columns forming a basis of $\mathcal X$ are linearly independent, so $X$ has rank $r$ and $Xv\ne0$ for $v\ne0$. Then $v^HX^HXv=(Xv)^H(Xv)=\norm{Xv}_2^2>0$, so $X^HX$ is positive definite, in particular invertible, and by part (a) it has the positive definite square root $\operatorabs X$, whose eigenvalues are the positive square roots of those of $X^HX$; a positive definite matrix is invertible, so $\operatorabs X^{-1}$ exists and $\widehat X$ is defined.

:::

:::

::: pf-step

(b) Since $\operatorabs{X}$ is Hermitian,
$$
\widehat X^H\widehat X
=\operatorabs{X}^{-1}X^HX\operatorabs{X}^{-1}
=\operatorabs{X}^{-1}\operatorabs{X}^2\operatorabs{X}^{-1}
=I_r,
$$
so the columns of $\widehat X$ are orthonormal, and $\operatorname{col}(\widehat X)=\operatorname{col}(X)=\mathcal X$.

::: pf-proof

$\operatorabs X$ is Hermitian and $\operatorabs X^2=X^HX$, so $\widehat X^H=(\operatorabs X^{-1})^HX^H=\operatorabs X^{-1}X^H$ by the definition of $\widehat X$; multiplying by $X\operatorabs X^{-1}$ gives the displayed chain. The entries $(\widehat X^H\widehat X)_{ij}$ are the inner products of the columns of $\widehat X$, so the columns are orthonormal. Right multiplication by the invertible $\operatorabs X^{-1}$ does not change the column space, since $X=X\operatorabs X^{-1}\operatorabs X$ and $\widehat X\operatorabs X=X$.

:::

:::

::: pf-step

(b) With $P=\widehat X\widehat X^H$ one has $P^H=P$ and
$$
P^2=\widehat X(\widehat X^H\widehat X)\widehat X^H=\widehat X\widehat X^H=P,
$$
and $\operatorname{im}P=\operatorname{col}(\widehat X)=\mathcal X$ because $P\widehat X=\widehat X$; so $P$ is the orthogonal projection onto $\mathcal X$.

::: pf-proof

$P^H=(\widehat X^H)^H\widehat X^H=P$ and the displayed computation uses $\widehat X^H\widehat X=I_r$ from step 6. $\operatorname{im}P=\operatorname{col}(\widehat X)$ because $(Pv)$ is a combination of columns of $\widehat X$, and $P\widehat X=\widehat X\widehat X^H\widehat X=\widehat X$ shows the column space is contained in the image. A Hermitian idempotent is the orthogonal projection onto its image: its kernel is the orthogonal complement of the image, since $Pw=0$ implies $(w,Pv)=(Pw,v)=0$, and on the image it acts as the identity. With the image equal to $\mathcal X$, $P$ is the orthogonal projection onto $\mathcal X$.

:::

:::

:::
:::
