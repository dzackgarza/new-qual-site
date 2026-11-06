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
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section VII.1,
    exercise 5, book page 335, read from the page image: "A matrix A ∈ Mat_n R is
    symmetric if A = A^t and skew-symmetric if A = -A^t. (a) If A and B are
    [skew] symmetric, then A + B is [skew] symmetric. (b) Let R be commutative. If
    A, B are symmetric, then AB is symmetric if and only if AB = BA. Also show
    that for any matrix B ∈ Mat_n R, BB^t and B + B^t are symmetric and B - B^t is
    skew-symmetric." Repaired here: the statement used to begin "Let R be a
    commutative ring" and so claimed part (a) only for commutative R, while the
    book introduces commutativity only at (b) and (c); the printed hypothesis is
    now restored and the solution says where commutativity is and is not used,
    since (X+Y)^t = X^t + Y^t and (-X)^t = -X^t are entrywise while
    (XY)^t = Y^t X^t needs it. All of (a), (b), (c) were checked as proofs; the
    proof of (a) never uses commutativity, so the restored part (a) is proved as
    stated. Complete.
---

::: {.problem}
Let $R$ be a ring with identity and let $A, B \in M_n(R)$ be $n \times n$ matrices, with $A$ symmetric ($A = A^t$) or skew-symmetric ($A = -A^t$).

(a) Show that if $A$ and $B$ are symmetric (respectively, skew-symmetric), then $A + B$ is symmetric (respectively, skew-symmetric).

Now let $R$ be commutative.

(b) Show that if $A$ and $B$ are symmetric, then the product $A B$ is symmetric if and only if $A B = B A$.

(c) Show that for any matrix $B \in M_n(R)$, the matrices $B B^t$ and $B + B^t$ are symmetric, and $B - B^t$ is skew-symmetric.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $X, Y \in M_n(R)$ over any ring with identity: $(X + Y)^t = X^t + Y^t$, $(-X)^t=-X^t$, and $(X^t)^t = X$. If in addition $R$ is commutative, then $(X Y)^t = Y^t X^t$.

::: pf-proof

The first three identities hold entrywise and use nothing about $R$ beyond the ring axioms. For the last, commutativity of $R$ gives
$$((XY)^t)_{i, j} = \sum_k X_{j, k} Y_{k, i} = \sum_k (Y^t)_{i, k} (X^t)_{k, j} = (Y^t X^t)_{i, j}.$$

:::

:::

::: pf-step

(a) Sums of symmetric matrices are symmetric, and sums of skew-symmetric matrices are skew-symmetric.

::: pf-proof

If $A^t = A$ and $B^t = B$, then $(A + B)^t = A + B$ by step [](#s1){.pf-ref}, using only the additive identities, so $R$ need not be commutative here. If $A^t = -A$ and $B^t = -B$, then $(A + B)^t = (-A) + (-B) = -(A + B)$.

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

::: {.remark title="Variations"}
Over a field $F$, symmetric and skew-symmetric matrices form subspaces of $M_n(F)$, and if $\operatorname{char}(F)\neq 2$ then $M_n(F)=\operatorname{Sym}_n(F)\oplus\operatorname{Skew}_n(F)$ as an internal direct sum.
:::
