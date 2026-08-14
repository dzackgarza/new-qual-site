---
schema: qual/card@1
id: P-3AREP
kind: problem
title: "Compute the following limit and justify your calculations: $\\lim_{n \\rightarrow \\infty} \\int_{1}^{n} \\frac{d x}{\\left(1+\\frac{x}{n}\\right)^{n} \\sqrt[n]{x}}$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - integrals
relations: []
review: draft
---
Compute the following limit and justify your calculations:
\[
\lim_{n \rightarrow \infty} \int_{1}^{n} \frac{d x}{\left(1+\frac{x}{n}\right)^{n} \sqrt[n]{x}}
\]

:::{.solution}
:::{.concept}
- ?
:::

- Note that $x^{1\over n} \converges{n\to\infty}\to 1$ for any $0 < x < \infty$.
- Thus the integrand converges to ${1\over e^x}$, which is integrable on $(0, \infty)$ and integrates to 1.
- Break the integrand up:
\[
\int_0^\infty {1 \over  \qty{ 1 + {x\over n} }^n x^{1\over n}} \,dx
= \int_0^1 {1 \over  \qty{ 1 + {x\over n} }^n x^{1\over n}} \,dx
= \int_1^\infty {1 \over  \qty{ 1 + {x\over n} }^n x^{1\over n}} \,dx
.\]
:::

