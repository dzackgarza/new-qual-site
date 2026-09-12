---
schema: qual/card@1
id: P-YCRKO
kind: problem
title: The derived series, the commutator, and two theorems on derived series
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Commutators
  - Solvable Groups
relations: []
review: draft
---

::: problem
Define the commutator and the derived series. State and prove two nontrivial theorems about derived series.
:::

::: solution
For $x,y\in G$, the commutator is
\[
[x,y]=xyx^{-1}y^{-1}.
\]
The commutator subgroup is
\[
G'=[G,G]=\langle[x,y]:x,y\in G\rangle.
\]
The derived series is defined recursively by
\[
G^{(0)}=G,
\qquad
G^{(n+1)}=[G^{(n)},G^{(n)}].
\]
A group is solvable exactly when $G^{(r)}=1$ for some $r$.

<1>1. Homomorphisms preserve the derived series.

If $\phi:G\to H$ is a group homomorphism, then
\[
\phi(G^{(n)})=\phi(G)^{(n)}
\]
for every $n\ge0$.

Indeed,
\[
\phi([x,y])=[\phi(x),\phi(y)],
\]
so
\[
\phi([A,A])=[\phi(A),\phi(A)]
\]
for every subgroup $A\le G$. Induction on $n$ proves the formula.

In particular, every $G^{(n)}$ is characteristic in $G$: for an automorphism $\phi$,
\[
\phi(G^{(n)})=G^{(n)}.
\]

<1>2. Solvability is closed under extensions.

Let $N\trianglelefteq G$. If both $N$ and $G/N$ are solvable, then $G$ is solvable.

Suppose
\[
(G/N)^{(r)}=1.
\]
By the quotient map and <1>1,
\[
G^{(r)}N/N=1,
\]
so
\[
G^{(r)}\le N.
\]
If $N^{(s)}=1$, then induction gives
\[
G^{(r+j)}\le N^{(j)}
\]
for every $j\ge0$. Hence
\[
G^{(r+s)}\le N^{(s)}=1.
\]
Therefore $G$ is solvable.
:::
