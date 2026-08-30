---
schema: qual/card@1
id: P-TOP-WORKSHOP-D2-02
kind: problem
title: Removing a product of proper subsets from a product of connected spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that if $A$ is a proper subset of a connected space $X$ and $B$ is a proper subset of a connected space $Y$, then $(X\times Y)\setminus(A\times B)$ is connected.
:::

::: {.solution}
<1>1. Point selection and set decomposition:
<2>1. Since $A \subsetneq X$ and $B \subsetneq Y$ are proper subsets, choose points $x_0 \in X \setminus A$ and $y_0 \in Y \setminus B$.
Proof: proper subsets have non-empty complements.
<2>2. The complement of the product $A \times B$ decomposes as:
\[
(X \times Y) \setminus (A \times B) = \big((X \setminus A) \times Y\big) \cup \big(X \times (Y \setminus B)\big).
\]
Proof: $(x, y) \notin A \times B \iff x \notin A \text{ or } y \notin B$.

<1>2. Connectedness of the central spine $S$:
<2>1. Define the subspace $S = (\{x_0\} \times Y) \cup (X \times \{y_0\})$.
Proof: definition of $S$.
<2>2. $\{x_0\} \times Y \cong Y$ is connected, and $X \times \{y_0\} \cong X$ is connected.
Their intersection is $(\{x_0\} \times Y) \cap (X \times \{y_0\}) = \{(x_0, y_0)\} \neq \emptyset$.
Thus $S$ is connected.
Proof: union of connected spaces sharing a common point is connected.

<1>3. Connectedness of the total complement:
<2>1. For each $x \in X \setminus A$, the slice $\{x\} \times Y \cong Y$ is connected and contains the point $(x, y_0) \in X \times \{y_0\} \subset S$.
Thus $(\{x\} \times Y) \cap S \neq \emptyset$.
Proof: $(x, y_0) \in S$.
<2>2. For each $y \in Y \setminus B$, the slice $X \times \{y\} \cong X$ is connected and contains the point $(x_0, y) \in \{x_0\} \times Y \subset S$.
Thus $(X \times \{y\}) \cap S \neq \emptyset$.
Proof: $(x_0, y) \in S$.
<2>3. The entire complement can be written as:
\[
(X \times Y) \setminus (A \times B) = S \cup \left(\bigcup_{x \in X \setminus A} (\{x\} \times Y)\right) \cup \left(\bigcup_{y \in Y \setminus B} (X \times \{y\})\right).
\]
Since each constituent subspace is connected and intersects the connected subspace $S$, the entire union is connected.
Proof: a union of connected subspaces that each intersect a fixed connected subspace is connected.

<1>4. Conclusion:
$(X \times Y) \setminus (A \times B)$ is connected. Q.E.D.
Proof: <1>2 and <1>3.
:::
