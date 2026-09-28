---
schema: qual/card@1
id: P-4Y4QT
kind: problem
title: $\int_0^\infty\frac{x^{\alpha-1}}{1+x^3}\,dx$ for $0<a<4$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.problem}
Let $0<a<4$ and evaluate
\[
\int_0^\infty \frac{x^{\alpha-1}}{1+x^3} ~dx
\]
:::

::: {.solution}
The statement is ambiguous as printed: it assumes $0<a<4$ but the integrand
contains the unrelated symbol $\alpha$.

If the intended correction is $\alpha=a$ while keeping the denominator
$1+x^3$, then the integral converges exactly for $0<a<3$ and
\[
\boxed{\int_0^\infty {x^{a-1}\over1+x^3}\,dx
={\pi\over3}\csc{\pi a\over3}}.
\]
Indeed, with $t=x^3$,
\[
\int_0^\infty {x^{a-1}\over1+x^3}\,dx
={1\over3}\int_0^\infty {t^{a/3-1}\over1+t}\,dt
={1\over3}B(a/3,1-a/3),
\]
and Euler's reflection formula gives the displayed value. For $3\le a<4$
the integral diverges at infinity.

On the other hand, the printed range $0<a<4$ is exactly the natural range for
the alternative integrand $x^{a-1}/(1+x^4)$, in which case the value would be
\[
{\pi\over4}\csc{\pi a\over4}.
\]
Thus the surviving source does not determine which of these two corrections
was intended, but both mathematically consistent readings are resolved above.
:::
