---
schema: qual/card@1
id: P-BKF09-4A
kind: problem
title: $p$-subgroups of $\operatorname{GL}_n(\FF_p)$ are conjugate into the unitriangular group
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the order of $U$, the $p$-part of the order of $G$
    with the row-by-row count supplying it, the identification of $U$ as a Sylow $p$-subgroup, and Sylow's
    theorem applied at the end. No retained solution set covers this exercise, so the argument is the
    card's own; the exponents $\binom{n}{2}$ were checked for this pass on both sides.
---

::: {.problem}
Let $p$, $n$ be positive integers with $p$ prime.
Let $G=\operatorname{GL}_n(\FF_p)$ be the group of invertible $n\times n$ matrices over the field with $p$ elements.
Let $U\subset G$ be the subgroup consisting of upper triangular matrices with all diagonal entries equal to $1$. Prove that every $p$-subgroup of $G$ is conjugate to a subgroup of $U$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and the two orders below were checked for this pass. Here $G=\operatorname{GL}_{n}(\FF_{p})$ and $U$ is the group of upper triangular matrices with all diagonal entries $1$.

::: pf

::: {.pf-step #order-u}
$\abs{U}=p^{\binom{n}{2}}$.

::: pf-proof
A matrix of $U$ has $1$ on the diagonal, $0$ below it, and an arbitrary entry of $\FF_{p}$ in each of the $\binom{n}{2}$ positions above the diagonal; the product of two such matrices is again of this form and the inverse of one is of this form, so the set of all such matrices is a subgroup of order $p^{\binom{n}{2}}$, that is $p$ raised to the number of free positions.
:::

:::

::: {.pf-step #order-g}
$\abs{G}=p^{\binom{n}{2}}(p^{n}-1)(p^{n-1}-1)\cdots(p-1)$, so the exact power of $p$ dividing $\abs{G}$ is $p^{\binom{n}{2}}$.

::: pf-proof
Count the rows of a matrix in $G$ in succession: the first row may be any nonzero vector, giving $p^{n}-1$ choices; having chosen $k-1$ linearly independent rows spanning a subspace of dimension $k-1$ with $p^{k-1}$ elements, the $k$-th row may be any vector outside that subspace, giving $p^{n}-p^{k-1}$ choices, and the chosen rows stay independent. Multiplying gives
$$
\abs{G}=\prod_{k=1}^{n}(p^{n}-p^{k-1})=p^{0+1+\cdots+(n-1)}\prod_{k=1}^{n}(p^{n-k+1}-1)=p^{\binom{n}{2}}(p^{n}-1)(p^{n-1}-1)\cdots(p-1),
$$
and none of the factors $p^{j}-1$ with $j\ge1$ is divisible by $p$.
:::

:::

::: {.pf-step #sylow}
$U$ is a Sylow $p$-subgroup of $G$.

::: pf-proof
$U$ is a subgroup of $G$ and a $p$-group, since $\abs{U}=p^{\binom{n}{2}}$ by step [](#order-u){.pf-ref}; and $p^{\binom{n}{2}}$ is the full power of $p$ dividing $\abs{G}$ by step [](#order-g){.pf-ref}, so no $p$-subgroup of $G$ can be larger than $U$. That is exactly the definition of a Sylow $p$-subgroup.
:::

:::

::: {.pf-step}
Every $p$-subgroup of $G$ is conjugate to a subgroup of $U$.

::: pf-proof
Let $H\le G$ be a $p$-subgroup. By Sylow's theorem every $p$-subgroup lies in a Sylow $p$-subgroup, so $H\subseteq Q$ for some Sylow $p$-subgroup $Q$; by step [](#sylow){.pf-ref} $U$ is a Sylow $p$-subgroup, and Sylow's theorem also says that any two Sylow $p$-subgroups are conjugate, so $Q=gUg^{-1}$ for some $g\in G$. Hence $g^{-1}Hg\subseteq g^{-1}Qg=U$, which is the assertion.
:::

:::

:::
:::
