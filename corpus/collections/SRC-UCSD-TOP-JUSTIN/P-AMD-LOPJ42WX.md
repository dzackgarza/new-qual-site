---
schema: qual/card@1
id: P-AMD-LOPJ42WX
kind: problem
title: Paths in a simply connected space are homotopic rel endpoints
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Show that $x,y\in X$ path & simply-connected $\implies$ all paths from $x$ to $y$ are homotopic rel $\{0, 1\}$.
:::

::: {.solution}
<1>1. Let $\alpha,\beta:I\to X$ be paths from $x$ to $y$. The concatenation
$$
\alpha*\overline\beta
$$
is a loop based at $x$.
::: {.proof}
Here $\overline\beta(t)=\beta(1-t)$ runs from $y$ back to $x$, so concatenation with $\alpha$ gives a loop at $x$.
:::

<1>2. Since $X$ is simply connected, $\alpha*\overline\beta$ is null-homotopic rel basepoint.
::: {.proof}
Simple connectivity means $\pi_1(X,x)=1$, so the based loop $\alpha*\overline\beta$ represents the identity element.
:::

<1>3. Therefore $\alpha$ and $\beta$ are homotopic relative to their endpoints.
::: {.proof}
The standard path-homotopy criterion says that two paths with the same endpoints are homotopic rel endpoints iff the loop obtained by following the first and then the reverse of the second is null-homotopic. Applying this criterion to <1>2 gives the conclusion.
:::
:::
