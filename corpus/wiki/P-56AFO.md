---
schema: qual/card@1
id: P-56AFO
kind: problem
title: Integrability of a radial power
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Euclidean Spaces
relations: []
review: draft
---

:::{.problem}
Let $n\geq 1$ and $p\in\RR$. Show that
\[
\int_{\BB^n} {1 \over \abs{x}^p } \dx &< \infty \iff p < n \\ \\ \\ 
\int_{\RR^n\sm \BB^n} {1 \over \abs{x}^p } \dx &< \infty \iff p > n 
.\]
:::

:::{.solution}
Use polar coordinates. Writing $\omega_{n-1}$ for the surface measure of the unit sphere,
the integral over a radial region becomes
\[
\int_{\abs{x}<R}\abs{x}^{-p}\,\dx
 = \omega_{n-1}\int_0^R r^{n-1-p}\,\dr,
\qquad
\int_{\abs{x}>R}\abs{x}^{-p}\,\dx
 = \omega_{n-1}\int_R^\infty r^{n-1-p}\,\dr.
\]
The first one is finite exactly when $n-1-p>-1$, that is, $p<n$. The second is finite
exactly when $n-1-p<-1$, that is, $p>n$. At $p=n$, both integrals contain $\int r^{-1}\,\dr$
and diverge.
:::
