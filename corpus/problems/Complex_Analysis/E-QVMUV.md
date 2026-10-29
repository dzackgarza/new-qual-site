---
schema: qual/card@1
id: E-QVMUV
kind: problem
title: Cauchy integral formula for coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Cauchy Integral Formula
  - Convergence Tests
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "if $f(z) \sum_{k} c_k (z-z_0)^k$" with no equality sign, uses the exponent $n+1$ in the coefficient formula for $c_k$, and writes the radii with $a_{\pm n}$. The statement now writes $f(z) = \sum_k c_k (z-z_0)^k$, the exponent $k+1$, the coefficients $c_{\pm n}$, and takes $\gamma$ to be a positively oriented circle about $z_0$ in the annulus.'
---

::: {.exercise}
Show that if $f(z) = \sum_{k\in \ZZ} c_k (z-z_0)^k$, then
$$
c_k = {1\over 2\pi i}\int_\gamma {f(z) \over (z-z_0)^{k+1}}\dz
$$
for every positively oriented circle $\gamma$ centered at $z_0$ in the annulus of convergence, and that the series converges in the annulus $D_R(z_0)\sm \bar{D_r(z_0)}$, where
$$
r=\limsup _{n \to \infty} \sqrt[n]{\abs{c_{-n}}} \quad \text{ and } \quad R=\frac{1}{\limsup _{n \to \infty} \sqrt[n]{\abs{c_{n}}}}.
$$
:::

::: {.hint}
Start with
$$
f(z)=\frac{1}{2 \pi i} \oint_{\abs{w-z_{0}}=s_{2}} \frac{f(w)}{w-z} \, dw-\frac{1}{2 \pi i} \oint_{\abs{w-z_{0}}=s_{1}} \frac{f(w)}{w-z} \, dw,
$$
and expand each kernel as a geometric series to obtain
$$
f(z)=\sum_{j=-\infty}^{\infty}\left(\frac{1}{2 \pi i} \oint_{\abs{w-z_{0}}=s} \frac{f(w)}{\left(w-z_{0}\right)^{j+1}} \, dw\right)\left(z-z_{0}\right)^{j}.
$$
:::

::: {.solution}

::: pf

::: pf-step
$c_k={1\over2\pi i}\int_\gamma {f(z)\over(z-z_0)^{k+1}}\dz$.

::: pf-proof
The series converges uniformly on the compact circle $\gamma$, so termwise integration is valid:
$$
{1\over2\pi i}\int_\gamma {f(z)\over(z-z_0)^{k+1}}\dz
=\sum_{j\in\ZZ}c_j{1\over2\pi i}\int_\gamma(z-z_0)^{j-k-1}\dz=c_k,
$$
because $\int_\gamma (z-z_0)^m\dz$ is $2\pi i$ for $m=-1$ and $0$ for every other integer $m$.
:::

:::

::: pf-step
The part $\sum_{n\ge 0}c_n(z-z_0)^n$ converges for $\abs{z-z_0}<R$.

::: pf-proof
This is the Cauchy--Hadamard formula for the radius of convergence of a power series.
:::

:::

::: pf-step
The part $\sum_{n\ge1}c_{-n}(z-z_0)^{-n}$ converges for $\abs{z-z_0}>r$.

::: pf-proof
Put $w=(z-z_0)^{-1}$. The power series $\sum_{n\ge1}c_{-n}w^n$ has radius of convergence $1/\limsup_{n}\abs{c_{-n}}^{1/n} = 1/r$ by Cauchy--Hadamard, so it converges for $\abs{w}<1/r$, that is, for $\abs{z-z_0}>r$.
:::

:::

::: pf-qed
The Laurent series converges exactly where both parts converge, which by the two preceding steps is the annulus $r<\abs{z-z_0}<R$.
:::

:::

:::
