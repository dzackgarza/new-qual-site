---
schema: qual/card@1
id: PR-YO7MV
kind: proposition
title: Markov and Chebyshev inequalities
slogan: 'Large-value sets are controlled by moments: $\mu\theset{\abs{f}>\alpha}\leq\alpha^{-p}\norm{f}_p^p$.'
prompts:
- State Chebyshev's inequality.
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Lp Spaces
  - Integrals
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $f\colon X\to\CC$ be [[D-DHFN4|measurable]], let $\alpha>0$, and put $S_\alpha\coloneqq\theset{x\in X\suchthat\abs{f(x)}>\alpha}$.
Then
$$
\mu(S_\alpha) \leq \frac{1}{\alpha}\int_X\abs{f}\dmu = \frac{1}{\alpha}\norm{f}_1,
$$
and more generally, for $0<p<\infty$,
$$
\mu(S_\alpha) \leq \frac{1}{\alpha^p}\int_X\abs{f}^p\dmu = \frac{1}{\alpha^p}\norm{f}_p^p.
$$
:::

::: {.proof}
On $S_\alpha$ we have $\abs{f(x)} > \alpha$, hence $\abs{f(x)}^p > \alpha^p$, so
$$
\int_X \abs{f}^p\dmu \geq \int_{S_\alpha} \abs{f}^p\dmu \geq \int_{S_\alpha} \alpha^p\dmu = \alpha^p \mu(S_\alpha).
$$
Dividing by $\alpha^p > 0$ gives the second inequality, and $p=1$ gives the first.

![Graph of a nonnegative function $f$ with the horizontal line at height $\alpha$; the set where $f > \alpha$ is two intervals, and the shaded rectangles of height $\alpha$ over them have total area $\alpha\, m(\theset{x \suchthat f(x)>\alpha})$ and lie under the graph of $f$](../../assets/figures/image_2021-06-02-22-59-46.png)
:::

::: {.remark}
For a probability space $(\Omega,\mathcal F,P)$ and a nonnegative random variable $Y$ with expectation $E(Y)$, the case $p=1$ reads $P(Y>\alpha)\leq E(Y)/\alpha$.
:::

::: {.remark title="Variations"}
The same bound holds for the larger set $\theset{x\in X\suchthat\abs{f(x)}\geq\alpha}$: since $\alpha^p\chi_{\theset{\abs{f}\geq\alpha}}\leq\abs{f}^p$ pointwise, integrating gives
$$
\mu\qty{\theset{x\in X\suchthat\abs{f(x)}\geq\alpha}}\leq\qty{\frac{\norm{f}_p}{\alpha}}^p .
$$
:::
