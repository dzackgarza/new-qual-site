---
schema: qual/card@1
id: E-8T3QS
kind: problem
title: The Tychonoff theorem via the well-ordering theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Here is a proof of the Tychonoff theorem that relies on the well-ordering theorem rather than on Zorn's lemma.
First, prove the following version of the tube lemma; then prove the theorem.

Lemma.
Let $\mathcal{A}$ be a collection of basis elements for the topology of the product space $X \times Y$, such that no finite subcollection of $\mathcal{A}$ covers $X \times Y$.
If $X$ is compact, there is a point $x \in X$ such that no finite subcollection of $\mathcal{A}$ covers the slice $\ts{x} \times Y$.

Theorem.
An arbitrary product of compact spaces is compact in the product topology.

Proof.
Let $\ts{X_\alpha}_{\alpha \in J}$ be an indexed family of compact spaces, let

$$
X = \prod_{\alpha \in J} X_\alpha.
$$

Let $\pi_\alpha: X \to X_\alpha$ be the projection map.
Well-order $J$, once and for all, in such a way that $J$ has a largest element.

(a) Let $\beta \in J$.
Suppose points $p_i \in X_i$ are given, for all $i < \beta$.
For any $\alpha < \beta$, let $Y_\alpha$ denote the subspace of $X$ defined by the equation

$$
Y_\alpha = \ts{\mathbf{x} \mid \pi_i(\mathbf{x}) = p_i \text{ for } i \leq \alpha}.
$$

Note that if $\alpha < \alpha'$, then $Y_\alpha \supset Y_{\alpha'}$.
Show that if $\mathcal{A}$ is a finite collection of basis elements for $X$ that covers the space

$$
Z_\beta = \bigcap_{\alpha < \beta} Y_\alpha = \ts{\mathbf{x} \mid \pi_i(\mathbf{x}) = p_i \text{ for } i < \beta},
$$

then $\mathcal{A}$ actually covers $Y_\alpha$ for some $\alpha < \beta$.
[Hint: If $\beta$ has an immediate predecessor in $J$, let $\alpha$ be that immediate predecessor. Otherwise, for each $A \in \mathcal{A}$, let $J_A$ denote the set of those indices $i < \beta$ for which $\pi_i(A) \neq X_i$; the union of the sets $J_A$, for $A \in \mathcal{A}$, is finite; let $\alpha$ be the largest element of this union.]

(b) Assume $\mathcal{A}$ is a collection of basis elements for $X$ such that no finite subcollection of $\mathcal{A}$ covers $X$.
Show that one can choose points $p_i \in X_i$ for all $i$, such that for each $\alpha$, the space $Y_\alpha$ defined in (a) cannot be finitely covered by $\mathcal{A}$.
When $\alpha$ is the largest element of $J$, one has a contradiction.
[Hint: If $\alpha$ is the smallest element of $J$, use the preceding lemma to choose $p_\alpha$. If $p_i$ is defined for all $i < \beta$, note that (a) implies that the space $Z_\beta$ cannot be finitely covered by $\mathcal{A}$ and use the lemma to find $p_\beta$.]
:::

::: solution
**Goal:** Prove the Lemma (generalized Tube Lemma for slices) and complete the transfinite induction proof of the Tychonoff Product Theorem via the Well-Ordering Theorem.

<1>1. Proof of the Lemma (Tube Lemma version for slices):
    *Proof:*
    <2>1. Suppose for contradiction that for every $x \in X$, there exists a finite subcollection $\mathcal{A}_x \subset \mathcal{A}$ that covers $\{x\} \times Y$.
    <2>2. The union $U_x = \bigcup_{A \in \mathcal{A}_x} A$ is an open set in $X \times Y$ containing the slice $\{x\} \times Y$.
    <2>3. Because $Y$ is compact (or simply by the Tube Lemma since $\{x\}$ is compact and $U_x$ contains the slice), there exists an open neighborhood $W_x$ of $x$ in $X$ such that $W_x \times Y \subseteq U_x$.
    <2>4. The collection $\{W_x\}_{x \in X}$ forms an open covering of the compact space $X$.
    <2>5. There exists a finite subcover $\{W_{x_1}, \dots, W_{x_k}\}$ of $X$.
    <2>6. Then the finite collection $\bigcup_{j=1}^k \mathcal{A}_{x_j} \subset \mathcal{A}$ covers $\bigcup_{j=1}^k (W_{x_j} \times Y) = X \times Y$, contradicting the hypothesis that no finite subcollection of $\mathcal{A}$ covers $X \times Y$.
    <2>7. Thus there exists $x \in X$ such that no finite subcollection of $\mathcal{A}$ covers $\{x\} \times Y$.

