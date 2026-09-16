---
schema: qual/card@1
id: P-TOPF19G
kind: problem
title: "Two maps from T^3 to S^3 are homotopic iff they have the same degree"
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $f$ and $g$ be two continuous maps from the three-torus $T^3 = S^1 \times S^1 \times S^1$ to the three-sphere $S^3$.
Show that $f$ is homotopic to $g$ if and only if they have the same mapping degree.
:::

::: {.solution}
<1>1. Since $S^3$ is $2$-connected, obstruction theory gives a natural bijection
$$[T^3,S^3]\cong H^3(T^3;\mathbb Z).$$
::: {.proof}
For a CW complex of dimension at most $3$ and a $2$-connected target whose first nonzero homotopy group is $\pi_3(S^3)=\mathbb Z$, the primary obstruction/classification class in $H^3(-;\mathbb Z)$ completely classifies maps up to homotopy.
:::

<1>2. Under this bijection, a map $f:T^3\to S^3$ corresponds to $f^*u$, where $u$ is the fundamental cohomology generator of $S^3$.
::: {.proof}
The universal degree-$3$ class represents the first Postnikov stage of $S^3$ through dimension $3$.
:::

<1>3. Since $H^3(T^3;\mathbb Z)\cong\mathbb Z$, one has
$$f^*u=(\deg f)\,v,$$
where $v$ is the orientation generator of $T^3$.
::: {.proof}
This is the cohomological definition of mapping degree between closed oriented $3$-manifolds.
:::

<1>4. Consequently
$$\boxed{f\simeq g\iff\deg f=\deg g.}$$
::: {.proof}
By <1>1--<1>3, equality of homotopy classes is exactly equality of the corresponding integers.
:::
:::
