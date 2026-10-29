---
schema: qual/card@1
id: P-TOPS05E
kind: problem
title: "Closed non-orientable 3-manifold has nonzero H^1"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Orientation
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints "compact non-orientable 3-manifold", which is false with boundary allowed (RP^2 x I has H^1 = 0). The statement now asks for a closed connected non-orientable 3-manifold.
---

::: {.problem}
Let $X$ be a closed (compact, without boundary) connected non-orientable $3$-manifold.
Prove $H^1(X; \ZZ) \neq 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s2}

The first Betti number satisfies $b_1(X)\ge1$.

::: pf-proof

A closed odd-dimensional manifold has Euler characteristic $0$, whether orientable or not: pass to the orientation double cover and use multiplicativity of Euler characteristic together with Poincaré duality upstairs. Since $X$ is connected and nonorientable, $H_3(X;\QQ)=0$, while $H_0(X;\QQ)\cong\QQ$. Thus
$$0=\chi(X)=1-b_1(X)+b_2(X),$$
so $b_1(X)=1+b_2(X)\ge1$.

:::

:::

::: pf-step

$$H^1(X;\ZZ)\ne0.$$

::: pf-proof

The universal coefficient theorem gives
$$H^1(X;\ZZ)\cong\operatorname{Hom}(H_1(X;\ZZ),\ZZ).$$
Since $b_1(X)>0$ by step [](#s2){.pf-ref}, $H_1(X;\ZZ)$ has a nonzero free summand, so the Hom group is nonzero.

:::

:::

:::

:::
