---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-04
kind: problem
title: All fibers of a cover over a connected base have the same finite cardinality
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(Purdue Jan ’09) Let $p:E\to B$ be a covering map with $B$ connected.
Suppose that $p^{-1}(b_0)$ is finite for some $b_0\in B$.
Prove that, for every $b\in B$, $p^{-1}(b)$ has the same number of elements as $p^{-1}(b_0)$.
:::

::: {.solution}
<1>1. Local constancy of fiber cardinality:
<2>1. By definition of a covering map, for each point $x \in B$, there exists an open neighborhood $U \subset B$ that is evenly covered by $p$:
\[
p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha,
\]
where $\{V_\alpha\}_{\alpha \in A}$ are pairwise disjoint open subsets of $E$ and each restriction $p|_{V_\alpha}: V_\alpha \to U$ is a homeomorphism.
Proof: definition of covering space.
<2>2. For any point $y \in U$, each $V_\alpha$ contains precisely one preimage point $(p|_{V_\alpha})^{-1}(y)$.
Thus the cardinality of the fiber is:
\[
|p^{-1}(y)| = |A| = |p^{-1}(x)| \quad \text{for all } y \in U.
\]
Therefore, the function $c: B \to \mathbb{N} \cup \{\infty\}$ given by $c(b) = |p^{-1}(b)|$ is locally constant.
Proof: homeomorphisms are bijections.

<1>2. Connectedness and constancy of fiber cardinality on $B$:
<2>1. Let $k = |p^{-1}(b_0)| \in \mathbb{N}$, and define the subset:
\[
S = \{b \in B \mid |p^{-1}(b)| = k\} = c^{-1}(\{k\}).
\]
Proof: definition of fiber-cardinality level set.
<2>2. $S$ is non-empty because $b_0 \in S$.
Proof: assumption $|p^{-1}(b_0)| = k$.
<2>3. $S$ is open: for any $b \in S$, let $U_b$ be an evenly covered neighborhood of $b$.
By <1>1, $|p^{-1}(y)| = |p^{-1}(b)| = k$ for all $y \in U_b$, so $U_b \subseteq S$.
Proof: union of open neighborhoods is open.
<2>4. $S$ is closed: its complement is $B \setminus S = \bigcup_{m \neq k} c^{-1}(\{m\})$.
For any $b' \in B \setminus S$, there is an evenly covered neighborhood $U_{b'}$ with $|p^{-1}(y)| = |p^{-1}(b')| \neq k$ for all $y \in U_{b'}$, so $U_{b'} \subseteq B \setminus S$.
Thus $B \setminus S$ is open, making $S$ closed.
Proof: complement of open set is closed.
<2>5. Since $B$ is connected and $S$ is a non-empty clopen subset of $B$, we have $S = B$.
Proof: connectedness of $B$.

<1>3. Conclusion:
$|p^{-1}(b)| = k = |p^{-1}(b_0)|$ for every $b \in B$. Q.E.D.
Proof: <1>1 and <1>2.
:::
