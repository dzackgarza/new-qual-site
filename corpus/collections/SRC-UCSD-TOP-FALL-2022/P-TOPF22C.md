---
schema: qual/card@1
id: P-TOPF22C
kind: problem
title: "Mod 2 cohomology ring of the Klein bottle times S^1"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Surfaces
relations: []
review: draft
---

::: problem
Let $K$ be the Klein bottle.
Compute the cohomology ring $H^*(K \times S^1; \mathbb{Z}_2)$.
:::

::: {.solution}
<1>1. Regard the Klein bottle as the closed nonorientable surface $N_2=\mathbb{RP}^2\#\mathbb{RP}^2$. Then
$$H^0(K;\mathbb F_2)\cong H^2(K;\mathbb F_2)\cong\mathbb F_2,\qquad H^1(K;\mathbb F_2)\cong\mathbb F_2^2.$$
::: {.proof}
This is the mod-$2$ cohomology of a closed connected surface of nonorientable genus $2$.
:::

<1>2. Choose degree-$1$ classes $x,y\in H^1(K;\mathbb F_2)$ dual to the two standard one-sided curves, and let $u\in H^2(K;\mathbb F_2)$ be the fundamental class. Then
$$x^2=u,\qquad y^2=u,\qquad xy=0.$$
::: {.proof}
For $N_2$, the mod-$2$ intersection form in the basis of the two crosscap curves is the diagonal matrix $\operatorname{diag}(1,1)$. Via Poincaré duality, cup product is the intersection pairing, giving the displayed products.
:::

<1>3. Thus
$$H^*(K;\mathbb F_2)\cong \mathbb F_2[x,y]/(xy,\ x^2+y^2,\ x^3,\ y^3),\qquad |x|=|y|=1.$$
::: {.proof}
The relations in <1>2 determine all products in degrees at most $2$, and every product of total degree greater than $2$ vanishes for dimensional reasons. Over $\mathbb F_2$, $x^2+y^2=0$ expresses equality of the two top classes.
:::

<1>4. Let $t\in H^1(S^1;\mathbb F_2)$ be the generator, so $t^2=0$. The field-coefficient Künneth theorem is multiplicative and gives
$$\boxed{H^*(K\times S^1;\mathbb F_2)\cong H^*(K;\mathbb F_2)\otimes_{\mathbb F_2}\mathbb F_2[t]/(t^2).}$$
::: {.proof}
Over a field there are no Tor terms, and the cross product identifies the cohomology ring of the product with the graded tensor product. Since the characteristic is $2$, there are no sign distinctions in commuting degree-$1$ generators.
:::

<1>5. Equivalently,
$$\boxed{H^*(K\times S^1;\mathbb F_2)\cong
\mathbb F_2[x,y,t]/(xy,\ x^2+y^2,\ x^3,\ y^3,\ t^2),}$$
with all three generators in degree $1$.
::: {.proof}
This is the tensor-product presentation from <1>3--<1>4. In particular $x^2t=y^2t\ne0$ generates $H^3$, while $xt$ and $yt$ are the two additional degree-$2$ classes besides $x^2=y^2$.
:::
:::
