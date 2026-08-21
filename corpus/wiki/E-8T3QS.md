---
schema: qual/card@1
id: E-8T3QS
kind: exercise
title: The Tychonoff theorem via the well-ordering theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
solved: false
---

Here is a proof of the Tychonoff theorem that relies on the well-ordering theorem rather than on Zorn's lemma. First, prove the following version of the tube lemma; then prove the theorem.

Lemma. Let $\mathcal{A}$ be a collection of basis elements for the topology of the product space $X \times Y$, such that no finite subcollection of $\mathcal{A}$ covers $X \times Y$. If $X$ is compact, there is a point $x \in X$ such that no finite subcollection of $\mathcal{A}$ covers the slice $\ts{x} \times Y$.

Theorem. An arbitrary product of compact spaces is compact in the product topology.

Proof. Let $\ts{X_\alpha}_{\alpha \in J}$ be an indexed family of compact spaces, let

$$
X = \prod_{\alpha \in J} X_\alpha.
$$

Let $\pi_\alpha: X \to X_\alpha$ be the projection map. Well-order $J$, once and for all, in such a way that $J$ has a largest element.

(a) Let $\beta \in J$. Suppose points $p_i \in X_i$ are given, for all $i < \beta$. For any $\alpha < \beta$, let $Y_\alpha$ denote the subspace of $X$ defined by the equation

$$
Y_\alpha = \ts{\mathbf{x} \mid \pi_i(\mathbf{x}) = p_i \text{ for } i \leq \alpha}.
$$

Note that if $\alpha < \alpha'$, then $Y_\alpha \supset Y_{\alpha'}$. Show that if $\mathcal{A}$ is a finite collection of basis elements for $X$ that covers the space

$$
Z_\beta = \bigcap_{\alpha < \beta} Y_\alpha = \ts{\mathbf{x} \mid \pi_i(\mathbf{x}) = p_i \text{ for } i < \beta},
$$

then $\mathcal{A}$ actually covers $Y_\alpha$ for some $\alpha < \beta$. [Hint: If $\beta$ has an immediate predecessor in $J$, let $\alpha$ be that immediate predecessor. Otherwise, for each $A \in \mathcal{A}$, let $J_A$ denote the set of those indices $i < \beta$ for which $\pi_i(A) \neq X_i$; the union of the sets $J_A$, for $A \in \mathcal{A}$, is finite; let $\alpha$ be the largest element of this union.]

(b) Assume $\mathcal{A}$ is a collection of basis elements for $X$ such that no finite subcollection of $\mathcal{A}$ covers $X$. Show that one can choose points $p_i \in X_i$ for all $i$, such that for each $\alpha$, the space $Y_\alpha$ defined in (a) cannot be finitely covered by $\mathcal{A}$. When $\alpha$ is the largest element of $J$, one has a contradiction. [Hint: If $\alpha$ is the smallest element of $J$, use the preceding lemma to choose $p_\alpha$. If $p_i$ is defined for all $i < \beta$, note that (a) implies that the space $Z_\beta$ cannot be finitely covered by $\mathcal{A}$ and use the lemma to find $p_\beta$.]

::: {.remark}
Munkres, *Topology*, §37 Exercise 5 (starred in the text).
:::
