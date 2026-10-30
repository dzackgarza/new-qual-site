---
schema: qual/card@1
id: P-4X7XU
kind: problem
title: A conformal map from $\{\Re z>0,\ \abs{z-1/2}>1/2\}$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from
$$
\theset{ z\st \abs{z -1 / 2} >1 / 2,\ \Re(z)>0 }
$$
to $\halfplane$.
:::

::: {.solution}
Let $R$ be the given region.

::: pf

::: {.pf-step #inv}
$z\mapsto1/z$ maps $R$ biholomorphically onto the strip $S=\{0<\Re w<1\}$.

::: pf-proof
For $z\neq0$, $\Re(1/z)=\Re z/\abs{z}^2$. So $\Re z>0$ iff $\Re(1/z)>0$, and $\abs{z-\frac12}>\frac12$ iff $\abs{z}^2>\Re z$ iff $\Re(1/z)<1$. Since $0\notin R$ and $0\notin S$, and $1/z$ is its own inverse, it is a bijection $R\to S$.
:::

:::

::: {.pf-step #exp}
$w\mapsto e^{\pi iw}$ maps $S$ biholomorphically onto $\halfplane$.

::: pf-proof
For $w=s+it\in S$, $e^{\pi iw}=e^{-\pi t}e^{i\pi s}$ has argument $\pi s\in(0,\pi)$, so it lies in $\halfplane$. Every $\zeta=\rho e^{i\theta}\in\halfplane$ with $0<\theta<\pi$ is the image of exactly one point of $S$, namely $w=\theta/\pi-(i/\pi)\log\rho$, because two preimages differ by an even integer and real parts in $(0,1)$ differ by less than $1$.
:::

:::

::: pf-qed
By steps [](#inv){.pf-ref} and [](#exp){.pf-ref}, $\boxed{z\mapsto e^{\pi i/z}}$ is a conformal map of $R$ onto $\halfplane$.
:::

:::

:::
