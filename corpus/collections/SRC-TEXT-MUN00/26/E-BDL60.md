---
schema: qual/card@1
id: E-BDL60
kind: problem
title: Compact subspaces in the finite complement and countable complement topologies
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

(a) Show that in the finite complement topology on $\mathbb{R}$, every subspace is compact.

(b) If $\mathbb{R}$ has the topology consisting of all sets $A$ such that $\mathbb{R} - A$ is either countable or all of $\mathbb{R}$, is $[0, 1]$ a compact subspace?
:::

::: {.solution}
(a) Let \(Y\subset \mathbb R\), with the subspace topology inherited from the finite-complement topology on \(\mathbb R\). If \(Y\) is finite it is compact. Suppose \(Y\) is infinite. Then a nonempty open set in \(Y\) has the form
\[
Y\cap U=Y\setminus F
\]
with \(F\) finite. Thus the subspace topology on \(Y\) is again the finite-complement topology. Given an open cover \(\{U_i\}_{i\in I}\) of \(Y\), choose one nonempty member \(U_{i_0}=Y\setminus F\). The finite set \(F\) is covered by finitely many further members of the cover, so together with \(U_{i_0}\) these form a finite subcover. Hence every subspace is compact.

(b) No. In the countable-complement topology, the subspace topology on \([0,1]\) is the countable-complement topology on \([0,1]\). Choose distinct points \(x_n\in[0,1]\), and set
\[
U_n=[0,1]\setminus\{x_m:m\ge n\}.
\]
Each \(U_n\) is open in the subspace, the family is increasing, and \(\bigcup_nU_n=[0,1]\). But a finite subfamily has union equal to its largest member \(U_N\), which omits infinitely many points \(x_m\) for \(m\ge N\). Thus there is no finite subcover.
:::
