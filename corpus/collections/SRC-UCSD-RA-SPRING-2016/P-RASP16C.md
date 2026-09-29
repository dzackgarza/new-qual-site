---
schema: qual/card@1
id: P-RASP16C
kind: problem
title: "Nested nonempty compact sets have nonempty intersection"
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Cantor Intersection Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $X$ be a topological space (in particular, compact Hausdorff).
Let $\{K_j\}_{j=1}^\infty$ be a sequence of decreasing, non-empty compact subsets of $X$:
$$K_1 \supseteq K_2 \supseteq K_3 \supseteq \cdots \quad \text{with } K_j \ne \emptyset \text{ for all } j \ge 1.$$
Prove that their intersection is non-empty:
$$\bigcap_{j=1}^\infty K_j \neq \emptyset \quad \text{(Cantor's Intersection Theorem)}.$$
:::

::: {.solution}
**Goal:** Prove that the intersection of a nested sequence of non-empty compact subsets is non-empty using the Finite Intersection Property (FIP) of compact spaces.

::: pf

::: pf-step
Working Inside the Compact Subspace $K_1$:

::: pf-proof

::: pf-step
Since $K_1 \subseteq X$ is compact, endowed with the subspace topology $K_1$ is a **compact topological space**.
:::

::: pf-step
For every $j \ge 1$, since $K_j$ is a compact subset of the Hausdorff space $X$, $K_j$ is a **closed subset of $X$**.
:::

::: pf-step
Since $K_j \subseteq K_1$, each $K_j$ is also a **closed subset of the compact space $K_1$**.
:::

:::

:::

::: pf-step
Finite Intersection Property for the Family $\{K_j\}$:

::: pf-proof

::: pf-step
Let $\{K_{j_1}, K_{j_2}, \dots, K_{j_m}\}$ be any finite subcollection of the family $\{K_j\}_{j=1}^\infty$.
:::

::: pf-step
Let $N = \max(j_1, j_2, \dots, j_m)$.
:::

::: pf-step
Since the sequence is nested ($K_1 \supseteq K_2 \supseteq \cdots \supseteq K_N$):
$$\bigcap_{k=1}^m K_{j_k} = K_N.$$
:::

::: pf-step
By hypothesis, each $K_j$ is non-empty, so $K_N \ne \emptyset$.
:::

::: pf-step
Therefore, every finite subcollection has a non-empty intersection:
$$\bigcap_{k=1}^m K_{j_k} \neq \emptyset.$$
:::

::: pf-step
Thus the collection of closed sets $\{K_j\}_{j=1}^\infty$ has the **Finite Intersection Property (FIP)** in $K_1$.
:::

:::

:::

::: pf-step
Conclusion via Compactness Characterization:

::: pf-proof

::: pf-step
A topological space is compact if and only if every collection of closed subsets with the Finite Intersection Property has a non-empty total intersection.
:::

::: pf-step
Since $K_1$ is compact and $\{K_j\}_{j=1}^\infty$ is a family of closed subsets in $K_1$ satisfying the FIP:
$$\bigcap_{j=1}^\infty K_j \neq \emptyset.$$
:::

:::

:::

::: pf-step
Alternative Direct Proof by Contradiction via Open Covers:

::: pf-proof

::: pf-step
Suppose, for contradiction, that $\bigcap_{j=1}^\infty K_j = \emptyset$.
:::

::: pf-step
Taking complements in the space $K_1$:
$$\bigcup_{j=1}^\infty (K_1 \setminus K_j) = K_1 \setminus \left( \bigcap_{j=1}^\infty K_j \right) = K_1 \setminus \emptyset = K_1.$$
:::

::: pf-step
Since each $K_j$ is closed in $K_1$, each $U_j \coloneqq K_1 \setminus K_j$ is an open subset of $K_1$.
:::

::: pf-step
Thus $\{U_j\}_{j=1}^\infty$ forms an **open cover** of the compact space $K_1$.
:::

::: pf-step
By compactness of $K_1$, there exists a finite subcover $\{U_{j_1}, \dots, U_{j_m}\}$ with $N = \max(j_1, \dots, j_m)$.
:::

::: pf-step
Since $K_1 \supseteq K_2 \supseteq \cdots$, we have $U_1 \subseteq U_2 \subseteq \cdots \subseteq U_N$.
:::

::: pf-step
Thus $\bigcup_{k=1}^m U_{j_k} = U_N = K_1 \setminus K_N = K_1$.
:::

::: pf-step
This implies $K_N = \emptyset$, contradicting the hypothesis that each $K_j$ is non-empty.
:::

:::

:::

::: pf-qed
Conclusion:
The intersection $\bigcap_{j=1}^\infty K_j$ is non-empty.
:::

:::
:::
