---
schema: qual/card@1
id: P-TOPS22C
kind: problem
title: "A simply-connected closed 5-manifold with H_2 = 0 is homotopy equivalent to S^5"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Homology
relations: []
review: draft
---

::: problem
Let $X$ be a $5$-dimensional simply-connected closed manifold.
If $H_2(X) = 0$, show that $X$ is homotopy equivalent to $S^5$.
:::

::: {.solution}
<1>1. Since $X$ is simply connected, it is orientable and
$$H_1(X;\mathbb Z)=0.$$
::: {.proof}
Simple connectivity implies $H_1=0$ by Hurewicz/abelianization, and the orientation character factors through $\pi_1$, hence is trivial.
:::

<1>2. By hypothesis $H_2(X;\mathbb Z)=0$, and therefore
$$H^2(X;\mathbb Z)=0.$$
::: {.proof}
The universal coefficient theorem gives
$$0\to\operatorname{Ext}(H_1(X),\mathbb Z)\to H^2(X;\mathbb Z)\to\operatorname{Hom}(H_2(X),\mathbb Z)\to0,$$
and both outer terms vanish.
:::

<1>3. Poincaré duality in dimension $5$ gives
$$H_3(X;\mathbb Z)\cong H^2(X;\mathbb Z)=0,\qquad
H_4(X;\mathbb Z)\cong H^1(X;\mathbb Z)=0.$$
::: {.proof}
The manifold is closed, connected, and orientable by <1>1, so integral Poincaré duality applies.
:::

<1>4. Thus $X$ has the integral homology of $S^5$.
::: {.proof}
Connectedness gives $H_0=\mathbb Z$, orientability gives $H_5=\mathbb Z$, and <1>1--<1>3 kill all intermediate homology groups.
:::

<1>5. Consequently
$$\boxed{X\simeq S^5.}$$
::: {.proof}
A simply connected integral homology sphere is a homotopy sphere: successive applications of Hurewicz show $X$ is $4$-connected and $\pi_5(X)\cong H_5(X)=\mathbb Z$. A generator gives a homology equivalence $S^5\to X$, which is a homotopy equivalence by the homological Whitehead theorem.
:::
:::
