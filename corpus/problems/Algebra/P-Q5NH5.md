---
schema: qual/card@1
id: P-Q5NH5
kind: problem
title: Group rings
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Representation Theory
  - Algebras
relations: []
review: draft
---

::: {.problem}
Define the group ring $R[G]$ and describe its basic structure and relation to representations.
:::

::: {.solution}
Let $R$ be a unital ring and $G$ a group. The group ring $R[G]$ is the set of finite formal sums $\sum_{g\in G}r_gg$ with $r_g\in R$, with coefficientwise addition and the multiplication determined by $(rg)(sh)=(rs)(gh)$ and distributivity.

::: pf

::: pf-step
As a left $R$-module, $R[G]$ is free with basis $G$. If $R$ is commutative, $R[G]$ is an $R$-algebra, and $R[G]$ is commutative if and only if $R$ is commutative and $G$ is abelian.

::: pf-proof
Each element has a unique expression $\sum r_gg$, which is freeness on $G$. If $R$ is commutative, the scalars $r\cdot e$ commute with every $sh$, so $R\to R[G]$, $r\mapsto re$, makes $R[G]$ an $R$-algebra. The elements $re$ and $g$ lie in $R[G]$, and $(re)(se)=(rs)e$ and $gh$ are their products, so commutativity of $R[G]$ forces that of $R$ and $G$; the converse holds on basis products and extends by distributivity.
:::

:::

::: pf-step
The augmentation $\varepsilon:R[G]\to R$, $\sum r_gg\mapsto\sum r_g$, is a surjective ring homomorphism, and its kernel, the augmentation ideal, is the left $R$-submodule spanned by the elements $g-e$.

::: pf-proof
$\varepsilon$ is additive and $\varepsilon((rg)(sh))=rs=\varepsilon(rg)\varepsilon(sh)$, and $\varepsilon(re)=r$. If $\sum r_g=0$, then $\sum r_gg=\sum r_g(g-e)$.
:::

:::

::: pf-step
Left $R[G]$-modules are the same as left $R$-modules $M$ with an action of $G$ by $R$-linear automorphisms. In particular, for a field $k$, representations $\rho:G\to\GL(V)$ on $k$-vector spaces are the same as left $k[G]$-modules.

::: pf-proof
Given a module, the elements $g\in G\subseteq R[G]$ act by maps that are $R$-linear, as $g$ commutes with $re$, and invertible with inverse $g^{-1}$. Conversely, given such an action, $\left(\sum r_gg\right)m\coloneqq\sum r_g(gm)$ is a module structure, by the defining multiplication rule. The two constructions are inverse.
:::

:::

::: pf-step
If $G$ is finite and $\operatorname{char}k\nmid\abs{G}$, then $k[G]$ is semisimple. If moreover $k$ is algebraically closed, then $k[G]\cong\prod_{i}\Mat_{d_i}(k)$, with one factor for each irreducible representation $V_i$ of $G$, where $d_i=\dim V_i$.

::: pf-proof
The first claim is Maschke's theorem. The second is the Artin--Wedderburn theorem: a finite-dimensional semisimple algebra over an algebraically closed field is a product of matrix algebras over $k$, one for each simple module.
:::

:::

:::

:::
