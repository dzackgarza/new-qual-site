---
schema: qual/card@1
id: PR-DWOXP
kind: proposition
title: Limits of differentiable functions need not be differentiable
slogan: 'Uniform limits can lose differentiability, and derivatives need not commute with uniform convergence.'
prompts:
- Give a sequence of differentiable functions whose derivatives do not converge pointwise.
- Give a sequence of differentiable functions $f_n \to f$ uniformly with $f_n' \to g$ pointwise but $g \neq f'$.
- Give a sequence of differentiable functions whose pointwise limit is not differentiable.
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
The functions $g_n(x)\coloneqq x^2/\sqrt{x^2+1/n}$ also work: they are differentiable since $x^2+1/n>0$, and
$$
\abs{\abs{x} - g_n(x)} = \frac{\abs{x}}{\sqrt{x^2+1/n}}\qty(\sqrt{x^2+1/n} - \abs{x}) \leq \frac{1/n}{\sqrt{x^2+1/n} + \abs{x}} \leq \frac{1}{\sqrt n}.
$$

(2) Let $f_n(x)\coloneqq n^{-1/2}\sin(nx)$.
Then $\sup_x\abs{f_n(x)}\le n^{-1/2}$, so $f_n\to f=0$ uniformly, but $f_n'(0)=n^{1/2}\to\infty\neq0=f'(0)$.
:::

::: {.remark}
If $f_n\colon[a,b]\to\RR$ are differentiable, $(f_n(x_0))$ converges for some $x_0\in[a,b]$, and $(f_n')$ converges uniformly on $[a,b]$, then $(f_n)$ converges uniformly on $[a,b]$ to a differentiable function $f$ with $f'=\lim_n f_n'$.
A uniform limit of differentiable functions can be differentiable at no point: by the [[T-3QNBQ|Weierstrass approximation theorem]], every continuous function on $[a,b]$, including a nowhere differentiable one, is a uniform limit of polynomials.
:::

::: {.remark title="Variations"}
In (2), $f_n(x)\coloneqq n^{-c}\sin(nx)$ works for every $0<c\leq1$: $f_n\to0$ uniformly and $f_n'(x)=n^{1-c}\cos(nx)$.
For $c=1$ the derivatives $\cos(nx)$ do not converge pointwise, since $f_n'(\pi)=(-1)^n$.

The functions $f_n(x)\coloneqq\frac{x}{1+nx^2}$ satisfy $\abs{f_n}\leq\frac{1}{2\sqrt n}$, because $1+nx^2\geq2\sqrt n\abs x$, so $f_n\to f\coloneqq0$ uniformly.
Their derivatives $f_n'(x)=\frac{1-nx^2}{(1+nx^2)^2}$ satisfy $f_n'(0)=1$ and $\abs{f_n'(x)}\leq\frac{1}{1+nx^2}\to0$ for $x\neq0$, so $f_n'\to\chi_{\theset0}$ pointwise, a limit different from $f'=0$.
:::
