---
schema: qual/card@1
id: E-HAT-2.1-28
kind: problem
title: Local homology groups of cone on 1-skeleton of $\Delta^3$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Local Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 28; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed against the relevant chain, relative-homology, local-homology, or covering-space calculation.
---

Let $X$ be the cone on the 1 skeleton of $\Delta^3$, the union of all line segments joining points in the six edges of $\Delta^3$ to the barycenter of $\Delta^3$.
Compute the local homology groups $H_n(X, X - \{x\})$ for all $x \in X$.
Define $\partial X$ to be the subspace of points $x$ such that $H_n(X, X - \{x\}) = 0$ for all $n$, and compute the local homology groups $H_n(\partial X, \partial X - \{x\})$.
Use these calculations to determine which subsets $A \subset X$ have the property that $f(A) \subset A$ for all homeomorphisms $f: X \to X$.

::: {.solution}
Let $G$ be the $1$-skeleton of $\Delta^3$, so $G\cong K_4$, and write
\[
X=CG
\]
with cone point $c$.
The graph $G$ has $4$ vertices and $6$ edges, hence
\[
\widetilde H_1(G)\cong\mathbb Z^{6-4+1}=\mathbb Z^3.
\]

<1>1. At the cone point $c$,
\[
H_n(X,X-\{c\})\cong
\begin{cases}
\mathbb Z^3,&n=2,\\
0,&n\ne2.
\end{cases}
\]
::: {.proof}
Since $X$ is contractible and $X-\{c\}$ deformation retracts onto $G$, the long exact sequence of the pair gives
\[
H_n(X,X-\{c\})\cong\widetilde H_{n-1}(G).
\]
The stated groups follow from the homology of $K_4$.
:::

<1>2. If $x$ lies in the interior of one of the four radial edges from $c$ to a vertex of $G$, then
\[
H_n(X,X-\{x\})\cong
\begin{cases}
\mathbb Z^2,&n=2,\\
0,&n\ne2.
\end{cases}
\]
::: {.proof}
Three triangular $2$-cells meet along each such radial edge. A neighborhood of $x$ is homeomorphic to
\[
\mathbb R\times C(P_3),
\]
where $P_3$ is a discrete set of three points and $x$ corresponds to $(0,\text{cone point})$. Local homology is shifted by the open $\mathbb R$ factor, so
\[
H_n(X,X-\{x\})\cong\widetilde H_{n-2}(P_3).
\]
Since $\widetilde H_0(P_3)\cong\mathbb Z^2$, the claim follows.
:::

<1>3. If $x$ lies in the interior of one of the six triangular $2$-cells, then
\[
H_n(X,X-\{x\})\cong
\begin{cases}
\mathbb Z,&n=2,\\
0,&n\ne2.
\end{cases}
\]
::: {.proof}
Such a point has a neighborhood homeomorphic to $\mathbb R^2$, whose local homology is $\mathbb Z$ in degree $2$ and zero otherwise.
:::

<1>4. If $x\in G$, then
\[
H_n(X,X-\{x\})=0
\qquad\text{for all }n.
\]
::: {.proof}
At an interior point of an edge of $G$, a neighborhood in $X$ is a half-plane, whose local homology at a boundary point vanishes. At a vertex of $G$, the local link in $X$ is a tree with one central vertex and three leaves, hence contractible; local homology is the reduced homology of this link shifted by one, so it vanishes in every degree.
:::

Thus
\[
\boxed{\partial X=G.}
\]

<1>5. The local homology in $\partial X=G$ is
\[
H_n(G,G-\{x\})\cong
\begin{cases}
\mathbb Z,&n=1,\quad x\text{ in the interior of an edge},\\
\mathbb Z^2,&n=1,\quad x\text{ a vertex},\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
At an interior edge point, $G$ is locally a line, giving local $H_1\cong\mathbb Z$. At a vertex, three half-edges meet. The local link is three points, so
\[
H_1(G,G-\{x\})\cong\widetilde H_0(P_3)\cong\mathbb Z^2.
\]
All other local groups vanish.
:::

<1>6. The homeomorphism group of $X$ has exactly five point-orbits:
\[
\{c\},
\quad
\text{open radial edges},
\quad
\text{open $2$-cells},
\quad
\text{vertices of }G,
\quad
\text{open edges of }G.
\]
::: {.proof}
The local homology calculations distinguish these five types: the first three by ranks $3,2,1$ of local $H_2$, and the last two by ranks $2,1$ of local $H_1$ inside the intrinsically defined subspace $\partial X$.

Conversely, the tetrahedral symmetry group is transitive on the vertices and edges of $G$, hence on the corresponding radial edges and triangular $2$-cells. Within any one open cell, a homeomorphism supported in that cell (and extended over its star when necessary) can move any chosen interior point to any other. Thus each listed stratum is a single orbit.
:::

<1>7. A subset $A\subseteq X$ satisfies
\[
f(A)\subseteq A
\qquad\text{for every homeomorphism }f:X\to X
\]
if and only if it is a union of these five orbits.
::: {.proof}
Applying the hypothesis to $f^{-1}$ gives $A\subseteq f(A)$, so in fact $f(A)=A$ for every homeomorphism. Therefore $A$ must be a union of point-orbits. Conversely every union of orbits is invariant. By <1>6 the five displayed strata are exactly the orbits.
:::

Hence there are exactly
\[
\boxed{2^5=32}
\]
such invariant subsets.
:::
