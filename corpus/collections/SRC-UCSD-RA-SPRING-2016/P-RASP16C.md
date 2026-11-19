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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the four containers state why their subclaims suffice, and the 19
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The Goal
    paragraph before the proof was removed, since CONTRIBUTING forbids restating the statement that way.
    The mathematics is unchanged: compact subsets of a Hausdorff space are closed, the nested family has
    the finite intersection property because a finite intersection is its largest member, Theorem 26.9
    turns that into a non-empty total intersection, and the direct argument takes complements in $K_1$,
    where they form an increasing open cover of a compact space. Nothing in the statement was changed.

---

::: {.problem}
Let $X$ be a compact Hausdorff topological space.
Let $\{K_j\}_{j=1}^\infty$ be a sequence of decreasing, non-empty compact subsets of $X$:
$$K_1 \supseteq K_2 \supseteq K_3 \supseteq \cdots \quad \text{with } K_j \ne \emptyset \text{ for all } j \ge 1.$$
Prove that their intersection is non-empty:
$$\bigcap_{j=1}^\infty K_j \neq \emptyset \quad \text{(Cantor's Intersection Theorem)}.$$
:::

::: {.solution}
::: pf

::: pf-step
Working Inside the Compact Subspace $K_1$:

::: pf-proof

::: pf-step
Since $K_1 \subseteq X$ is compact, endowed with the subspace topology $K_1$ is a **compact topological space**.

::: pf-proof
A compact subset of a Hausdorff space is closed (Theorem 26.3), and a closed subset of a compact space is compact, so $K_1$ is compact in its subspace topology.
:::

:::

::: pf-step
For every $j \ge 1$, since $K_j$ is a compact subset of the Hausdorff space $X$, $K_j$ is a **closed subset of $X$**.

::: pf-proof
A compact subset of a Hausdorff space is closed (Theorem 26.3).
:::

:::

::: pf-step
Since $K_j \subseteq K_1$, each $K_j$ is also a **closed subset of the compact space $K_1$**.

::: pf-proof
A subset closed in $X$ and contained in $K_1$ is closed in the subspace $K_1$.
:::

:::

:::

:::

::: pf-step
Finite Intersection Property for the Family $\{K_j\}$:

::: pf-proof

::: pf-step
Let $\{K_{j_1}, K_{j_2}, \dots, K_{j_m}\}$ be any finite subcollection of the family $\{K_j\}_{j=1}^\infty$.

::: pf-proof
This is an arbitrary finite subcollection of the family, which is what the finite intersection property quantifies over.
:::

:::

::: pf-step
Let $N = \max(j_1, j_2, \dots, j_m)$.

::: pf-proof
A non-empty finite set of positive integers has a maximum.
:::

:::

::: pf-step
Since the sequence is nested ($K_1 \supseteq K_2 \supseteq \cdots \supseteq K_N$):
$$\bigcap_{k=1}^m K_{j_k} = K_N.$$

::: pf-proof
Each $K_{j_k}$ contains $K_N$ because $N\ge j_k$ and the sequence is decreasing, and $K_N$ is one of the sets, so the intersection is exactly $K_N$.
:::

:::

::: pf-step
By hypothesis, each $K_j$ is non-empty, so $K_N \ne \emptyset$.

::: pf-proof
The hypothesis says every $K_j$, and in particular $K_N$, is non-empty.
:::

:::

::: pf-step
Therefore, every finite subcollection has a non-empty intersection:
$$\bigcap_{k=1}^m K_{j_k} \neq \emptyset.$$

::: pf-proof
That intersection is $K_N$, which is non-empty by the preceding subclaim.
:::

:::

::: pf-step
Thus the collection of closed sets $\{K_j\}_{j=1}^\infty$ has the **Finite Intersection Property (FIP)** in $K_1$.

::: pf-proof
This is the definition of the finite intersection property: every finite subcollection has non-empty intersection.
:::

:::

:::

:::

::: pf-step
Conclusion via Compactness Characterization:

::: pf-proof

::: pf-step
A topological space is compact if and only if every collection of closed subsets with the Finite Intersection Property has a non-empty total intersection.

::: pf-proof
This is the standard characterization of compactness: a space is compact exactly when every family of closed subsets with the finite intersection property has non-empty intersection (Theorem 26.9).
:::

:::

::: pf-step
Since $K_1$ is compact and $\{K_j\}_{j=1}^\infty$ is a family of closed subsets in $K_1$ satisfying the FIP:
$$\bigcap_{j=1}^\infty K_j \neq \emptyset.$$

::: pf-proof
Apply that characterization in the compact space $K_1$, to the closed family $\{K_j\}$ that has just been shown to satisfy the finite intersection property.
:::

:::

:::

:::

::: pf-step
Alternative Direct Proof by Contradiction via Open Covers:

::: pf-proof

::: pf-step
Suppose, for contradiction, that $\bigcap_{j=1}^\infty K_j = \emptyset$.

::: pf-proof
This is the negation of the assertion to be proved.
:::

:::

::: pf-step
Taking complements in the space $K_1$:
$$\bigcup_{j=1}^\infty (K_1 \setminus K_j) = K_1 \setminus \left( \bigcap_{j=1}^\infty K_j \right) = K_1 \setminus \emptyset = K_1.$$

::: pf-proof
De Morgan's law in the space $K_1$.
:::

:::

::: pf-step
Since each $K_j$ is closed in $K_1$, each $U_j \coloneqq K_1 \setminus K_j$ is an open subset of $K_1$.

::: pf-proof
The complement in $K_1$ of a subset closed in $K_1$ is open in $K_1$.
:::

:::

::: pf-step
Thus $\{U_j\}_{j=1}^\infty$ forms an **open cover** of the compact space $K_1$.

::: pf-proof
Their union is all of $K_1$ by the preceding subclaim, which is what an open cover is.
:::

:::

::: pf-step
By compactness of $K_1$, there exists a finite subcover $\{U_{j_1}, \dots, U_{j_m}\}$ with $N = \max(j_1, \dots, j_m)$.

::: pf-proof
Compactness of $K_1$ supplies finitely many of the $U_j$ covering it, and $N$ is the largest of their indices.
:::

:::

::: pf-step
Since $K_1 \supseteq K_2 \supseteq \cdots$, we have $U_1 \subseteq U_2 \subseteq \cdots \subseteq U_N$.

::: pf-proof
Complementation reverses inclusions, so the decreasing chain $K_1\supseteq K_2\supseteq\cdots$ becomes the increasing chain $U_1\subseteq U_2\subseteq\cdots$.
:::

:::

::: pf-step
Thus $\bigcup_{k=1}^m U_{j_k} = U_N = K_1 \setminus K_N = K_1$.

::: pf-proof
The union of an increasing chain is its largest member, namely $U_N$, and $U_N=K_1\setminus K_N$ by definition.
:::

:::

::: pf-step
This implies $K_N = \emptyset$, contradicting the hypothesis that each $K_j$ is non-empty.

::: pf-proof
If $K_1\setminus K_N=K_1$ then $K_N$ has no point, contradicting the hypothesis that $K_N$ is non-empty.
:::

:::

:::

:::

::: pf-qed
Conclusion:
The intersection $\bigcap_{j=1}^\infty K_j$ is non-empty.
:::

:::
:::
