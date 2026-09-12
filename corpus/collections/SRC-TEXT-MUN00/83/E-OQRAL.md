---
schema: qual/card@1
id: E-OQRAL
kind: problem
title: Euler numbers of standard graphs and their coverings
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
---

::: {.exercise}

The Euler number of a finite linear graph $X$ equals the number of vertices of $X$ minus the number of edges of $X$.
It is in fact a topological invariant of $X$, as we shall see.
What is the Euler number of an arc?
a circle?
a wedge of $n$ circles?
the complete graph on $n$ vertices?
If $E$ is an $n$-fold covering space of $X$, how are the Euler numbers of $E$ and $X$ related?
:::

::: {.solution}
For a finite graph,
\[
\chi(X)=V-E.
\]

An arc has \(V=2,E=1\), hence
\[
\chi=1.
\]
A circle has \(\chi=0\) (for example one may subdivide it into \(r\) vertices and \(r\) edges).

A wedge of \(n\) circles has one more vertex than the total excess contributed by its \(n\) cycles; using a model with one vertex and \(n\) loop-edges, or any subdivision,
\[
\chi=1-n.
\]

The complete graph \(K_n\) has
\[
V=n,\qquad E=\binom n2,
\]
so
\[
\chi(K_n)=n-\binom n2=\frac{n(3-n)}2.
\]

Finally, if \(p:E\to X\) is an \(r\)-fold covering of a finite graph, every vertex of \(X\) has exactly \(r\) lifts and every edge has exactly \(r\) lifted edges. Therefore
\[
V(E)=rV(X),\qquad E(E)=rE(X),
\]
and hence
\[
\boxed{\chi(E)=r\chi(X).}
\]
:::
