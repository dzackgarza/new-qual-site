---
schema: qual/card@1
id: P-BKF09-7B
kind: problem
title: Evaluation of $\int_0^{2\pi} d\theta/(1-2\alpha\cos\theta+\alpha^2)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose $\alpha$ is a complex number, $\abs{\alpha}\neq1$.
Compute
$$
\int_0^{2\pi}\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}
$$
by integrating $(z-\alpha)^{-1}(z-\alpha^{-1})^{-1}$ over the unit circle.
:::

::: {.solution}
Parameterize the unit circle $C$ by $z(\theta)=e^{i\theta}$, $\theta\in[0,2\pi]$.
Then $z'(\theta)=ie^{i\theta}=iz(\theta)$, and we have $\cos\theta=\frac12(e^{i\theta}+e^{-i\theta})=\frac12(z+z^{-1})$.
We also have $d\theta=-i\,dz/z$, so we have
$$
\begin{aligned}
\int_0^{2\pi}\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}
&=\int_C\frac{-i\,dz/z}{1-\alpha(z+z^{-1})+\alpha^2}
=\int_C\frac{i\,dz\,\alpha^{-1}}{z^2-(\alpha+\alpha^{-1})z+1}\\
&=\frac{i}{\alpha}\int_C\frac{dz}{(z-\alpha)(z-\alpha^{-1})}.
\end{aligned}
$$
If $\alpha=0$, then
$$
\int_0^{2\pi}\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}=\int_0^{2\pi}d\theta=2\pi=\frac{2\pi}{1-\alpha^2}.
$$
If $0<\abs{\alpha}<1$, then $\frac{1}{z-\alpha^{-1}}$ is analytic inside $C$ since $\abs{\alpha^{-1}}>1$, so by Cauchy's integral formula, we have
$$
i\alpha^{-1}\int_C\frac{(z-\alpha^{-1})^{-1}\,dz}{z-\alpha}=i\alpha^{-1}\frac{2\pi i}{\alpha-\alpha^{-1}}=\frac{2\pi}{1-\alpha^2}.
$$
If $\abs{\alpha}>1$, then exchanging the roles of $\alpha$ and $\alpha^{-1}$, we have
$$
i\alpha^{-1}\int_C\frac{(z-\alpha)^{-1}\,dz}{z-\alpha^{-1}}=i\alpha^{-1}\frac{2\pi i}{\alpha^{-1}-\alpha}=\frac{2\pi}{\alpha^2-1}.
$$
So we have for $\abs{\alpha}\neq1$
$$
\int_0^{2\pi}\frac{d\theta}{1-2\alpha\cos\theta+\alpha^2}=\frac{2\pi}{\alpha^2-1}\cdot\frac{\abs{\alpha}-1}{\bigl\lvert\abs{\alpha}-1\bigr\rvert}.
$$
:::
