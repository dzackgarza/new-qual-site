---
schema: qual/card@1
id: D-Q8XRV
kind: definition
title: Residue at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Singularities
relations: []
review: draft
---

::: {.definition}
Let $R>0$ and let $f$ be [[D-E7A5W|holomorphic]] on $\theset{z : \abs z>R}$.
The \dfn{residue of $f$ at $\infty$} is
$$
\Res_{z=\infty}f\coloneqq\Res_{z=0}g,\qquad
g(z)\coloneqq-\frac{1}{z^2}f\qty{\frac 1z},\quad 0<\abs z<\frac1R.
$$
:::

::: {.remark}
The substitution $w=1/z$ carries the form $f(z)\dz$ to $f(1/w)\,d(1/w)=-\frac{1}{w^2}f(1/w)\dw$, so the minus sign is the one $d(1/w)$ supplies; the circle $\abs z=\rho$ becomes $\abs w=1/\rho$ with the opposite orientation, which accounts for the same sign when the residue is written as an integral.
:::
