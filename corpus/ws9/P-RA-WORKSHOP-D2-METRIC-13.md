---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-13
kind: problem
title: 'Verify that an induced norm metric satisfies the metric axioms'
classification:
  areas:
  - real-analysis
  topics:
  - metric-spaces
  - norms
relations: []
review: draft
---

::: {.problem title="?"}
Verify the remark following the definition of normed space: Every normed space $(X,\lVert\cdot\rVert)$ is a metric space by taking $d(x,y)=\lVert x-y\rVert$, while the converse is not true in general—even if $X$ is a vector space.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Every normed space is a metric space via $d(x,y) = \lVert x-y\rVert$.
<2>1. Non-negativity and separation: $\lVert x-y\rVert \ge 0$ with equality iff $x = y$ (norm axioms), so $d(x,y) \ge 0$ and $d(x,y) = 0$ iff $x = y$.
<2>2. Symmetry: $d(x,y) = \lVert x-y\rVert = \lVert -(y-x)\rVert = \lVert y-x\rVert = d(y,x)$ (homogeneity with $\lambda = -1$).
<2>3. Triangle inequality: $d(x,z) = \lVert x-z\rVert = \lVert (x-y) + (y-z)\rVert \le \lVert x-y\rVert + \lVert y-z\rVert = d(x,y) + d(y,z)$.
<1>2. The converse fails in general, even for a vector space.
    Proof: take $X = \mathbb{R}$ with the discrete metric $d(x,y) = 1$ for $x \ne y$, $d(x,x) = 0$. This is a metric on the vector space $\mathbb{R}$. But no norm induces it: a norm-induced metric satisfies $d(nx, 0) = \lVert nx\rVert = n\lVert x\rVert$, which grows with $n$, whereas the discrete metric gives $d(nx,0) = 1$ for every $n \ge 1$ (with $x \ne 0$). Contradiction. (More conceptually, a norm-induced metric is translation-invariant and homogeneous; the discrete metric is neither.)
<1>3. Q.E.D.
:::
