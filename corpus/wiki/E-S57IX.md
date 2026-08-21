---
schema: qual/card@1
id: E-S57IX
kind: exercise
title: Products of quotient maps with locally compact Hausdorff factors
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Compactness
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §29.11"}


(a) Lemma. If $p: X \to Y$ is a quotient map and if $Z$ is a locally compact Hausdorff space, then the map

$$
\pi = p \times i_Z: X \times Z \to Y \times Z
$$

is a quotient map.

[Hint: If $\pi^{-1}(A)$ is open and contains $x \times y$, choose open sets $U_1$ and $V$ with $\overline{V}$ compact, such that $x \times y \in U_1 \times V$ and $U_1 \times \overline{V} \subset \pi^{-1}(A)$. Given $U_i \times \overline{V} \subset \pi^{-1}(A)$, use the tube lemma to choose an open set $U_{i+1}$ containing $p^{-1}(p(U_i))$ such that $U_{i+1} \times \overline{V} \subset \pi^{-1}(A)$. Let $U = \bigcup U_i$; show that $U \times V$ is a saturated neighborhood of $x \times y$ that is contained in $\pi^{-1}(A)$.]

An entirely different proof of this result will be outlined in the exercises of §46.

(b) Theorem. Let $p: A \to B$ and $q: C \to D$ be quotient maps. If $B$ and $C$ are locally compact Hausdorff spaces, then $p \times q: A \times C \to B \times D$ is a quotient map.
:::
