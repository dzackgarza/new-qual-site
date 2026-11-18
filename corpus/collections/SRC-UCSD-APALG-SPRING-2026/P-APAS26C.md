---
schema: qual/card@1
id: P-APAS26C
kind: problem
title: Maximal singular vectors of a $G$-map form a subrepresentation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Singular Values
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The adjoint-equivariance is now derived (take adjoints, use unitarity to replace the adjoint by the inverse, replace g by g^{-1}), the positivity facts about A*A and about sigma_1^2 I - A*A are proved, and the key equivalence "||Av|| = sigma_1 ||v|| iff v is in the top eigenspace" is established through the positive semidefinite square root B of sigma_1^2 I - A*A, since <(sigma_1^2 I - A*A)v,v> = ||Bv||^2 vanishes exactly when Bv = 0. The prose had asserted that equivalence from the spectral theorem without the argument. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Let $(V, \varphi)$ and $(W, \psi)$ be finite-dimensional unitary representations of a group $G$.
Let $A \in \operatorname{Hom}_G(V, W)$ be a $G$-equivariant linear map with operator norm $\sigma_1 > 0$.
Prove that
$$
V_1 = \{v \in V : \norm{Av} = \sigma_1 \norm{v}\}
$$
is a subrepresentation of $(V, \varphi)$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Let $\sigma_1=\norm A>0$ be the operator norm and write $\inner{\cdot}{\cdot}$ for the inner product of $V$, with $A^*:W\to V$ the adjoint.

::: pf

::: {.pf-step #adjoint}
$A^*\psi(g)=\varphi(g)A^*$ for every $g\in G$.

::: pf-proof
$A\varphi(g)=\psi(g)A$ by equivariance. Taking adjoints gives $\varphi(g)^*A^*=A^*\psi(g)^*$, and unitarity gives $\varphi(g)^*=\varphi(g)^{-1}$ and $\psi(g)^*=\psi(g)^{-1}$. So $\varphi(g)^{-1}A^*=A^*\psi(g)^{-1}$; replacing $g$ by $g^{-1}$ gives the claim.
:::

:::

::: {.pf-step #commute}
$A^*A$ commutes with $\varphi(g)$ for every $g$, so it is $G$-equivariant as an operator on $V$.

::: pf-proof
$A^*A\varphi(g)=A^*\psi(g)A=\varphi(g)A^*A$ by step [](#adjoint){.pf-ref} and equivariance of $A$.
:::

:::

::: {.pf-step #psd}
$A^*A$ is Hermitian and positive semidefinite, $\sigma_1^2$ is its largest eigenvalue, and $\sigma_1^2I-A^*A$ is positive semidefinite.

::: pf-proof
$\inner{A^*Av}{v}=\inner{Av}{Av}=\norm{Av}^2\ge0$ and $\inner{A^*Av}{w}=\overline{\inner{A^*Aw}{v}}$, so $A^*A$ is positive semidefinite and Hermitian; by the spectral theorem for such an operator it is diagonalisable with nonnegative real eigenvalues, and $\max_v\inner{A^*Av}{v}/\norm v^2=\max\norm{Av}^2/\norm v^2=\norm A^2=\sigma_1^2$ over $v\ne0$. Hence every eigenvalue of $A^*A$ is at most $\sigma_1^2$, and $\inner{(\sigma_1^2I-A^*A)v}{v}=\sigma_1^2\norm v^2-\norm{Av}^2\ge0$.
:::

:::

::: {.pf-step #kernel}
Let $B$ be the positive semidefinite square root of $\sigma_1^2I-A^*A$. Then for every $v$,
$$
\norm{Av}=\sigma_1\norm v\iff Bv=0\iff(\sigma_1^2I-A^*A)v=0 .
$$

::: pf-proof
$\norm{Av}^2=\inner{A^*Av}{v}$, so $\norm{Av}=\sigma_1\norm v$ is equivalent to $\inner{(\sigma_1^2I-A^*A)v}{v}=0$. Since $B$ is Hermitian and $B^2=\sigma_1^2I-A^*A$,
$$
\inner{(\sigma_1^2I-A^*A)v}{v}=\inner{B^2v}{v}=\inner{Bv}{Bv}=\norm{Bv}^2,
$$
which vanishes exactly when $Bv=0$. Finally $Bv=0$ implies $(\sigma_1^2I-A^*A)v=B^2v=0$, and conversely $(\sigma_1^2I-A^*A)v=0$ implies $\norm{Bv}^2=0$, so $Bv=0$.
:::

:::

::: {.pf-step #subrep}
$V_1=\ker(\sigma_1^2I-A^*A)$ is a $G$-stable linear subspace of $V$.

::: pf-proof
$V_1$ equals the eigenspace of $A^*A$ for $\sigma_1^2$ by step [](#kernel){.pf-ref}, and a kernel of a linear map is a linear subspace. If $v\in V_1$ and $g\in G$, then $A^*A\varphi(g)v=\varphi(g)A^*Av=\varphi(g)\sigma_1^2v=\sigma_1^2\varphi(g)v$ by step [](#commute){.pf-ref}, so $\varphi(g)v\in V_1$. Thus $V_1$ is invariant under $\varphi(g)$ for every $g$, which is to say that it is a subrepresentation of $(V,\varphi)$.
:::

:::

:::
:::
