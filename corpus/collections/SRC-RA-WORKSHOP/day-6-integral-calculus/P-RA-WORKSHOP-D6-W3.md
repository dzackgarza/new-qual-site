---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W3
kind: problem
title: Epsilon-delta continuity and differentiability of an integral of $1/t$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Differentiation
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(January 2007 #1) Let $$f(x)=\int_1^x\frac1t\,dt$$ for $x>0$.
(a) Use an $\epsilon$-$\delta$ proof to show that $f$ is continuous on $(0,\infty)$.
(b) Use an $\epsilon$-$\delta$ proof to show that $f$ is differentiable on $(0,\infty)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $f$ is continuous at every $x_0>0$.

::: pf-proof

Fix $x_0>0$ and $\varepsilon>0$, and choose
\[
\delta=\min\left\{\frac{x_0}{2},\frac{\varepsilon x_0}{2}\right\}>0.
\]
If $|x-x_0|<\delta$, then every $t$ between $x$ and $x_0$ satisfies $t>x_0/2$. By the additivity and orientation conventions for definite integrals,
\[
|f(x)-f(x_0)|
=\left|\int_{x_0}^{x}\frac{dt}{t}\right|
\leq\frac{2}{x_0}|x-x_0|<\varepsilon.
\]
This is the epsilon-delta criterion at $x_0$.

:::

:::

::: {.pf-step #s2}

For every $x>0$ and every $h\ne0$ with $|h|<x/2$,
\[
\left|\frac{f(x+h)-f(x)}h-\frac1x\right|
\leq\frac{2|h|}{x^2}.
\]

::: pf-proof

The difference quotient equals $h^{-1}\int_x^{x+h}t^{-1}\,dt$. Subtracting $1/x$ and applying the absolute integral bound on the unoriented interval between $x$ and $x+h$ gives
\[
\left|\frac1h\int_x^{x+h}\left(\frac1t-\frac1x\right)dt\right|
\leq\sup_{t\text{ between }x\text{ and }x+h}\left|\frac1t-\frac1x\right|.
\]
On that interval, $t>x/2$ and $|t-x|\leq|h|$, so $|1/t-1/x|=|t-x|/(tx)\leq2|h|/x^2$.

:::

:::

::: {.pf-step #s3}

The function $f$ is differentiable on $(0,\infty)$ with $\boxed{f'(x)=1/x}$.

::: pf-proof

Fix $x>0$ and $\varepsilon>0$. Choose $\delta=\min\{x/2,\varepsilon x^2/2\}>0$. Whenever $0<|h|<\delta$, step [](#s2){.pf-ref} yields
\[
\left|\frac{f(x+h)-f(x)}h-\frac1x\right|
\leq\frac{2|h|}{x^2}<\varepsilon.
\]
This is the epsilon-delta definition of the derivative.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), and step [](#s3){.pf-ref} proves part (b).

:::

:::

:::
