---
schema: qual/card@1
id: P-AMD-ML25AJS7
kind: problem
title: Maps into $S^n$ that are nowhere antipodal are homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
---

::: {.problem}
Let $f,g \rightarrow S^n$ be such that $\forall x\in X, f(x) \neq -g(x)$.
Show that $f \simeq g$.
:::

::: {.solution}
<1>1. Define
$$
H:X\times I\longrightarrow S^n,
\qquad
H(x,t)=\frac{(1-t)f(x)+t g(x)}{\|(1-t)f(x)+t g(x)\|}.
$$
::: {.proof}
We regard $S^n$ as the unit sphere in $\mathbb R^{n+1}$. The only issue is whether the denominator can vanish.
:::

<1>2. The denominator in <1>1 is nonzero for every $(x,t)$.
::: {.proof}
If
$$
(1-t)f(x)+t g(x)=0,
$$
then, since both $f(x)$ and $g(x)$ have norm $1$, taking norms gives $1-t=t$, hence $t=1/2$, and then $g(x)=-f(x)$. This is excluded by hypothesis.
:::

<1>3. Thus $H$ is a continuous homotopy from $f$ to $g$.
::: {.proof}
By <1>2 the normalization map is defined continuously everywhere. At the endpoints,
$$
H(x,0)=f(x),\qquad H(x,1)=g(x).
$$
Therefore
$$
\boxed{f\simeq g}.
$$
:::
:::
