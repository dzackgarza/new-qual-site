---
schema: qual/card@1
id: E-RIGIX
kind: problem
title: Complete normality of standard spaces and constructions
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
---

::: {.exercise}

Which of the following spaces are completely normal?
Justify your answers.

(a) A subspace of a completely normal space.

(b) The product of two completely normal spaces.

(c) A well-ordered set in the order topology.

(d) A metrizable space.

(e) A compact Hausdorff space.

(f) A regular space with a countable basis.

(g) The space $\mathbb{R}_\ell$.
:::

::: {.solution}
(a) Yes. Every subspace of a subspace of a completely normal space is a subspace of the original space, hence normal.

(b) No. The Sorgenfrey line \(\mathbb R_\ell\) is completely normal, but the Sorgenfrey plane \(\mathbb R_\ell\times\mathbb R_\ell\) is not normal, as shown by the anti-diagonal exercise of §31.

(c) Yes. More generally, linearly ordered topological spaces are hereditarily normal; in particular every subspace of a well-ordered set in the order topology is normal.

(d) Yes. Every subspace of a metrizable space is metrizable, hence normal.

(e) No. Let \(J\) be uncountable. The cube \([0,1]^J\) is compact Hausdorff, but it contains the subspace \((0,1)^J\), which is homeomorphic to \(\mathbb R^J\) and is not normal by Stone's theorem. Thus \([0,1]^J\) is not completely normal.

(f) Yes. Every subspace of a regular second-countable space is regular and second countable. Second-countable spaces are Lindelöf, so every subspace is regular Lindelöf and hence normal by the preceding exercise. Thus the original space is completely normal.

(g) Yes. First, every subspace \(A\subset\mathbb R_\ell\) is Lindelöf. Given an open cover of \(A\), refine it so that for each \(x\in A\) one chosen member contains a basic interval \([x,b_x)\cap A\). The ordinary open intervals \((x,b_x)\) have union \(O\subset\mathbb R\). Since the usual real line is second countable, \(O\) is Lindelöf, so countably many of these ordinary intervals cover \(O\). The exceptional set
\[
D=A\setminus O
\]
is countable: if \(d<d'\) are in \(D\), then \(d'\notin(d,b_d)\), hence \(d'\ge b_d\); therefore the intervals \((d,b_d)\), \(d\in D\), are pairwise disjoint, and assigning a rational point to each gives an injection \(D\hookrightarrow\mathbb Q\). Adding one chosen cover member for each point of the countable set \(D\) gives a countable subcover of \(A\).

The Sorgenfrey line is regular, and regularity is hereditary to subspaces. Hence every subspace is regular Lindelöf and therefore normal by the preceding exercise. Thus \(\mathbb R_\ell\) is completely normal.
:::