<1>2. Proof of Part (a):
    *Proof:*
    <2>1. Let $\mathcal{A}_0 \subset \mathcal{A}$ be a finite collection of basic open sets covering $Z_\beta$.
    <2>2. For each $A \in \mathcal{A}_0$, let $J_A = \{i < \beta \mid \pi_i(A) \neq X_i\}$. Since each $A$ is a basic open set in the product topology, $J_A$ is finite.
    <2>3. Because $\mathcal{A}_0$ is finite, the union $F = \bigcup_{A \in \mathcal{A}_0} J_A \subset \{i \in J \mid i < \beta\}$ is finite.
    <2>4. If $F = \varnothing$, let $\alpha$ be any index less than $\beta$. If $F \neq \varnothing$, let $\alpha = \max F < \beta$.
    <2>5. Let $\mathbf{x} \in Y_\alpha$, so $\pi_i(\mathbf{x}) = p_i$ for all $i \le \alpha$.
    <2>6. Construct a point $\mathbf{x}' \in Z_\beta$ by setting $\pi_i(\mathbf{x}') = p_i$ for all $i < \beta$, and $\pi_i(\mathbf{x}') = \pi_i(\mathbf{x})$ for all $i \ge \beta$.
    <2>7. Since $\mathcal{A}_0$ covers $Z_\beta$, $\mathbf{x}' \in A$ for some $A \in \mathcal{A}_0$.
    <2>8. For all $i \in J$, if $i \le \alpha$, $\pi_i(\mathbf{x}) = p_i = \pi_i(\mathbf{x}') \in \pi_i(A)$. If $\alpha < i < \beta$, $i \notin F$, so $\pi_i(A) = X_i$, hence $\pi_i(\mathbf{x}) \in \pi_i(A)$. If $i \ge \beta$, $\pi_i(\mathbf{x}) = \pi_i(\mathbf{x}') \in \pi_i(A)$.
    <2>9. Thus $\mathbf{x} \in A$, so $\mathcal{A}_0$ covers $Y_\alpha$.

<1>3. Proof of Part (b) and Theorem:
    *Proof:*
    <2>1. Assume $\mathcal{A}$ is a basic open cover of $X$ with no finite subcover.
    <2>2. Well-order $J$ so that $J$ has a maximum element $\Omega = \max J$.
    <2>3. By transfinite induction, we choose $p_\beta \in X_\beta$ for each $\beta \in J$ such that $Y_\beta$ cannot be covered by any finite subcollection of $\mathcal{A}$:
        - For the minimal element $0 \in J$, $X \cong X_0 \times \prod_{\alpha > 0} X_\alpha$. By <1>1, choose $p_0 \in X_0$ such that $Y_0 = \{p_0\} \times \prod_{\alpha > 0} X_\alpha$ is not finitely covered.
        - Assuming $p_i$ is defined for all $i < \beta$, Part (a) implies $Z_\beta$ cannot be finitely covered by $\mathcal{A}$.
        - Writing $Z_\beta \cong X_\beta \times \prod_{j > \beta} X_j$, applying <1>1 to the compact factor $X_\beta$ produces $p_\beta \in X_\beta$ such that $Y_\beta$ cannot be finitely covered by $\mathcal{A}$.
    <2>4. For the maximal element $\Omega = \max J$, $Y_\Omega = \{(p_i)_{i \in J}\}$ is a single point in $X$.
    <2>5. Since $\mathcal{A}$ covers $X$, the single point $Y_\Omega$ is covered by a single element of $\mathcal{A}$, contradicting the fact that $Y_\Omega$ cannot be finitely covered.
    <2>6. Therefore, every basic open cover of $X$ has a finite subcover, proving $X = \prod_{\alpha \in J} X_\alpha$ is compact. Q.E.D.
:::
