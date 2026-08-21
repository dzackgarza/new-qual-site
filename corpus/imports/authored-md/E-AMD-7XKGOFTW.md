---
schema: qual/card@1
id: E-AMD-7XKGOFTW
kind: exercise
title: Nilpotent groups have nontrivial centers
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Centralizers and Normalizers
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that nilpotent groups have nontrivial centers.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $G$ be a non-trivial nilpotent group (i.e., $G \neq \{e\}$). Prove that the center $Z(G)$ is non-trivial, i.e., $Z(G) \neq \{e\}$.

<1>1. Definition of a nilpotent group via the upper central series: <2>1. The upper central series of $G$ is the sequence of normal subgroups $\{Z_i(G)\}_{i \ge 0}$ defined by: - $Z_0(G) = \{e\}$, - $Z_1(G) = Z(G)$, - $Z_{i+1}(G) / Z_i(G) = Z(G / Z_i(G))$, meaning $Z_{i+1}(G) = \{x \in G \mid [x, g] \in Z_i(G) \text{ for all } g \in G\}$.
Proof: Standard definition of the upper central series.
<2>2. A group $G$ is nilpotent if and only if there exists a non-negative integer $c \ge 0$ such that $Z_c(G) = G$.
The minimal such integer $c$ is called the nilpotency class of $G$.
Proof: Standard definition of group nilpotency.

<1>2. Proof that $Z(G) \neq \{e\}$ when $G \neq \{e\}$: <2>1. Since $G$ is nilpotent, there exists $c \ge 0$ such that $Z_c(G) = G$.
Proof: By <1>1.<2>2. <2>2. Since $G \neq \{e\}$, we must have $c \ge 1$.
Proof: If $c = 0$, then $G = Z_0(G) = \{e\}$, contradicting $G \neq \{e\}$.
<2>3. Consider the least integer $k \ge 1$ such that $Z_k(G) \neq \{e\}$.
Proof: The set of positive integers $\{m \ge 1 \mid Z_m(G) \neq \{e\}\}$ is non-empty because $c$ belongs to it ($Z_c(G) = G \neq \{e\}$). By the Well-Ordering Principle of the positive integers, this set has a least element $k \ge 1$.
<2>4. For this least integer $k$, we must have $k = 1$.
<3>1. By definition of $k$ as the minimal positive integer with $Z_k(G) \neq \{e\}$, we have $Z_{k-1}(G) = \{e\}$.
Proof: If $k-1 \ge 1$, then $Z_{k-1}(G)$ must be $\{e\}$ by minimality of $k$.
If $k = 1$, $Z_{k-1}(G) = Z_0(G) = \{e\}$ by definition.
<3>2. By the recursive definition of the upper central series (<1>1.<2>1), $Z_k(G) / Z_{k-1}(G) = Z(G / Z_{k-1}(G))$.
Proof: Definition of $Z_k(G)$.
<3>3. Substituting $Z_{k-1}(G) = \{e\}$ gives: $$Z_k(G) / \{e\} \cong Z_k(G) = Z(G / \{e\}) \cong Z(G) = Z_1(G).$$ Proof: Quotient by the trivial subgroup $\{e\}$ is the group itself.
<3>4. Therefore, $Z_1(G) = Z_k(G)$.
Since $Z_k(G) \neq \{e\}$, we have $Z_1(G) = Z(G) \neq \{e\}$.
Proof: $Z_k(G) \neq \{e\}$ by choice of $k$.
<3>5. Q.E.D. Proof: This forces $k = 1$ and $Z_1(G) = Z(G) \neq \{e\}$.
<2>5. Consequently, $Z(G)$ contains elements other than the identity $e$.
Proof: $Z(G) \neq \{e\}$.

<1>3. Alternative proof via the lower central series (for finite or general groups with terminating series): <2>1. The lower central series is defined by $\gamma_1(G) = G$ and $\gamma_{i+1}(G) = [\gamma_i(G), G]$.
Proof: Standard definition.
<2>2. $G$ is nilpotent of class $c$ if and only if $\gamma_{c+1}(G) = \{e\}$ and $\gamma_c(G) \neq \{e\}$.
Proof: Equivalence of nilpotency characterizations.
<2>3. Since $\gamma_{c+1}(G) = [\gamma_c(G), G] = \{e\}$, every element $x \in \gamma_c(G)$ satisfies $[x, g] = e$ for all $g \in G$, which means $\gamma_c(G) \subseteq Z(G)$.
Proof: Commutator $[x, g] = e \iff x g = g x$.
<2>4. Since $\gamma_c(G) \neq \{e\}$ and $\gamma_c(G) \subseteq Z(G)$, $Z(G)$ must be non-trivial.
Proof: A superset of a non-trivial set is non-trivial.

<1>4. Conclusion: Every non-trivial nilpotent group has a non-trivial center.
Proof: By <1>2 and <1>3.
:::
