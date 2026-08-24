---
schema: qual/card@1
id: P-ALGF24E
kind: problem
title: Support of a finitely generated module equals $V(\operatorname{ann}(M))$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
---

::: problem
Suppose $A$ is a unital commutative ring and $\operatorname{Spec}(A)$ is the set of all the prime ideals of $A$.
For an $A$-module $M$ and $\mathfrak{p} \in \operatorname{Spec}(A)$, let $M_{\mathfrak{p}}$ be the localization of $M$ at $\mathfrak{p}$.
Let
\[
\operatorname{supp} M := \{\mathfrak{p} \in \operatorname{Spec}(A) \mid M_{\mathfrak{p}} \neq 0\}.
\]
Prove that for a finitely generated $A$-module $M$,
\[
\operatorname{supp} M = \{\mathfrak{p} \in \operatorname{Spec}(A) \mid \operatorname{ann}(M) \subseteq \mathfrak{p}\},
\]
where $\operatorname{ann}(M)$ is the annihilator of $M$.
:::
