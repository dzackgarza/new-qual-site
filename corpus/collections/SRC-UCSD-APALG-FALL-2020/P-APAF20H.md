---
schema: qual/card@1
id: P-APAF20H
kind: problem
title: Orthogonal complement of a $G$-invariant subspace is $G$-invariant
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $U\colon G\to\mathrm{U}(H)$ be a unitary representation of a compact group $G$ on a Hilbert space $H$.
Prove that, if $K$ is a closed subspace of $H$ invariant under the action of $G$, so is $K^\perp$.
:::

::: {.solution}

::: pf

::: {.pf-step #adjoint}

For every $g\in G$, $U(g)^*=U(g^{-1})$.

::: pf-proof

$U(g)$ is unitary, so $U(g)^*=U(g)^{-1}$, and $U(g)^{-1}=U(g^{-1})$ because $U$ is a homomorphism.

:::

:::

::: pf-qed

Let $v\in K^\perp$, $g\in G$ and $w\in K$. By step [](#adjoint){.pf-ref}, $\langle U(g)v,w\rangle=\langle v,U(g^{-1})w\rangle$. Since $K$ is $G$-invariant, $U(g^{-1})w\in K$, so this inner product is $0$. As $w\in K$ is arbitrary, $U(g)v\in K^\perp$; hence $K^\perp$ is $G$-invariant. ($K^\perp$ is closed for any subspace $K$.)

:::

:::
:::
