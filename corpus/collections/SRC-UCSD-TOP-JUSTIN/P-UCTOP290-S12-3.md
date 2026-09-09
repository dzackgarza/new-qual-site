---
schema: qual/card@1
id: P-UCTOP290-S12-3
kind: problem
title: "Cohomology rings of a disjoint union and a wedge in terms of the summands"
classification:
  areas:
  - topology
  topics:
  - Cohomology Ring
relations: []
review: draft
---

::: problem
Describe the cohomology rings $H^*(X \sqcup Y)$ and $H^*(X \vee Y)$ in terms of $H^*(X)$ and $H^*(Y)$.
:::

::: {.solution}
<1>1. For a disjoint union,
$$
\boxed{H^*(X\sqcup Y;R)\cong H^*(X;R)\times H^*(Y;R)}
$$
as graded rings.
::: {.proof}
A singular simplex in $X\sqcup Y$ lies entirely in exactly one component, so the cochain complex splits as the product of the cochain complexes of $X$ and $Y$. Cup products are computed componentwise, giving the product-ring structure.
:::

<1>2. For a wedge of based path-connected spaces,
$$
\widetilde H^*(X\vee Y;R)
\cong \widetilde H^*(X;R)\oplus\widetilde H^*(Y;R)
$$
as graded groups.
::: {.proof}
The wedge is the union of $X$ and $Y$ with contractible intersection consisting of the basepoint. The reduced Mayer--Vietoris sequence gives the direct-sum decomposition.
:::

<1>3. Under the decomposition in <1>2, products between positive-degree classes from different summands vanish, while products within a summand are its original cup products.
::: {.proof}
Let $i_X:X\hookrightarrow X\vee Y$ and $i_Y:Y\hookrightarrow X\vee Y$. A class coming from $X$ restricts trivially to $Y$ in positive degree, and vice versa. Hence the product of one class from each summand restricts to zero on both $X$ and $Y$, and therefore is zero under the Mayer--Vietoris identification. Naturality of cup product shows that products of two $X$-classes, or two $Y$-classes, agree with the original ring structures.
:::

<1>4. Equivalently, for path-connected $X,Y$,
$$
\boxed{H^*(X\vee Y;R)\cong H^*(X;R)\times_R H^*(Y;R),}
$$
where the fiber product identifies the two degree-zero copies of $R$.
::: {.proof}
This is exactly the combination of the common unit in degree zero with the positive-degree direct sum and zero cross-products described in <1>2--<1>3.
:::
:::
