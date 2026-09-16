---
schema: qual/card@1
id: T-C5VEI
kind: theorem
title: Casorati--Weierstrass theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Essential Singularities
relations: []
review: draft
---

::: {.theorem ref="Casorati"}
Let $\Omega\subseteq\CC$ be open, $z_0\in\Omega$, and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega\sm\ts{z_0}$ with an [[D-VKP6N|essential singularity]] at $z_0$.
Then for every punctured neighborhood $V=D_\varepsilon(z_0)\sm\ts{z_0}\subseteq\Omega$ of $z_0$, the image $f(V)$ is dense in $\CC$.

Equivalently, for every $w_0\in\CC$ there is a sequence $z_n\to z_0$, $z_n\neq z_0$, with $f(z_n)\to w_0$.
:::

::: {.proof}
Suppose instead that for some $\varepsilon>0$ and some $w\in\CC$ and $R>0$, the disc $D_R(w)$ does not meet $f(V)$, where $V=D_\varepsilon(z_0)\sm\ts{z_0}$.
Then $g(z)\coloneqq\frac{1}{f(z)-w}$ is holomorphic on $V$ and $\abs{g}\le1/R$, so by Riemann's removable singularity theorem $g$ extends holomorphically to $D_\varepsilon(z_0)$.
If $g(z_0)\neq0$, then $f=w+1/g$ extends holomorphically over $z_0$; if $g(z_0)=0$, then since $g$ is not identically zero, $f=w+1/g$ has a pole at $z_0$.
Either case contradicts that $z_0$ is essential.

![](../../assets/Complex_Analysis/070_Omitted Values/figures/2022-01-05_05-28-04.png)
:::
