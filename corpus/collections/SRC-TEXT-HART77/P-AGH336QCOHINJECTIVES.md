---
schema: qual/card@1
id: P-AGH336QCOHINJECTIVES
kind: problem
title: Quasi-coherent sheaves have enough injectives, and they are flasque
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Quasicoherent Sheaves
  - Injective Sheaves
relations: []
review: draft
---

::: problem
Let $X$ be a noetherian scheme.

a. Show that the sheaf $\mcg$ constructed in the proof of (3.6) is an injective object in the category $\QCoh(X)$ of quasi-coherent sheaves on $X$.
Thus $\QCoh(X)$ has enough injectives.

b. Show that any injective object of $\QCoh(X)$ is flasque.

Hints: The method of proof of (2.4) will not work, because $\mco_U$ is not quasi-coherent on $X$ in general.
Instead, use (II, Ex.
5.15) to show that if $\mci \in \QCoh(X)$ is injective, and if $U \subseteq X$ is an open subset, then $\ro{\mci}{U}$ is an injective object of $\QCoh(U)$.
Then cover $X$ with open affines.

c. Conclude that one can compute cohomology as the derived functors of $\Gamma(X, \wait)$, considered as a functor from $\QCoh(X)$ to $\Ab$.
:::
