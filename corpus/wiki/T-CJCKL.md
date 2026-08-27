---
schema: qual/card@1
id: T-CJCKL
kind: theorem
title: Rouché's Theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Winding Number
  - Meromorphic Functions
relations: []
review: draft
---

:::{.theorem ref="Rouche"}
Let $M, m$ be meromorphic on $\Omega$ and write $Z_M, Z_m, P_M, P_m$ for the numbers of zeros and poles of $M$ and $m$ respectively.
Suppose $\gamma \subseteq \Omega$ is a toy contour winding about each zero and pole of $f$ and $g$ precisely once.
Then
\[
\abs{m} \leq \abs{M} \text{ on } \gamma \implies \Index_{z=0}(M\circ \gamma)(z) 
&= \Index_{z=0}((M+m)\circ \gamma)(z) \\
\implies Z_M - P_M 
&= Z_{M+m} - P_{M+m}
.\]
In particular, if $M, m$ are *holomorphic* on $\Omega$, then $M$ and $M+m$ have the same number of zeros in $\Omega$, i.e. $Z_M = Z_{M+m}$.
:::
