---
schema: qual/card@1
id: E-GZX7B
kind: exercise
title: Components of locally compact paracompact Hausdorff spaces are second countable
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Theorem.
If $X$ is a Hausdorff space that is locally compact and paracompact, then each component of $X$ has a countable basis.

Proof.
If $X_0$ is a component of $X$, then $X_0$ is locally compact and paracompact.
Let $\mathcal{C}$ be a locally finite covering of $X_0$ by sets open in $X_0$ that have compact closures.
Let $U_1$ be a nonempty element of $\mathcal{C}$, and in general let $U_n$ be the union of all elements of $\mathcal{C}$ that intersect $\overline{U}_{n-1}$.
Show that $\overline{U}_n$ is compact, and the sets $U_n$ cover $X_0$.
:::

::: {.solution}
<1>1. Show that $\overline{U}_n$ is compact for every $n \ge 1$ by induction: <2>1. **Base case $n = 1$:** $U_1 \in \mathcal{C}$.
By the construction of $\mathcal{C}$, every element of $\mathcal{C}$ has compact closure, so $\overline{U}_1$ is compact.
Proof: definition of $\mathcal{C}$.
<2>2. **Inductive step:** Assume $\overline{U}_{n-1}$ is compact for $n \ge 2$.
Proof: induction hypothesis.
<2>3. Let $\mathcal{C}_n = \{V \in \mathcal{C} : V \cap \overline{U}_{n-1} \neq \emptyset\}$, so $U_n = \bigcup_{V \in \mathcal{C}_n} V$.
Proof: definition of $U_n$.
<2>4. Since $\mathcal{C}$ is a locally finite collection in the Hausdorff space $X_0$, each point $x \in \overline{U}_{n-1}$ has an open neighborhood $W_x$ that intersects only finitely many elements of $\mathcal{C}$.
Proof: definition of local finiteness.
<2>5. The collection $\{W_x : x \in \overline{U}_{n-1}\}$ is an open cover of the compact set $\overline{U}_{n-1}$.
By compactness, there exist finitely many points $x_1, \dots, x_k$ such that $\overline{U}_{n-1} \subseteq \bigcup_{i=1}^k W_{x_i}$.
Proof: definition of compactness.
<2>6. Since each $W_{x_i}$ meets only finitely many elements of $\mathcal{C}$, the union $\bigcup_{i=1}^k W_{x_i}$ meets only finitely many elements of $\mathcal{C}$.
Therefore $\mathcal{C}_n = \{V_1, \dots, V_m\}$ is a **finite** set of open sets.
Proof: finite union of finite sets is finite.
<2>7. The closure of a finite union is the union of closures:
\[
\overline{U}_n = \overline{V_1 \cup \cdots \cup V_m} = \overline{V}_1 \cup \cdots \cup \overline{V}_m.
\]
Proof: properties of topological closure.
<2>8. Since each $\overline{V}_i$ is compact, $\overline{U}_n$ is a finite union of compact sets, hence compact.
Proof: finite unions of compact sets are compact.

<1>2. Show that $A = \bigcup_{n=1}^\infty U_n$ equals $X_0$: <2>1. Since $U_1 \neq \emptyset$, $A \neq \emptyset$.
Proof: $U_1 \subseteq A$.
<2>2. Each $U_n$ is a union of open sets in $X_0$, so each $U_n$ is open in $X_0$.
Thus $A = \bigcup_{n=1}^\infty U_n$ is open in $X_0$.
Proof: arbitrary unions of open sets are open.
<2>3. Show that $A$ is closed in $X_0$: Let $x \in \overline{A}$.
Since $\mathcal{C}$ is a covering of $X_0$, there exists some $V_0 \in \mathcal{C}$ containing $x$.
Proof: $\mathcal{C}$ covers $X_0$.
<2>4. Since $V_0$ is an open neighborhood of $x$ and $x \in \overline{A}$, we have $V_0 \cap A \neq \emptyset$.
Proof: characterization of closure points.
<2>5. Since $A = \bigcup_{n=1}^\infty U_n$, $V_0 \cap U_{n-1} \neq \emptyset$ for some $n \ge 2$.
Proof: union definition.
<2>6. Since $U_{n-1} \subseteq \overline{U}_{n-1}$, $V_0 \cap \overline{U}_{n-1} \neq \emptyset$.
By the definition of $U_n$, this implies $V_0 \subseteq U_n \subseteq A$.
Proof: definition of $U_n$ in <1>1. <2>7. Since $x \in V_0 \subseteq A$, we have $x \in A$.
Thus $\overline{A} = A$, so $A$ is closed in $X_0$.
Proof: <2>3 through <2>6. <2>8. Since $X_0$ is a connected component of $X$, $X_0$ is connected.
The only non-empty clopen subset of a connected space is the space itself, so $A = X_0$.
Proof: connectedness of $X_0$.

<1>3. Conclusion: Each $\overline{U}_n$ is compact, and $\bigcup_{n=1}^\infty U_n = X_0$.
Q.E.D. Proof: <1>1 and <1>2.
:::
