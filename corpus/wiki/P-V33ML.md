---
schema: qual/card@1
id: P-V33ML
kind: problem
title: Layer-cake formula for a measurable function
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
relations: []
review: draft
solved: true
---

Let $f:\\RR^n\\to\\RR$ be measurable. Show that
\[
\int_{\RR^n} \abs{ f} = \int_0^{\infty } m(A_t)\dt && A_t \da \ts{x\in \RR^n \st \abs{f(x)} > t}
.\]

:::{.solution}
For every $x$, the nonnegative function $t\mapsto \mathbf{1}_{A_t}(x)$ is the indicator of
$0\leq t<\abs{f(x)}$. Therefore
\[
\abs{f(x)} = \int_0^\infty \mathbf{1}_{A_t}(x)\,\dt.
\]
The integrand is measurable and nonnegative on $\RR^n\times[0,\infty)$. Tonelli's theorem
then permits the order of integration to be exchanged:
\[
\int_{\RR^n}\abs{f(x)}\,\dx
 = \int_{\RR^n}\int_0^\infty \mathbf{1}_{A_t}(x)\,\dt\,\dx
 = \int_0^\infty \int_{\RR^n}\mathbf{1}_{A_t}(x)\,\dx\,\dt
 = \int_0^\infty m(A_t)\,\dt.
\]
Both sides may be $+\infty$; no integrability assumption is needed.
:::
