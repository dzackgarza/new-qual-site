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
Let $$f(x)=\int_1^x\frac1t\,dt$$ for $x>0$.

(a) Use an $\varepsilon$-$\delta$ proof to show that $f$ is continuous on $(0,\infty)$.

(b) Use an $\varepsilon$-$\delta$ proof to show that $f$ is differentiable on $(0,\infty)$.
:::

::: {.solution}

::: pf

::: pf-step

(a) The function $f$ is continuous at every $x_0>0$.

::: pf-proof

Fix $x_0>0$ and $\varepsilon>0$, and choose
$$
\delta=\min\left\{\frac{x_0}{2},\frac{\varepsilon x_0}{2}\right\}>0.
$$
If $\abs{x-x_0}<\delta$, then every $t$ between $x$ and $x_0$ satisfies $t>x_0/2$. By the additivity and orientation conventions for definite integrals,
$$
\abs{f(x)-f(x_0)}
=\abs{\int_{x_0}^{x}\frac{dt}{t}}
\leq\frac{2}{x_0}\abs{x-x_0}<\varepsilon.
$$
This is the $\varepsilon$-$\delta$ criterion at $x_0$.

:::

:::

::: pf-step

(b) The function $f$ is differentiable on $(0,\infty)$ with $\boxed{f'(x)=1/x}$.

::: pf-proof

::: {.pf-step #quotient-bound}

For every $x>0$ and every $h\ne0$ with $\abs{h}<x/2$,
$$
\abs{\frac{f(x+h)-f(x)}h-\frac1x}
\leq\frac{2\abs{h}}{x^2}.
$$

::: pf-proof

The difference quotient equals $h^{-1}\int_x^{x+h}t^{-1}\,dt$. Subtracting $1/x$ and applying the absolute integral bound on the unoriented interval between $x$ and $x+h$ gives
$$
\abs{\frac1h\int_x^{x+h}\left(\frac1t-\frac1x\right)dt}
\leq\sup_{t\text{ between }x\text{ and }x+h}\abs{\frac1t-\frac1x}.
$$
On that interval, $t>x/2$ and $\abs{t-x}\leq\abs{h}$, so $\abs{1/t-1/x}=\abs{t-x}/(tx)\leq2\abs{h}/x^2$.

:::

:::

::: pf-qed

Fix $x>0$ and $\varepsilon>0$. Choose $\delta=\min\{x/2,\varepsilon x^2/2\}>0$. Whenever $0<\abs{h}<\delta$, step [](#quotient-bound){.pf-ref} yields
$$
\abs{\frac{f(x+h)-f(x)}h-\frac1x}
\leq\frac{2\abs{h}}{x^2}<\varepsilon.
$$
This is the $\varepsilon$-$\delta$ definition of the derivative $f'(x)=1/x$.

:::

:::

:::

:::

:::
