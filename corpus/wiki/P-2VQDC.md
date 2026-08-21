---
schema: qual/card@1
id: P-2VQDC
kind: problem
title: Liouville's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Cauchy Estimates
  - Entire Functions
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Prove Liouville's theorem: suppose $f:\CC\to\CC$ is entire and bounded. 
Use Cauchy's formula to prove that $f'\equiv 0$ and hence $f$ is constant.
:::

:::{.solution}
The main idea:
\[
\abs{f'(z)} 
&\leq {1\over 2\pi }\oint_R {\abs{f(\xi)} \over \abs{\xi}^2 } \dxi\\
&= {1\over 2\pi }\oint_R {\abs{f(\xi)}  } R^{-2} \dxi\\
&\leq {1\over 2\pi }\oint_R M R^{-2} \dxi\\
&= {1\over 2\pi} MR^{-2}\cdot 2\pi R \\
&= MR^{-1} \\
&\convergesto{R\to\infty}0
.\]
So $f'\equiv 0$.
Since $\CC$ is connected, $f'\equiv 0$ implies $f$ is constant.
:::
