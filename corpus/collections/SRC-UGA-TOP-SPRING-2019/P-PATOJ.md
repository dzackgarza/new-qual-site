---
schema: qual/card@1
id: P-PATOJ
kind: problem
title: The one-point compactification of a Hausdorff space is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Point-Set Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Spring 2019 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the topology axioms, including the Hausdorff compact-complement argument for arbitrary unions, and the finite-subcover proof of compactness.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the five containers state why their subclaims suffice, and the 18
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged and was re-read in the course of writing the justifications: the two axioms
    of a topology, with the Hausdorff property used exactly where a compact set has to be closed (the
    arbitrary-union case, the finite-intersection case, and the trace V_i = U_i cap X), De Morgan in both
    complement computations, and the finite-subcover argument from K = X* minus U_{i_0}. Checked against
    the statement on the card, problem 2 of the UGA Spring 2019 topology exam. Nothing in the statement
    was changed.
---

::: {.problem}
Let $X$ be a Hausdorff space, and recall that the *one-point compactification* $X^* = X \cup \{\infty\}$ (where $\infty \notin X$) is defined with the collection of open sets $\mathcal{T}^*$ such that $U \subseteq X^*$ belongs to $\mathcal{T}^*$ if and only if either:
1. $U \subseteq X$ and $U$ is open in $X$, or
2. $\infty \in U$ and $X \setminus U$ is a compact subset of $X$.

Prove that $\mathcal{T}^*$ defines a topology on $X^*$ and that $(X^*, \mathcal{T}^*)$ is a compact space.
:::

::: {.solution}
::: pf

::: pf-step
$\mathcal{T}^*$ contains $\emptyset$ and $X^*$:

::: pf-proof
The subclaims treat the two defining conditions separately.

::: pf-step
The empty set $\emptyset \subseteq X$ is open in $X$, so $\emptyset \in \mathcal{T}^*$ by condition (1).

::: pf-proof
The empty set is open in every topological space, so condition (1) applies to it.
:::

:::

::: pf-step
The whole space $X^*$ contains $\infty$, and $X \setminus X^* = \emptyset$.

::: pf-proof
Every point of $X^*$ lies in $X$ or equals $\infty$, so $X^*$ contains $\infty$; its complement in $X$ is empty because $X\subseteq X^*$.
:::

:::

::: pf-step
The empty set $\emptyset$ is compact in $X$, so $X^* \in \mathcal{T}^*$ by condition (2).

::: pf-proof
Condition (2) requires $\infty\in X^*$ and $X\setminus X^*$ compact, and the two preceding subclaims supply exactly that, the empty set being compact.
:::

:::

:::

:::

::: pf-step
$\mathcal{T}^*$ is closed under arbitrary unions:

::: pf-proof
The two cases separate the unions in which no member contains $\infty$ from those in which some member does.

::: pf-step
Let $\{U_\alpha\}_{\alpha \in A} \subseteq \mathcal{T}^*$, and define $U = \bigcup_{\alpha \in A} U_\alpha$.

::: pf-proof
This names an arbitrary subcollection of $\mathcal{T}^*$ and its union, which is what closure under arbitrary unions quantifies over.
:::

:::

::: pf-step
Case 1 (for all $\alpha \in A$, $\infty \notin U_\alpha$):

- Each $U_\alpha$ is an open subset of $X$.
- The union $U = \bigcup_{\alpha \in A} U_\alpha \subseteq X$ is an open subset of $X$.
- Thus $U \in \mathcal{T}^*$ by condition (1).

::: pf-proof
If no $U_\alpha$ contains $\infty$ then each lies in $X$ and is open there by condition (1); an arbitrary union of open subsets of $X$ is open in $X$, and condition (1) then puts $U$ in $\mathcal{T}^*$.
:::

:::

::: pf-step
Case 2 (there exists $\alpha_0 \in A$ such that $\infty \in U_{\alpha_0}$):

