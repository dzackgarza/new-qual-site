---
schema: qual/card@1
id: P-V45EL
kind: problem
title: Representations of a finite $p$-group on a vector space over a finite field of characteristic $p$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - p-Groups
  - Characteristic
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite $p$-group and let $V$ be a nonzero finite-dimensional vector space over a finite field $k$ of characteristic $p$. What can be said about a representation
\[
G\to GL(V)?
\]
:::

::: {.solution}
Every such representation has a nonzero fixed vector:
\[
V^G\ne0.
\]

Indeed, let $G$ act on the finite set underlying $V$. Every orbit has size a power of $p$. Hence all nontrivial orbits have cardinality divisible by $p$. Therefore
\[
|V|\equiv |V^G|\pmod p.
\]
Since
\[
|V|=|k|^{\dim V}
\]
is divisible by $p$, it follows that
\[
|V^G|\equiv0\pmod p.
\]
The zero vector is fixed, so $|V^G|\ge p$ and there is a nonzero fixed vector.

Consequently every irreducible $k$-representation of $G$ is trivial. If $V$ is irreducible, then the nonzero fixed subspace $V^G$ is a nonzero $G$-stable subspace, so
\[
V^G=V.
\]
Thus $G$ acts trivially. Irreducibility then forces $\dim_kV=1$.

More generally, every finite-dimensional representation admits a filtration whose successive quotients are trivial one-dimensional representations: choose a nonzero fixed vector, quotient by its span, and argue inductively.
:::
