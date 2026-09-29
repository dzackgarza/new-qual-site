---
schema: qual/card@1
id: P-MMAQ-SNLQTGU5TQ
kind: problem
title: Every vector space has a basis, by Zorn's lemma
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Vector Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Carefully state Zorn's lemma and use it to prove that every vector space has a basis.
:::

::: {.solution}

::: pf

::: pf-step
Statement of Zorn’s Lemma:

::: pf-proof

::: pf-step
**Zorn’s Lemma:** Let $(\mathcal{P}, \le)$ be a non-empty partially ordered set. If every non-empty chain (totally ordered subset) $\mathcal{C} \subseteq \mathcal{P}$ has an upper bound in $\mathcal{P}$, then $\mathcal{P}$ contains at least one maximal element.

::: pf-proof
Zorn's lemma is equivalent to the axiom of choice over ZF and is taken as an axiom here.
:::

:::

:::

:::

::: {.pf-step #poset-of-linear-independent-sets}
Definition of the poset of linearly independent subsets:

::: pf-proof

::: pf-step
Let $V$ be a vector space over a field $F$. Define:
\[
\mathcal{P} = \{S \subseteq V \mid S \text{ is linearly independent over } F\},
\]
partially ordered by set inclusion $\subseteq$.

::: pf-proof
Inclusion is reflexive, antisymmetric, and transitive on subsets of $V$.
:::

:::

::: pf-step
$\mathcal{P} \neq \emptyset$ because the empty set $\emptyset$ is vacuously linearly independent, so $\emptyset \in \mathcal{P}$.

::: pf-proof
The empty set admits no nontrivial linear relation.
:::

:::

:::

:::

::: {.pf-step #chain-has-upper-bound}
Verification of the chain condition:

::: pf-proof

::: pf-step
Let $\mathcal{C} = \{S_i\}_{i \in I}$ be a non-empty totally ordered chain in $\mathcal{P}$.
Define $U = \bigcup_{i \in I} S_i \subseteq V$.

::: pf-proof
This is a definition.
:::

:::

::: {.pf-step #u-relation-setup}
Show $U \in \mathcal{P}$ (i.e. $U$ is linearly independent):
Suppose $\sum_{j=1}^k c_j v_j = 0$ for scalars $c_j \in F$ and distinct vectors $v_1, \dots, v_k \in U$.

::: pf-proof
This fixes an arbitrary finite linear relation among elements of $U$.
:::

:::

::: pf-step
For each $j \in \{1, \dots, k\}$, there exists $i_j \in I$ such that $v_j \in S_{i_j}$.
Since $\mathcal{C}$ is totally ordered, the finite collection $\{S_{i_1}, \dots, S_{i_k}\}$ has a maximum element $S_{i_{\max}} \in \mathcal{C}$ under inclusion.
Thus $\{v_1, \dots, v_k\} \subseteq S_{i_{\max}}$.

::: pf-proof
A nonempty finite subset of a totally ordered set has a largest element, by induction on its size.
:::

:::

::: {.pf-step #u-is-independent}
Since $S_{i_{\max}} \in \mathcal{P}$, it is linearly independent, which forces $c_1 = \cdots = c_k = 0$.
Thus $U$ is linearly independent, so $U \in \mathcal{P}$.

::: pf-proof
The relation of step [](#u-relation-setup){.pf-ref} is a linear relation among distinct elements of $S_{i_{\max}}$, which is linearly independent.
:::

:::

::: pf-step
By construction, $S_i \subseteq U$ for all $i \in I$, so $U$ is an upper bound for the chain $\mathcal{C}$ in $\mathcal{P}$.

::: pf-proof
Each $S_i$ is contained in the union $U$, and $U\in\mathcal P$ by step [](#u-is-independent){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Existence of a basis via maximality:

::: pf-proof

::: pf-step
By Zorn’s Lemma applied to $\mathcal{P}$, there exists a maximal element $B \in \mathcal{P}$.

::: pf-proof
Step [](#poset-of-linear-independent-sets){.pf-ref} shows that $\mathcal P$ is a nonempty partially ordered set, and step [](#chain-has-upper-bound){.pf-ref} shows that every nonempty chain in $\mathcal P$ has an upper bound; Zorn's lemma applies.
:::

:::

::: {.pf-step #basis-candidate-is-independent}
Since $B \in \mathcal{P}$, $B$ is linearly independent.

::: pf-proof
Elements of $\mathcal P$ are linearly independent sets by definition.
:::

:::

::: pf-step
Show that $\operatorname{span}_F(B) = V$:
Suppose for contradiction that there exists $v \in V \setminus \operatorname{span}_F(B)$.
Consider $B' = B \cup \{v\}$.

::: pf-proof
This is the hypothesis of the argument by contradiction in steps [](#b-union-v-independent){.pf-ref} and [](#maximality-forces-spanning){.pf-ref}.
:::

:::

::: {.pf-step #b-union-v-independent}
Show that $B'$ is linearly independent:
Suppose $c v + \sum_{b \in B} c_b b = 0$ for $c, c_b \in F$.
If $c \neq 0$, then $v = -\sum_{b \in B} (c_b / c) b \in \operatorname{span}_F(B)$, contradicting $v \notin \operatorname{span}_F(B)$.
Thus $c = 0$, which implies $\sum_{b \in B} c_b b = 0 \implies c_b = 0$ for all $b$ since $B$ is linearly independent.
Thus $B' \in \mathcal{P}$.

::: pf-proof
Only finitely many $c_b$ are nonzero, so the displayed relation is a finite linear relation, and the argument in the claim of this step shows that all its coefficients vanish.
:::

:::

::: {.pf-step #maximality-forces-spanning}
Since $v \notin B$, $B \subsetneq B'$, which contradicts the maximality of $B$ in $\mathcal{P}$.
Thus no such $v$ exists, so $\operatorname{span}_F(B) = V$.

::: pf-proof
Step [](#b-union-v-independent){.pf-ref} gives $B'\in\mathcal P$ with $B\subsetneq B'$, which is impossible for a maximal element.
:::

:::

:::

:::

::: pf-qed
$B$ is linearly independent and spans $V$, so $B$ is a basis for $V$.
Steps [](#basis-candidate-is-independent){.pf-ref} and [](#maximality-forces-spanning){.pf-ref} give linear independence and spanning.
:::

:::
:::
