---
schema: qual/card@1
id: E-LKUPH
kind: problem
title: Transitivity of deformation retracts
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that if $A$ is a deformation retract of $X$, and $B$ is a deformation retract of $A$, then $B$ is a deformation retract of $X$.
:::

::: {.solution}
Let \(H:X\times I\to X\) be a deformation retraction of \(X\) onto \(A\), and let \(K:A\times I\to A\) be a deformation retraction of \(A\) onto \(B\). Thus
\[
H(x,0)=x,\quad H(x,1)\in A,\quad H(a,t)=a,
\]
and
\[
K(a,0)=a,\quad K(a,1)\in B,\quad K(b,t)=b.
\]
Define \(F:X\times I\to X\) by
\[
F(x,t)=
\begin{cases}
H(x,2t),&0\le t\le1/2,\\
K(H(x,1),2t-1),&1/2\le t\le1.
\end{cases}
\]
The two formulas agree at \(t=1/2\), so the pasting lemma gives continuity. We have \(F(x,0)=x\) and \(F(x,1)\in B\). If \(b\in B\subset A\), then both \(H(b,t)=b\) and \(K(b,t)=b\), hence \(F(b,t)=b\) for all \(t\). Therefore \(F\) is a deformation retraction of \(X\) onto \(B\).
:::
