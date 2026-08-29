---
schema: qual/card@1
id: P-VAJSW
kind: problem
title: Compact Hausdorff spaces are normal
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Prove that every compact, Hausdorff topological space is normal.
:::

::: solution
Let $X$ be compact and Hausdorff.  
Let $F,G\subseteq X$ be disjoint closed sets.

<1>1. Each of $F$ and $G$ is compact.
    <1>1.1. In a Hausdorff space, compact sets are closed, so both $F$ and $G$ are compact and disjoint.
<1>2. For each $x\in F$, separate $x$ from $G$ pointwise.
    <1>2.1. For every $y\in G$, Hausdorffness gives disjoint open sets $U_{x,y}\ni x$ and $V_{x,y}\ni y$.
    <1>2.2. The sets $\{V_{x,y}\}_{y\in G}$ cover $G$. By compactness of $G$, choose $y_1,\dots,y_{k_x}$ with
    \[
    G\subseteq \bigcup_{i=1}^{k_x}V_{x,y_i}.
    \]
    Define
    \[
    U_x:=\bigcap_{i=1}^{k_x}U_{x,y_i},\qquad
    V_x:=\bigcup_{i=1}^{k_x}V_{x,y_i}.
    \]
    Then $U_x$ and $V_x$ are open, $x\in U_x$, $G\subseteq V_x$, and $U_x\cap V_x=\varnothing$.
<1>3. Use compactness of $F$ to choose finitely many $x_1,\dots,x_m\in F$ with
    $F\subseteq \bigcup_{j=1}^m U_{x_j}$.
    Set
    \[
    U:=\bigcup_{j=1}^m U_{x_j},\qquad V:=\bigcap_{j=1}^m V_{x_j}.
    \]
    Then $U,V$ are open, $F\subseteq U$, $G\subseteq V$.
<1>4. Show $U\cap V=\varnothing$.
    <1>4.1. If $u\in U\cap V$, then $u\in U_{x_j}$ for some $j$ and $u\in V_{x_i}$ for all $i$, hence $u\in U_{x_j}\cap V_{x_j}$, contradiction.
    <1>4.2. Therefore $U\cap V=\emptyset$.

Thus compact Hausdorff spaces are normal: disjoint closed sets admit disjoint open neighborhoods.
:::
