---
schema: qual/card@1
id: FE-2UZDB
kind: example
title: Uniformly convergent differentiable $f_n\to f$ with $f_n'\to g$ pointwise and $g\neq f'$
prompts:
- Give a sequence of differentiable functions $f_n \to f$ uniformly with $f_n' \to g$ pointwise but $g \neq f'$.
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Differentiation
  - Counterexamples
relations: []
review: draft
---

::: {.example}
A sequence of differentiable functions can [[D-YZC3C|converge uniformly]] to a differentiable function $f$ while the derivatives [[D-IYDZU|converge pointwise]] to a function $g\neq f'$.

For $n\geq 1$ let $f_n\colon\RR\to\RR$, $f_n(x) \coloneqq \frac{x}{1+nx^2}$.
Since $1+nx^2\geq 2\sqrt{n}\abs{x}$, we have $\abs{f_n(x)}\leq \frac{1}{2\sqrt n}$ for all $x\in\RR$, with equality at $x = 1/\sqrt n$.
Hence $\norm{f_n}_\infty = \frac{1}{2\sqrt n}\to 0$, and $f_n\to f\coloneqq 0$ uniformly on $\RR$.

The derivatives are
$$
f_n'(x) = \frac{1-nx^2}{(1+nx^2)^2}.
$$
For every $n$, $f_n'(0) = 1$; for $x\neq 0$, $\abs{f_n'(x)}\leq \frac{1+nx^2}{(1+nx^2)^2} = \frac{1}{1+nx^2}\to 0$.
Hence $f_n'\to g\coloneqq\chi_{\theset{0}}$ pointwise on $\RR$, while $f' = 0$ and $g(0) = 1\neq f'(0)$.
:::
