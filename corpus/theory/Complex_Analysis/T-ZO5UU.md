---
schema: qual/card@1
id: T-ZO5UU
kind: theorem
title: Jordan's lemma
slogan: 'Choose the semicircle where $e^{i\alpha z}$ decays; the arc integral is bounded by $\pi M_R/\abs{\alpha}$.'
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

![The upper semicircle of radius R, traversed counterclockwise from R to -R.](../../assets/Complex_Analysis/040_Residues/figures/2021-12-20_20-35-11.png)

Let $\alpha>0$, let $g$ be continuous on $C_R$, and let $M_R\coloneqq\sup_{z\in C_R}\abs{g(z)}$.
Then
$$
\abs{\int_{C_R}e^{i\alpha z}g(z)\dz}\leq\frac{\pi}{\alpha}M_R.
$$
In particular, if $g$ is continuous on $\{z : \operatorname{Im}z\geq0,\ \abs{z}\geq R_0\}$ for some $R_0$ and $M_R\to0$ as $R\to\infty$, then $\int_{C_R}e^{i\alpha z}g(z)\dz\to0$.

For $\alpha<0$ the same statements hold with $C_R$ replaced by the lower semicircle $t\mapsto Re^{-it}$, $t\in[0,\pi]$, and $\pi/\alpha$ replaced by $\pi/\abs{\alpha}$.

Jordan's lemma is §6.222 of Whittaker and Watson, *A Course of Modern Analysis*, fourth edition, where it is stated for a function $Q$ analytic for $\abs z>c$ in $0\le\arg z\le\pi$ with $Q(z)\to0$ uniformly as $\abs z\to\infty$ there: the integral of $e^{miz}Q(z)$ over the semicircle of radius $\rho$ above the axis tends to $0$. The quantitative bound above is the estimate its proof carries out, and the estimate uses only the supremum of $\abs Q$ on the arc: choosing $\rho_0$ with $\abs{Q}<\varepsilon/\pi$ beyond it, the section bounds the integral by $\frac{2\varepsilon}{\pi}\int_0^{\pi/2}\rho e^{-m\rho\sin\theta}\dtheta$, uses $\sin\theta\ge2\theta/\pi$, and obtains $\frac{\varepsilon}{m}$, which for $m=\alpha$ and $\varepsilon=\pi M_R$ is $\frac{\pi}{\alpha}M_R$. The hypothesis above is weaker in asking only that $g$ be continuous on the arc, which is all that estimate consumes; the $\alpha<0$ clause is the same estimate on the reflected arc, and is not stated in that section.
:::
