---
schema: qual/card@1
id: D-OAFF5
kind: definition
title: Wirtinger operators $\partial$ and $\bar\partial$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $U\subseteq\CC$ be open, identify $\CC$ with $\RR^2$ by $z=x+iy$, and let $F\colon U\to\CC$ be $C^1$ as a function of $(x,y)$.
The \dfn{Wirtinger derivatives} of $F$ are
$$
\frac{\partial F}{\partial z}\coloneqq\frac12\qty{\frac{\partial F}{\partial x}-i\frac{\partial F}{\partial y}},\qquad
\frac{\partial F}{\partial\bar z}\coloneqq\frac12\qty{\frac{\partial F}{\partial x}+i\frac{\partial F}{\partial y}},
$$
and the operators $\del\coloneqq\del_z\coloneqq\frac12(\del_x-i\del_y)$ and $\delbar\coloneqq\del_{\bar z}\coloneqq\frac12(\del_x+i\del_y)$ are the \dfn{del} and \dfn{del-bar} operators.
:::

::: {.remark}
Since $\frac1i=-i$, the same formulas read $\frac{\partial F}{\partial z}=\frac12\qty{\frac{\partial F}{\partial x}+\frac1i\frac{\partial F}{\partial y}}$ and $\frac{\partial F}{\partial\bar z}=\frac12\qty{\frac{\partial F}{\partial x}-\frac1i\frac{\partial F}{\partial y}}$.
:::

::: {.proposition}
With $F$ as in the definition, $dz=dx+i\,dy$, and $d\bar z=dx-i\,dy$, the differential of $F$ is
$$
dF=\frac{\partial F}{\partial z}\dz+\frac{\partial F}{\partial\bar z}\dzbar.
$$
:::

::: {.proof}
Substituting $dz$ and $d\bar z$, the right side equals
$$
\frac12\qty{F_x-iF_y}(dx+i\,dy)+\frac12\qty{F_x+iF_y}(dx-i\,dy)=F_x\dx+F_y\dy=dF.
$$
:::
