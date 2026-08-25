---
schema: qual/card@1
id: D-YO6NZ
kind: definition
title: Characterizations of connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
---

:::{.definition title="Connected"}
A space $X$ is **disconnected** iff 

- There exists a *separation of $X$*: a decomposition $X = U\Disjoint V$ with $U, V$ disjoint, open, and nonempty.
  - I.e. $X$ can not be decomposed as the disjoint union of two proper nonempty sets.
- The only clopen sets of $X$ are $\emptyset, X$
  -I.e. $X$ contains no proper nonempty clopen sets.
- For $Y \subseteq X$ a subspace, $Y$ is disconnected iff $Y$ is disconnected in the subspace topology.
  Equivalently, a *separation of $Y$ in $X$* is a decomposition $Y = U \Disjoint V$ with $U, V$ open in $Y$ and 
\[
\cl_{Y}(U) \intersect V = \emptyset,\qquad U \intersect \cl_{Y}(V) = \emptyset
,\]
  so neither set contains a limit point of the other.
- $\Hom_\Top(X, \ts{0, 1}) \cong \ts{0, 1}$, i.e. all such continuous functions are constant. 

:::{.example}
Some examples:

- $\QQ$ is disconnected, and $\pi_0(\QQ) \cong \QQ$: the only connected components are singletons.

:::

:::
