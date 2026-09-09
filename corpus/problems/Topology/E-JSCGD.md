---
schema: qual/card@1
id: E-JSCGD
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Let $X$ be a compact topological space and let $A \subseteq X$ be a closed subset of $X$.
Prove that $A$ is compact in the subspace topology.
:::

::: solution
<1>1. Let $\{V_i\}_{i\in I}$ be an open cover of $A$ in the subspace topology. For each $i$, choose an open set $U_i\subseteq X$ with
\[
V_i=U_i\cap A.
\]

<1>2. Since $A$ is closed, $X\setminus A$ is open. Hence
\[
\{U_i:i\in I\}\cup\{X\setminus A\}
\]
is an open cover of $X$.

<1>3. Compactness of $X$ gives finitely many indices $i_1,\dots,i_m$ such that
\[
X\subseteq U_{i_1}\cup\cdots\cup U_{i_m}\cup(X\setminus A).
\]
Intersecting with $A$ yields
\[
A\subseteq V_{i_1}\cup\cdots\cup V_{i_m}.
\]
Thus every open cover of $A$ has a finite subcover, so $A$ is compact.
:::
