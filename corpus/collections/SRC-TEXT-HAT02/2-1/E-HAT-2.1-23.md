---
schema: qual/card@1
id: E-HAT-2.1-23
kind: problem
title: Second barycentric subdivision of $\Delta$-complex is simplicial
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
  - Barycentric Subdivision
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 23; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked at chain/skeletal/combinatorial level.
---

Show that the second barycentric subdivision of a $\Delta$-complex is a simplicial complex.
Namely, show that the first barycentric subdivision produces a $\Delta$-complex with the property that each simplex has all its vertices distinct, then show that for a $\Delta$-complex with this property, barycentric subdivision produces a simplicial complex.

::: {.solution}
Recall that the vertices of the barycentric subdivision are barycenters of simplices, and its simplices correspond to chains of faces.

<1>1. Every simplex in the first barycentric subdivision of a $\Delta$-complex has distinct vertices.
::: {.proof}
A $k$-simplex in the barycentric subdivision is determined inside some original simplex by a strict chain of faces
\[
\sigma_0<\sigma_1<\cdots<\sigma_k.
\]
Its vertices are the barycenters
\[
b_{\sigma_0},b_{\sigma_1},\dots,b_{\sigma_k}.
\]
Since the face inclusions are strict,
\[
\dim\sigma_0<\dim\sigma_1<\cdots<\dim\sigma_k,
\]
so these simplices, and hence their barycenters as vertices of the subdivided $\Delta$-complex, are all distinct.
:::

<1>2. Suppose now that a $\Delta$-complex $Y$ has the property that every simplex has distinct vertices. Then a face of a simplex of $Y$ is determined uniquely by its set of vertices.
::: {.proof}
Let $\tau$ be an $m$-simplex of $Y$. Its characteristic simplex has $m+1$ distinct image vertices. A face of $\tau$ is obtained by deleting a subset of these vertices. Because the vertices are distinct, two different faces of the standard simplex have different image vertex sets. Hence within $\tau$ a prescribed subset of its vertices determines at most one face.
:::

<1>3. In the barycentric subdivision $Y'$, a finite set of vertices spans at most one simplex.
::: {.proof}
A vertex of $Y'$ is a simplex of $Y$. A set
\[
\{\sigma_0,\dots,\sigma_k\}
\]
spans a simplex of $Y'$ exactly when these simplices can be ordered into a strict face chain
\[
\sigma_{i_0}<\sigma_{i_1}<\cdots<\sigma_{i_k}.
\]
Such an ordering is unique because dimensions strictly increase along a proper face inclusion. By <1>2, the individual face incidences are themselves unambiguous. Hence the given vertex set determines at most one simplex of $Y'$.
:::

<1>4. Intersections of simplices in $Y'$ are common faces.
::: {.proof}
Write two simplices as chains of simplices of $Y$. Their common vertices are exactly the simplices appearing in both chains. Since each chain is totally ordered by face inclusion, the common vertices again form a chain, hence span a face of each subdivided simplex. By <1>3 there is no second simplex with the same vertex set. Therefore the intersection is precisely this common face.
:::

Properties <1>3 and <1>4 are the defining combinatorial conditions for a simplicial complex. Applying <1>1 to the first barycentric subdivision $X'$ and then <1>2--<1>4 to $Y=X'$ shows that
\[
\boxed{X''\text{ is a simplicial complex}.}
\]
:::
