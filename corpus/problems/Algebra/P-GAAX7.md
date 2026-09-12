---
schema: qual/card@1
id: P-GAAX7
kind: problem
title: Derived subgroup equals the centre for nonabelian groups of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Commutators
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $G$ be a nonabelian group of order $p^3$, where $p$ is prime. Prove that
\[
G'=Z(G).
\]
:::


::: {.solution}
<1>1. One has
\[
|Z(G)|=p.
\]
::: {.proof}
Every finite $p$-group has nontrivial center, so $|Z(G)|$ is $p$, $p^2$, or $p^3$. Since $G$ is nonabelian, $|Z(G)|\ne p^3$.

If $|Z(G)|=p^2$, then $G/Z(G)$ has order $p$ and is therefore cyclic. A group with cyclic central quotient is abelian, contradiction. Hence $|Z(G)|=p$.
:::

<1>2. The quotient $G/Z(G)$ is abelian.
::: {.proof}
By <1>1 it has order
\[
|G/Z(G)|=p^2,
\]
and every group of order $p^2$ is abelian.
:::

<1>3. Therefore
\[
G'\le Z(G).
\]
::: {.proof}
The derived subgroup $G'=[G,G]$ is the smallest normal subgroup $N$ such that $G/N$ is abelian. Since $G/Z(G)$ is abelian by <1>2, this universal property gives
\[
G'\le Z(G).
\]
:::

<1>4. The subgroup $G'$ is nontrivial.
::: {.proof}
If $G'=1$, then $G$ itself is abelian, contrary to hypothesis.
:::

<1>5. Hence
\[
G'=Z(G).
\]
::: {.proof}
By <1>1, the center has prime order $p$. By <1>3 and <1>4, $G'$ is a nontrivial subgroup of $Z(G)$. The only nontrivial subgroup of a group of prime order is the whole group.
:::
:::
