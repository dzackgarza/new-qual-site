---
schema: qual/card@1
id: P-DBY54
kind: problem
title: "Let $R$ be a commutative ring, and $S\\subset R$ be a nonempty subset t\u2026"
classification:
  areas:
  - algebra
  topics:
  - prime-ideals
  - ideals
  - zorns-lemma
relations: []
review: draft
solved: true
---
Let $R$ be a commutative ring, and $S\subset R$ be a nonempty subset that does not contain 0 such that for all $x, y\in S$ we have $xy\in S$.
Let $\mci$ be the set of all ideals $I\normal R$ such that $I\intersect S = \emptyset$.

Show that for every ideal $I\in \mci$, there is an ideal $J\in \mci$ such that $I\subset J$ and $J$ is not properly contained in any other ideal in $\mci$.

Prove that every such ideal $J$ is prime.


:::{.solution}
\envlist

- Restating, take the poset $S\da \ts{J\in \Id(R) \st J \intersect S = \emptyset, I\neq R, I \subseteq J}$ ordered by inclusion.
  Note that $S$ is nonempty since it contains $I$.
  It suffices to produce a maximal element of $S$.
- Applying Zorn's lemma, let $C: C_1 \subseteq C_2 \subseteq \cdots$ be a chain and define $\hat{C} \da \union C_i$.
- By standard arguments, $\hat{C} \in \Id(R)$ and $\hat{C} \contains I$, and it suffices to show $\hat{C} \intersect S = \emptyset$ and $\hat{C}\neq R$.
- $\hat{C} \intersect S = \emptyset$:
  - By contradiction, if $x\in \hat{C} \intersect S$ then $x\in C_j$ for some $j$, and $x\in S$.
    But then $x \in C_j \intersect S = \emptyset$.
- $\hat{C} \neq R$:
  - By contradiction, if so then $1 \in \hat{C} \implies 1 \in C_j$ for some $j$, forcing $C_j = R$.
- So Zorn's lemma applies and we obtain some ideal $\mfp$, which we now claim is prime.
- Let $ab\in \mfp$, we want to show $a\in \mfp$ or $b\in\mfp$.
- Suppose not, then neither $a,b\in \mfp$. 
  By maximality, $\mfp + Ra = R$, and so $\mfp + Ra$ intersects $S$.
  Similarly $\mfp + Rb = R$ so $\mfp + Rb$ intersects $S$.
- Produce elements $x\da p_1 + r_1a, y\da p_2 + r_2b\in S$, then since $S$ is multiplicatively closed,
\[
xy&\da (p_1 + r_1 a)(p_2 + r_2b)\in S \\
&\implies p_1 p_2 + p_1r_2 b + p_2 r_1 a + r_1 r_2 ab \in S \\ 
&\implies xy\in \mfp + \mfp Rb + \mfp Ra + R\mfp && \text{since } p_i, ab\in \mfp \\
&\implies xy \in (\mfp + Rb + Ra + R)\mfp \subseteq \mfp
.\]
  But then $xy\in S \intersect \mfp$, a contradiction.

:::
