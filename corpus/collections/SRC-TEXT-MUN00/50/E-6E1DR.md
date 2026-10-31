---
schema: qual/card@1
id: E-6E1DR
kind: problem
title: Characterization of closed imbeddings into $\RR^N$
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Corollary.
A space $X$ can be imbedded as a closed subspace of $\RR^N$ for some $N$ if and only if $X$ is locally compact and Hausdorff with a countable basis, and has finite topological dimension.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Direct implication ($\implies$): Suppose $h: X \to \RR^N$ is an embedding onto a closed subspace $h(X) \subseteq \RR^N$.

::: pf-proof

::: pf-step
**Locally compact Hausdorff:** $\RR^N$ is locally compact and Hausdorff.
Closed subspaces of locally compact Hausdorff spaces are locally compact Hausdorff, so $X \cong h(X)$ is locally compact Hausdorff.
:::

::: pf-step
**Second-countable:** $\RR^N$ is second-countable.
Second-countability is hereditary to all subspaces, so $X$ has a countable basis.
:::

::: pf-step
**Finite topological dimension:** By the dimension properties of Euclidean space, $\dim \RR^N = N$.
The image $h(X)$ is closed, so dimension monotonicity for closed subspaces gives $\dim X = \dim h(X) \le N < \infty$.
:::

:::

:::

::: {.pf-step #s2}
Converse implication ($\impliedby$): Suppose $X$ is locally compact Hausdorff, second-countable, with finite topological dimension.

::: pf-proof

::: pf-step
If $X=\varnothing$, it is closed in $\RR^0$. Otherwise let $m=\dim X\ge0$. Every compact subspace $K$ is closed in the Hausdorff space $X$, so $\dim K\le m$ by dimension monotonicity for closed subspaces.
:::

::: pf-step
For nonempty $X$, [[E-26ELV]] embeds a locally compact Hausdorff space with a countable basis whose compact subspaces have dimension at most $m$ as a closed subspace of $\RR^{2m+1}$. Apply it to $X$.
:::

:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves the forward implication, and step [](#s2){.pf-ref} imbeds $X$ as a closed subspace of some Euclidean space.
:::

:::

:::
