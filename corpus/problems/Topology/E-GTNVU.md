---
schema: qual/card@1
id: E-GTNVU
kind: problem
title: Homology of product of spheres
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
---

::: {.exercise}
Compute all of the possible cases for $H_*(S^a\cross S^b)$, where $a, b\geq 0$ are not necessarily distinct.
:::

::: {.solution}
<1>1. For $a,b>0$, Künneth gives
$$H_k(S^a\times S^b;\mathbb Z)\cong\bigoplus_{i+j=k}H_i(S^a)\otimes H_j(S^b),$$
with no Tor terms.
::: {.proof}
All homology groups of spheres are free abelian.
:::

<1>2. If $a,b>0$ and $a\ne b$, then
$$\boxed{H_k\cong\begin{cases}\mathbb Z,&k=0,a,b,a+b,\\0,&\text{otherwise.}\end{cases}}$$
::: {.proof}
The four tensor products from degrees $(0,0),(a,0),(0,b),(a,b)$ occur in distinct total degrees.
:::

<1>3. If $a=b>0$, then
$$\boxed{H_k\cong\begin{cases}\mathbb Z,&k=0,2a,\\\mathbb Z^2,&k=a,\\0,&\text{otherwise.}\end{cases}}$$
::: {.proof}
The two middle tensor products now occur in the same degree $a$.
:::

<1>4. Since $S^0$ is two points, if exactly one of $a,b$ is zero then $S^a\times S^b$ is a disjoint union of two copies of the positive-dimensional sphere; if $a=b=0$ it is four points.
::: {.proof}
Products with a finite discrete set are disjoint unions indexed by that set. Thus for, say, $a=0<b$, $H_0\cong H_b\cong\mathbb Z^2$ and all other groups vanish; for $a=b=0$, $H_0\cong\mathbb Z^4$.
:::
:::
