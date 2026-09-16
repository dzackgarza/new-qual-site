---
schema: qual/card@1
id: E-SS9.EX-6
kind: problem
title: "The differential equation for the Weierstrass p-function"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
6. Prove that $\wp ^ { \prime \prime }$ is a quadratic polynomial in $\wp$
:::

::: {.solution}
The Weierstrass function is elliptic, so \(\wp''\) and \(\wp^2\) are elliptic. Near a lattice point, by translation it suffices to work near \(0\). From the defining series,
\[
\wp(z)=\frac1{z^2}+c_2z^2+O(z^4)
\]
for some constant \(c_2\); there are no odd powers because \(\wp\) is even. Consequently
\[
\wp''(z)=\frac6{z^4}+2c_2+O(z^2),
\qquad
6\wp(z)^2=\frac6{z^4}+12c_2+O(z^2).
\]
Thus
\[
H(z):=\wp''(z)-6\wp(z)^2
\]
has a removable singularity at every lattice point. Hence \(H\) extends to an entire elliptic function. It is bounded on a fundamental parallelogram and therefore bounded on \(\mathbb C\); Liouville's theorem gives \(H\equiv C\) for some constant \(C\). Therefore
\[
\boxed{\wp''(z)=6\wp(z)^2+C},
\]
which is a quadratic polynomial in \(\wp\).

More explicitly, if
\[
g_2=60\sum_{\omega\in\Lambda\setminus\{0\}}\omega^{-4},
\]
then the Laurent expansion gives \(c_2=g_2/20\), hence \(C=-g_2/2\) and
\[
\wp''=6\wp^2-\frac{g_2}{2}.
\]
:::
