---
schema: qual/card@1
id: P-BKF18-6B
kind: problem
title: Strict diagonal dominance implies invertibility
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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. If Ax = 0 and x != 0, choosing i with |x_i| maximal gives
    (|a_ii| - sum_{j != i} |a_ij|)|x_i| <= 0, and strict diagonal dominance makes the bracket
    positive, so x_i = 0 and then x = 0. Checked that the hypothesis is used strictly, at the single
    point where the bracket's sign is decided, and that the maximal-coordinate choice is what lets
    every |x_j| be replaced by |x_i|. Not checked: the printed paper, which was not re-read.
---

::: {.problem}
Show that if $A=(a_{ij})$ is an $n\times n$ complex matrix satisfying
$$
\abs{a_{ii}}>\sum_{j\ne i}\abs{a_{ij}}
$$
for all $i\in\{1,\dots,n\}$, then $A$ is invertible.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $Ax=0$, then $x=0$.

::: pf-proof

Suppose $Ax=0$ and choose $i$ with $\abs{x_i}=\max_j\abs{x_j}$. Row $i$ gives $a_{ii}x_i=-\sum_{j\ne i}a_{ij}x_j$, so
$$
\abs{a_{ii}}\abs{x_i}\le\sum_{j\ne i}\abs{a_{ij}}\abs{x_j}\le\Big(\sum_{j\ne i}\abs{a_{ij}}\Big)\abs{x_i}.
$$
Thus $\big(\abs{a_{ii}}-\sum_{j\ne i}\abs{a_{ij}}\big)\abs{x_i}\le0$. The first factor is positive, so $x_i=0$, and by the choice of $i$, $x=0$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $A$ has trivial kernel. A square matrix with trivial kernel is invertible.

:::

:::

:::
