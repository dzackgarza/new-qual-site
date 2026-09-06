---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-19
kind: problem
title: Removing a point from a connected manifold of dimension at least 3
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Manifolds
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part Two, question 7 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Verified that the stated local-Euclidean definition is enough: it implies
    T1 and local path-connectedness. Proved M minus q is path-connected, then
    used a Euclidean chart U at q with U minus q simply connected for n at least
    3 and applied van Kampen to U union (M minus q).
---

::: {.problem}
For the sake of this problem a manifold of dimension $n$ will be defined as a topological space in which each point has a neighborhood that is homeomorphic to $\mathbb R^n$.
If $M$ is a connected manifold of dimension at least $3$ and $q\in M$, show that $\pi_1(M-\{q\})$ is isomorphic to $\pi_1(M)$.
:::

::: {.solution}
Let
\[
V=M\setminus\{q\}.
\]
We first verify the point-set facts needed to apply van Kampen under the definition of manifold given in the problem.

<1>1. Every singleton in $M$ is closed; in particular, $V$ is open in $M$.
::: {.proof}
Fix distinct points $x,y\in M$.
Choose a Euclidean neighborhood $N$ of $y$ and an open set $O\subseteq M$ with
\[
y\in O\subseteq N.
\]
If $x\notin N$, then $O$ is already an open neighborhood of $y$ avoiding $x$.

If $x\in N$, the space $N$ is homeomorphic to $\mathbb R^n$ and hence is $T_1$.
Thus there is a set $W$ open in the subspace $N$ such that
\[
y\in W
\qquad\text{and}\qquad
x\notin W.
\]
Write
\[
W=N\cap G
\]
for some open $G\subseteq M$.
Then
\[
O\cap G
\]
is an open neighborhood of $y$ in $M$ that avoids $x$.

Thus, for every $y\ne x$, there is an open neighborhood of $y$ disjoint from $\{x\}$.
Hence
\[
M\setminus\{x\}
\]
is open, so $\{x\}$ is closed.
Taking $x=q$ proves that $V$ is open.
:::

<1>2. We may choose an open neighborhood $U$ of $q$ homeomorphic to $\mathbb R^n$, with $q$ corresponding to $0$.
::: {.proof}
Let $N$ be a neighborhood of $q$ homeomorphic by
\[
h:N\longrightarrow\mathbb R^n
\]
to Euclidean space.
Since $N$ is a neighborhood, choose open $O\subseteq M$ with
\[
q\in O\subseteq N.
\]
The set $h(O)$ is open in $\mathbb R^n$ relative to the chart, so it contains an open Euclidean ball $B$ about $h(q)$.
After translating coordinates, take $h(q)=0$.
Then
\[
U=h^{-1}(B)
\]
is open in $M$: because $h^{-1}(B)$ is open in the subspace $N$, write it as $N\cap G$ for some open $G\subseteq M$; since it lies in $O\subseteq N$, it equals $O\cap G$.
Finally, composing $h|_U$ with a homeomorphism $B\cong\mathbb R^n$ gives the desired open chart
\[
U\cong\mathbb R^n
\]
sending $q$ to $0$.
:::

<1>3. The punctured chart
\[
U\setminus\{q\}
\]
is path-connected.
::: {.proof}
By <1>2,
\[
U\setminus\{q\}
\cong
\mathbb R^n\setminus\{0\}.
\]
The radial map
\[
x\longmapsto\frac{x}{\|x\|}
\]
is the endpoint of the deformation retraction
\[
H(x,t)
=\left((1-t)+\frac{t}{\|x\|}\right)x
\]
from $\mathbb R^n\setminus\{0\}$ onto $S^{n-1}$.
Since $n\ge3$, the sphere $S^{n-1}$ has dimension at least $2$ and is path-connected.
Therefore $U\setminus\{q\}$ is path-connected.
:::

<1>4. The punctured manifold $V=M\setminus\{q\}$ is path-connected.
::: {.proof}
Every point of $M$ has a Euclidean neighborhood, so $M$ is locally path-connected.
The open subspace $V$ is therefore locally path-connected as well.
Hence every path component of $V$ is open in $V$, and by <1>1 is consequently open in $M$.

By <1>3, the set
\[
U\setminus\{q\}
\]
is path-connected, so it lies in a single path component $C_0$ of $V$.
Suppose there were another path component.
Let $W$ be the union of all path components of $V$ other than $C_0$.
Then $W$ is a nonempty open subset of $M$.
Moreover,
\[
C_0\cup\{q\}=C_0\cup U,
\]
because $U\setminus\{q\}\subseteq C_0$.
The right-hand side is open in $M$, and it is the complement of $W$.
Thus
\[
M=W\sqcup(C_0\cup\{q\})
\]
would be a separation of $M$, contradicting the connectedness of $M$.
Therefore $W$ is empty and $V=C_0$ is path-connected.
:::

<1>5. For $n\ge3$, the punctured chart $U\setminus\{q\}$ is simply connected.
::: {.proof}
By <1>3 it deformation retracts onto
\[
S^{n-1}.
\]
It therefore suffices to show that $S^m$ is simply connected for $m\ge2$.

Cover $S^m$ by two open sets $A,B$, each obtained by enlarging an open hemisphere slightly past the equator.
Both $A$ and $B$ are contractible.
Their intersection deformation retracts onto the equatorial sphere
\[
S^{m-1},
\]
which is path-connected because $m-1\ge1$.
The Seifert--van Kampen theorem gives
\[
\pi_1(S^m)
\cong
\pi_1(A)*_{\pi_1(A\cap B)}\pi_1(B).
\]
Since
\[
\pi_1(A)=\pi_1(B)=0,
\]
this amalgamated product is the trivial group.
Thus $S^m$ is simply connected for $m\ge2$, and hence so is $U\setminus\{q\}$.
:::

<1>6. The inclusion
\[
i:V=M\setminus\{q\}\hookrightarrow M
\]
induces an isomorphism on fundamental groups.
::: {.proof}
Choose a basepoint
\[
x_0\in U\setminus\{q\}.
\]
By <1>1--<1>2, both $U$ and $V$ are open, and
\[
M=U\cup V.
\]
By <1>3--<1>4, the sets $U$, $V$, and
\[
U\cap V=U\setminus\{q\}
\]
are path-connected.
Furthermore,
\[
\pi_1(U,x_0)=0
\]
because $U\cong\mathbb R^n$, and by <1>5,
\[
\pi_1(U\cap V,x_0)=0.
\]

The Seifert--van Kampen theorem identifies $\pi_1(M,x_0)$ with the pushout
\[
\pi_1(U,x_0)
*_{\pi_1(U\cap V,x_0)}
\pi_1(V,x_0).
\]
Both groups involving $U$ are trivial, so this pushout is canonically
\[
\pi_1(V,x_0).
\]
Under this identification, the canonical map from $\pi_1(V,x_0)$ to the pushout is exactly the homomorphism induced by the inclusion $i$.
Therefore
\[
i_*:\pi_1(M\setminus\{q\},x_0)
\xrightarrow{\ \cong\ }
\pi_1(M,x_0).
\]
Hence
\[
\boxed{\pi_1(M\setminus\{q\})\cong\pi_1(M).}
\]
:::
:::
