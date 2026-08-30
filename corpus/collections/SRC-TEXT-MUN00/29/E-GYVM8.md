---
schema: qual/card@1
id: E-GYVM8
kind: exercise
title: Compactness characterized by subnets
classification:
  areas:
  - topology
  topics:
  - Nets
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
$X$ is compact if and only if every net in $X$ has a convergent subnet.

[Hint: To prove the implication $\Rightarrow$, let $B_\alpha = \ts{x_\beta \mid \alpha \preceq \beta}$ and show that $\ts{B_\alpha}$ has the finite intersection property. To prove $\Leftarrow$, let $\mathcal{A}$ be a collection of closed sets having the finite intersection property, and let $\mathcal{B}$ be the collection of all finite intersections of elements of $\mathcal{A}$, partially ordered by reverse inclusion.]
:::

::: {.solution}
<1>1. Equivalence of convergent subnets and cluster points:
<2>1. A point $x \in X$ is a **cluster point** of a net $(x_\alpha)_{\alpha \in A}$ if for every neighborhood $U$ of $x$ and every $\alpha \in A$, there exists $\beta \succeq \alpha$ such that $x_\beta \in U$.
Proof: definition of net cluster point.
<2>2. A net $(x_\alpha)_{\alpha \in A}$ has a convergent subnet converging to $x$ if and only if $x$ is a cluster point of $(x_\alpha)$.
Proof: standard characterization of subnets.

<1>2. Forward direction ($\implies$): Compactness implies every net has a convergent subnet:
<2>1. Let $X$ be compact, and let $(x_\alpha)_{\alpha \in A}$ be a net in $X$.
For each $\alpha \in A$, define the tail set $T_\alpha = \{x_\beta \mid \beta \succeq \alpha\}$ and its closed closure $F_\alpha = \overline{T_\alpha}$.
Proof: definition of closed tails.
<2>2. The family $\{F_\alpha\}_{\alpha \in A}$ has the Finite Intersection Property (FIP):
For any finite collection $\{\alpha_1, \dots, \alpha_n\} \subseteq A$, directedness of $A$ provides $\gamma \in A$ with $\gamma \succeq \alpha_i$ for all $1 \le i \le n$.
Then $x_\gamma \in T_{\alpha_i} \subseteq F_{\alpha_i}$ for each $i$, so $x_\gamma \in \bigcap_{i=1}^n F_{\alpha_i} \neq \emptyset$.
Proof: directedness of $A$.
<2>3. Since $X$ is compact and $\{F_\alpha\}$ has the FIP, the total intersection is non-empty:
\[
\bigcap_{\alpha \in A} F_\alpha = \bigcap_{\alpha \in A} \overline{T_\alpha} \neq \emptyset.
\]
Proof: FIP characterization of compactness.
<2>4. Choose $x \in \bigcap_{\alpha \in A} \overline{T_\alpha}$.
For every neighborhood $U$ of $x$ and any $\alpha \in A$, $x \in \overline{T_\alpha} \implies U \cap T_\alpha \neq \emptyset$.
Thus there exists $\beta \succeq \alpha$ with $x_\beta \in U$, so $x$ is a cluster point of $(x_\alpha)$.
By <1>1, $(x_\alpha)$ has a subnet converging to $x$.
Proof: topological closure definition.

<1>3. Reverse direction ($\impliedby$): Every net having a convergent subnet implies compactness:
<2>1. We show that every family of closed sets with the FIP has non-empty intersection.
Let $\mathcal{A}$ be a family of closed subsets of $X$ with the FIP.
Let $\mathcal{B}$ be the collection of all non-empty finite intersections of members of $\mathcal{A}$:
\[
\mathcal{B} = \{F_1 \cap \dots \cap F_n \mid F_i \in \mathcal{A}, \, n \ge 1\}.
\]
Proof: definition of finite intersections.
<2>2. Direct $\mathcal{B}$ by reverse inclusion: $B_1 \preceq B_2 \iff B_2 \subseteq B_1$.
For any $B_1, B_2 \in \mathcal{B}$, $B_1 \cap B_2 \in \mathcal{B}$ with $B_1 \cap B_2 \subseteq B_1, B_2$, so $B_1 \cap B_2 \succeq B_1, B_2$. Thus $(\mathcal{B}, \preceq)$ is a directed set.
Proof: closure of $\mathcal{B}$ under finite intersections.
<2>3. For each $B \in \mathcal{B}$, choose an element $x_B \in B$.
This defines a net $(x_B)_{B \in \mathcal{B}}$ in $X$.
By hypothesis, this net has a convergent subnet, hence a cluster point $x \in X$.
Proof: Axiom of Choice and hypothesis.
<2>4. For any $F \in \mathcal{A}$, note $F \in \mathcal{B}$.
For all $B \succeq F$ in $\mathcal{B}$, $B \subseteq F$, so $x_B \in B \subseteq F$.
Thus the tail $\{x_B \mid B \succeq F\} \subseteq F$.
Since $F$ is closed and $x$ is a cluster point of $(x_B)$, we have $x \in \overline{\{x_B \mid B \succeq F\}} \subseteq \overline{F} = F$.
Proof: closed sets contain all cluster points of their sub-tails.
<2>5. Since $x \in F$ for every $F \in \mathcal{A}$, we obtain $x \in \bigcap_{F \in \mathcal{A}} F \neq \emptyset$.
Thus $X$ is compact.
Proof: FIP characterization of compactness.

<1>4. Conclusion:
$X$ is compact if and only if every net in $X$ has a convergent subnet. Q.E.D.
Proof: <1>2 and <1>3.
:::
