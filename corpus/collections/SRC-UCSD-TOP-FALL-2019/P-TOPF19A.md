---
schema: qual/card@1
id: P-TOPF19A
kind: problem
title: "A map from R^n to R^n bounded distance from the identity is surjective"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theory
relations: []
review: draft
---

::: {.problem}
Let $f : \mathbb{R}^n \to \mathbb{R}^n$ be a continuous map.
Suppose that there exists a uniform constant $C$ such that $\|f(\vec{x}) - \vec{x}\| \leq C$ for any $\vec{x} \in \mathbb{R}^n$.
Prove that $f$ is surjective.
:::

::: {.solution}
<1>1. Fix $y\in\mathbb R^n$ and choose $R>C+\|y\|$.
::: {.proof}
We will prove that $y$ lies in the image of the restriction of $f$ to the ball $B_R$.
:::

<1>2. On the sphere $S_R^{n-1}$, the maps $x\mapsto f(x)-y$ and $x\mapsto x-y$ are homotopic through maps avoiding $0$.
::: {.proof}
Use the straight-line homotopy
$$H_t(x)=(1-t)(x-y)+t(f(x)-y).$$
For $\|x\|=R$,
$$\|H_t(x)-x\|\le \|y\|+t\|f(x)-x\|<R,$$
so $H_t(x)\ne0$.
:::

<1>3. The normalized boundary map
$$x\longmapsto \frac{f(x)-y}{\|f(x)-y\|}$$
has degree $1$.
::: {.proof}
By <1>2 it is homotopic to the normalized map $x\mapsto(x-y)/\|x-y\|$. Since $y\in B_R$, the latter has degree $1$.
:::

<1>4. Therefore $f(x)=y$ for some $x\in B_R$.
::: {.proof}
If $f(x)\ne y$ on all of $B_R$, then the normalized map $(f-y)/\|f-y\|$ would extend from $S_R^{n-1}$ to $B_R$, forcing its boundary degree to be $0$, contradicting <1>3.
:::

<1>5. Since $y$ was arbitrary, $f$ is surjective.
::: {.proof}
Apply <1>4 to every $y\in\mathbb R^n$.
:::
:::
