---
schema: qual/card@1
id: P-APASP08H
kind: problem
title: "Representation-theoretic interpretation of a symmetric function identity"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Give a representation-theoretic interpretation of the identity
$$
\frac{\partial}{\partial p_1}p_1^n = n p_1^{n-1}.
$$
:::

::: solution
**Goal:** Interpret the power-sum derivative as a character operation removing one $1$-cycle.

<1> In the Frobenius characteristic map
$$
\operatorname{ch}:\mathrm{class\ functions\ of\ }S_n\to\Lambda,
$$
power sums are images of class sums: $p_\lambda$ corresponds to cycle type $\lambda$, and $p_1^n=p_{(1^n)}$ corresponds to $n$ fixed points.

<1> Let $X$ be the class function on $S_n$ with $\operatorname{ch}(X)=p_1^n$.
    This is the class function of the identity conjugacy class $(1^n)$.

<1> The Hall inner product satisfies
    $$
    \frac{\partial}{\partial p_1}
    \quad\text{adjoint to}\quad
    \times p_1.
    $$

<1> Differentiating $p_1^n$ gives
$$
\frac{\partial}{\partial p_1}p_1^n
=n p_1^{n-1}.
$$
    Combinatorially this is the $n$ choices of deleting one fixed point from a cycle type $(1^n)$, producing $(1^{n-1})$.

<1> Representation-theoretically, this is the restriction of class functions from $S_n$ to $S_{n-1}$ along the subgroup fixing one letter:
    $$
    X\downarrow^{S_n}_{S_{n-1}}
    \longleftrightarrow
    \frac{\partial}{\partial p_1}\operatorname{ch}(X).
    $$
    Thus $n$ ways to remove one fixed point appears as the scalar $n$ in the identity.

Authored by **Codex 5.3 Spark Extra High**.
:::
