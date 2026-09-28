---
schema: qual/card@1
id: P-BKF04-9A
kind: problem
title: $\int_0^1 f(x)e^{inx^3}\,dx\to0$ for continuous $f$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f\colon[0,1]\to\mathbb{R}$ be a continuous function. Show that

$$
\lim_{n\to\infty}\int_0^1 f(x)e^{inx^3}\,dx=0.
$$
:::

::: {.solution}
Every continuous function on $[0,1]$ is a uniform limit of smooth functions, and $\abs{\int_0^1(f-g)e^{inx^3}\,dx}\leq\sup\abs{f-g}$ for every $n$, so it suffices to prove the statement when $f$ is smooth.

Choose $M$ such that $\abs{f(x)}<M$ for all $x\in[0,1]$. Let $\varepsilon>0$. Then

$$
\abs{\int_0^\varepsilon f(x)e^{inx^3}\,dx}\le\varepsilon M.
$$

On the remaining interval, integrate by parts:

$$
\begin{aligned}
\int_\varepsilon^1 f(x)e^{inx^3}\,dx
&=\int_\varepsilon^1\frac{f(x)}{x^2}\,x^2e^{inx^3}\,dx\\
&=\frac1{in}\left(f(1)e^{in}-\frac{f(\varepsilon)}{\varepsilon^2}e^{in\varepsilon^3}-\int_\varepsilon^1\frac{d}{dx}\left(\frac{f(x)}{x^2}\right)e^{inx^3}\,dx\right).
\end{aligned}
$$

Letting $n$ tend to infinity,

$$
\lim_{n\to\infty}\int_\varepsilon^1 f(x)e^{inx^3}\,dx=0.
$$

Adding to this the bound on $[0,\varepsilon]$,

$$
\lim_{n\to\infty}\abs{\int_0^1 f(x)e^{inx^3}\,dx}\le\varepsilon M.
$$

The conclusion follows by letting $\varepsilon$ tend to $0$.
:::
