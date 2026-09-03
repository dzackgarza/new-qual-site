---
schema: qual/card@1
id: E-ZXKDY
kind: problem
title: Degree of a non-surjective map $S^n\to S^n$ is zero
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is not surjective then $\deg f = 0$.
:::

::: {.solution}
Choose $p\in S^n\setminus f(S^n)$.
Then $f$ factors as
\[
S^n \mapsvia{f_1} S^n\smts{p}\mapsvia{j} S^n,
\]
where $j$ is the inclusion.
Since $S^n\smts{p}\cong\RR^n$ is contractible,
\[
H_n(S^n\smts{p})=0.
\]
Hence the induced map on top homology factors through the zero group:
\[
H_n(S^n)\mapsvia{(f_1)_*}0\mapsvia{j_*}H_n(S^n).
\]
Thus $f_*=0$ on $H_n(S^n)\cong\ZZ$.
By the definition of degree, $\deg f=0$.
:::
