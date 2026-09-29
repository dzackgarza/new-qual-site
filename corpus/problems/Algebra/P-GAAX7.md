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

::: {.problem}
Let $G$ be a nonabelian group of order $p^3$, where $p$ is prime. Prove that
\[
G'=Z(G).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has
\[
|Z(G)|=p.
\]

::: pf-proof

Every finite $p$-group has nontrivial center, so $|Z(G)|$ is $p$, $p^2$, or $p^3$. Since $G$ is nonabelian, $|Z(G)|\ne p^3$.

If $|Z(G)|=p^2$, then $G/Z(G)$ has order $p$ and is therefore cyclic. A group with cyclic central quotient is abelian, contradiction. Hence $|Z(G)|=p$.

:::

:::

::: {.pf-step #s2}

The quotient $G/Z(G)$ is abelian.

::: pf-proof

By step [](#s1){.pf-ref} it has order
\[
|G/Z(G)|=p^2,
\]
and every group of order $p^2$ is abelian.

:::

:::

::: {.pf-step #s3}

Therefore
\[
G'\le Z(G).
\]

::: pf-proof

The derived subgroup $G'=[G,G]$ is the smallest normal subgroup $N$ such that $G/N$ is abelian. Since $G/Z(G)$ is abelian by step [](#s2){.pf-ref}, this universal property gives
\[
G'\le Z(G).
\]

:::

:::

::: {.pf-step #s4}

The subgroup $G'$ is nontrivial.

::: pf-proof

If $G'=1$, then $G$ itself is abelian, contrary to hypothesis.

:::

:::

::: pf-step

Hence
\[
G'=Z(G).
\]

::: pf-proof

By step [](#s1){.pf-ref}, the center has prime order $p$. By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $G'$ is a nontrivial subgroup of $Z(G)$. The only nontrivial subgroup of a group of prime order is the whole group.

:::

:::

:::

:::
