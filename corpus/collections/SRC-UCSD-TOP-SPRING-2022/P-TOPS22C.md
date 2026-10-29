---
schema: qual/card@1
id: P-TOPS22C
kind: problem
title: 'A simply connected closed $5$-manifold with $H_2=0$ is homotopy equivalent to $S^5$'
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

::: {.problem}
Let $X$ be a $5$-dimensional simply-connected closed manifold.
If $H_2(X) = 0$, show that $X$ is homotopy equivalent to $S^5$.
:::

::: {.solution}

::: pf

::: {.pf-step #simply-connected-h1-vanishes}
Since $X$ is simply connected, it is orientable and
$$H_1(X;\ZZ)=0.$$

::: pf-proof
Simple connectivity implies $H_1=0$ by Hurewicz/abelianization, and the orientation character factors through $\pi_1$, hence is trivial.
:::

:::

::: {.pf-step #h2-cohomology-vanishes}
By hypothesis $H_2(X;\ZZ)=0$, and therefore
$$H^2(X;\ZZ)=0.$$

::: pf-proof
The universal coefficient theorem gives
$$0\to\operatorname{Ext}(H_1(X),\ZZ)\to H^2(X;\ZZ)\to\operatorname{Hom}(H_2(X),\ZZ)\to0,$$
and both outer terms vanish.
:::

:::

::: {.pf-step #poincare-duality-h3-h4-vanish}
Poincaré duality in dimension $5$ gives
$$H_3(X;\ZZ)\cong H^2(X;\ZZ)=0,\qquad
H_4(X;\ZZ)\cong H^1(X;\ZZ)=0.$$

::: pf-proof
The manifold is closed, connected, and orientable by step [](#simply-connected-h1-vanishes){.pf-ref}, so integral Poincaré duality applies.
:::

:::

::: pf-step
Thus $X$ has the integral homology of $S^5$.

::: pf-proof
Connectedness gives $H_0=\ZZ$, orientability gives $H_5=\ZZ$, and steps [](#simply-connected-h1-vanishes){.pf-ref}, [](#h2-cohomology-vanishes){.pf-ref} and [](#poincare-duality-h3-h4-vanish){.pf-ref} kill all intermediate homology groups.
:::

:::

::: pf-step
Consequently
$$\boxed{X\simeq S^5.}$$

::: pf-proof
A simply connected integral homology sphere is a homotopy sphere: successive applications of Hurewicz show $X$ is $4$-connected and $\pi_5(X)\cong H_5(X)=\ZZ$. A generator gives a homology equivalence $S^5\to X$, which is a homotopy equivalence by the homological Whitehead theorem.
:::

:::

:::

:::
