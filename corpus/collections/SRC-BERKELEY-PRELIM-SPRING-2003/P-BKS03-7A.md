---
schema: qual/card@1
id: P-BKS03-7A
kind: problem
title: When a union of subgroups is a subgroup
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}

(a) If $H_1,H_2\le G$ and $H_1\cup H_2$ is a subgroup, prove that $H_1\subseteq H_2$ or $H_2\subseteq H_1$.

(b) For every $n\ge3$, construct a group $G$ with subgroups $H_1,\dots,H_n$, none contained in another, such that $H_1\cup\cdots\cup H_n$ is a subgroup.
:::

::: {.solution}

The argument is the card's own: in (a) two elements outside each other's subgroup multiply into a contradiction, and in (b) an elementary abelian group is covered by subgroups of index $2$.

::: pf

::: {.pf-step #parta}

(a) If $H_{1}\cup H_{2}$ is a subgroup then $H_{1}\subseteq H_{2}$ or $H_{2}\subseteq H_{1}$.

::: pf-proof

Suppose neither inclusion holds; then there are $h_{1}\in H_{1}-H_{2}$ and $h_{2}\in H_{2}-H_{1}$. Both lie in the subgroup $H_{1}\cup H_{2}$, so $h_{1}h_{2}\in H_{1}\cup H_{2}$. If $h_{1}h_{2}\in H_{1}$ then $h_{2}=h_{1}^{-1}(h_{1}h_{2})\in H_{1}$, since $H_{1}$ is a subgroup; contradiction. If $h_{1}h_{2}\in H_{2}$ then $h_{1}=(h_{1}h_{2})h_{2}^{-1}\in H_{2}$; contradiction. Both cases are impossible.

:::

:::

::: {.pf-step #construction}

(b) For $n\ge3$, in $G=(\ZZ/2\ZZ)^{n-1}$ put $H_{i}=\{x:x_{i}=0\}$ for $1\le i\le n-1$ and $H_{n}=\{x:x_{1}+x_{2}=0\}$.

::: pf-proof

Each $H_{i}$ is the kernel of a nonzero $\FF_2$-linear functional on $G$, hence a subgroup of order $2^{n-2}$; distinct nonzero functionals have distinct kernels, so the $H_{i}$ are pairwise distinct subgroups of the same order. Here $n-1\ge2$ guarantees that $x_{1}+x_{2}$ is a nonzero functional and that its kernel differs from $\ker(x_{1})$: the vector with $x_{1}=x_{2}=1$ and all other coordinates $0$ lies in $H_{n}$ but not in $H_{1}$.

:::

:::

::: {.pf-step #cover}

$H_{1}\cup\cdots\cup H_{n}=G$.

::: pf-proof

The vector $(1,\dots,1)$ lies in none of $H_{1},\dots,H_{n-1}$, since all its coordinates are $1$, but it lies in $H_{n}$ because $1+1=0$ in $\ZZ/2\ZZ$. Every other vector of $G$ has some coordinate $0$ among $1,\dots,n-1$, hence lies in the corresponding $H_{i}$. So the union is all of $G$, and it is a subgroup.

:::

:::

::: {.pf-step #incomparable}

No $H_{i}$ is contained in another.

::: pf-proof

All have the same order $2^{n-2}$ and they are pairwise distinct; a containment between two subgroups of equal finite order would be an equality. Hence each $H_{i}$ is contained in no other, and with step [](#cover){.pf-ref}:
$$
\boxed{n\ge3:\ G=(\ZZ/2)^{n-1}\ \text{is the union of } n \text{ pairwise incomparable subgroups.}}
$$

:::

:::

:::

:::
