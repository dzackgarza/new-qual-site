---
schema: qual/card@1
id: P-NY56Z
kind: problem
title: $\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx$ for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: {.problem}
Let $a>0$ and calculate
\[
\int_0^\infty {\cos(x) \over (x^2 + a^2)^2}\, dx
.\]
:::

::: {.solution}
Start from the standard residue evaluation
\[
I(a):=\int_0^\infty\frac{\cos x}{x^2+a^2}\,dx
=\frac{\pi}{2a}e^{-a},
\qquad a>0.
\]
Differentiation under the integral sign is justified locally in $a>0$ by an
integrable majorant, and gives
\[
I'(a)
=-2a\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx.
\]
On the other hand,
\[
I'(a)
=-\frac{\pi e^{-a}}{2a}
-\frac{\pi e^{-a}}{2a^2}
=-\frac{\pi e^{-a}(a+1)}{2a^2}.
\]
Hence
\[
\boxed{
\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx
=\frac{\pi e^{-a}(a+1)}{4a^3}.}
\]
:::
