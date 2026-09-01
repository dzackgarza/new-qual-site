---
schema: qual/card@1
id: P-ULPU3
kind: problem
title: Herglotz's theorem for positive harmonic functions on the disc
classification:
  areas:
  - real-analysis
  topics:
  - Harmonic Functions
  - Measure Theory
  - Integrals
relations: []
review: draft
---

::: {.problem}
The Poisson kernel for $0\le \rho<1$ is the $2\pi$-periodic function on $\mathbb{R}$ defined by $$P_\rho(\theta) = \text{Re}\left(\frac{1+\rho e^{i\theta}}{1-\rho e^{i\theta}}\right).$$ For functions $h$ continuous on and harmonic inside the closed disc of radius $R$ about the origin one has $$h(re^{i\eta}) = \frac{1}{2\pi}\int_0^{2\pi} P_{r/R}(\eta-\theta) h(Re^{i\theta})\,d\theta.$$ Assume that $h$ is harmonic and positive on $\mathbb{D}$.
Prove that there exists a positive Borel measure $\mu$ on $[0,2\pi]$ such that for all $re^{i\nu}\in\mathbb{D}$ one has $$h(re^{i\nu}) = \int_0^{2\pi} P_r(\eta-\theta)\,d\mu(\theta).$$
:::

:::{.solution}
For each $0<R<1$, define the measure $\mu_R$ by $d\mu_R(\theta) = h(Re^{i\theta})\,d\theta$. By scaling we may assume $h(0)=1$. Since $h$ is positive and continuous, each $\mu_R$ is a positive Borel measure on $[0,2\pi]$. By the Riesz representation theorem, we may view each $\mu_R$ as a bounded linear functional on the Banach space $C([0,2\pi])$. Note that by the special case of the given formula with $r=0$ (i.e. the mean value property), we have
$$||\mu_R|| = \mu_R([0,2\pi]) = \frac{1}{2\pi}\int_0^{2\pi} h(Re^{i\theta})\,d\theta = h(0).$$
Thus each $\mu_R$ is in the unit ball of the dual space $C([0,2\pi])^*$. By Banach-Alaoglu and the fact that $C([0,2\pi])$ is separable, this implies that we have a subsequence of $R$s converging to 1 and some measure $\mu$ in the unit ball of $C([0,2\pi])^*$ with $\mu_R \to \mu$ in the weak-$*$ topology. A standard approximation argument shows that $\mu$ must also be a positive measure since each $\mu_R$ is. We claim that $\mu$ is the desired measure. Fix $re^{i\eta}\in\mathbb{D}$. Note that each $P_\rho$ is continuous on $[0,2\pi]$ and $P_{r/R}\to P_r$ uniformly on $[0,2\pi]$ as $R\to 1$. For each $R<1$ the given formula tells us
$$h(re^{i\eta}) = \int_0^{2\pi} P_{r/R}(\eta-\theta)\,d\mu_R(\theta).$$
Taking the limit as $R\to1$ on both sides gives the desired result, where we have assumed the following lemma: if $f_n$ are continuous and $f_n\to f$ uniformly on $[0,2\pi]$ and $\mu_n\to\mu$ in weak-$*$, then $\int f_n\,d\mu_n \to \int f\,d\mu$. The proof of this just follows by writing
$$\left|\int f_n\,d\mu_n - \int f\,d\mu\right| \le \left|\int f_n\,d\mu_n - \int f_n\,d\mu\right| + \left|\int f_n\,d\mu - \int f\,d\mu\right|$$
and noting that the first term goes to 0 by weak-$*$ convergence and the second term goes to zero by uniform convergence. $\square$
:::
