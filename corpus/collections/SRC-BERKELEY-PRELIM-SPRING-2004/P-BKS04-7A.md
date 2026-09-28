---
schema: qual/card@1
id: P-BKS04-7A
kind: problem
title: UC Berkeley Spring 2004 prelim 7A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Evaluate $\int_0^\infty\frac{\sin x}{x}\,dx$.
:::

::: {.solution}
For $R>1$, let $\gamma_1$ be the straight line path from $1/R$ to $R$, let $\gamma_2$ be the straight line path from $R$ to $R+Ri$, let $\gamma_3$ be the straight line path from $R+Ri$ to $-R+Ri$, let $\gamma_4$ be the straight line path from $-R+Ri$ to $-R$, let $\gamma_5$ be the straight line path from $-R$ to $-1/R$, and let $\gamma_6$ be the upper semicircle from $-1/R$ to $1/R$ given by the parameterization $\gamma_6(t)=(1/R)e^{it}$ for $t$ running from $\pi$ to $0$. Let $\gamma$ be the closed loop formed by concatenating these six paths.
Cauchy's theorem implies that $\int_\gamma\frac{e^{iz}}{z}\,dz=0$.

We have

$$
\abs{\int_{\gamma_2}\frac{e^{iz}}{z}\,dz}\leq\int_0^R\frac{e^{-t}}{R}\,dt=\frac{1-e^{-R}}{R}\to0
$$

as $R\to\infty$. Similarly $\int_{\gamma_4}\frac{e^{iz}}{z}\,dz\to0$, and

$$
\abs{\int_{\gamma_3}\frac{e^{iz}}{z}\,dz}\leq\int_{-R}^R\frac{e^{-R}}{R}\,dt=2e^{-R}\to0.
$$

On the other hand, $e^{iz}/z$ differs from $1/z$ by a holomorphic function, and $\gamma_6$ is shrinking to a point, so

$$
\begin{aligned}
\lim_{R\to\infty}\int_{\gamma_6}\frac{e^{iz}}{z}\,dz&=\lim_{R\to\infty}\int_{\gamma_6}\frac1z\,dz\\
&=\lim_{R\to\infty}\int_\pi^0\frac{1}{(1/R)e^{it}}(1/R)ie^{it}\,dt\\
&=-\pi i.
\end{aligned}
$$

Thus

$$
\int_{\gamma_1}\frac{e^{iz}}{z}\,dz+\int_{\gamma_5}\frac{e^{iz}}{z}\,dz\to\pi i
$$

as $R\to\infty$. Taking imaginary parts and using the fact that $(\sin z)/z$ is an even function, we find that

$$
2\int_{1/R}^R\frac{\sin z}{z}\,dz\to\pi
$$

as $R\to\infty$. Since $(\sin z)/z$ is holomorphic, it does not hurt to replace the lower limit $1/R$ by $0$, so $\int_0^\infty\frac{\sin x}{x}\,dx=\pi/2$.
:::
