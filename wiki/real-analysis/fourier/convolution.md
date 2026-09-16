---
title: Convolution
order: 0
topics:
- Convolution
- Approximations to the Identity
---

# Convolution

For measurable $f,g$ on $\RR^n$, the convolution is $f * g(x) \coloneqq \int f(x-y)g(y)\dy$ wherever the integral converges absolutely.

::: {.remark title="Properties of convolution from Fubini--Tonelli"}
Each basic property of convolution is proved by applying [[real-analysis/fubini-tonelli/statements|Tonelli's or Fubini's theorem]] to the function $(x,y)\mapsto f(x-y)g(y)$ on $\RR^n\times\RR^n$:

- for $f,g\in L^1$, Tonelli's theorem applied to $\abs{f(x-y)g(y)}$ gives $\int\int\abs{f(x-y)g(y)}\dy\dx = \norm f_1\norm g_1$, so $f*g(x)$ is defined for almost every $x$ and $\norm{f*g}_1 \leq \norm f_1\norm g_1$;

- commutativity and associativity follow from the change of variables $y \mapsto x-y$ and Fubini's theorem;

- Young's inequality $\norm{f*g}_r \leq \norm f_p\norm g_q$ with $\frac1r = \frac1p + \frac1q - 1$ follows from Hölder's inequality applied inside Tonelli's theorem.

:::

::: {.remark title="Smoothing"}
If $f\in L^1(\RR^n)$ and $g\in C^k(\RR^n)$ with $\partial^\alpha g$ bounded for $\abs\alpha\leq k$, then $f*g\in C^k$ and $\partial^\alpha(f*g) = f*\partial^\alpha g$, by differentiating under the integral with the dominating function $\abs f\,\norm{\partial^\alpha g}_\infty$.
With $\phi\in C_c^\infty$, $\int\phi=1$, and $\phi_t(x)\coloneqq t^{-n}\phi(x/t)$, the functions $f*\phi_t$ are smooth and converge to $f$ in $L^p$ as $t\to0$ for $f\in L^p$, $1\leq p<\infty$; this proves density of $C^\infty$ functions in $L^p$.

:::

## Approximate identities

[[T-HHFGB]]

[[T-3UXK7]]

[[PR-PRSKG]]

[[PR-A7UFG]]
