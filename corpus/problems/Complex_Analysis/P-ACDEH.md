---
schema: qual/card@1
id: P-ACDEH
kind: problem
title: Entire functions of quadratic growth are polynomials of degree at most $2$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Liouville's Theorem
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some disk for some constant $M$.
Show that $f(z)$ is a polynomial in $z$ of degree $\leq 2$.
:::

::: {.solution}
**Goal:** Prove that if $f$ is entire and $\abs{f(z)} \leq M \abs z^2$ for all $z$ outside some disk (i.e. for $\abs z \geq R_0$), then $f$ is a polynomial of degree $\leq 2$.

::: pf

::: {.pf-step #taylor-expansion}
Write $f(z) = \sum_{n=0}^{\infty} a_n z^n$.

::: pf-proof
$f$ is entire.
:::

:::

::: {.pf-step #max-modulus-bound}
For $R \geq R_0$, $M(R) := \max_{\abs z = R} \abs{f(z)} \leq M R^2$.

::: pf-proof
By hypothesis applied on the circle $\abs z = R$.
:::

:::

::: {.pf-step #coefficient-bound}
For $n \geq 3$ and $R \geq R_0$, $\abs{a_n} \leq \frac{M(R)}{R^n} \leq \frac{M R^2}{R^n} = M R^{2-n}$.

::: pf-proof
Cauchy's estimate, step [](#max-modulus-bound){.pf-ref}.
:::

:::

::: {.pf-step #higher-coeffs-zero}
$a_n = 0$ for all $n \geq 3$.

::: pf-proof
Step [](#coefficient-bound){.pf-ref} holds for arbitrarily large $R$, and $R^{2-n} \to 0$ as $R \to \infty$ for $n \geq 3$.
:::

:::

::: {.pf-step #polynomial-degree-2}
$f(z) = a_0 + a_1 z + a_2 z^2$, a polynomial of degree at most $2$.

::: pf-proof
Steps [](#taylor-expansion){.pf-ref} and [](#higher-coeffs-zero){.pf-ref}.
:::

:::

::: pf-qed
Step [](#polynomial-degree-2){.pf-ref} is the claim.
:::

:::

:::

::: {.solution}
Take a Laurent expansion at zero:
\[
f(z) = \sum_{k\geq 0} c_k z^k,\qquad c_k = {1\over k!} f^{(k)}(0) = {1\over 2\pi i}\oint_{\abs{\xi} = R} {f(\xi) \over \xi^{k+1}}\dxi
.\]
The usual estimate:
\[
2\pi i\abs{c_k} \leq \oint_{\abs{\xi} = R} R^{-(k+1)}\abs{f(\xi)} \dxi
&\leq \oint_{\abs{\xi} = R}R^{-(k+1)} M R^2 \dxi \\
&= M R^{-(k-1)} \cdot 2\pi R \\
&= 2\pi M R^{-k+2} \\
&\convergesto{R\to\infty}0
,\]
provided $-k+2<0 \iff k>2$.
:::
