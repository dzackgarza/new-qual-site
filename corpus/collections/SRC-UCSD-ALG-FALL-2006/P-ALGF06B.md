---
schema: qual/card@1
id: P-ALGF06B
kind: problem
title: "Existence and uniqueness of polar decomposition"
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
  note: Checked against Question 1.2 of the official UCSD Algebra Qualifying Examination, Fall 2006; the local statement matches the source, including the unconditional uniqueness claim.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: "The sourced uniqueness claim is false for singular A. The solution gives an explicit counterexample and proves the corrected theorem: H is always unique, while U is unique exactly when A has full column rank."
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks for a unique U and a unique H, which is false for rank-deficient A. The statement now asks for existence, uniqueness of H, and uniqueness of U exactly when A has rank n.
---

::: {.problem}
Given $A \in M_{m,n}$ with $m \geq n$, prove that there exist $U \in M_{m,n}$ with orthonormal columns and a Hermitian positive semidefinite $H \in M_n$ such that $A = UH$.
Prove that $H$ is unique, and that $U$ is unique if and only if $A$ has rank $n$.
(State in detail any auxiliary results that you use.)
:::


::: {.solution}
::: pf

::: {.pf-step #psd-square-root-unique}
A positive semidefinite matrix has a unique positive semidefinite square root.

::: pf-proof
Let $B$ be Hermitian positive semidefinite.
By the spectral theorem there are a unitary matrix $Q$ and numbers $\mu_1,\ldots,\mu_n\ge0$ such that
\[
B=Q\operatorname{diag}(\mu_1,\ldots,\mu_n)Q^*.
\]
Hence
\[
B^{1/2}:=Q\operatorname{diag}(\sqrt{\mu_1},\ldots,\sqrt{\mu_n})Q^*
\]
is Hermitian positive semidefinite and satisfies $(B^{1/2})^2=B$.

For uniqueness, suppose $C$ is Hermitian positive semidefinite and $C^2=B$.
Then $CB=C^3=BC$, so every eigenspace of $B$ is $C$-invariant.
On the $\mu$-eigenspace of $B$, the restriction of $C$ is positive semidefinite and its square is $\mu I$.
The spectral theorem applied to that restriction shows that every eigenvalue is the nonnegative number $\sqrt\mu$.
Thus $C=\sqrt\mu I$ on each eigenspace of $B$, so $C=B^{1/2}$.
:::

:::

::: pf-step
In every factorization $A=UH$ with $U^*U=I_n$ and $H\ge0$, one has
\[
H=(A^*A)^{1/2}.
\]

::: pf-proof
Indeed,
\[
A^*A=H U^*UH=H^2.
\]
By step [](#psd-square-root-unique){.pf-ref}, $H$ is the unique positive semidefinite square root of $A^*A$.
Thus the factor $H$ is unique whenever such a factorization exists.
:::

:::

::: {.pf-step #existence}
Such a factorization exists for every $A\in M_{m,n}$ with $m\ge n$.

::: pf-proof
Set
\[
H:=(A^*A)^{1/2},
\qquad
K:=\ker H.
\]
Since $H^2=A^*A$,
\[
\|Hv\|^2
=\langle H^2v,v\rangle
=\langle A^*Av,v\rangle
=\|Av\|^2,
\]
so
\[
K=\ker A.
\]

On $K^\perp$, define a map first on vectors of the form $Hv$ by
\[
U_0(Hv):=Av.
\]
The restriction $H\vert_{K^\perp}$ is injective and maps $K^\perp$ onto $K^\perp$, so this defines a linear map
\[
U_0:K^\perp\longrightarrow \operatorname{Ran}A.
\]
Moreover, for $v\in K^\perp$,
\[
\|U_0(Hv)\|=\|Av\|=\|Hv\|,
\]
so $U_0$ is an isometry.

Write $r=\operatorname{rank}A$.
Then
\[
\dim K=n-r,
\qquad
\dim(\operatorname{Ran}A)^\perp=m-r\ge n-r.
\]
Choose an isometric embedding
\[
V:K\longrightarrow(\operatorname{Ran}A)^\perp
\]
and define $U$ to equal $U_0$ on $K^\perp$ and $V$ on $K$.
The two image subspaces are orthogonal, so $U$ is an isometry $\CC^n\to\CC^m$, equivalently $U^*U=I_n$.
Finally, $Hv\in K^\perp$ for every $v$, and therefore
\[
UHv=U_0Hv=Av.
\]
Thus $A=UH$.
:::

:::

::: pf-step
The factor $U$ is unique exactly when $A$ has full column rank.

::: pf-proof
If $\operatorname{rank}A=n$, then $H$ is invertible, so every factorization satisfies
\[
U=AH^{-1}.
\]
Hence $U$ is unique.

Conversely, if $\operatorname{rank}A<n$, then $K=\ker A\neq0$.
In the construction of step [](#existence){.pf-ref}, choose an isometric embedding $V:K\to(\operatorname{Ran}A)^\perp$.
Replacing $V$ by $-V$ gives a distinct isometric extension of $U_0$, hence a distinct matrix $U$, while $UH=A$ is unchanged because $H$ vanishes on $K$.
Therefore $U$ is not unique.
:::

:::

:::
:::
