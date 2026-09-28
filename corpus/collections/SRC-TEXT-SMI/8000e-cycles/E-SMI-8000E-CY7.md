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
Define a binary relation $\sim$ on the set $\{1, 2, \dots, n\}$ by setting:
$$j \sim k \iff (j = k) \text{ or } ((j\,k) \in H).$$
Prove that $\sim$ is an **equivalence relation** on $\{1, 2, \dots, n\}$.
*(Note: If $j \sim k$ is defined solely by $(j\,k) \in H$, adding $j=k$ makes reflexivity explicit).*
:::

::: {.solution}
<1>1. $\sim$ is reflexive.

::: {.proof}
For every $j$, the clause $j = j$ of the definition gives $j \sim j$.
:::

<1>2. $\sim$ is symmetric.

::: {.proof}
Let $j \sim k$. If $j = k$, then $k \sim j$ by step <1>1. If $j \ne k$, then $(j\,k) \in H$, and $(k\,j) = (j\,k)$ as permutations, so $k \sim j$.
:::

<1>3. $\sim$ is transitive.

::: {.proof}
Let $j \sim k$ and $k \sim \ell$. If $j = k$ or $k = \ell$, then $j \sim \ell$ is one of the hypotheses, and if $j = \ell$, then $j \sim \ell$ by step <1>1. Otherwise $j, k, \ell$ are distinct and $(j\,k), (k\,\ell) \in H$. Put $\sigma = (j\,k)(k\,\ell)(j\,k)$, which lies in $H$ because $H$ is a subgroup. Composing from the right,
$$
\sigma(j) = (j\,k)(k\,\ell)(k) = \ell,
\qquad
\sigma(\ell) = (j\,k)(k\,\ell)(\ell) = j,
\qquad
\sigma(k) = (j\,k)(k\,\ell)(j) = k,
$$
and $\sigma$ fixes every index outside $\{j, k, \ell\}$. Hence $\sigma = (j\,\ell) \in H$, and $j \sim \ell$.
:::

<1>4. Q.E.D.

::: {.proof}
By steps <1>1--<1>3, $\sim$ is an equivalence relation on $\{1, 2, \dots, n\}$.
:::
:::
