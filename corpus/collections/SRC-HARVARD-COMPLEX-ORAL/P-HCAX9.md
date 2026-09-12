---
schema: qual/card@1
id: P-HCAX9
kind: problem
title: Derivatives under compact-uniform convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Convergence
relations: []
review: draft
---

::: problem
Let $f_n$ be holomorphic on a domain $\Omega$, and suppose $f_n\to F$ uniformly on compact subsets of $\Omega$.
What can be said about the derivatives $f_n'$?
:::

::: solution
The limit $F$ is holomorphic on $\Omega$, and
\[
f_n'\longrightarrow F'
\]
uniformly on compact subsets of $\Omega$. More generally, every fixed derivative converges locally uniformly:
\[
f_n^{(k)}\longrightarrow F^{(k)}.
\]

To prove this, fix a closed disk
\[
\overline{D(a,R)}\subset\Omega.
\]
For $|z-a|<R$, Cauchy's formula gives
\[
f_n(z)=\frac1{2\pi i}
\int_{|\zeta-a|=R}
\frac{f_n(\zeta)}{\zeta-z}\,d\zeta.
\]
The convergence $f_n\to F$ is uniform on the integration circle, so passing to the limit under the integral yields the same Cauchy formula for $F$. Hence $F$ is holomorphic.

Now fix $0<r<R$. For $|z-a|\le r$, Cauchy's differentiation formula gives
\[
f_n'(z)-F'(z)
=\frac1{2\pi i}
\int_{|\zeta-a|=R}
\frac{f_n(\zeta)-F(\zeta)}{(\zeta-z)^2}\,d\zeta.
\]
Since $|\zeta-z|\ge R-r$ on the contour,
\[
\sup_{|z-a|\le r}|f_n'(z)-F'(z)|
\le
\frac{R}{(R-r)^2}
\sup_{|\zeta-a|=R}|f_n(\zeta)-F(\zeta)|,
\]
and the right-hand side tends to $0$.

Every compact subset of $\Omega$ is covered by finitely many such smaller disks, so $f_n'\to F'$ uniformly on compact subsets. The same argument with Cauchy's formula for higher derivatives proves the final assertion.
:::
