---
schema: qual/card@1
id: E-GPCW2
kind: problem
title: $\int_{-1}^1 ((x-a)\sqrt{1-x^2})^{-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
For $a\in\RR$ with $|a|>1$, evaluate
\[
I(a)\da \int_{-1}^1 {dx\over (x-a)\sqrt{1-x^2}}.
\]
:::

::: {.solution}
Put $x=\cos\theta$.
Since $\sqrt{1-x^2}=\sin\theta$ for $0<\theta<\pi$,
\[
I(a)=\int_0^\pi {d\theta\over \cos\theta-a}.
\]
Now set $t=\tan(\theta/2)$, so
\[
\cos\theta={1-t^2\over1+t^2},
\qquad
d\theta={2\,dt\over1+t^2}.
\]
Therefore
\[
I(a)=2\int_0^\infty {dt\over (1-a)-(1+a)t^2}.
\]

If $a>1$, then
\[
I(a)=-2\int_0^\infty {dt\over (a-1)+(a+1)t^2}
=-{\pi\over\sqrt{a^2-1}}.
\]
If $a<-1$, both coefficients in the denominator are positive and the same calculation gives
\[
I(a)={\pi\over\sqrt{a^2-1}}.
\]
Thus
\[
I(a)=-\operatorname{sgn}(a){\pi\over\sqrt{a^2-1}},
\qquad |a|>1.
\]
:::
