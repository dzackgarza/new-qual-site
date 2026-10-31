---
schema: qual/card@1
id: P-PRACT20-W4-08
kind: problem
title: The Cauchy--Euler equation $2x^2y''+3xy'-15y=0$ and the repeated-root case
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
(Cauchy-Euler Equations) Consider the equation $2x^{2} y'' + 3x y' - 15y = 0$ for $x > 0$.

(a) Find the general solution, either by making the substitution $x = e^{t}$ or by searching for a solution of the form $y(x) = x^{\lambda}$. The latter leads to a quadratic polynomial for $\lambda$ which has two roots.

(b) If the equation were changed so that the polynomial has only one root, the search for $y=x^\lambda$ would give only one solution. How could you adjust to find another linearly independent solution?
:::

::: {.solution}
We’ll do the problem both ways.
First, substituting $y(x)=x^\lambda$, we find

$$
2\lambda(\lambda-1)x^\lambda+3\lambda x^\lambda-15x^\lambda=0.
$$

Since this must hold for all $x>0$, we need $2\lambda^2+\lambda-15=0$, that is, $(2\lambda-5)(\lambda+3)=0$. The two solutions $x^{5/2}$ and $x^{-3}$ are linearly independent, so the general solution is

$$
\boxed{y(x)=C_1x^{5/2}+C_2x^{-3}}.
$$

Now we use the substitution $x=e^t$. Define $Y(t)=y(e^t)$; we find a differential equation for $Y$. We see

$$
\begin{aligned}
Y'(t)&=e^ty'(e^t),\\
Y''(t)&=e^{2t}y''(e^t)+e^ty'(e^t).
\end{aligned}
$$

Thus

$$
2Y''(t)+Y'(t)=2(e^t)^2y''(e^t)+3e^ty'(e^t)=15y(e^t)=15Y(t).
$$

This is a constant-coefficient equation; substituting $Y(t)=e^{rt}$ gives $2r^2+r-15=0$, so $r=5/2,-3$, the same roots as $\lambda$ above. Thus

$$
Y(t)=C_1e^{\frac52t}+C_2e^{-3t}\implies\boxed{y(x)=Y(\log x)=C_1x^{5/2}+C_2x^{-3}}.
$$

The second method answers the last question: what if $\lambda$ were a repeated root? Then the transformed equation for $Y(t)$ has characteristic polynomial a multiple of $(r-r_1)^2$, and its solutions are

$$
Y(t)=C_1e^{r_1t}+C_2te^{r_1t}\quad\Longrightarrow\quad\boxed{y(x)=Y(\log x)=C_1x^{r_1}+C_2x^{r_1}\log x}.
$$
:::
