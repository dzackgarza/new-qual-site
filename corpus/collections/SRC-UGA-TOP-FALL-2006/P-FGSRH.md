---
schema: qual/card@1
id: P-FGSRH
kind: problem
title: Fall 2006, 7
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: {.problem}
A topological space is **sequentially compact** if every infinite sequence in $X$ has a convergent subsequence.

Prove that every compact metric space is sequentially compact.
:::

::: {.solution}
Let $(X,d)$ be compact and let $(x_n)$ be a sequence in $X$.

If some value occurs infinitely often, the corresponding constant subsequence
converges. Thus suppose every value occurs only finitely often. Then the set
\[
A=\{x_n:n\ge1\}
\]
is infinite.

We first show that every infinite subset of a compact space has a limit point.
If $A$ had no limit point, then for each $x\in X$ there would be an open
neighborhood $U_x$ such that
\[
U_x\cap A\subseteq\{x\}.
\]
The family $\{U_x:x\in X\}$ covers $X$. Compactness gives a finite subcover
$U_{x_1},\ldots,U_{x_m}$, whence
\[
A\subseteq\{x_1,\ldots,x_m\},
\]
contradicting that $A$ is infinite. Hence $A$ has a limit point $p\in X$.

For each $k\ge1$, the ball $B(p,1/k)$ contains a point of $A$ different from
$p$; indeed it contains infinitely many points of $A$, since otherwise deleting
those finitely many points would leave a smaller neighborhood of $p$ disjoint
from $A\setminus\{p\}$. We may therefore choose recursively indices
\[
n_1<n_2<\cdots
\]
such that
\[
x_{n_k}\in B(p,1/k).
\]
Then
\[
d(x_{n_k},p)<{1\over k}\to0,
\]
so $x_{n_k}\to p$. Thus every sequence in $X$ has a convergent subsequence,
and $X$ is sequentially compact.
:::
