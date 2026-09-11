---
schema: qual/card@1
id: T-FULBETTI
kind: theorem
title: Betti numbers of a smooth complete toric variety from the cone counts
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cohomology
  - Fans
relations:
- kind: uses
  target: PR-TORMOR
- kind: uses
  target: T-TORDIV
review: draft
prompts:
- Compute the Betti numbers of a smooth complete toric variety from its fan.
- Why is the odd cohomology of a smooth complete toric variety zero?
---

::: {.theorem title="Betti numbers"}
Let $X_\Sigma$ be smooth and complete of dimension $n$, and write $\Sigma(k)$ for the set of $k$-dimensional cones.
Then the odd Betti numbers vanish and
\[
\beta_{2k} = \sum_{i=k}^{n} (-1)^{i-k} \binom{i}{k} \size \Sigma(n-i) .
\]
:::

::: {.theorem title="Two special cases"}
\[
\beta_0 = \beta_{2n} = 1, \qquad \chi(X_\Sigma) = \size \Sigma(n) ,
\]
and when every maximal cone has dimension $n$,
\[
H^2(X_\Sigma; \ZZ) \cong \Pic(X_\Sigma), \qquad \beta_2 = \size \Sigma(1) - n .
\]
:::

::: {.remark title="Where the formula comes from"}
Cohomology of an affine piece is exterior algebra on the lattice orthogonal to the cone,
\[
H^i(U_\sigma; \ZZ) \cong \Extpower^i M(\sigma), \qquad M(\sigma) \da \sigma^\perp \intersect M ,
\]
so the Mayer--Vietoris spectral sequence for the cover by the $U_\sigma$ over maximal cones has
\[
E_1^{p,q} = \bigoplus_{i_0 < \cdots < i_p} \Extpower^q M(\sigma_{i_0} \intersect \cdots \intersect \sigma_{i_p}) \abuts H^{p+q}(X_\Sigma; \ZZ) .
\]
The alternating sum over $q$ of $\rank \Extpower^q M(\tau)$ is $0$ unless $\dim \tau = n$, where it is $1$, and only the maximal cones survive.
That is the Euler characteristic statement, and tracking the individual ranks gives the binomial formula.
:::

::: {.remark title="Check it on the two standard surfaces"}
For $\PP^2$: $\size \Sigma(2) = 3$, $\size \Sigma(1) = 3$, $\size \Sigma(0) = 1$, giving $\beta_0 = 1$, $\beta_2 = 1$, $\beta_4 = 1$ and $\chi = 3$.
For $\FF_a$: $\size \Sigma(2) = 4$, $\size \Sigma(1) = 4$, giving $\beta_2 = 2 = \rank \Pic(\FF_a)$ and $\chi = 4$.

The formula is worth carrying because it turns a cohomology question into counting cones, and it makes the vanishing of odd cohomology a structural fact rather than a computation: the torus orbits give a cell decomposition with only even-dimensional cells.
:::
