---
schema: qual/card@1
id: P-SMJE7
kind: problem
title: The limit $\lim_{n\to\infty}\int_1^n \frac{n e^{-x}}{1+nx^2}\sin(x/n)\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

:::{.problem}
Compute the following limit:
\[
\lim _{n \rightarrow \infty} \int_{1}^{n} \frac{n e^{-x}}{1+n x^{2}} \, \sin \left(\frac x n\right) \, dx
\]

:::

:::{.solution}
\[
I = \lim_{n\to\infty} \int_1^\infty {e^{-x} \over {1\over n} + x^2 }\sin\qty{x\over n}\chi_{[1, n]}  \dx
= \int_1^\infty{e^{-x}\over x^2}\lim_{n\to\infty }\sin\qty{x\over n } \chi_{[1, n]} \dx
= 0
,\]
since $\sin(x/n) \to 0$.
Passing the limit through the integral is justified by the DCT: write
\[
f_n(x) \da {ne^{-x} \over 1 + nx^2}\sin\qty{x\over n}\chi_{[1, n]}
.\]
Then
\[
\abs{f_n(x)} \leq g(x) \da {e^{-x}\over x^2}\in L^1(1, \infty)
,\]

since
\[
\norm{f}_{L^1(1, \infty)}
=
\int_1^\infty \abs{1\over x^2e^x}\dx \leq \int_1^\infty \abs{1\over x^2}\dx = 1 < \infty
.\]





:::

