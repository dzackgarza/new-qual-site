---
schema: qual/card@1
id: P-BKS04-5A
kind: problem
title: UC Berkeley Spring 2004 prelim 5A
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
Suppose $f\colon\RR\to\CC$ satisfies $f'(t)+2itf(t)=e^{2it}$ and $f(0)=0$. Compute

$$
\lim_{t\to+\infty}e^{it^2}(f(t)-f(-t)).
$$

You may assume $\int_0^\infty e^{-t^2}\,dt=\sqrt\pi/2$.
:::

::: {.solution}
Multiply the ODE by the integrating factor $e^{it^2}$, and integrate to get

$$
e^{it^2}f(t)=\int_0^te^{ix^2+2ix}\,dx
$$

(The hypothesis $f(0)=0$ implies that there is no constant of integration.)
Substituting $-t$ for $t$ and subtracting, we get

$$
\begin{aligned}
e^{it^2}(f(t)-f(-t))&=\int_{-t}^te^{ix^2+2ix}\,dx\\
&=e^{-i}\int_{-t}^te^{i(x+1)^2}\,dx\\
&=e^{-i}\int_{-t+1}^{t+1}e^{iz^2}\,dz.
\end{aligned}
$$

Since $e^{iz^2}$ is an even function, the limit as $t\to+\infty$ equals $2e^{-i}I$, where $I\coloneqq\lim_{R\to+\infty}\int_0^Re^{iz^2}\,dz$ (assuming for now that the latter limit exists).
Apply Cauchy's theorem to the triangular contour from $0$ to $R$ to $R+Ri$ and back to $0$. The vertical part contributes

$$
\int_R^{R+Ri}e^{iz^2}\,dz=\int_0^Re^{i(R+ti)^2}\,i\,dt,
$$

whose absolute value is bounded by

$$
\begin{aligned}
\int_0^R\abs{e^{i(R+ti)^2}}\,dt&=\int_0^Re^{-2Rt}\,dt\\
&=\frac{1}{2R}\int_0^{2R^2}e^{-u}\,du,
\end{aligned}
$$

which goes to $0$ as $R\to\infty$. Thus

$$
\begin{aligned}
I&=\lim_{R\to\infty}\int_0^{R+Ri}e^{iz^2}\,dz&&\text{(if the limit exists)}\\
&=\lim_{R\to\infty}\int_0^Re^{i(e^{i\pi/4}t)^2}e^{i\pi/4}\,dt&&\text{(if the limit exists)}\\
&=e^{i\pi/4}\lim_{R\to\infty}\int_0^Re^{-t^2}\,dt&&\text{(if the limit exists)}\\
&=e^{i\pi/4}\frac{\sqrt\pi}{2}.
\end{aligned}
$$

Thus we now know that all the limits exist, and the answer is $2e^{-i}I=e^{-i+i\pi/4}\sqrt\pi$.
:::
