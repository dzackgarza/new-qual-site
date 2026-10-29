---
schema: qual/card@1
id: P-CAF13F
kind: problem
title: "A conformal map from the slit disk does not extend to a boundary homeomorphism"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $\varphi: \DD \setminus [0, 1) \to \DD$ be a conformal bijection.
Prove that $\varphi$ does not extend to a homeomorphism $\overline{\DD} \to \overline{\DD}$.
:::

::: {.solution}
Suppose, for contradiction, that there were a homeomorphism
\[
\Phi:\overline{\DD}\to\overline{\DD}
\]
whose restriction to $\DD\setminus[0,1)$ is $\varphi$.

A homeomorphism of the closed disk carries its boundary circle onto the boundary
circle, hence carries the interior disk onto the interior disk. Choose any
$x\in(0,1)$. Then $\Phi(x)\in\DD$. Since $\varphi$ is onto $\DD$,
there exists
\[
y\in\DD\setminus[0,1)
\]
such that
\[
\varphi(y)=\Phi(x).
\]
But $\Phi(y)=\varphi(y)$, so
\[
\Phi(y)=\Phi(x).
\]
This contradicts injectivity of the homeomorphism $\Phi$, because $y\ne x$.
Therefore no such boundary homeomorphism extension exists.
:::
