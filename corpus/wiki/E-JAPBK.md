---
schema: qual/card@1
id: E-JAPBK
kind: exercise
title: "Quotient by nilradical is reduced"
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - ideals
  - rings
relations: []
review: draft
solved: true
---
:::{.exercise title="Quotient by nilradical is reduced"}
Show $\nilrad{R} \normal R$ is an ideal and $A/\nilrad{R}$ is reduced.
:::

:::{.solution}
\envlist

- $R\nilrad{R} \subseteq R$:
  For $r$ nilpotent of order $n$ and $x\in R$, $xr$ is nilpotent since 
\[
(xr)^n = (xr)(xr)\cdots(xr) = x^n r^n = x^n 0 = 0
.\]

- $R^2 \subseteq R$, for $r,s\in \nilrad{R}$ write $r^{n} = s^m = 0$, then
\[
(r+s)^{N} = \sum_{k\geq 0}{N \choose k} r^k s^{N-k}
,\]
so just choose $N$ large enough so that either $k>n$ or $N-k> m$ always holds, e.g. $N\da n+m-1$.

- $R/\nilrad{R}$ has no nonzero nilpotents:
  Take $\bar{r} \in R/\nilrad{R}$ for some $r\in R$, then $\phi(r^n) = \phi(r)^n = \bar{r}^n$.
  So\[
\bar{r}^n=0 \mod \nilrad{R} \iff \bar{r^n} \equiv 0 \mod \nilrad{R} \iff r^n \in \nilrad{R} \iff r\in 0_R
  .\]

:::
