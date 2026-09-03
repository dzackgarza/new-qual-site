---
schema: qual/card@1
id: E-54CQC
kind: problem
title: Local homeomorphisms of compact Hausdorff spaces are covering maps
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Compactness
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that a local homeomorphism between compact Hausdorff spaces is a covering space.
:::

::: solution
**Goal:** Prove that if $E$ and $B$ are compact Hausdorff spaces (with $p$ surjective, or $B$ connected and $E \neq \varnothing$), any local homeomorphism $p: E \to B$ is a finite-sheeted covering map.

<1>1. Properties of $p$ (surjectivity and closedness): *Proof:* <2>1. A local homeomorphism is an open map, so $p(E)$ is open in $B$.
<2>2. Since $E$ is compact and $B$ is Hausdorff, $p(E)$ is compact and therefore closed in $B$.
<2>3. If $B$ is connected and $E \neq \varnothing$, $p(E)$ is a non-empty clopen subset of $B$, so $p(E) = B$ (surjective).
(If $B$ is not connected, we restrict to the clopen component $p(E)$.)
<2>4. Because every closed subset $C \subseteq E$ is compact, $p(C)$ is compact and thus closed in $B$, so $p$ is a closed map.

<1>2. Finiteness of fibers: For every $b \in B$, the fiber $p^{-1}(b)$ is finite.
*Proof:* <2>1. The fiber $p^{-1}(b)$ is closed in the compact space $E$, hence compact.
<2>2. For each $x \in p^{-1}(b)$, local homeomorphy provides an open neighborhood $U_x \subseteq E$ such that $p|_{U_x}: U_x \to p(U_x)$ is a homeomorphism.
<2>3. In particular, $U_x \cap p^{-1}(b) = \{x\}$, showing that $p^{-1}(b)$ is a discrete subspace.
<2>4. A compact discrete space is finite, so $p^{-1}(b) = \{x_1, \dots, x_k\}$ for some integer $k \ge 1$.

<1>3. Construction of an evenly covered neighborhood: For any $b \in B$, there exists an open neighborhood $V \subseteq B$ of $b$ that is evenly covered by $p$.
*Proof:* <2>1. Since $E$ is Hausdorff, choose pairwise disjoint open neighborhoods $U_1, \dots, U_k$ of $x_1, \dots, x_k$ such that each $p|_{U_i}: U_i \to p(U_i)$ is a homeomorphism.
<2>2. The set $K = E \setminus \bigcup_{i=1}^k U_i$ is closed in $E$, hence compact.
<2>3. Its image $p(K)$ is compact, hence closed in $B$.
<2>4. Since $p^{-1}(b) \subseteq \bigcup_{i=1}^k U_i$, we have $b \notin p(K)$, so $B \setminus p(K)$ is an open neighborhood of $b$.
<2>5. Define $V = (B \setminus p(K)) \cap \bigcap_{i=1}^k p(U_i)$.
<2>6. Since local homeomorphisms are open maps, each $p(U_i)$ is open, so $V$ is an open neighborhood of $b$ in $B$.
<2>7. Since $V \subseteq B \setminus p(K)$, $p^{-1}(V)$ is disjoint from $K$, so: $$p^{-1}(V) \subseteq \bigcup_{i=1}^k U_i \implies p^{-1}(V) = \bigsqcup_{i=1}^k (U_i \cap p^{-1}(V)) = \bigsqcup_{i=1}^k V_i,$$ where $V_i = U_i \cap p^{-1}(V)$ are pairwise disjoint open sets in $E$.
<2>8. For each $i \in \{1, \dots, k\}$, $p|_{V_i}: V_i \to V$ is a homeomorphism because it is the restriction of the homeomorphism $p|_{U_i}$ to the open set $V_i = (p|_{U_i})^{-1}(V)$.

<1>4. Conclusion: Every point $b \in B$ has an evenly covered neighborhood $V$.
Therefore $p: E \to B$ is a covering map.
Q.E.D.
:::
