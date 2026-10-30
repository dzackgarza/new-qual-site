---
schema: qual/card@1
id: P-TOPF02I
kind: problem
title: 'A compact manifold with vanishing cup products need not have the cohomology of $S^n$'
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Poincaré Duality
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M$ be an $n$-dimensional compact connected manifold.
Suppose all cup products vanish in $H^*(M;\ZZ)$.
Prove that $H^*(M;\ZZ)$ is isomorphic to $H^*(S^n;\ZZ)$.
:::

::: {.remark}
As stated the claim is false; the solution gives counterexamples and proves the correct statement for closed orientable $M$ with rational coefficients.
Here "all cup products vanish" means $\alpha\smile\beta=0$ whenever $\deg\alpha,\deg\beta>0$.
:::

::: {.solution}

::: pf

::: {.pf-step #counterexamples}

The claim fails without further hypotheses.

::: pf-proof

The closed disk $D^n$ is compact and connected with $H^*(D^n;\ZZ)\cong H^*(\text{pt};\ZZ)$, so all cup products vanish, but $H^n(D^n;\ZZ)=0\ne\ZZ$.

The closed nonorientable surface $\RP^2$ has $H^0=\ZZ$, $H^1=0$, $H^2=\ZZ_2$; all products of positive-degree classes land in degree at least $4$ or involve $H^1=0$, so they vanish, but $H^2(\RP^2;\ZZ)\ne\ZZ$.

The lens space $L(p,1)$, $p\ge2$, is closed and orientable with $H^0=\ZZ$, $H^1=0$, $H^2=\ZZ_p$, $H^3=\ZZ$. A product of two positive-degree classes has degree at least $4>3$ unless one factor lies in $H^1=0$, so all cup products vanish, but $H^2(L(p,1);\ZZ)\ne0$.

:::

:::

::: {.pf-step #rational}

If $M$ is closed and orientable and all cup products of positive-degree classes vanish in $H^*(M;\QQ)$, then $H^*(M;\QQ)\cong H^*(S^n;\QQ)$.

::: pf-proof

Since $M$ is closed, connected and orientable, $H^0(M;\QQ)\cong H^n(M;\QQ)\cong\QQ$.
For $0<k<n$, Poincaré duality over the field $\QQ$ makes the cup-product pairing
$$
H^k(M;\QQ)\times H^{n-k}(M;\QQ)\to H^n(M;\QQ)\cong\QQ
$$
nondegenerate. Both degrees are positive, so the pairing is zero by hypothesis; nondegeneracy then forces $H^k(M;\QQ)=0$.

:::

:::

::: pf-qed

Step [](#counterexamples){.pf-ref} shows the integral statement is false for manifolds with boundary, for nonorientable closed manifolds, and for closed orientable manifolds with torsion. Step [](#rational){.pf-ref} gives the true statement: for closed orientable $M$ the free part of $H^*(M;\ZZ)$ is that of $S^n$, since vanishing integral products imply vanishing rational products by $H^*(M;\QQ)\cong H^*(M;\ZZ)\otimes\QQ$.

:::

:::

:::
