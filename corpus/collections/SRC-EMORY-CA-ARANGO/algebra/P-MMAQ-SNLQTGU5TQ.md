---
schema: qual/card@1
id: P-MMAQ-SNLQTGU5TQ
kind: problem
title: Carefully state Zorn's lemma and use it to prove that every vector
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

::: problem
Carefully state Zorn's lemma and use it to prove that every vector space has a basis.
:::

::: {.solution}
<1>1. Statement of Zorn’s Lemma:
<2>1. **Zorn’s Lemma:** Let $(\mathcal{P}, \le)$ be a non-empty partially ordered set. If every non-empty chain (totally ordered subset) $\mathcal{C} \subseteq \mathcal{P}$ has an upper bound in $\mathcal{P}$, then $\mathcal{P}$ contains at least one maximal element.
::: {.proof}
equivalent to the Axiom of Choice.
:::

<1>2. Definition of the poset of linearly independent subsets:
<2>1. Let $V$ be a vector space over a field $F$. Define:
\[
\mathcal{P} = \{S \subseteq V \mid S \text{ is linearly independent over } F\},
\]
partially ordered by set inclusion $\subseteq$.
::: {.proof}
definition of poset.
:::
<2>2. $\mathcal{P} \neq \emptyset$ because the empty set $\emptyset$ is vacuously linearly independent, so $\emptyset \in \mathcal{P}$.
::: {.proof}
$\emptyset \in \mathcal{P}$.
:::

<1>3. Verification of the chain condition:
<2>1. Let $\mathcal{C} = \{S_i\}_{i \in I}$ be a non-empty totally ordered chain in $\mathcal{P}$.
Define $U = \bigcup_{i \in I} S_i \subseteq V$.
::: {.proof}
union of chain.
:::
<2>2. Show $U \in \mathcal{P}$ (i.e. $U$ is linearly independent):
Suppose $\sum_{j=1}^k c_j v_j = 0$ for scalars $c_j \in F$ and distinct vectors $v_1, \dots, v_k \in U$.
::: {.proof}
setup linear dependence relation.
:::
<2>3. For each $j \in \{1, \dots, k\}$, there exists $i_j \in I$ such that $v_j \in S_{i_j}$.
Since $\mathcal{C}$ is totally ordered, the finite collection $\{S_{i_1}, \dots, S_{i_k}\}$ has a maximum element $S_{i_{\max}} \in \mathcal{C}$ under inclusion.
Thus $\{v_1, \dots, v_k\} \subseteq S_{i_{\max}}$.
::: {.proof}
total ordering of finite subsets of chains.
:::
<2>4. Since $S_{i_{\max}} \in \mathcal{P}$, it is linearly independent, which forces $c_1 = \cdots = c_k = 0$.
Thus $U$ is linearly independent, so $U \in \mathcal{P}$.
::: {.proof}
definition of linear independence.
:::
<2>5. By construction, $S_i \subseteq U$ for all $i \in I$, so $U$ is an upper bound for the chain $\mathcal{C}$ in $\mathcal{P}$.
::: {.proof}
definition of set union.
:::

<1>4. Existence of a basis via maximality:
<2>1. By Zorn’s Lemma applied to $\mathcal{P}$, there exists a maximal element $B \in \mathcal{P}$.
::: {.proof}
Zorn's Lemma applied to <1>2 and <1>3.
:::
<2>2. Since $B \in \mathcal{P}$, $B$ is linearly independent.
::: {.proof}
definition of $\mathcal{P}$.
:::
<2>3. Show that $\operatorname{span}_F(B) = V$:
Suppose for contradiction that there exists $v \in V \setminus \operatorname{span}_F(B)$.
Consider $B' = B \cup \{v\}$.
::: {.proof}
proof by contradiction.
:::
<2>4. Show that $B'$ is linearly independent:
Suppose $c v + \sum_{b \in B} c_b b = 0$ for $c, c_b \in F$.
If $c \neq 0$, then $v = -\sum_{b \in B} (c_b / c) b \in \operatorname{span}_F(B)$, contradicting $v \notin \operatorname{span}_F(B)$.
Thus $c = 0$, which implies $\sum_{b \in B} c_b b = 0 \implies c_b = 0$ for all $b$ since $B$ is linearly independent.
Thus $B' \in \mathcal{P}$.
::: {.proof}
linear independence test.
:::
<2>5. Since $v \notin B$, $B \subsetneq B'$, which contradicts the maximality of $B$ in $\mathcal{P}$.
Thus no such $v$ exists, so $\operatorname{span}_F(B) = V$.
::: {.proof}
contradiction to maximality.
:::

<1>5. Conclusion:
$B$ is linearly independent and spans $V$, so $B$ is a basis for $V$. Q.E.D.
::: {.proof}
<1>4.
:::
:::