- Then $\infty \in U$.
- Compute the complement in $X$:
$$X \setminus U = X \setminus \bigcup_{\alpha \in A} U_\alpha = \bigcap_{\alpha \in A} (X \setminus U_\alpha) \subseteq X \setminus U_{\alpha_0}.$$
- For every $\alpha \in A$:
    - If $\infty \in U_\alpha$, $X \setminus U_\alpha$ is compact in $X$. Since $X$ is Hausdorff, every compact subset is closed in $X$, so $X \setminus U_\alpha$ is closed in $X$.
    - If $\infty \notin U_\alpha$, $U_\alpha$ is open in $X$, so $X \setminus U_\alpha$ is closed in $X$.
- Thus $X \setminus U = \bigcap_{\alpha \in A} (X \setminus U_\alpha)$ is an intersection of closed sets, hence closed in $X$.
- Since $X \setminus U$ is a closed subset of the compact set $X \setminus U_{\alpha_0}$, $X \setminus U$ is compact in $X$.
- Thus $U \in \mathcal{T}^*$ by condition (2).

::: pf-proof
$\infty\in U$ because $\infty\in U_{\alpha_0}$, and the displayed identity is De Morgan's law, the inclusion following from $U_{\alpha_0}\subseteq U$. Each $X\setminus U_\alpha$ is closed in $X$: for $\infty\in U_\alpha$ it is compact by condition (2) and compact subsets of the Hausdorff space $X$ are closed; for $\infty\notin U_\alpha$ it is the complement of an open set of $X$. An intersection of closed sets is closed, and a closed subset of the compact set $X\setminus U_{\alpha_0}$ is compact, so condition (2) applies to $U$.
:::

:::

:::

:::

::: pf-step
$\mathcal{T}^*$ is closed under finite intersections:

::: pf-proof
The two cases separate the pairs in which at least one member misses $\infty$ from the pairs in which both contain it.

::: pf-step
Let $U_1, U_2 \in \mathcal{T}^*$, and define $U = U_1 \cap U_2$.

::: pf-proof
This names an arbitrary pair of members of $\mathcal{T}^*$ and its intersection.
:::

:::

::: pf-step
Case 1 ($\infty \notin U_1$ or $\infty \notin U_2$):

- WLOG assume $\infty \notin U_1$, so $U_1$ is open in $X$.
- Then $U = U_1 \cap U_2 = U_1 \cap (U_2 \cap X)$.
- If $\infty \notin U_2$, $U_2$ is open in $X$, so $U$ is the intersection of two open sets in $X$, hence open in $X$.
- If $\infty \in U_2$, $X \setminus U_2$ is compact (hence closed in Hausdorff $X$), so $U_2 \cap X = X \setminus (X \setminus U_2)$ is open in $X$.
- Then $U = U_1 \cap (U_2 \cap X)$ is open in $X$.
- Thus $U \in \mathcal{T}^*$ by condition (1).

::: pf-proof
$\infty\notin U_1$ forces $U_1\subseteq X$, which is the displayed rewriting of $U$. If $\infty\notin U_2$ both factors are open in $X$; if $\infty\in U_2$ then $X\setminus U_2$ is compact by condition (2), hence closed because $X$ is Hausdorff, so $U_2\cap X$ is its open complement. Either way $U$ is open in $X$ and condition (1) applies.
:::

:::

::: pf-step
Case 2 ($\infty \in U_1$ and $\infty \in U_2$):

- Then $\infty \in U_1 \cap U_2 = U$.
- Compute the complement in $X$:
$$X \setminus U = X \setminus (U_1 \cap U_2) = (X \setminus U_1) \cup (X \setminus U_2).$$
- Since $X \setminus U_1$ and $X \setminus U_2$ are compact subsets of $X$, their finite union is compact in $X$.
- Thus $U \in \mathcal{T}^*$ by condition (2).

::: pf-proof
$\infty$ lies in both members, hence in $U$; the complement identity is De Morgan's law; the two sets are compact by condition (2), and a finite union of compact subsets of $X$ is compact, so condition (2) applies.
:::

