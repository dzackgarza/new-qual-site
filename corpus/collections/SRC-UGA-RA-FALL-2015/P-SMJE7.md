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
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the UGA Fall 2015 real-analysis qualifying exam recorded by SRC-UGA-RA-FALL-2015.
- event: solution-written
  by: prior-author
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Compute the following limit:
\[
\lim _{n \rightarrow \infty} \int_{1}^{n} \frac{n e^{-x}}{1+n x^{2}} \, \sin \left(\frac x n\right) \, dx
\]

:::

::: solution
\[
I = \lim_{n\to\infty} \int_1^\infty {e^{-x} \over {1\over n} + x^2 }\sin(x/n)\chi_{[1, n]} \,dx
= \int_1^\infty{e^{-x}\over x^2}\lim_{n\to\infty }\sin\qty{x\over n } \chi_{[1, n]}\,dx
= 0
,\]
since $\sin(x/n) \to 0$.
Passing the limit through the integral is justified by the DCT: write
\[
f_n(x) := {ne^{-x} \over 1 + nx^2}\sin(x/n)\chi_{[1, n]}
.\]
Then
\[
|f_n(x)| \leq g(x) := {e^{-x}\over x^2}\in L^1(1, \infty)
,\]

since
\[
\|g\|_{L^1(1,\infty)}
=
\int_1^\infty \left|1/(x^2e^x)\right|\dx \leq \int_1^\infty 1/x^2\dx = 1 < \infty
.\]





:::

