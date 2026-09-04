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
Let $\mathcal U$ be an open cover of $[0,1]$.
We use the least-upper-bound property of $\RR$.

Define
\[
S=\{x\in[0,1]:[0,x]\text{ is covered by finitely many members of }\mathcal U\}.
\]
The set $S$ is nonempty.
Indeed, choose $U_0\in\mathcal U$ with $0\in U_0$.
Since $U_0$ is open, some $\delta>0$ satisfies
\[
[0,\delta)\subseteq U_0,
\]
after decreasing $\delta$ if necessary; hence every $x\in[0,\min\{\delta/2,1\}]$ lies in $S$.

Let $s=\sup S$.
We first show $s=1$.
Suppose $s<1$.
Choose $U\in\mathcal U$ with $s\in U$.
Since $U$ is open, there is $\varepsilon>0$ such that
\[
(s-\varepsilon,s+\varepsilon)\subseteq U.
\]
By the definition of supremum, choose $x\in S$ with $s-\varepsilon/2<x\le s$.
A finite subfamily of $\mathcal U$ covers $[0,x]$, and adjoining $U$ gives a finite cover of
\[
[0,s+\varepsilon/2].
\]
Thus $s+\varepsilon/2\in S$, contradicting that $s$ is an upper bound for $S$.
Therefore $s=1$.

Finally choose $U_1\in\mathcal U$ containing $1$.
For some $\varepsilon>0$,
\[
(1-\varepsilon,1]\subseteq U_1.
\]
Since $\sup S=1$, choose $x\in S$ with $1-\varepsilon<x\le1$.
A finite subfamily covers $[0,x]$, and together with $U_1$ it covers all of $[0,1]$.
Hence every open cover of $[0,1]$ has a finite subcover, so $[0,1]$ is compact.
:::
