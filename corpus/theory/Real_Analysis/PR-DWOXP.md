---
schema: qual/card@1
id: PR-DWOXP
kind: proposition
title: Limits of differentiable functions need not be differentiable
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Uniform Convergence
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
1. There are differentiable functions $f_n\colon\RR\to\RR$ that [[D-YZC3C|converge uniformly]] on $\RR$ to a function that is not differentiable.

2. There are differentiable functions $f_n\colon\RR\to\RR$ that converge uniformly on $\RR$ to a differentiable function $f$ while $f_n'(0)\not\to f'(0)$.
:::

::: {.proof}
(1) Let $f_n(x)\coloneqq\sqrt{x^2+1/n}$.
Each $f_n$ is differentiable, and
$$
0\le f_n(x)-\abs{x}=\frac{1/n}{\sqrt{x^2+1/n}+\abs{x}}\le\frac{1}{\sqrt n},
$$
so $f_n\to\abs{x}$ uniformly on $\RR$, and $\abs{x}$ is not differentiable at $0$.

(2) Let $f_n(x)\coloneqq n^{-1/2}\sin(nx)$.
Then $\sup_x\abs{f_n(x)}\le n^{-1/2}$, so $f_n\to f=0$ uniformly, but $f_n'(0)=n^{1/2}\to\infty\neq0=f'(0)$.
:::

::: {.remark}
Uniform convergence of the derivatives restores the interchange: if $f_n\colon[a,b]\to\RR$ are differentiable, $(f_n(x_0))$ converges for some $x_0\in[a,b]$, and $(f_n')$ converges uniformly on $[a,b]$, then $(f_n)$ converges uniformly on $[a,b]$ to a differentiable function $f$ with $f'=\lim_n f_n'$.
Without such a hypothesis nothing survives: by the [[T-3QNBQ|Weierstrass approximation theorem]], every continuous function on $[a,b]$, including a nowhere differentiable one, is a uniform limit of polynomials.
:::
