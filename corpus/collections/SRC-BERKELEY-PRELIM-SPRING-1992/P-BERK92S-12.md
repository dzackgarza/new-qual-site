---
schema: qual/card@1
id: P-BERK92S-12
kind: problem
title: A symmetric nonnegative matrix has a nonnegative eigenvector
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A$ be a real symmetric $n\times n$ matrix with nonnegative entries. Prove that $A$ has an eigenvector whose entries are all nonnegative.
:::

::: {.solution}
Let
$$
\lambda_{\max}\coloneqq
\max_{\norm{x}=1}x^{\mathsf T}Ax.
$$
The maximum exists because the unit sphere is compact.

::: pf

::: {.pf-step #s1}

There is a unit vector $u$ with nonnegative entries such that
$$
u^{\mathsf T}Au=\lambda_{\max}.
$$

::: pf-proof

Choose a unit vector $v$ attaining the maximum and put
$$
u\coloneqq
(\abs{v_1},\ldots,\abs{v_n})^{\mathsf T}.
$$
Then $\norm{u}=\norm{v}=1$. Since every entry $a_{ij}$ of $A$ is
nonnegative,
$$
\begin{aligned}
u^{\mathsf T}Au
&=\sum_{i,j}a_{ij}\abs{v_i}\abs{v_j}\\
&\ge
\sum_{i,j}a_{ij}v_iv_j
=v^{\mathsf T}Av
=\lambda_{\max}.
\end{aligned}
$$
By the definition of $\lambda_{\max}$, equality must hold. Thus $u$
is a nonnegative maximizing unit vector.

:::

:::

::: {.pf-step #s2}

Every unit vector attaining $\lambda_{\max}$ is an eigenvector
of $A$ with eigenvalue $\lambda_{\max}$.

::: pf-proof

By the spectral theorem, choose an orthonormal eigenbasis
$e_1,\ldots,e_n$ for $A$, with eigenvalues
$\lambda_1,\ldots,\lambda_n\le\lambda_{\max}$. If
$x=\sum_i c_ie_i$ is a unit vector, then
$$
x^{\mathsf T}Ax
=\sum_i\lambda_i c_i^2
\le
\lambda_{\max}\sum_i c_i^2
=\lambda_{\max}.
$$
Equality holds only if $c_i=0$ whenever
$\lambda_i<\lambda_{\max}$. Hence a maximizing vector lies in the
$\lambda_{\max}$-eigenspace.

:::

:::

::: {.pf-step #s3}

$A$ has a nonnegative eigenvector.

::: pf-proof

The vector $u$ from step [](#s1){.pf-ref} is nonzero and has nonnegative entries.
By step [](#s2){.pf-ref},
$$
Au=\lambda_{\max}u.
$$
Thus $u$ is the required eigenvector.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the claim.

:::

:::

:::
