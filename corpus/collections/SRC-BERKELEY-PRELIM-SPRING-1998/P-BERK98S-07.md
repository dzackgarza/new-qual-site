---
schema: qual/card@1
id: P-BERK98S-07
kind: problem
title: Two commuting complex matrices have a common eigenvector
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
Suppose $A$ and $B$ are commuting $n\times n$ complex matrices. Prove that $A$ and $B$ have a common eigenvector.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The matrix $A$ has a nonzero eigenspace
$$
E_\lambda\coloneqq\ker(A-\lambda I)
$$
for some $\lambda\in\CC$.

::: pf-proof

The characteristic polynomial of $A$ has a root $\lambda\in\CC$ by the
fundamental theorem of algebra. Hence $A-\lambda I$ is singular, so
$E_\lambda$ is nonzero.

:::

:::

::: {.pf-step #s2}

The subspace $E_\lambda$ is invariant under $B$.

::: pf-proof

Let $v\in E_\lambda$. Since $AB=BA$,
$$
A(Bv)
=B(Av)
=B(\lambda v)
=\lambda Bv.
$$
Thus $Bv\in E_\lambda$.

:::

:::

::: {.pf-step #s3}

The restriction
$$
B\vert_{E_\lambda}:E_\lambda\longrightarrow E_\lambda
$$
has a nonzero eigenvector $v$.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $E_\lambda$ is a nonzero finite-dimensional
complex vector space and $B\vert_{E_\lambda}$ is an endomorphism of it.
Its characteristic polynomial therefore has a root $\mu\in\CC$, so there
is a nonzero $v\in E_\lambda$ satisfying
$$
Bv=\mu v.
$$

:::

:::

::: {.pf-step #s4}

The vector $v$ from step [](#s3){.pf-ref} is a common eigenvector of $A$ and
$B$.

::: pf-proof

Because $v\in E_\lambda$,
$$
Av=\lambda v.
$$
Step [](#s3){.pf-ref} gives
$$
Bv=\mu v.
$$
Since $v\neq0$, it is an eigenvector of both matrices.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
