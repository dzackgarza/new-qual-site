---
schema: qual/card@1
id: E-SMI-8000E-CY7
kind: problem
title: Transpositions in a subgroup of $S_n$ define an equivalence relation
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Let $H$ be a subgroup of the symmetric group $S_n$.
Prove that setting $j \sim k$ if and only if $j = k$ or the $2$-cycle $(j\,k)$ belongs to $H$ defines an equivalence relation on $\{1, 2, \dots, n\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\sim$ is reflexive.

::: pf-proof

For every $j$, the clause $j = j$ of the definition gives $j \sim j$.

:::

:::

::: {.pf-step #s2}

$\sim$ is symmetric.

::: pf-proof

Let $j \sim k$. If $j = k$, then $k \sim j$ by step [](#s1){.pf-ref}. If $j \ne k$, then $(j\,k) \in H$, and $(k\,j) = (j\,k)$ as permutations, so $k \sim j$.

:::

:::

::: {.pf-step #s3}

$\sim$ is transitive.

::: pf-proof

Let $j \sim k$ and $k \sim \ell$. If $j = k$ or $k = \ell$, then $j \sim \ell$ is one of the hypotheses, and if $j = \ell$, then $j \sim \ell$ by step [](#s1){.pf-ref}. Otherwise $j, k, \ell$ are distinct and $(j\,k), (k\,\ell) \in H$. Put $\sigma = (j\,k)(k\,\ell)(j\,k)$, which lies in $H$ because $H$ is a subgroup. Composing from the right,
$$
\sigma(j) = (j\,k)(k\,\ell)(k) = \ell,
\qquad
\sigma(\ell) = (j\,k)(k\,\ell)(\ell) = j,
\qquad
\sigma(k) = (j\,k)(k\,\ell)(j) = k,
$$
and $\sigma$ fixes every index outside $\{j, k, \ell\}$. Hence $\sigma = (j\,\ell) \in H$, and $j \sim \ell$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\sim$ is an equivalence relation on $\{1, 2, \dots, n\}$.

:::

:::

:::
