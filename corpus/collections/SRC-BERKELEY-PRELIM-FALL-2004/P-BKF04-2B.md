---
schema: qual/card@1
id: P-BKF04-2B
kind: problem
title: Decay of the Newtonian potential $\int f(y)/|x-y|\,dy$ of a compactly supported $f$ on $\RR^3$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f \colon  { \mathbb { R } } ^ { 3 } \to  { \mathbb { R } }$ be a continuous function of compact support (i.e., $f$ vanishes outside some bounded set).

(a) Show that

$$
u ( x ) : = \int { \frac { f ( y ) } { | x - y | } } d y
$$

converges, where the integral is over all $\boldsymbol { y } \in \mathbb { R } ^ { 3 }$

(b) Show that $\lim_{|x|\to\infty}u(x)|x|$ exists.
:::

::: {.solution}
(a) Let $M$ be the maximum value of $\abs{f}$; it exists because $f$ is continuous and vanishes outside a compact set. Fix $x$. Choose $R$ large enough that $f(y)=0$ whenever $\abs{x-y}>R$. Using polar coordinates centered at $x$,

$$
\int\frac{\abs{f(y)}}{\abs{x-y}}\,dy\leq\int_0^R\frac{M}{r}\,4\pi r^2\,dr,
$$

which is finite, so the integral defining $u(x)$ converges absolutely.

(b) Writing $f(y)=\max\{f(y),0\}+\min\{f(y),0\}$ and using linearity of $u$ in $f$ reduces the problem to the case that $f$ is nonnegative everywhere. Let $R_0>0$ be such that $f(y)=0$ for $\abs y>R_0$. If $\abs x\geq nR_0$ with $n\geq2$, and $\abs y\leq R_0$, then

$$
\frac{\abs x}{\abs{x-y}}\leq\frac{\abs x}{\abs x-\abs y}=\frac1{1-\abs y/\abs x}\leq\frac1{1-1/n}=\frac n{n-1},
$$

$$
\frac{\abs x}{\abs{x-y}}\geq\frac{\abs x}{\abs x+\abs y}=\frac1{1+\abs y/\abs x}\leq\frac1{1+1/n}=\frac n{n+1}.
$$

Hence

$$
\frac n{n+1}\int f\,dy\leq u(x)\abs x\leq\frac n{n-1}\int f\,dy
$$

whenever $\abs x\geq nR_0$. Since $n$ is arbitrary, $\lim_{\abs x\to\infty}u(x)\abs x=\int f\,dy$.
:::
