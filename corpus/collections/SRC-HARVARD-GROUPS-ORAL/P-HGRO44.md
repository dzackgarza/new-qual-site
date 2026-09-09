---
schema: qual/card@1
id: P-HGRO44
kind: problem
title: The Frobenius kernel of a sharply two-transitive action
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $G$ act sharply $2$-transitively on a set $X$.
Prove that the Frobenius kernel has cardinality $|X|$.
:::

::: solution
Let $N$ be the Frobenius kernel. By definition, $N\trianglelefteq G$, and every
nonidentity element of $N$ acts without fixed points on $X$.

<1>1. A $2$-transitive action is primitive.
::: proof
Suppose $B\subseteq X$ is a block containing distinct points $x,y$. Let
$z\in X$. By $2$-transitivity there is $g\in G$ with
\[
g(x)=x,
\qquad
g(y)=z.
\]
Since $x\in B\cap gB$, the block property gives $gB=B$, hence $z\in B$.
Thus a block containing two points is all of $X$; the only blocks are therefore
singletons and $X$.
:::

<1>2. The $N$-orbits form a $G$-invariant block system.
::: proof
Because $N$ is normal, for $g\in G$ and $x\in X$,
\[
g(Nx)=gNg^{-1}(gx)=N(gx).
\]
Hence $G$ permutes the $N$-orbits. Equivalently, every $N$-orbit is a block for
the action of $G$.
:::

<1>3. The subgroup $N$ acts transitively on $X$.
::: proof
The Frobenius kernel is nontrivial. Choose $1\ne n\in N$ and $x\in X$.
Since $n$ is fixed-point free, $nx\ne x$, so the orbit $Nx$ contains at least
two points. By <1>1 and <1>2, this orbit must therefore be all of $X$.
:::

<1>4. The action of $N$ on $X$ is free.
::: proof
If $n\in N$ fixes some $x\in X$, then the defining fixed-point-free property
of the Frobenius kernel forces $n=1$.
:::

<1>5. Hence $|N|=|X|$.
::: proof
Fix $x\in X$. By <1>3 the orbit map
\[
N\longrightarrow X,
\qquad
n\longmapsto nx
\]
is surjective. By <1>4 it is injective. Thus it is a bijection, so
\[
|N|=|X|.
\]
:::
:::
