---
schema: qual/card@1
id: P-PRACT20-W3-24
kind: problem
title: The Dirichlet integral $\int_0^\infty\frac{\sin t}{t}\,dt$ by differentiating under the integral
classification:
  areas:
  - prelim
  topics:
  - Improper Integrals
  - Differentiation Under the Integral
relations: []
review: draft
---

::: {.problem}
Evaluate $\int_{0}^{\infty} \frac{\sin(t)}{t}\, dt$ by differentiating $I(s) = \int_{0}^{\infty} e^{-st} \frac{\sin(t)}{t}\, dt$ with respect to $s$.
:::

::: {.solution}
For $s>0$ the $s$-derivative of the integrand is $-e^{-st}\sin t$, which is bounded by $e^{-s_0t}$ for $s\ge s_0>0$, so differentiation under the integral sign is valid and

$$
I'(s)=\int_0^\infty\frac{\partial}{\partial s}e^{-st}\frac{\sin t}{t}\,dt=-\int_0^\infty e^{-st}\sin t\,dt.
$$

Integrating by parts twice, with boundary terms vanishing at $\infty$ because $s>0$,

$$
\begin{aligned}
I'(s)&=-\left(\Bigl[-e^{-st}\cos t\Bigr]_{t=0}^{t\to\infty}-s\int_0^\infty e^{-st}\cos t\,dt\right)\\
&=-\left(1-\Bigl[se^{-st}\sin t\Bigr]_{t=0}^{t\to\infty}-s^2\int_0^\infty e^{-st}\sin t\,dt\right)\\
&=-1-s^2I'(s)\quad\Longrightarrow\quad I'(s)=-\frac{1}{1+s^2}.
\end{aligned}
$$

The integral defining $I(s)$ converges uniformly for $s\in[0,\infty)$ (Dirichlet's test: $\int_0^T\sin t\,dt$ is bounded and $e^{-st}/t$ decreases to $0$ in $t$, uniformly in $s\ge0$), so $I$ is continuous on $[0,\infty)$. Integrating,

$$
I(s)-I(0)=\int_0^sI'(r)\,dr=-\int_0^s\frac{dr}{1+r^2}=-\arctan s.
$$

Since $\abs{\sin t/t}\le1$, $\abs{I(s)}\le\int_0^\infty e^{-st}\,dt=1/s$ for $s>0$, so $\lim_{s\to\infty}I(s)=0$ and

$$
\int_0^\infty\frac{\sin t}{t}\,dt=I(0)=\lim_{s\to\infty}\bigl(I(s)+\arctan s\bigr)=\frac{\pi}{2}.
$$

The computation also shows that the Laplace transform of $\frac{\sin(t)}{t}$ is $I(s) = \frac{\pi}{2} - \arctan(s)$.
:::
