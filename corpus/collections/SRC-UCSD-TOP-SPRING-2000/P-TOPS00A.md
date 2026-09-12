---
schema: qual/card@1
id: P-TOPS00A
kind: problem
title: "Compactly supported cohomology of a non-compact path-connected space vanishes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Compact Support
relations: []
review: draft
---

::: problem
Let $X$ be a path connected topological space which is not compact.
Show that $\bar{H}^0_{\mathrm{comp}}(X) = 0$.
:::

::: {.solution}
<1>1. A compactly supported degree-zero cocycle on a path-connected space is locally constant, hence constant.
::: {.proof}
For singular cohomology, a degree-zero cocycle assigns a coefficient to each point, and the cocycle condition on every singular $1$-simplex says the values at its two endpoints agree. Since any two points in a path-connected space are joined by a path, all values are equal.
:::

<1>2. A nonzero constant degree-zero cocycle has support all of $X$.
::: {.proof}
If the constant value is nonzero, it is nonzero at every point, so its support is $X$ itself.
:::

<1>3. Since $X$ is noncompact, no nonzero constant cocycle has compact support. Therefore
$$
\boxed{\bar H^0_{\mathrm{comp}}(X)=0}.
$$
::: {.proof}
By <1>1 every compactly supported cocycle is constant, and by <1>2 a nonzero one would have noncompact support. Thus the only compactly supported degree-zero cocycle is zero.
:::
:::
