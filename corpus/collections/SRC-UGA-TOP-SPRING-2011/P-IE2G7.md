---
schema: qual/card@1
id: P-IE2G7
kind: problem
title: Discrete spaces are totally disconnected, but not conversely
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Point-Set Topology
relations: []
review: draft
---

::: {.problem}
A topological space is **totally disconnected** if its only connected subsets are one-point sets.

Is it true that if $X$ has the discrete topology, it is totally disconnected?

Is the converse true?
Justify your answers.
:::

::: {.solution}
Yes: every discrete space is totally disconnected. Let $C\subseteq X$ contain at least two points and choose $x\in C$. Since $X$ is discrete, both
\[
\{x\}
\qquad\text{and}\qquad
C\setminus\{x\}
\]
are open in the subspace $C$. They are disjoint, nonempty, and cover $C$, so $C$ is disconnected. Hence every nonempty connected subset of $X$ is a singleton.

The converse is false. Take $\QQ$ with the topology inherited from $\RR$. It is not discrete: no singleton $\{q\}$ is open in $\QQ$.

To see that $\QQ$ is totally disconnected, let $C\subseteq\QQ$ contain distinct points $a<b$. Choose an irrational number $r$ with
\[
a<r<b.
\]
Then
\[
C_-=C\cap(-\infty,r),
\qquad
C_+=C\cap(r,\infty)
\]
are disjoint nonempty sets open in the subspace $C$. Because $r\notin\QQ$, they cover $C$. Thus every subset of $\QQ$ containing at least two points is disconnected, so $\QQ$ is totally disconnected but not discrete.
:::
