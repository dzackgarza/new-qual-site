---
schema: qual/card@1
id: E-PAQWN
kind: problem
title: Polynomial growth of entire functions and Liouville for bounded real part
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

::: {.problem}
(a) Let $f:\CC\rightarrow \CC$ be an entire function. Assume the existence of a non-negative integer $m$, and of positive constants $L$ and $R$, such that for all $z$ with $\abs{z}>R$ the inequality $$\abs{f(z)} \leq L \abs{z}^m$$ holds.
Prove that $f$ is a polynomial of degree $\leq m$.

(b) Let $f:\CC\rightarrow \CC$ be an entire function. Suppose that there exists a real number $M$ such that for all $z\in \CC, \Re(f) \leq M$.
Prove that $f$ must be a constant.
:::

::: {.solution}

Write $f(z)=\sum_{n\geq0}c_nz^n$, the Taylor series of $f$ at $0$, which converges on $\CC$.

::: pf

::: {.pf-step #cauchy}
(a) For every $n\geq0$ and $\rho>R$, $\abs{c_n}\leq L\rho^{m-n}$.

::: pf-proof
By the Cauchy integral formula on the circle $\abs{\xi}=\rho$,
$$
\abs{c_n} = \abs{\frac{1}{2\pi i}\oint_{\abs{\xi}=\rho}\frac{f(\xi)}{\xi^{n+1}}\,d\xi} \leq \frac{1}{2\pi}\cdot 2\pi\rho\cdot\frac{L\rho^m}{\rho^{n+1}} = L\rho^{m-n}.
$$
:::

:::

::: pf-step
(a) $f$ is a polynomial of degree at most $m$.

::: pf-proof
For $n>m$, letting $\rho\to\infty$ in step [](#cauchy){.pf-ref} gives $c_n=0$.
:::

:::

::: pf-step
(b) $f$ is constant.

::: pf-proof
$g\coloneqq e^{f}$ is entire and $\abs{g} = e^{\Re f}\leq e^M$, so $g$ is constant by Liouville's theorem.
Then $0 = g' = f'e^{f}$, and $e^{f}$ never vanishes, so $f'\equiv0$ and $f$ is constant.
:::

:::

:::

:::

::: {.remark title="Variations"}
In (a), the bound $\abs{f(z)}\leq A+B\abs{z}^k$ for $\abs{z}\geq M$ also forces $f$ to be a polynomial of degree at most $k$: the Cauchy estimate becomes $\abs{c_n}\leq A\rho^{-n}+B\rho^{k-n}$, which tends to $0$ for $n>k$.

The weaker hypothesis $f(z)/z^n\to0$ as $z\to\infty$, for an integer $n\geq1$, gives degree at most $n-1$: for each $\varepsilon>0$ the same estimate yields $\abs{c_k}\leq\varepsilon\rho^{n-k}\leq\varepsilon$ for $k\geq n$ and all large $\rho\geq1$, so $c_k=0$.
:::
