---
schema: qual/card@1
id: E-0NSGA
kind: problem
title: Products of compact sets in topological groups
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $G$ be a topological group.

(a) Let $A$ and $B$ be subspaces of $G$.
If $A$ is closed and $B$ is compact, show $A \cdot B$ is closed.
[Hint: If $c$ is not in $A \cdot B$, find a neighborhood $W$ of $c$ such that $W \cdot B^{-1}$ is disjoint from $A$.]

(b) Let $H$ be a subgroup of $G$; let $p: G \to G/H$ be the quotient map.
If $H$ is compact, show that $p$ is a closed map.

(c) Let $H$ be a compact subgroup of $G$.
Show that if $G/H$ is compact, then $G$ is compact.
:::

::: solution
**Goal:** Prove that the product of a closed set and a compact set in a topological group is closed, deduce that quotient maps by compact subgroups are closed, and prove that group extensions by compact groups are compact.

<1>1. Part (a): If $A$ is closed and $B$ is compact in a topological group $G$, then $A \cdot B$ is closed.
    *Proof:*
    <2>1. We show that $G \setminus (A \cdot B)$ is open. Let $c \in G \setminus (A \cdot B)$.
    <2>2. Then for every $b \in B$, $c b^{-1} \notin A$, so $c b^{-1} \in G \setminus A$.
    <2>3. Since $A$ is closed, $G \setminus A$ is open.
    <2>4. The map $\phi: G \times G \to G$ defined by $\phi(x, y) = x y^{-1}$ is continuous.
    <2>5. For each $b \in B$, since $\phi(c, b) = c b^{-1} \in G \setminus A$, continuity of $\phi$ provides open neighborhoods $U_b$ of $c$ and $V_b$ of $b$ such that $U_b \cdot V_b^{-1} \subseteq G \setminus A$.
    <2>6. The open sets $\{V_b : b \in B\}$ cover the compact set $B$. Choose a finite subcover $V_{b_1}, \dots, V_{b_k}$ of $B$.
    <2>7. Define $W = \bigcap_{i=1}^k U_{b_i}$. As a finite intersection of open neighborhoods of $c$, $W$ is an open neighborhood of $c$.
    <2>8. For any $w \in W$ and $b \in B$, $b \in V_{b_i}$ for some $i$, so $w b^{-1} \in U_{b_i} \cdot V_{b_i}^{-1} \subseteq G \setminus A$, meaning $w b^{-1} \notin A$.
    <2>9. Thus $w \notin A \cdot B$ for all $w \in W$, so $W \cap (A \cdot B) = \emptyset$.
    <2>10. Hence $W \subseteq G \setminus (A \cdot B)$, proving that $G \setminus (A \cdot B)$ is open and $A \cdot B$ is closed.

<1>2. Part (b): If $H \le G$ is compact, then the quotient map $p: G \to G/H$ is a closed map.
    *Proof:*
    <2>1. Let $C \subseteq G$ be closed.
    <2>2. Under the quotient topology on $G/H$, $p(C)$ is closed in $G/H$ if and only if $p^{-1}(p(C))$ is closed in $G$.
    <2>3. We identify $p^{-1}(p(C))$:
        $$p^{-1}(p(C)) = \{g \in G : gH \in p(C)\} = \{g \in G : gH = cH \text{ for some } c \in C\} = C \cdot H.$$
    <2>4. Since $C$ is closed and $H$ is compact, by <1>1 the product $C \cdot H$ is closed in $G$.
    <2>5. Thus $p^{-1}(p(C))$ is closed in $G$, so $p(C)$ is closed in $G/H$. Hence $p$ is a closed map.

<1>3. Part (c): If $H \le G$ is compact and $G/H$ is compact, then $G$ is compact.
    *Proof:*
    <2>1. Let $\mathcal{U} = \{O_\alpha\}_{\alpha \in I}$ be an open cover of $G$.
    <2>2. For each $x \in G$, the coset $xH = L_x(H)$ is compact as the continuous image of the compact set $H$ under the left translation homeomorphism $L_x$.
    <2>3. Since $xH$ is compact, there exists a finite subset $I_x \subset I$ such that $xH \subseteq V_x := \bigcup_{\alpha \in I_x} O_\alpha$.
    <2>4. The set $V_x$ is open in $G$, so $C_x = G \setminus V_x$ is closed in $G$.
    <2>5. By <1>2, $p$ is a closed map, so $p(C_x)$ is closed in $G/H$, and $W_x = (G/H) \setminus p(C_x)$ is open in $G/H$.
    <2>6. Since $xH \cap C_x = \emptyset$, $xH \notin p(C_x)$, so $xH \in W_x$.
    <2>7. If $yH \in W_x$, then $yH \cap C_x = \emptyset$, so $yH \subseteq V_x = \bigcup_{\alpha \in I_x} O_\alpha$.
    <2>8. The family $\{W_x : xH \in G/H\}$ is an open cover of $G/H$.
    <2>9. Since $G/H$ is compact, there exist finitely many points $x_1, \dots, x_m \in G$ such that $G/H = \bigcup_{j=1}^m W_{x_j}$.
    <2>10. Therefore $G = \bigcup_{j=1}^m p^{-1}(W_{x_j}) \subseteq \bigcup_{j=1}^m V_{x_j} = \bigcup_{j=1}^m \bigcup_{\alpha \in I_{x_j}} O_\alpha$.
    <2>11. This is a finite subcover of $\mathcal{U}$ covering $G$. Hence $G$ is compact. Q.E.D.
:::
