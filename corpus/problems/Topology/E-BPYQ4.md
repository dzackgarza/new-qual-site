---
schema: qual/card@1
id: E-BPYQ4
kind: problem
title: $[0,1]$ is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: exercise
Show that $[0, 1]$ is compact.
:::

::: solution
Let $\mathcal U$ be an open cover of $[0,1]$ and define
\[
S=\{x\in[0,1]:[0,x]\text{ is covered by finitely many members of }\mathcal U\}.
\]

<1>1. $S$ is nonempty.
::: {.proof}
Choose $U_0\in\mathcal U$ with $0\in U_0$. Since $U_0$ is open in $\RR$, there is $\delta>0$ such that
\[
[0,\delta)\subseteq U_0
\]
after decreasing $\delta$ if necessary. Hence every
\[
x\in[0,\min\{\delta/2,1\}]
\]
belongs to $S$.
:::

<1>2. If $s=\sup S$, then $s=1$.
::: {.proof}
The least-upper-bound property of $\RR$ applies because $S$ is nonempty by <1>1 and is bounded above by $1$.

Suppose $s<1$. Choose $U\in\mathcal U$ with $s\in U$. Since $U$ is open, there is $\varepsilon>0$ such that
\[
(s-\varepsilon,s+\varepsilon)\subseteq U.
\]
By the defining property of the supremum, choose $x\in S$ with
\[
s-\varepsilon/2<x\le s.
\]
A finite subfamily of $\mathcal U$ covers $[0,x]$. Adjoining $U$ therefore gives a finite cover of
\[
[0,s+\varepsilon/2],
\]
so $s+\varepsilon/2\in S$, contradicting that $s$ is an upper bound of $S$. Thus $s=1$.
:::

<1>3. The cover $\mathcal U$ has a finite subcover.
::: {.proof}
Choose $U_1\in\mathcal U$ with $1\in U_1$. For some $\varepsilon>0$,
\[
(1-\varepsilon,1]\subseteq U_1.
\]
By <1>2, $\sup S=1$, so choose $x\in S$ with
\[
1-\varepsilon<x\le1.
\]
By the definition of $S$, finitely many members of $\mathcal U$ cover $[0,x]$. Together with $U_1$, they cover all of $[0,1]$.
:::

<1>4. $[0,1]$ is compact.
::: {.proof}
The open cover $\mathcal U$ was arbitrary, and <1>3 gives it a finite subcover. This is exactly compactness.
:::
:::
