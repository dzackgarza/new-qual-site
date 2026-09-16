---
schema: qual/card@1
id: D-UEWPN
kind: definition
title: Long exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Homology
relations: []
review: draft
---

::: {.definition}
A \dfn{long exact sequence} is an [[D-STPAM|exact sequence]] with infinitely many terms, indexed by $\ZZ$ or by an infinite interval of $\ZZ$.
:::

::: {.theorem}
Let $0\to A_\bullet\mapsvia{i}B_\bullet\mapsvia{j}C_\bullet\to0$ be a short exact sequence of chain complexes of abelian groups.
There are homomorphisms $\del\colon H_n(C_\bullet)\to H_{n-1}(A_\bullet)$, the \dfn{connecting homomorphisms}, such that
$$
\cdots\to H_n(A_\bullet)\mapsvia{i_*}H_n(B_\bullet)\mapsvia{j_*}H_n(C_\bullet)\mapsvia{\del}H_{n-1}(A_\bullet)\to\cdots
$$
is exact [@Hat02, Theorem 2.16].
:::

::: {.example}
For a topological space $X$ and a subspace $A$, the short exact sequence $0\to C_\bullet(A)\to C_\bullet(X)\to C_\bullet(X,A)\to0$ of singular chain complexes gives the long exact sequence of the pair
$$
\cdots\to H_n(A)\to H_n(X)\to H_n(X,A)\mapsvia{\del}H_{n-1}(A)\to\cdots\to H_0(X,A)\to0
$$
[@Hat02, p. 117].
:::
