---
schema: qual/card@1
id: P-WESCA10-II1
kind: problem
title: 'Limit of a semicircular contour integral'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
For $r>0$, let
$$
\gamma_r(t)=re^{it},\qquad 0\le t\le\pi.
$$
Calculate
$$
\lim_{r\to\infty}\int_{\gamma_r}\frac{e^{iz}}{z^2}\,dz.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $r>0$,
$$
\abs{\int_{\gamma_r}\frac{e^{iz}}{z^2}\,dz}
\le \frac{\pi}{r}.
$$


::: pf-proof

For $z\in\gamma_r$, one has $\abs{z}=r$ and
$$
\abs{e^{iz}}=e^{-\operatorname{Im}z}\le 1,
$$
because $\operatorname{Im}z\ge0$ on the upper semicircle. Hence
$$
\abs{\frac{e^{iz}}{z^2}}\le\frac1{r^2}.
$$
The length of $\gamma_r$ is $\pi r$, so the ML inequality gives
$$
\abs{\int_{\gamma_r}\frac{e^{iz}}{z^2}\,dz}
\le (\pi r)\frac1{r^2}
=\frac\pi r.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{\lim_{r\to\infty}\int_{\gamma_r}\frac{e^{iz}}{z^2}\,dz=0}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the absolute value of the integral is bounded by $\pi/r$, which tends to $0$ as $r\to\infty$. The squeeze theorem gives the stated limit.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested value.

:::

:::

:::
