---
schema: qual/card@1
id: T-ZO5UU
kind: theorem
title: Jordan's lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
---

::: {.theorem}
For $R>0$ let $C_R$ be the upper semicircle $t\mapsto Re^{it}$, $t\in[0,\pi]$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-20_20-35-11.png)

Let $\alpha>0$, let $g$ be continuous on $C_R$, and let $M_R\coloneqq\sup_{z\in C_R}\abs{g(z)}$.
Then
$$
\abs{\int_{C_R}e^{i\alpha z}g(z)\dz}\leq\frac{\pi}{\alpha}M_R.
$$
In particular, if $g$ is continuous on $\{z : \operatorname{Im}z\geq0,\ \abs{z}\geq R_0\}$ for some $R_0$ and $M_R\to0$ as $R\to\infty$, then $\int_{C_R}e^{i\alpha z}g(z)\dz\to0$.

For $\alpha<0$ the same statements hold with $C_R$ replaced by the lower semicircle $t\mapsto Re^{-it}$, $t\in[0,\pi]$, and $\pi/\alpha$ replaced by $\pi/\abs{\alpha}$.
:::

::: {.proof}
For $\alpha>0$ and $z=Re^{it}$, $\abs{e^{i\alpha z}}=e^{-\alpha R\sin t}$ and $\abs{\dz}=R\,dt$, so
$$
\abs{\int_{C_R}e^{i\alpha z}g(z)\dz}\leq M_R\int_0^\pi e^{-\alpha R\sin t}R\,dt=2M_R\int_0^{\pi/2}e^{-\alpha R\sin t}R\,dt.
$$
Since $\sin t\geq 2t/\pi$ for $t\in[0,\pi/2]$,
$$
\int_0^{\pi/2}e^{-\alpha R\sin t}R\,dt\leq\int_0^{\pi/2}e^{-2\alpha Rt/\pi}R\,dt\leq\frac{\pi}{2\alpha},
$$
which gives the bound.
For $\alpha<0$ and $z=Re^{-it}$ with $t\in[0,\pi]$, $\abs{e^{i\alpha z}}=e^{\alpha R\sin t}=e^{-\abs{\alpha}R\sin t}$, and the same estimate applies with $\abs{\alpha}$ in place of $\alpha$.
:::
