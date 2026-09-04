---
schema: qual/card@1
id: P-LMVF6
kind: problem
title: Finite trees are contractible
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked leaf existence, preservation of the tree property after leaf deletion, and the terminal-edge strong deformation retraction.
---

::: problem
Prove that any finite tree is contractible, where a **tree** is a connected graph that contains no closed edge paths.
:::

::: {.solution}
<1>1. If a finite tree \(T\) has at least one edge, then \(T\) has a vertex of degree \(1\).
::: {.proof}
Choose a simple edge path
\[
v_0,e_1,v_1,\dots,e_m,v_m
\]
of maximal length; such a path exists because \(T\) has finitely many vertices and edges.
Since \(T\) has an edge, \(m\ge1\).

Consider an edge \(e\) incident to the endpoint \(v_m\). If \(e\ne e_m\) and its other endpoint \(w\) is not already among
\[
v_0,\dots,v_m,
\]
then adjoining \(e,w\) extends the chosen simple path, contradicting maximality.
If instead \(w=v_j\) for some \(j<m\), then the segment of the chosen path from \(v_j\) to \(v_m\), together with \(e\), forms a closed edge cycle, contradicting that \(T\) is a tree.
Thus the only edge incident to \(v_m\) is \(e_m\), so
\[
\deg(v_m)=1.
\]
:::

<1>2. Let \(v\) be a degree-\(1\) vertex of \(T\), let \(e\) be its unique incident edge, and let \(w\) be the other endpoint of \(e\). Removing \(v\) and the open edge \(e\) leaves a finite tree
\[
T'=T\setminus(\{v\}\cup e^\circ).
\]
::: {.proof}
The graph \(T'\) is finite.
It contains no closed edge cycle, since any such cycle would already be a cycle in \(T\).

It remains to prove connectedness.
Let \(x,y\) be vertices of \(T'\). Since \(T\) is connected, there is an edge path from \(x\) to \(y\). Delete loops from this path until it is simple.
A simple path joining two vertices different from \(v\) cannot pass through \(v\): if it did, the degree-\(1\) vertex \(v\) would have to be an interior vertex of the path and hence would need two distinct incident path edges.
Therefore the simple path lies entirely in \(T'\). Thus \(T'\) is connected and hence is again a tree.
:::

<1>3. The tree \(T\) strongly deformation retracts onto \(T'\).
::: {.proof}
Identify the closed edge \(e\) with the interval \([0,1]\) so that
\[
w\leftrightarrow0,
\qquad
v\leftrightarrow1.
\]
Define
\[
H:T\times[0,1]\to T
\]
by fixing every point of \(T'\) and, for \(s\in[0,1]\cong e\), setting
\[
H(s,t)=(1-t)s.
\]
On the common point \(w\), both formulas give \(w\), so the two definitions paste to a continuous map.
At \(t=0\), \(H\) is the identity.
At \(t=1\), the entire edge \(e\) has collapsed to \(w\), and every point of \(T'\) has remained fixed throughout.
Hence \(H\) is a strong deformation retraction of \(T\) onto \(T'\).
:::

<1>4. Every finite tree is contractible.
::: {.proof}
Induct on the number \(m\) of edges.

If \(m=0\), connectedness implies that the graph consists of a single vertex, so it is a point and is contractible.

Assume every finite tree with fewer than \(m\) edges is contractible, and let \(T\) have \(m\ge1\) edges.
By <1>1 choose a leaf \(v\), and form \(T'\) as in <1>2. Then \(T'\) is a finite tree with \(m-1\) edges, so by the induction hypothesis \(T'\) is contractible.
By <1>3, \(T\) deformation retracts onto \(T'\). A space that deformation retracts onto a contractible subspace is contractible: compose the deformation retraction with a contraction of \(T'\) to a point.
Therefore \(T\) is contractible.
:::
:::
