---
schema: qual/card@1
id: P-BKF07-3B
kind: problem
title: Closed coefficient sets map to closed linear-combination sets
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the basis extension, the closed product subset, and
    preservation of closed sets by the induced linear homeomorphism against the
    vendored solution.
---

::: {.problem}
Let \(u_1,\ldots,u_k\) be linearly independent vectors in \(\mathbb R^n\), and let \(A\subseteq\mathbb R^k\) be closed.
Define
\[
S=\left\{\alpha_1u_1+\cdots+\alpha_ku_k:(\alpha_1,\ldots,\alpha_k)\in A\right\}.
\]
Show that \(S\) is closed in \(\mathbb R^n\).
:::

::: {.solution}

Extend $u_1,\ldots,u_k$ to a basis
$u_1,\ldots,u_n$ of $\RR^n$, and let
$$
U:\RR^n\longrightarrow\RR^n
$$
be the linear map whose matrix has columns $u_1,\ldots,u_n$ in the
standard basis.

::: pf

::: {.pf-step #U-homeomorphism}
The map $U$ is a homeomorphism of $\RR^n$.

::: pf-proof
The vectors $u_1,\ldots,u_n$ form a basis, so the matrix of $U$ is
invertible. Hence $U$ and $U^{-1}$ are linear maps between
finite-dimensional normed spaces and are continuous. Thus $U$ is a
homeomorphism.
:::

:::

::: {.pf-step #A-times-zero-closed}
The subset
$$
A\times\{0\}\subseteq\RR^k\times\RR^{n-k}=\RR^n
$$
is closed.

::: pf-proof
The set $A$ is closed in $\RR^k$ by hypothesis, and $\{0\}$ is
closed in $\RR^{n-k}$. Their product is therefore closed in
$\RR^k\times\RR^{n-k}$.
:::

:::

::: {.pf-step #image-equals-S}
The image of $A\times\{0\}$ under $U$ is exactly $S$.

::: pf-proof
For $(\alpha_1,\ldots,\alpha_k,0,\ldots,0)\in A\times\{0\}$,
the definition of $U$ gives
$$
U(\alpha_1,\ldots,\alpha_k,0,\ldots,0)
=\alpha_1u_1+\cdots+\alpha_ku_k.
$$
As $(\alpha_1,\ldots,\alpha_k)$ ranges over $A$, these are exactly
the elements of $S$.
:::

:::

::: {.pf-step #S-closed}
The set $S$ is closed in $\RR^n$.

::: pf-proof
By step [](#A-times-zero-closed){.pf-ref}, $A\times\{0\}$ is closed. By step [](#U-homeomorphism){.pf-ref}, the
homeomorphism $U$ maps closed sets to closed sets. Step [](#image-equals-S){.pf-ref} identifies
its image with $S$, so $S$ is closed.
:::

:::

::: pf-qed
Step [](#S-closed){.pf-ref} is the required conclusion.
:::

:::

:::
