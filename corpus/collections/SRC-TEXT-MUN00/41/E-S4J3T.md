---
schema: qual/card@1
id: E-S4J3T
kind: problem
title: Unions of closed paracompact subspaces
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ be a regular space.

(a) If $X$ is a finite union of closed paracompact subspaces of $X$, then $X$ is paracompact.

(b) If $X$ is a countable union of closed paracompact subspaces whose interiors cover $X$, show $X$ is paracompact.
:::

::: {.solution}
We use the closed-refinement characterization: a regular space is paracompact iff every open cover has a locally finite closed refinement covering the space.

(a) Suppose
\[
X=A_1\cup\cdots\cup A_m
\]
with each \(A_i\) closed and paracompact. Let \(\mathcal U\) be an open cover of \(X\). Its restriction to \(A_i\) has a locally finite closed refinement \(\mathcal F_i\) covering \(A_i\). Because \(A_i\) is closed in \(X\), every member of \(\mathcal F_i\) is closed in \(X\). A finite union of locally finite families is locally finite, so
\[
\mathcal F_1\cup\cdots\cup\mathcal F_m
\]
is a locally finite closed refinement of \(\mathcal U\) covering \(X\). Thus \(X\) is paracompact.

(b) Suppose
\[
X=\bigcup_{n\ge1}A_n
\]
where each \(A_n\) is closed and paracompact and the interiors \(A_n^\circ\) cover \(X\). Define
\[
C_n=A_n-\bigcup_{i<n}A_i^\circ.
\]
Each \(C_n\) is closed in \(X\), is a closed subspace of the paracompact space \(A_n\), hence is paracompact, and the \(C_n\)'s cover \(X\). They are locally finite: if \(x\in A_m^\circ\), then the neighborhood \(A_m^\circ\) misses \(C_n\) for every \(n>m\).

Let \(\mathcal U\) be an open cover of \(X\). For each \(n\), choose a locally finite closed refinement \(\mathcal F_n\) of the restricted cover on \(C_n\), covering \(C_n\). Since \(C_n\) is closed in \(X\), all members of \(\mathcal F_n\) are closed in \(X\). The union
\[
\mathcal F=\bigcup_{n\ge1}\mathcal F_n
\]
is locally finite: near a fixed point only finitely many \(C_n\)'s occur, and within each of those finitely many \(C_n\)'s the corresponding family \(\mathcal F_n\) is locally finite. Thus \(\mathcal F\) is a locally finite closed refinement of \(\mathcal U\) covering \(X\). Hence \(X\) is paracompact.
:::
