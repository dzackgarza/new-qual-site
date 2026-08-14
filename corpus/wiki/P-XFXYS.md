---
schema: qual/card@1
id: P-XFXYS
kind: problem
title: "Let $R$ be a rng (a ring without 1) which contains an element $u$ suc\u2026"
classification:
  areas:
  - algebra
  topics:
  - maximal-ideals
  - ideals
  - zorns-lemma
relations: []
review: draft
---
Let $R$ be a rng (a ring without 1) which contains an element $u$ such that for all $y\in R$, there exists an $x\in R$ such that $xu=y$.

Prove that $R$ contains a maximal left ideal.

> Hint: imitate the proof (using Zorn's lemma) in the case where $R$ does have a 1.

:::{.solution}
\envlist

- Define the map
\[
\phi_u: R &\to R\\
x &\mapsto xu
,\]
  which is right-multiplication by $u$.
  By assumption, $\phi_u$ is surjective, so the principal ideal $Ru$ equals $R$.

- Then $K \da \ker \phi_u \in \Id(R)$ is an ideal.
- $K$ is proper -- otherwise, noting $Ru=R$, if $K=R$ we have $Ru = 0$ and thus $R=0$.
  So suppose $R\neq 0$.
- Take a poset $S \da \ts{J\in \Id(R) \st J \contains K, J\neq R}$, the set of all ideals containing $K$, ordered by subset inclusion.
  Note that $K \in S$, so $S$ is nonempty.
- Apply Zorn's lemma: let $C: C_1 \subseteq C_2 \subseteq \cdots$ be a chain (totally ordered sub-poset) in $S$.
  If $C$ is the empty chain, $K$ is an upper bound.
  Otherwise, if $C$ is nonempty, define $\hat{C} \da \Union_{i=1}^\infty C_i$.
  - $\hat{C}$ is an ideal: if $a,b\in \hat{C}$, then $a\in C_i, b\in C_j$ for some $i,j$.
  But without loss of generality, using that chains are totally ordered, $C_i \subseteq C_j$, so $a,b\in C_j$ and thus $ab\in C_j$.
  Similarly for $x\in \hat{C}$, $x\in C_j$ for some $j$, and thus $Rx \subseteq C_j$ since $C_j$ is an ideal.
  - $\hat{C}$ is in $S$:
  It clearly contains $K$, since for example $K \subseteq C_1 \subseteq \hat{C}$.
    - That $\hat{C} \neq R$: an ideal equals $R$ iff it contains a unit.
    But if $r\in \hat{C}$ is a unit, $r\in C_j$ for some $j$ is a unit, making $C_j=R$. $\contradiction$
- So by Zorn's lemma, $\hat{C}$ contains a maximal ideal (incidentally containing $K$).
:::
