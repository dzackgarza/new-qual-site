---
schema: qual/card@1
id: P-HGRO43
kind: problem
title: Multiple and sharp transitivity
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Define a $k$-transitive group action and a sharply $k$-transitive group action.
Discuss multiple transitivity.
:::

::: {.solution}
Let a group $G$ act on a set $X$, and let $k\ge1$. The action is
\dfn{$k$-transitive} if for any two ordered $k$-tuples $(x_1,\ldots,x_k)$ and
$(y_1,\ldots,y_k)$ of distinct elements of $X$ there is $g\in G$ with
$gx_i=y_i$ for all $i$. It is \dfn{sharply $k$-transitive} if moreover this
$g$ is unique.

::: pf

::: pf-step

For $n\ge2$, $S_n$ acts sharply $n$-transitively on $\{1,\ldots,n\}$.

::: pf-proof

A bijection between two orderings of $\{1,\ldots,n\}$ is exactly one
permutation.

:::

:::

::: pf-step

For $n\ge3$, $A_n$ acts $(n-2)$-transitively on $\{1,\ldots,n\}$.

::: pf-proof

Given two ordered $(n-2)$-tuples of distinct points, there are two
permutations sending one to the other; they differ by the transposition of the
two remaining target points, so exactly one of them is even.

:::

:::

::: pf-step

For a field $k$, $\operatorname{PGL}_2(k)$ acts sharply $3$-transitively
on $\PP^1(k)$.

::: pf-proof

For distinct $z_1,z_2,z_3\in\PP^1(k)$ there is exactly one Möbius
transformation sending them to $\infty,0,1$, namely
$z\mapsto\frac{(z-z_2)(z_3-z_1)}{(z-z_1)(z_3-z_2)}$, with the usual
interpretation when some $z_i=\infty$. Composing one such map with the inverse
of another sends any triple of distinct points to any other, uniquely.

:::

:::

::: pf-step

For a field $k$, the affine group
$\operatorname{AGL}_1(k)=\{x\mapsto ax+b:a\in k^\times,\ b\in k\}$ acts sharply
$2$-transitively on $k$.

::: pf-proof

For $x_1\ne x_2$ and $y_1\ne y_2$, the conditions $ax_i+b=y_i$ have the unique
solution $a=(y_1-y_2)/(x_1-x_2)\ne0$, $b=y_1-ax_1$.

:::

:::

:::

:::
