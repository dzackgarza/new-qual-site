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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source asked for a unique U with orthonormal columns for every A, false for A = 0; the statement now asks for existence of U, uniqueness of H, and uniqueness of U when A has rank n.'
---

::: {.problem}
Given $A \in M_{m,n}$ with $m \geq n$, prove that there exist $U \in M_{m,n}$ with orthonormal columns and a unique Hermitian positive semidefinite $H \in M_n$ such that $A = UH$, and that $U$ is also unique when $A$ has rank $n$.
(State in detail any auxiliary results used without proof.)
:::

::: {.solution}
We use the standard fact that a Hermitian positive semidefinite matrix has a unique Hermitian positive semidefinite square root.

::: pf

::: {.pf-step #s3}

Put $H=(A^*A)^{1/2}$ and $K=\ker H$. Then $K=\ker A$ and $\operatorname{im}H=K^\perp$.

::: pf-proof

For every $x$,
$$
\|Ax\|^2=\langle A^*Ax,x\rangle=\langle H^2x,x\rangle=\|Hx\|^2,
$$
so $Ax=0$ iff $Hx=0$. Since $H$ is Hermitian, $\operatorname{im}H=(\ker H)^\perp$.

:::

:::

::: pf-step

Define $U_0:K^\perp\to\CC^m$ by $U_0(Hx)=Ax$. This is well-defined and isometric.

::: pf-proof

If $Hx=Hy$, then $x-y\in K=\ker A$, so $Ax=Ay$. Also $\|U_0(Hx)\|=\|Ax\|=\|Hx\|$.

:::

:::

::: pf-step

Extend $U_0$ to an isometry $U:\CC^n\to\CC^m$. Then $U$ has orthonormal columns and $A=UH$.

::: pf-proof

Extend an orthonormal basis of $K^\perp$ to one of $\CC^n$, and extend its $U_0$-image to an orthonormal $n$-frame in $\CC^m$; this is possible because $m\ge n$. Then $UH x=U_0(Hx)=Ax$.

:::

:::

::: pf-step

The factor $H$ is unique.

::: pf-proof

If $A=U_1H_1$ with $U_1^*U_1=I$ and $H_1\ge0$, then
$$
A^*A=H_1U_1^*U_1H_1=H_1^2.
$$
Hence $H_1$ is the positive semidefinite square root of $A^*A$, so $H_1=H$.

:::

:::

::: pf-step

If $A$ has rank $n$, then $H$ is invertible and $U=AH^{-1}$, so $U$ is unique.

::: pf-proof

Rank $n$ is equivalent to $\ker H=0$ by step [](#s3){.pf-ref}.

:::

:::

:::

:::
