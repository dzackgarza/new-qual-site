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
<1>1. The matrix $A$ has a nonzero eigenspace
$$
E_\lambda\coloneqq\ker(A-\lambda I)
$$
for some $\lambda\in\CC$.

::: {.proof}
The characteristic polynomial of $A$ has a root $\lambda\in\CC$ by the
fundamental theorem of algebra. Hence $A-\lambda I$ is singular, so
$E_\lambda$ is nonzero.
:::

<1>2. The subspace $E_\lambda$ is invariant under $B$.

::: {.proof}
Let $v\in E_\lambda$. Since $AB=BA$,
$$
A(Bv)
=B(Av)
=B(\lambda v)
=\lambda Bv.
$$
Thus $Bv\in E_\lambda$.
:::

<1>3. The restriction
$$
B\vert_{E_\lambda}:E_\lambda\longrightarrow E_\lambda
$$
has a nonzero eigenvector $v$.

::: {.proof}
By steps <1>1 and <1>2, $E_\lambda$ is a nonzero finite-dimensional
complex vector space and $B\vert_{E_\lambda}$ is an endomorphism of it.
Its characteristic polynomial therefore has a root $\mu\in\CC$, so there
is a nonzero $v\in E_\lambda$ satisfying
$$
Bv=\mu v.
$$
:::

<1>4. The vector $v$ from step <1>3 is a common eigenvector of $A$ and
$B$.

::: {.proof}
Because $v\in E_\lambda$,
$$
Av=\lambda v.
$$
Step <1>3 gives
$$
Bv=\mu v.
$$
Since $v\neq0$, it is an eigenvector of both matrices.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
