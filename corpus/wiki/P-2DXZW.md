---
schema: qual/card@1
id: P-2DXZW
kind: problem
title: "Suppose $f: \\CC\\to \\CC$ is entire and $\\abs{f(z)} \\leq \\abs{z}^{1\\over 2} \\quad\\text{ when } \\abs{z} > 10$ Prove that $f$ is constant. Let $R> 10$, then\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - liouville-s-theorem
  - cauchy-estimates
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Suppose $f: \CC\to \CC$ is entire and
\[
\abs{f(z)} \leq \abs{z}^{1\over 2} \quad\text{ when } \abs{z} > 10
.\]

Prove that $f$ is constant.
:::

:::{.solution}
Let $R> 10$, then by Cauchy:
\[
2\pi \abs{f'(z)} 
&\leq \oint_{\abs{\xi} = R} { \abs{ f(\xi)} \over \abs{\xi}^2 } \dxi \\
&\leq \oint_{\abs{\xi} = R} R^{-2} \abs{\xi}^{1\over 2} \dxi \\
&= R^{-{3\over 2}} \cdot 2\pi R \\
&\sim R^{-{1\over 2}} \\
&\convergesto{R\to\infty} 0
.\]
:::
