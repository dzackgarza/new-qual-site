---
schema: qual/card@1
id: P-BKF18-7A
kind: problem
title: Entry bound for a positive semidefinite matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose $A=(a_{ij})$ is a real symmetric $n\times n$ matrix with nonnegative eigenvalues.
Show that
$$
\abs{a_{ij}}\le \sqrt{a_{ii}a_{jj}}
$$
for all distinct $i,j\le n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There are vectors $v_1,\dots,v_n\in\RR^n$ with $a_{ij}=\langle v_i,v_j\rangle$.

::: pf-proof

By the spectral theorem, $A=UDU^T$ with $U$ orthogonal and $D$ diagonal with nonnegative entries. Put $C=D^{1/2}U^T$. Then $A=C^TC$, so $a_{ij}=\langle v_i,v_j\rangle$ with $v_i$ the $i$-th column of $C$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref} and the Cauchy–Schwarz inequality,
$$
\abs{a_{ij}}=\abs{\langle v_i,v_j\rangle}\le\norm{v_i}\norm{v_j}=\sqrt{a_{ii}a_{jj}}.
$$

:::

:::

:::
