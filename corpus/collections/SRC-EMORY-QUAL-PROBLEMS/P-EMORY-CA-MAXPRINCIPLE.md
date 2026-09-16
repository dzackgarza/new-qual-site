---
schema: qual/card@1
id: P-EMORY-CA-MAXPRINCIPLE
kind: problem
title: The maximum modulus principle from the Cauchy integral formula
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (3) of Arango-Piñeros, Some quals problems; restored the source's phrase the Cauchy integral formula; merged the duplicate P-EMCA3, whose solution repeats this mean-value argument."
---

::: {.problem}
Use the Cauchy integral formula to prove the maximum principle for analytic functions.
:::

::: {.solution}
We prove the strong local form of the maximum modulus principle. Let $G$ be a
region, let $f\in H(G)$, and suppose that $|f|$ has a local maximum at
$z_0\in G$. We show that $f$ is constant.

Choose $r>0$ so small that $\overline{D(z_0,r)}\subset G$ and
\[
|f(z)|\le |f(z_0)|
\qquad (z\in \overline{D(z_0,r)}).
\]
If $f(z_0)=0$, then $f\equiv0$ on this disk and hence on $G$ by the identity
theorem. Thus assume $M:=|f(z_0)|>0$, and multiply $f$ by the unimodular
constant $\overline{f(z_0)}/M$. This does not change its modulus, so we may
assume $f(z_0)=M>0$.

For every $0<\rho<r$, Cauchy's integral formula gives the mean-value identity
\[
f(z_0)=\frac1{2\pi}\int_0^{2\pi}
f(z_0+\rho e^{it})\,dt.
\]
Taking real parts,
\[
M=\frac1{2\pi}\int_0^{2\pi}
\Re f(z_0+\rho e^{it})\,dt.
\]
But for every $t$,
\[
\Re f(z_0+\rho e^{it})
\le |f(z_0+\rho e^{it})|\le M.
\]
The integrand is continuous and bounded above by $M$, while its average is
exactly $M$; therefore it is identically $M$. Hence on the circle
$|z-z_0|=\rho$ we have both $\Re f(z)=M$ and $|f(z)|\le M$. This forces
$f(z)=M$ at every point of that circle.

Thus $f-M$ has infinitely many zeros with an accumulation point in $G$, so the
identity theorem gives $f\equiv M$ on $G$. Consequently a nonconstant analytic
function cannot attain a local maximum of its modulus at an interior point.
In particular, on any bounded domain where $f$ is continuous up to the
boundary, the maximum of $|f|$ is attained on the boundary.
:::
