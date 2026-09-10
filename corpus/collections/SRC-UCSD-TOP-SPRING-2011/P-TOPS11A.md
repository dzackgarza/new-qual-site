---
schema: qual/card@1
id: P-TOPS11A
kind: problem
title: "Maps to S^2 with no antipodal values are homotopic"
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Spheres
relations: []
review: draft
---

::: problem
Let $f, g : X \to S^2$ be continuous maps such that for all $x$ in $X$, $f(x)$ is not antipodal to $g(x)$.
Show that $f$ is homotopic to $g$.
:::

::: {.solution}
<1>1. For $x\in X$ and $t\in I$, define
$$
H(x,t)=\frac{(1-t)f(x)+t g(x)}{\|(1-t)f(x)+t g(x)\|}.
$$
::: {.proof}
We regard $S^2$ as the unit sphere in $\mathbb R^3$.
:::

<1>2. The denominator never vanishes.
::: {.proof}
If $(1-t)f(x)+t g(x)=0$, then the two unit vectors $f(x)$ and $g(x)$ are collinear with opposite directions. Since their norms are equal, this forces $t=1/2$ and $g(x)=-f(x)$, contrary to the hypothesis.
:::

<1>3. Hence $H$ is a continuous map $X\times I\to S^2$ with
$$
H(x,0)=f(x),\qquad H(x,1)=g(x).
$$
::: {.proof}
Continuity follows from <1>2, and the endpoint formulas are immediate.
:::

<1>4. Therefore
$$
\boxed{f\simeq g.}
$$
::: {.proof}
The map $H$ is the required homotopy.
:::
:::
