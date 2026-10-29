---
schema: qual/card@1
id: P-SJBKE
kind: problem
title: Frobenius reciprocity
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
State and prove Frobenius reciprocity for group representations.
:::

::: {.solution}

Let $H\le G$, let $R$ be a commutative ring, let $V$ be an $R[H]$-module, and let $W$ be an $R[G]$-module. Write $\operatorname{Ind}_H^GV=R[G]\otimes_{R[H]}V$, and let $\operatorname{Res}_H^GW$ be $W$ viewed as an $R[H]$-module.

::: pf

::: pf-step

Statement: there is an isomorphism, natural in $V$ and $W$,
$$
\Hom_{R[G]}\bigl(\operatorname{Ind}_H^GV,W\bigr)\cong\Hom_{R[H]}\bigl(V,\operatorname{Res}_H^GW\bigr).
$$

:::

::: {.pf-step #phi}

For a $G$-map $F\colon\operatorname{Ind}_H^GV\to W$, the map $\Phi(F)\colon v\mapsto F(1\otimes v)$ is $H$-linear.

::: pf-proof

For $h\in H$, $\Phi(F)(hv)=F(1\otimes hv)=F(h\otimes v)=hF(1\otimes v)=h\,\Phi(F)(v)$.

:::

:::

::: {.pf-step #psi}

For an $H$-map $f\colon V\to W$, there is a $G$-map $\Psi(f)$ with $\Psi(f)(g\otimes v)=gf(v)$.

::: pf-proof

The map $R[G]\times V\to W$, $(x,v)\mapsto xf(v)$, is $R$-bilinear and $R[H]$-balanced: for $h\in H$, $(xh)f(v)=x\,f(hv)$ because $f$ is $H$-linear. By the universal property of $\otimes_{R[H]}$ it induces $\Psi(f)$, which is $G$-linear because $g'\bigl(gf(v)\bigr)=(g'g)f(v)$.

:::

:::

::: pf-qed

By steps [](#phi){.pf-ref} and [](#psi){.pf-ref}, $\Phi$ and $\Psi$ are defined, and
$$
\Phi(\Psi(f))(v)=f(v),\qquad \Psi(\Phi(F))(g\otimes v)=gF(1\otimes v)=F(g\otimes v).
$$
Since the elements $g\otimes v$ generate $\operatorname{Ind}_H^GV$, $\Phi$ and $\Psi$ are mutually inverse. Both are $R$-linear and commute with maps $V\to V'$ and $W\to W'$, so the isomorphism is natural.

:::

:::

:::
