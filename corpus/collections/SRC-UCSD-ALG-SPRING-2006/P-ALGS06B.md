---
schema: qual/card@1
id: P-ALGS06B
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
Given $A \in M_{m,n}$ with $m \geq n$, prove that there exists a unique $U \in M_{m,n}$ with orthonormal columns, and a unique Hermitian positive semidefinite $H \in M_n$ such that $A = UH$.
(State in detail any auxiliary results used without proof.)
:::

::: {.solution}
<1>1. The uniqueness assertion for $U$ is false as printed. If $A=0$, then $H=0$, while every $m\times n$ matrix with orthonormal columns satisfies $A=UH$.
::: {.proof}
Since $m\ge n$, such matrices exist and are not unique.
:::

<1>2. The correct statement is that $H=(A^*A)^{1/2}$ is uniquely determined, there exists an isometry $U:\mathbb C^n\to\mathbb C^m$ with $A=UH$, and $U$ is unique exactly when $A$ has full column rank.
::: {.proof}
We use the standard fact that a Hermitian positive semidefinite matrix has a unique Hermitian positive semidefinite square root.
:::

<1>3. Put $H=(A^*A)^{1/2}$ and $K=\ker H$. Then $K=\ker A$ and $\operatorname{im}H=K^\perp$.
::: {.proof}
For every $x$,
\[
\|Ax\|^2=\langle A^*Ax,x\rangle=\langle H^2x,x\rangle=\|Hx\|^2,
\]
so $Ax=0$ iff $Hx=0$. Since $H$ is Hermitian, $\operatorname{im}H=(\ker H)^\perp$.
:::

<1>4. Define $U_0:K^\perp\to\mathbb C^m$ by $U_0(Hx)=Ax$. This is well-defined and isometric.
::: {.proof}
If $Hx=Hy$, then $x-y\in K=\ker A$, so $Ax=Ay$. Also $\|U_0(Hx)\|=\|Ax\|=\|Hx\|$.
:::

<1>5. Extend $U_0$ to an isometry $U:\mathbb C^n\to\mathbb C^m$. Then $U$ has orthonormal columns and $A=UH$.
::: {.proof}
Extend an orthonormal basis of $K^\perp$ to one of $\mathbb C^n$, and extend its $U_0$-image to an orthonormal $n$-frame in $\mathbb C^m$; this is possible because $m\ge n$. Then $UH x=U_0(Hx)=Ax$.
:::

<1>6. The factor $H$ is unique.
::: {.proof}
If $A=U_1H_1$ with $U_1^*U_1=I$ and $H_1\ge0$, then
\[
A^*A=H_1U_1^*U_1H_1=H_1^2.
\]
Hence $H_1$ is the positive semidefinite square root of $A^*A$, so $H_1=H$.
:::

<1>7. If $A$ has full column rank, then $H$ is invertible and $U=AH^{-1}$, so $U$ is unique.
::: {.proof}
Full column rank is equivalent to $\ker H=0$ by <1>3.
:::

<1>8. If $A$ is rank-deficient, then $U$ is not unique.
::: {.proof}
Now $K\ne0$. The map $U$ is fixed on $K^\perp$ but may be changed on $K$ by choosing a different orthonormal extension; since $H$ vanishes on $K$, all such extensions still satisfy $UH=A$.
:::
:::
