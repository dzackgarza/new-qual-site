---
schema: qual/card@1
id: P-TFKBW
kind: problem
title: A finite abelian group with at most $n$ elements of order dividing $n$ is cyclic
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Cyclic Groups
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite abelian group. Suppose that for every positive integer $n$, at most $n$ elements of $G$ satisfy $x^n=e$ (equivalently, have order dividing $n$). Prove that $G$ is cyclic.
:::

::: {.solution}
Let $m$ be the exponent of $G$, the least positive integer such that $x^m=e$ for every $x\in G$.

::: pf

::: {.pf-step #exponent}
$m=\abs{G}$.

::: pf-proof
Every element of $G$ satisfies $x^m=e$, so the hypothesis with $n=m$ gives $\abs{G}\le m$.
By Lagrange's theorem every element satisfies $x^{\abs{G}}=e$, so $m\le\abs{G}$.
:::

:::

::: {.pf-step #attained}
$G$ has an element of order $m$.

::: pf-proof
Write $G=\prod_p G_p$ as the product of its Sylow subgroups.
In the finite abelian $p$-group $G_p$, an element $g_p$ of maximal order has order equal to the exponent $p^{e_p}$ of $G_p$, and $m=\prod_p p^{e_p}$.
Since the orders of the commuting elements $g_p$ are pairwise coprime, $g=\prod_p g_p$ has order $\prod_p p^{e_p}=m$.
:::

:::

::: pf-step
$G$ is cyclic.

::: pf-proof
By step [](#attained){.pf-ref} and step [](#exponent){.pf-ref}, $G$ has an element of order $\abs{G}$, and that element generates $G$.
:::

:::

:::

:::
