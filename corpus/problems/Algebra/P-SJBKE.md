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
Let $H\le G$, let $R$ be a commutative coefficient ring, let $V$ be an $R[H]$-module, and let $W$ be an $R[G]$-module. Frobenius reciprocity is the natural isomorphism
\[
\operatorname{Hom}_{R[G]}\!\left(R[G]\otimes_{R[H]}V,W\right)
\cong
\operatorname{Hom}_{R[H]}\!\left(V,\operatorname{Res}_H^G W\right).
\]
Equivalently,
\[
\operatorname{Hom}_G(\operatorname{Ind}_H^G V,W)
\cong
\operatorname{Hom}_H(V,\operatorname{Res}_H^G W).
\]

Given a $G$-map
\[
F:R[G]\otimes_{R[H]}V\to W,
\]
define
\[
\Phi(F)(v)=F(1\otimes v).
\]
For $h\in H$,
\[
\Phi(F)(hv)=F(1\otimes hv)=F(h\otimes v)=hF(1\otimes v),
\]
so $\Phi(F)$ is $H$-linear.

Conversely, given an $H$-map $f:V\to W$, define
\[
\Psi(f)(g\otimes v)=g f(v).
\]
This is well defined because
\[
\Psi(f)(gh\otimes v)=ghf(v)=g f(hv)=\Psi(f)(g\otimes hv),
\]
and it is visibly $G$-linear.

Finally,
\[
\Phi(\Psi(f))(v)=f(v)
\]
and
\[
\Psi(\Phi(F))(g\otimes v)=gF(1\otimes v)=F(g\otimes v).
\]
Thus $\Phi$ and $\Psi$ are inverse natural isomorphisms.
:::
