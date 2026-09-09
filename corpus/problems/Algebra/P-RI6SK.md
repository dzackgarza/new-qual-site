---
schema: qual/card@1
id: P-RI6SK
kind: problem
title: $O_p(G)$ is the maximal normal $p$-subgroup of $G$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
---

::: problem
Let
\[
O_p(G)=\bigcap_{P\in\operatorname{Syl}_p(G)}P.
\]
Show that $O_p(G)\normal G$ and that it contains every normal $p$-subgroup of $G$.
:::

::: solution
Conjugation permutes the Sylow $p$-subgroups, so for every $g\in G$,
\[
gO_p(G)g^{-1}
=\bigcap_{P\in\operatorname{Syl}_p(G)}gPg^{-1}
=\bigcap_{P\in\operatorname{Syl}_p(G)}P
=O_p(G).
\]
Thus $O_p(G)\normal G$. Since it is contained in a Sylow $p$-subgroup, it is itself a $p$-group.

Now let $N\normal G$ be any normal $p$-subgroup. Fix a Sylow $p$-subgroup $P$. Since $NP$ is a subgroup and
\[
|NP|=\frac{|N||P|}{|N\cap P|}
\]
is a power of $p$, maximality of $P$ among $p$-subgroups gives $NP=P$. Hence $N\le P$.

This holds for every Sylow $p$-subgroup $P$, so
\[
N\le \bigcap_{P\in\operatorname{Syl}_p(G)}P=O_p(G).
\]
Therefore $O_p(G)$ is the unique largest normal $p$-subgroup of $G$.
:::
