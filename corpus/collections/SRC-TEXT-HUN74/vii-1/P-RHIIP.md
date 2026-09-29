---
schema: qual/card@1
id: P-RHIIP
kind: problem
title: Sums, products, and transposes of symmetric and skew-symmetric matrices
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring and let $A, B \in M_n(R)$ be $n \times n$ matrices.

(a) Show that if $A$ and $B$ are symmetric (respectively, skew-symmetric), then $A + B$ is symmetric (respectively, skew-symmetric).

(b) Show that if $A$ and $B$ are symmetric, then the product $A B$ is symmetric if and only if $A B = B A$.

(c) Show that for any matrix $B \in M_n(R)$, the matrices $B B^t$ and $B + B^t$ are symmetric, and $B - B^t$ is skew-symmetric.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $X, Y \in M_n(R)$: $(X + Y)^t = X^t + Y^t$, $(-X)^t=-X^t$, $(X^t)^t = X$, and $(X Y)^t = Y^t X^t$.

::: pf-proof

The first three identities hold entrywise. For the last, commutativity of $R$ gives
$$((XY)^t)_{i, j} = \sum_k X_{j, k} Y_{k, i} = \sum_k (Y^t)_{i, k} (X^t)_{k, j} = (Y^t X^t)_{i, j}.$$

:::

:::

::: pf-step

(a) Sums of symmetric matrices are symmetric, and sums of skew-symmetric matrices are skew-symmetric.

::: pf-proof

If $A^t = A$ and $B^t = B$, then $(A + B)^t = A + B$ by step [](#s1){.pf-ref}. If $A^t = -A$ and $B^t = -B$, then $(A + B)^t = (-A) + (-B) = -(A + B)$.

:::

:::

::: pf-step

(b) If $A$ and $B$ are symmetric, then $AB$ is symmetric if and only if $AB = BA$.

::: pf-proof

By step [](#s1){.pf-ref}, $(A B)^t = B^t A^t = B A$, so $(AB)^t=AB$ if and only if $BA=AB$.

:::

:::

::: pf-step

(c) $B B^t$ and $B + B^t$ are symmetric and $B - B^t$ is skew-symmetric.

::: pf-proof

By step [](#s1){.pf-ref},
$$(B B^t)^t = (B^t)^t B^t = B B^t,\qquad (B + B^t)^t = B^t + B,\qquad (B - B^t)^t = B^t - B = -(B - B^t).$$

:::

:::

:::

:::
