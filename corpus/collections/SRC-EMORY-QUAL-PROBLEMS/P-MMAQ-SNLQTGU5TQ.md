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
<1>1. Statement of Zorn’s Lemma:
<2>1. **Zorn’s Lemma:** Let $(\mathcal{P}, \le)$ be a non-empty partially ordered set. If every non-empty chain (totally ordered subset) $\mathcal{C} \subseteq \mathcal{P}$ has an upper bound in $\mathcal{P}$, then $\mathcal{P}$ contains at least one maximal element.
::: {.proof}
Zorn's lemma is equivalent to the axiom of choice over ZF and is taken as an axiom here.
:::

<1>2. Definition of the poset of linearly independent subsets:
<2>1. Let $V$ be a vector space over a field $F$. Define:
\[
\mathcal{P} = \{S \subseteq V \mid S \text{ is linearly independent over } F\},
\]
partially ordered by set inclusion $\subseteq$.
::: {.proof}
Inclusion is reflexive, antisymmetric, and transitive on subsets of $V$.
:::
<2>2. $\mathcal{P} \neq \emptyset$ because the empty set $\emptyset$ is vacuously linearly independent, so $\emptyset \in \mathcal{P}$.
::: {.proof}
The empty set admits no nontrivial linear relation.
:::

<1>3. Verification of the chain condition:
<2>1. Let $\mathcal{C} = \{S_i\}_{i \in I}$ be a non-empty totally ordered chain in $\mathcal{P}$.
Define $U = \bigcup_{i \in I} S_i \subseteq V$.
::: {.proof}
This is a definition.
:::
<2>2. Show $U \in \mathcal{P}$ (i.e. $U$ is linearly independent):
Suppose $\sum_{j=1}^k c_j v_j = 0$ for scalars $c_j \in F$ and distinct vectors $v_1, \dots, v_k \in U$.
::: {.proof}
This fixes an arbitrary finite linear relation among elements of $U$.
:::
<2>3. For each $j \in \{1, \dots, k\}$, there exists $i_j \in I$ such that $v_j \in S_{i_j}$.
Since $\mathcal{C}$ is totally ordered, the finite collection $\{S_{i_1}, \dots, S_{i_k}\}$ has a maximum element $S_{i_{\max}} \in \mathcal{C}$ under inclusion.
Thus $\{v_1, \dots, v_k\} \subseteq S_{i_{\max}}$.
::: {.proof}
A nonempty finite subset of a totally ordered set has a largest element, by induction on its size.
:::
<2>4. Since $S_{i_{\max}} \in \mathcal{P}$, it is linearly independent, which forces $c_1 = \cdots = c_k = 0$.
Thus $U$ is linearly independent, so $U \in \mathcal{P}$.
::: {.proof}
The relation of step <2>2 is a linear relation among distinct elements of $S_{i_{\max}}$, which is linearly independent.
:::
<2>5. By construction, $S_i \subseteq U$ for all $i \in I$, so $U$ is an upper bound for the chain $\mathcal{C}$ in $\mathcal{P}$.
::: {.proof}
Each $S_i$ is contained in the union $U$, and $U\in\mathcal P$ by step <2>4.
:::

<1>4. Existence of a basis via maximality:
<2>1. By Zorn’s Lemma applied to $\mathcal{P}$, there exists a maximal element $B \in \mathcal{P}$.
::: {.proof}
Step <1>2 shows that $\mathcal P$ is a nonempty partially ordered set, and step <1>3 shows that every nonempty chain in $\mathcal P$ has an upper bound; Zorn's lemma applies.
:::
<2>2. Since $B \in \mathcal{P}$, $B$ is linearly independent.
::: {.proof}
Elements of $\mathcal P$ are linearly independent sets by definition.
:::
<2>3. Show that $\operatorname{span}_F(B) = V$:
Suppose for contradiction that there exists $v \in V \setminus \operatorname{span}_F(B)$.
Consider $B' = B \cup \{v\}$.
::: {.proof}
This is the hypothesis of the argument by contradiction in steps <2>4 and <2>5.
:::
<2>4. Show that $B'$ is linearly independent:
Suppose $c v + \sum_{b \in B} c_b b = 0$ for $c, c_b \in F$.
If $c \neq 0$, then $v = -\sum_{b \in B} (c_b / c) b \in \operatorname{span}_F(B)$, contradicting $v \notin \operatorname{span}_F(B)$.
Thus $c = 0$, which implies $\sum_{b \in B} c_b b = 0 \implies c_b = 0$ for all $b$ since $B$ is linearly independent.
Thus $B' \in \mathcal{P}$.
::: {.proof}
Only finitely many $c_b$ are nonzero, so the displayed relation is a finite linear relation, and the argument in the claim of this step shows that all its coefficients vanish.
:::
<2>5. Since $v \notin B$, $B \subsetneq B'$, which contradicts the maximality of $B$ in $\mathcal{P}$.
Thus no such $v$ exists, so $\operatorname{span}_F(B) = V$.
::: {.proof}
Step <2>4 gives $B'\in\mathcal P$ with $B\subsetneq B'$, which is impossible for a maximal element.
:::

<1>5. Conclusion:
$B$ is linearly independent and spans $V$, so $B$ is a basis for $V$. Q.E.D.
::: {.proof}
Steps <1>4.<2>2 and <1>4.<2>5 give linear independence and spanning.
:::
:::
