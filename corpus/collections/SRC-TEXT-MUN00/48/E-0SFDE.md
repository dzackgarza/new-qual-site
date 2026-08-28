---
schema: qual/card@1
id: E-0SFDE
kind: exercise
title: The line as a countable union of sets with empty interior
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

The Baire category theorem implies that $\mathbb{R}$ cannot be written as a countable union of closed subsets having empty interiors.
Show this fails if the sets are not required to be closed.
:::

::: solution
**Goal:** Construct a countable collection of subsets $\{A_n\}_{n=0}^\infty$ of $\mathbb{R}$ such that $\operatorname{Int}(A_n) = \emptyset$ for all $n \ge 0$ and $\mathbb{R} = \bigcup_{n=0}^\infty A_n$.

<1>1. Construction of the partition:
    1. Let $\mathbb{Q}$ be the set of rational numbers in $\mathbb{R}$. Since $\mathbb{Q}$ is countably infinite, choose an enumeration $\mathbb{Q} = \{q_1, q_2, q_3, \dots\}$.
    2. Let $A_0 = \mathbb{R} \setminus \mathbb{Q}$ be the set of all irrational numbers.
    3. For each $n \in \mathbb{Z}_+$, let $A_n = \{q_n\}$.
    4. Then $\bigcup_{n=0}^\infty A_n = (\mathbb{R} \setminus \mathbb{Q}) \cup \bigcup_{n=1}^\infty \{q_n\} = (\mathbb{R} \setminus \mathbb{Q}) \cup \mathbb{Q} = \mathbb{R}$.

<1>2. Each singleton $A_n = \{q_n\}$ has empty interior for $n \ge 1$:
    *Proof:* Every non-empty open subset of $\mathbb{R}$ contains an open interval $(a, b)$ with $a < b$, which contains uncountably many points. Since $A_n$ contains exactly one point, $A_n$ contains no open interval. Thus $\operatorname{Int}(A_n) = \emptyset$.

<1>3. The set of irrationals $A_0 = \mathbb{R} \setminus \mathbb{Q}$ has empty interior:
    *Proof:* If $\operatorname{Int}(\mathbb{R} \setminus \mathbb{Q}) \neq \emptyset$, it would contain a non-empty open interval $(a, b)$ with $a < b$. By the density of $\mathbb{Q}$ in $\mathbb{R}$, there exists a rational number $q \in (a, b) \subset \mathbb{R} \setminus \mathbb{Q}$, which contradicts $q \in \mathbb{Q}$. Thus $\operatorname{Int}(A_0) = \emptyset$.

<1>4. $A_0$ is not closed in $\mathbb{R}$:
    *Proof:* By the density of the irrationals in $\mathbb{R}$, the closure of $A_0 = \mathbb{R} \setminus \mathbb{Q}$ is $\overline{\mathbb{R} \setminus \mathbb{Q}} = \mathbb{R} \neq A_0$.

<1>5. Conclusion:
    $\mathbb{R} = \bigcup_{n=0}^\infty A_n$ expresses $\mathbb{R}$ as a countable union of subsets each having empty interior, showing that the closedness hypothesis in the Baire Category Theorem cannot be omitted. Q.E.D.
:::
