---
schema: qual/card@1
id: P-UMVRP
kind: problem
title: Groups with trivial automorphism group
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Groups
relations: []
review: draft
---

::: {.problem}
Which groups have trivial automorphism group?
:::

::: {.solution}

::: pf

::: {.pf-step #abelian}

If $\Aut(G)=1$, then $G$ is abelian.

::: pf-proof

Every inner automorphism is trivial, so $\Inn(G)\cong G/Z(G)$ is trivial and $G=Z(G)$.

:::

:::

::: {.pf-step #exp2}

If $\Aut(G)=1$, then every element of $G$ has order dividing $2$, so $G$ is a vector space over $\FF_2$.

::: pf-proof

By step [](#abelian){.pf-ref}, inversion $x\mapsto x^{-1}$ is an automorphism of $G$. It is trivial, so $x=x^{-1}$ for every $x\in G$.

:::

:::

::: {.pf-step #dim}

If $\Aut(G)=1$, then $G=1$ or $G\cong C_2$.

::: pf-proof

By step [](#exp2){.pf-ref}, $G$ is an $\FF_2$-vector space, and every linear automorphism is a group automorphism. If its dimension were at least $2$, the linear map interchanging two basis vectors and fixing the others would be a nontrivial automorphism. So the dimension is at most $1$.

:::

:::

::: pf-qed

Conversely, $1$ and $C_2$ have only the identity automorphism, since an automorphism fixes the identity and $C_2$ has only one other element. With step [](#dim){.pf-ref}, the groups with trivial automorphism group are exactly
$$\boxed{1\quad\text{and}\quad C_2.}$$

:::

:::

:::
