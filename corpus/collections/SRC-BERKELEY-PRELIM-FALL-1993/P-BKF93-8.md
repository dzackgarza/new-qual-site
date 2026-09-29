---
schema: qual/card@1
id: P-BKF93-8
kind: problem
title: A complex matrix of finite order is diagonalizable
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used that the minimal polynomial divides t^k-1 and that t^k-1 has only
    simple roots over C, so the minimal polynomial is square-free and split.
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix. Prove that if
\[
A^k=I
\]
for some positive integer $k$, then $A$ is diagonalizable.
:::

::: {.solution}
Let $m_A(t)$ denote the minimal polynomial of $A$.

::: pf

::: {.pf-step #s1}

One has
$$
m_A(t)\mid t^k-1.
$$

::: pf-proof

The hypothesis $A^k=I$ says
$$
(A^k-I)=0,
$$
so the polynomial $t^k-1$ annihilates $A$. By the defining property of the
minimal polynomial, $m_A(t)$ divides every polynomial that annihilates $A$.

:::

:::

::: {.pf-step #s2}

The polynomial
$$
t^k-1
$$
has no repeated roots in $\CC$.

::: pf-proof

Its derivative is
$$
kt^{k-1}.
$$
A repeated root would be a common root of $t^k-1$ and $kt^{k-1}$. Since the
base field has characteristic zero, the only root of $kt^{k-1}$ is $0$, while
$0$ is not a root of $t^k-1$. Hence no repeated root exists.

:::

:::

::: {.pf-step #s3}

The minimal polynomial $m_A(t)$ splits over $\CC$ into distinct linear
factors.

::: pf-proof

The polynomial $t^k-1$ splits completely over $\CC$, and by step [](#s2){.pf-ref} its
linear factors are distinct. Step [](#s1){.pf-ref} shows that $m_A(t)$ is a divisor of
that polynomial, so $m_A(t)$ also splits and has no repeated root.

:::

:::

::: {.pf-step #s4}

The matrix $A$ is diagonalizable over $\CC$.

::: pf-proof

A complex matrix is diagonalizable if and only if its minimal polynomial
splits into distinct linear factors. Step [](#s3){.pf-ref} verifies this criterion for
$A$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