:::

::: pf-step
By induction, $\mathcal{T}^*$ is closed under all finite intersections.

::: pf-proof
The binary case just proved extends to any finite number of factors by induction on that number, the intersection of no members being $X^*$, which was shown to lie in $\mathcal{T}^*$.
:::

:::

:::

:::

::: pf-step
$X^*$ is compact:

::: pf-proof
The subclaims pass to the compact complement of a member containing $\infty$ and cover it by the traces of the given cover on $X$.

::: pf-step
Let $\mathcal{U} = \{U_i\}_{i \in I}$ be an open cover of $X^*$.

::: pf-proof
This is an arbitrary open cover of $X^*$, which is what compactness quantifies over.
:::

:::

::: pf-step
Since $\infty \in X^* = \bigcup_{i \in I} U_i$, there exists an index $i_0 \in I$ such that $\infty \in U_{i_0}$.

::: pf-proof
The members of the cover fill $X^*$, and $\infty$ is one of its points.
:::

:::

::: pf-step
By condition (2), $K = X \setminus U_{i_0}$ is a compact subset of $X$.

::: pf-proof
$U_{i_0}$ belongs to $\mathcal{T}^*$ and contains $\infty$, so condition (2) describes it precisely this way.
:::

:::

::: pf-step
For each $i \in I$, the set $V_i = U_i \cap X$ is open in $X$.

::: pf-proof
If $\infty\notin U_i$ this is condition (1); if $\infty\in U_i$ then $X\setminus U_i$ is compact, hence closed because $X$ is Hausdorff, and $U_i\cap X$ is its complement in $X$.
:::

:::

::: pf-step
The collection $\{V_i\}_{i \in I}$ is an open cover of $K$ in $X$:
$$K = X^* \setminus U_{i_0} \subseteq \bigcup_{i \in I} U_i \setminus U_{i_0} \subseteq \bigcup_{i \in I} (U_i \cap X) = \bigcup_{i \in I} V_i.$$

::: pf-proof
The first inclusion holds because $X^*=\bigcup_i U_i$, and the second because $\infty\in U_{i_0}$ keeps $\infty$ out of $U_i\setminus U_{i_0}$, so that set lies in $U_i\cap X$.
:::

:::

::: pf-step
Since $K$ is compact, there exists a finite subcollection $\{V_{i_1}, \dots, V_{i_m}\}$ covering $K$:
$$K \subseteq V_{i_1} \cup \dots \cup V_{i_m} \subseteq U_{i_1} \cup \dots \cup U_{i_m}.$$

::: pf-proof
This is the definition of compactness of $K$ applied to the open cover of the preceding subclaim, and each $V_{i_j}$ is contained in $U_{i_j}$.
:::

:::

::: pf-step
Since $X^* = U_{i_0} \cup K$, the finite subcollection $\{U_{i_0}, U_{i_1}, \dots, U_{i_m}\} \subseteq \mathcal{U}$ satisfies
$$X^* = U_{i_0} \cup K \subseteq U_{i_0} \cup U_{i_1} \cup \dots \cup U_{i_m}.$$

::: pf-proof
$K$ is by definition $X^*\setminus U_{i_0}$, so $U_{i_0}\cup K=X^*$; the inclusion is the covering of $K$ by the finitely many $U_{i_j}$ together with $U_{i_0}$ itself.
:::

:::

::: pf-step
Thus every open cover of $X^*$ has a finite subcover, so $X^*$ is compact.

::: pf-proof
The preceding subclaims produced, from an arbitrary open cover, a finite subcollection covering $X^*$; that is the definition of compactness.
:::

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The first three containers verify the three defining properties of a topology on $X^*$ — the empty set and the whole space, arbitrary unions, finite intersections — and the fourth shows that every open cover of $X^*$ has a finite subcover. Hence $\mathcal{T}^*$ is a topology on $X^*$ and $(X^*, \mathcal{T}^*)$ is compact.
:::

:::

:::

:::
