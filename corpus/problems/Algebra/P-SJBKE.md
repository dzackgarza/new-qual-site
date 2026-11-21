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
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. The statement step was the single step
    without a justification, and it now says where the bijection comes from: the tensor--hom adjunction
    for $R[G]\otimes_{R[H]}V$ together with the observation that $G$-linearity of the left-hand map is
    exactly $H$-linearity of its restriction to the generators $1\otimes v$. The two constructions and
    the closing inverse-and-naturality argument were already justified and are unchanged. The card stands
    alone, with no collection provenance and no retained published solution, so the argument is the
    card's own. The statement is unchanged.
---

::: {.problem}
State and prove Frobenius reciprocity for group representations.
:::

::: {.solution}

Let $H\le G$, let $R$ be a commutative ring, let $V$ be an $R[H]$-module, and let $W$ be an $R[G]$-module. Write $\operatorname{Ind}_H^GV=R[G]\otimes_{R[H]}V$, and let $\Res_H^GW$ be $W$ viewed as an $R[H]$-module.

::: pf

::: pf-step

Statement: there is an isomorphism, natural in $V$ and $W$,
$$
\Hom_{R[G]}\bigl(\operatorname{Ind}_H^GV,W\bigr)\cong\Hom_{R[H]}\bigl(V,\Res_H^GW\bigr).
$$


::: pf-proof
Unwinding the two sides: a $G$-linear map out of $R[G]\otimes_{R[H]}V$ is determined by its values on the generators $1\otimes v$, because those generate the module over $R[G]$, and the adjunction $\Hom_R(R[G]\otimes_{R[H]}V, W)\cong\Hom_{R[H]}(V,W)$ identifies the $R$-linear maps on the left with the $H$-linear maps $V\to W$; the requirement that the map be $G$-linear is exactly that the corresponding $H$-map be $H$-linear. So the stated bijection is the tensor--hom adjunction restricted to the trivial action on $W$, and the two steps below construct both directions on elements, the closing step proving them inverse and natural.
:::

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
