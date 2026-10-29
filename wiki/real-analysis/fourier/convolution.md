---
title: Convolution
order: 0
topics:
- Convolution
- Approximations to the Identity
---

# Convolution

[[D-TS42Y]]

::: {.remark}
For $f,g,h\in L^1(\RR^n)$, convolution is commutative and associative, $f*g\in L^1$, and $\norm{f*g}_1\leq\norm f_1\norm g_1$, by [[real-analysis/fubini-tonelli/statements|Tonelli's and Fubini's theorems]] applied to $(x,y)\mapsto f(x-y)g(y)$.
More generally, [[PR-PRSKG|Young's inequality]] bounds $\norm{f*g}_r$.

:::

::: {.remark title="Smoothing"}
If $f\in L^1(\RR^n)$ and $g\in C^k(\RR^n)$ with $\partial^\alpha g$ bounded for $\abs\alpha\leq k$, then $f*g\in C^k$ and $\partial^\alpha(f*g) = f*\partial^\alpha g$.
With $\phi\in C_c^\infty$, $\int\phi=1$, and $\phi_t(x)\coloneqq t^{-n}\phi(x/t)$, the functions $f*\phi_t$ are smooth and converge to $f$ in $L^p$ as $t\to0$ for $f\in L^p$, $1\leq p<\infty$; this proves density of $C^\infty$ functions in $L^p$.

:::

## Approximate identities

[[T-HHFGB]]

[[T-3UXK7]]

[[PR-PRSKG]]
