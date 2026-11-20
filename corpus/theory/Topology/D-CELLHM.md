---
schema: qual/card@1
id: D-CELLHM
kind: proposition
title: Computing cellular homology
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a CW complex with finitely many cells in each dimension.
The cellular chain group $C_n(X)$ is free abelian on the $n$-cells $e^n_\alpha$, and the differential is
$$
\del_n(e^n_\alpha) = \sum_\beta d_{\alpha\beta}\, e^{n-1}_\beta,
$$
where $d_{\alpha\beta}$ is the degree of the map $S^{n-1}\to X^{(n-1)}\to X^{(n-1)}/(X^{(n-1)}\sm e^{n-1}_\beta)\cong S^{n-1}$ obtained from the attaching map of $e^n_\alpha$ by collapsing the complement of the $\beta$-cell.
The homology of this chain complex is $H_n(X)$ [@Hat02, Theorem 2.35]; in particular $H_n(X)=0$ if $X$ has no $n$-cells, and $H_n(X)$ is free on the $n$-cells if no two cells lie in adjacent dimensions.
:::
