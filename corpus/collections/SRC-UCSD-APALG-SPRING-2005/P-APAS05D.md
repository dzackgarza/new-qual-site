---
schema: qual/card@1
id: P-APAS05D
kind: problem
title: Unique subgroup of each dividing order implies a finite abelian group is cyclic
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - Abelian Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite abelian group of order $n$.
Suppose that $G$ has a unique subgroup of order $d$ for each positive divisor of $n$.
Prove that $G$ is cyclic.
:::

::: {.solution}
<1>1. For every prime $p\mid |G|$, the $p$-primary component $G_p$ is cyclic.
::: {.proof}
By the fundamental theorem of finite abelian groups,
\[
G_p\cong C_{p^{a_1}}\times\cdots\times C_{p^{a_r}}
\]
for some integers $a_i\ge1$.
Suppose $r\ge2$. In the first two factors choose elements
\[
u=(p^{a_1-1},0,\ldots,0),
\qquad
v=(0,p^{a_2-1},0,\ldots,0).
\]
Both have order $p$. Their cyclic subgroups
\[
\langle u\rangle,
\qquad
\langle v\rangle
\]
are distinct subgroups of $G_p$, hence of $G$, both of order $p$. This contradicts the hypothesis that $G$ has a unique subgroup of order $p$.
Therefore $r=1$, so $G_p$ is cyclic.
:::

<1>2. The group $G$ is cyclic.
::: {.proof}
Again by the primary decomposition theorem,
\[
G\cong\prod_{p\mid |G|}G_p.
\]
By <1>1, each $G_p$ is cyclic of order $p^{a_p}$. The orders of distinct primary components are pairwise coprime.
If $g_p$ generates $G_p$, then the element
\[
g=(g_p)_p\in\prod_pG_p
\]
has order
\[
\operatorname{lcm}_p(p^{a_p})=\prod_p p^{a_p}=|G|.
\]
Thus $g$ generates $G$, so $G$ is cyclic.
:::
:::
