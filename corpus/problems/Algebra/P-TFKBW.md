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
Let $m$ be the exponent of $G$, the least positive integer such that
\[
x^m=e\qquad\text{for every }x\in G.
\]
Since every element of $G$ satisfies $x^m=e$, the hypothesis with $n=m$ gives
\[
|G|\le m.
\]
On the other hand, the order of every element divides $|G|$ by Lagrange's theorem, so the exponent also divides $|G|$. Hence
\[
m\le |G|.
\]
Therefore
\[
m=|G|.
\]

For a finite abelian group, the exponent is attained as the order of some element. Indeed, decompose $G$ into its Sylow subgroups
\[
G=\prod_p G_p.
\]
For each $p$, choose an element $g_p\in G_p$ of maximal order, equal to the exponent of $G_p$. Since these orders are pairwise coprime, the element
\[
g=\prod_p g_p
\]
has order equal to the product of those exponents, namely $m$.

Thus $G$ contains an element of order
\[
m=|G|.
\]
That element generates all of $G$, so $G$ is cyclic.
:::
