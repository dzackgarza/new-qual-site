---
schema: qual/card@1
id: P-EMCA3
kind: problem
title: "Maximum principle via Cauchy integral formula"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Use the Cauchy integral formula to prove the maximum principle for analytic functions.
:::

::: solution
Let $f$ be holomorphic on a region $\Omega$. Suppose that $|f|$ has a local
maximum at $a\in\Omega$. Choose $r>0$ with
$\overline{B(a,r)}\subset\Omega$ and
\[
|f(z)|\le |f(a)|\qquad (|z-a|\le r).
\]
For every $0<\rho<r$, Cauchy's integral formula gives
\[
f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+\rho e^{it})\,dt.
\]
Hence
\[
|f(a)|
\le \frac1{2\pi}\int_0^{2\pi}|f(a+\rho e^{it})|\,dt
\le |f(a)|.
\]
Both inequalities are equalities. If $f(a)=0$, the local maximality already
implies $f=0$ on $B(a,r)$. Otherwise set
$u(t)=f(a+\rho e^{it})/f(a)$. Then $|u(t)|\le1$ and
\[
\frac1{2\pi}\int_0^{2\pi}u(t)\,dt=1.
\]
Taking real parts yields
\[
\frac1{2\pi}\int_0^{2\pi}\operatorname{Re}u(t)\,dt=1,
\qquad \operatorname{Re}u(t)\le1.
\]
Continuity forces $\operatorname{Re}u(t)=1$ for every $t$, and $|u(t)|\le1$
then forces $u(t)=1$. Thus $f$ is constant on every circle
$|z-a|=\rho$, hence on $B(a,r)$.

By the identity theorem, $f$ is constant on the connected region $\Omega$.
Therefore a nonconstant holomorphic function cannot attain a local maximum of
its modulus at an interior point. In particular, on a bounded domain where
$f$ is continuous up to the boundary, the maximum of $|f|$ is attained on the
boundary.
:::
