---
schema: qual/card@1
id: P-AMD-ZBOGZX5H
kind: problem
title: $H^1(X)$ is free abelian
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homological Algebra
relations: []
review: draft
---

::: {.problem}
For any space $X$, show that $H^1(X)$ is free abelian
:::

::: {.solution}
<1>1. As stated for an arbitrary space $X$, the claim is false.
::: {.proof}
By the universal coefficient theorem,
$$
H^1(X;\mathbb Z)\cong\operatorname{Hom}(H_1(X;\mathbb Z),\mathbb Z)
$$
when $H_0(X)$ is free (as it always is), but the dual of an arbitrary abelian group need not be a free abelian group. For example, there exist torsion-free abelian groups $A$ whose dual $\operatorname{Hom}(A,\mathbb Z)$ is not free; such groups can be realized as $H_1$ of connected CW complexes.
:::

<1>2. The standard valid version is: if $H_1(X;\mathbb Z)$ is finitely generated (for example, if $X$ is a finite CW complex), then $H^1(X;\mathbb Z)$ is free abelian.
::: {.proof}
Write the finitely generated abelian group as
$$
H_1(X;\mathbb Z)\cong\mathbb Z^r\oplus T
$$
with $T$ finite. Then
$$
H^1(X;\mathbb Z)\cong\operatorname{Hom}(H_1(X),\mathbb Z)
\cong\mathbb Z^r,
$$
since every homomorphism from the torsion group $T$ to the torsion-free group $\mathbb Z$ is zero.
:::
:::
