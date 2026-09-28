---
schema: qual/card@1
id: E-SS2.EX-4
kind: problem
title: "SS 2.4: The Gaussian is its own Fourier transform"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
4. Prove that for all $\xi \in \mathbb { C }$ we have $e ^ { - \pi \xi ^ { 2 } } = \int _ { - \infty } ^ { \infty } e ^ { - \pi x ^ { 2 } } e ^ { 2 \pi i x \xi } d x .$
:::

::: {.solution}
Define, for $\xi\in\mathbb C$,
\[
F(\xi)=\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
\]
For $\xi$ in any compact subset of $\mathbb C$, the integrand and all its $\xi$-derivatives are dominated by a function of the form
\[
C_N(1+|x|)^N e^{-\pi x^2+C|x|},
\]
which is integrable. Hence $F$ is entire and differentiation under the integral sign is valid.

Differentiating once,
\[
F'(\xi)=2\pi i\int_{-\infty}^{\infty}x e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
\]
Since
\[
\frac{d}{dx}e^{-\pi x^2}=-2\pi x e^{-\pi x^2},
\]
integration by parts gives
\[
\begin{aligned}
F'(\xi)
&=-i\int_{-\infty}^{\infty}\frac{d}{dx}(e^{-\pi x^2})e^{2\pi i x\xi}\,dx\\
&=i\int_{-\infty}^{\infty}e^{-\pi x^2}(2\pi i\xi)e^{2\pi i x\xi}\,dx\\
&=-2\pi\xi F(\xi),
\end{aligned}
\]
because the boundary term vanishes by Gaussian decay.

Thus
\[
\frac{d}{d\xi}\left(e^{\pi\xi^2}F(\xi)\right)=0,
\]
so $e^{\pi\xi^2}F(\xi)$ is constant on $\mathbb C$. At $\xi=0$,
\[
F(0)=\int_{-\infty}^{\infty}e^{-\pi x^2}\,dx=1.
\]
Therefore
\[
\boxed{F(\xi)=e^{-\pi\xi^2}}
\]
for every $\xi\in\mathbb C$.
:::
