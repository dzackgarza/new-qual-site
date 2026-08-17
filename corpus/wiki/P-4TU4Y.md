---
schema: qual/card@1
id: P-4TU4Y
kind: problem
title: Entire functions with $|f(z)|\le|z|^{1/2}$ for $|z|>10$ are constant
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
Find all entire functions satisfying
\[
\abs{f(z)} \leq \abs{z}^{1\over 2} \quad\text{ for } \abs{z} > 10
.\]
:::

:::{.solution}
Since $f$ is entire, take a Laurent expansion at $z=0$, so $f(z) = \sum_{k\geq 0} c_k z^k$ where ${2\pi i\over k!} c_k = f^{(k)}(0)$ by Cauchy's integral formula.
Take a Cauchy estimate on a disc of radius $R>10$:
\[
\abs{c_k} 
&\leq {k!\over 2\pi}\int_{\abs{z} = R} \abs{f(\xi) \over (\xi - 0)^{k+1}}\dxi\\
&\leq {k! \over 2\pi}\int_{\abs z = R}{ \abs{\xi}^{1\over 2} \over \abs{\xi}^{k+1} }\dxi \\
&= {k! \over 2\pi} \cdot {1\over R^{k+{1\over 2}}}\cdot 2\pi R \\
&= \bigo(1/R^{k-{1\over 2}})
.\]
So in particular, if $k\geq 1$ then $k-{1\over 2}>0$ and $c_k = 0$.
This forces $f = c_0$ to be constant.

:::
