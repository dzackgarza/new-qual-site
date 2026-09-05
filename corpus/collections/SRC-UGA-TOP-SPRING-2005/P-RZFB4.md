---
schema: qual/card@1
id: P-RZFB4
kind: problem
title: $n$-fold covering spaces of the torus, and $3$-fold covering spaces
  of a torus minus a disk
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Checked problem 6 and its punctured-torus diagram against the official UGA
    Spring 2005 topology exam. Removed the card's unsupported connectedness
    hypothesis in part (a); the source does not assume either covering is
    connected.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Classified all connected components by covering degree, Euler
    characteristic, orientability, and boundary monodromy; the disconnected
    degree-three cases are included rather than silently assuming connectedness.
---

::: problem
a. Suppose $Y$ is an $n$-fold covering space of the (one-holed) torus $S^1\times S^1$.
Up to homeomorphism, what is $Y$? Justify your answer.

b. Let $X$ be the topological space obtained by deleting a disk from a torus.
Suppose $Y$ is a $3$-fold covering space of $X$.
What surfaces could $Y$ be?
Justify your answer, but you need not exhibit the covering maps explicitly.
:::

::: {.solution}
Write $\Sigma_{g,b}$ for the compact connected orientable surface of genus $g$ with $b$ boundary components.

<1>1. Every connected finite-sheeted covering of the torus $T^2$ is homeomorphic to $T^2$.
::: {.proof}
Let $Z\to T^2$ be a connected covering of degree $d<\infty$.
Lifting a finite CW structure on $T^2$ gives a finite CW structure on $Z$ with $d$ lifts of every cell, so
\[
\chi(Z)=d\,\chi(T^2)=0.
\]
The space $Z$ is a compact connected surface without boundary.
It is orientable because an orientation atlas on $T^2$ lifts through the local homeomorphism $Z\to T^2$.
Hence the classification theorem for compact connected orientable surfaces gives
\[
0=\chi(Z)=2-2g,
\]
so $g=1$ and $Z\cong T^2$.
:::

<1>2. In part (a), if $Y$ has $k$ connected components, then
\[
\boxed{Y\cong\coprod_{j=1}^{k}T^2}
\qquad\text{for some }1\le k\le n.
\]
Conversely every $k\in\{1,\ldots,n\}$ occurs.
::: {.proof}
Each component of a covering maps onto the connected base $T^2$ and has some positive covering degree $d_j$.
The degrees satisfy
\[
d_1+\cdots+d_k=n.
\]
By <1>1 every component is a torus, proving the displayed homeomorphism type.

Conversely, for every positive integer $d$ the map
\[
S^1\times S^1\longrightarrow S^1\times S^1,
\qquad
(z,w)\longmapsto(z^d,w)
\]
is a connected $d$-sheeted covering.
Given $1\le k\le n$, take one component of degree $n-k+1$ and $k-1$ components of degree $1$.
Their disjoint union is an $n$-sheeted covering with exactly $k$ torus components.
:::

<1>3. For part (b), the base is
\[
X\cong\Sigma_{1,1},
\qquad
\chi(X)=-1,
\qquad
\pi_1(X)\cong F(a,b),
\]
and its boundary loop represents the commutator $[a,b]=aba^{-1}b^{-1}$.
::: {.proof}
Removing the interior of a disk from a torus gives the once-bordered torus $\Sigma_{1,1}$.
Its Euler characteristic is
\[
2-2(1)-1=-1.
\]
Collapsing the usual square model away from the boundary gives the standard free generators $a,b$, while the boundary of the removed disk is homotopic, with a choice of orientation, to the commutator attaching word $[a,b]$.
:::

<1>4. A connected $3$-sheeted cover $Z\to X$ is homeomorphic to exactly one of
\[
\boxed{\Sigma_{2,1}\quad\text{or}\quad\Sigma_{1,3},}
\]
and both possibilities occur.
::: {.proof}
The cover $Z$ is compact, connected, and orientable, and
\[
\chi(Z)=3\chi(X)=-3.
\]
If $Z\cong\Sigma_{g,b}$, then
\[
2-2g-b=-3,
\qquad\text{hence}\qquad
2g+b=5.
\]
The inverse image of the one boundary circle of $X$ is nonempty and has at most three components, so $1\le b\le3$.
The equation $2g+b=5$ therefore leaves only
\[
(g,b)=(2,1)\quad\text{or}\quad(1,3).
\]

It remains to see that both occur.
A connected $3$-sheeted cover of $X$ is specified by a transitive monodromy action
\[
\rho:F(a,b)\longrightarrow S_3.
\]
The number of boundary components upstairs is the number of cycles of the permutation $\rho([a,b])$, because these cycles are precisely the connected components of the covering restricted to the boundary circle.

For
\[
\rho(a)=(123),
\qquad
\rho(b)=1,
\]
the action is transitive and $\rho([a,b])=1$, which has three cycles; this gives $\Sigma_{1,3}$.
For
\[
\rho(a)=(12),
\qquad
\rho(b)=(23),
\]
the generated subgroup is $S_3$, hence transitive, and $\rho([a,b])$ is a $3$-cycle; this gives $\Sigma_{2,1}$.
Thus both topological types occur.
:::

<1>5. A connected $2$-sheeted cover of $X$ is homeomorphic to
\[
\Sigma_{1,2}.
\]
::: {.proof}
For a connected double cover $Z\to X$,
\[
\chi(Z)=2\chi(X)=-2.
\]
Its monodromy takes values in the abelian group $S_2$, so the commutator $[a,b]$ acts trivially on the two sheets.
Thus the inverse image of $\partial X$ has two components.
Writing $Z\cong\Sigma_{g,2}$ gives
\[
2-2g-2=-2,
\]
so $g=1$.
:::

<1>6. Therefore every $3$-sheeted covering in part (b) is homeomorphic to exactly one of
\[
\boxed{
\Sigma_{2,1},\qquad
\Sigma_{1,3},\qquad
\Sigma_{1,2}\amalg\Sigma_{1,1},\qquad
\Sigma_{1,1}\amalg\Sigma_{1,1}\amalg\Sigma_{1,1}.
}
\]
::: {.proof}
The degrees of the connected components form a partition of $3$.
For the partition $3$, <1>4 gives the two connected possibilities.
For $2+1$, <1>5 gives $\Sigma_{1,2}$ for the degree-$2$ component and the degree-$1$ component is $X\cong\Sigma_{1,1}$.
For $1+1+1$, all three components are copies of $X$.
These exhaust the partitions of $3$.
:::
:::
