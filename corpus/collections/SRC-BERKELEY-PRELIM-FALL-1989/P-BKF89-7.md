---
schema: qual/card@1
id: P-BKF89-7
kind: problem
title: A commuting diagonalizable operator is diagonalizable on each eigenspace
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $A$ and $B$ be diagonalizable linear transformations of $\mathbb R^n$ satisfying $AB=BA$. Let $E$ be an eigenspace of $A$. Prove that the restriction $B|_E$ is diagonalizable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The eigenspace $E$ is invariant under $B$.

::: pf-proof

Let $\lambda$ be the eigenvalue of $A$ corresponding to $E$, and let $v\in E$. Then
$$
Av=\lambda v.
$$
Using $AB=BA$,
$$
A(Bv)
=
B(Av)
=
\lambda Bv.
$$
Thus $Bv\in E$, so $B(E)\subseteq E$.

:::

:::

::: {.pf-step #s2}

The minimal polynomial of $B|_E$ divides the minimal polynomial of $B$.

::: pf-proof

Let $m_B(t)$ be the minimal polynomial of $B$. Since
$$
m_B(B)=0
$$
on $\RR^n$, its restriction to the $B$-invariant subspace $E$ from step [](#s1){.pf-ref} is also zero:
$$
m_B(B|_E)=0.
$$
By the defining divisibility property of the minimal polynomial,
$$
m_{B|_E}(t)\mid m_B(t).
$$

:::

:::

::: {.pf-step #s3}

The polynomial $m_{B|_E}$ splits over $\RR$ into distinct linear factors.

::: pf-proof

Because $B$ is diagonalizable over $\RR$, its minimal polynomial splits into distinct linear factors:
$$
m_B(t)
=
\prod_{j=1}^s(t-\mu_j)
$$
with the $\mu_j$ distinct. By step [](#s2){.pf-ref}, $m_{B|_E}$ divides this polynomial, so it too is a product of distinct linear factors over $\RR$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{B|_E\text{ is diagonalizable}}.
$$

::: pf-proof

A linear transformation over $\RR$ is diagonalizable exactly when its minimal polynomial splits into distinct linear factors. Step [](#s3){.pf-ref} verifies this criterion for $B|_E$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
