---
schema: qual/card@1
id: FF-4XBYG
kind: fact
title: Cauchy--Schwarz inequality in $L^2$
prompts:
- State the Cauchy-Schwarz inequality for integrals.
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - L²
  - Inner Product Spaces
relations: []
review: draft
---

::: {.fact}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $f, g\in L^2(\mu)$, and put $\inner{f}{g}\coloneqq\int_X f\overline{g}\dmu$.
Then $fg\in L^1(\mu)$ and
$$
\abs{\inner{f}{g}} \leq \norm{fg}_1 \leq \norm{f}_2 \norm{g}_2, \quad\text{that is,}\quad
\abs{\int_X f\overline{g}\dmu}\leq\int_X\abs{fg}\dmu \leq \qty{\int_X \abs{f}^2\dmu}^{1/2} \qty{\int_X \abs{g}^2\dmu}^{1/2}.
$$
Moreover, $\abs{\inner{f}{g}} = \norm{f}_2\norm{g}_2$ if and only if $f$ and $g$ are linearly dependent in $L^2(\mu)$.
:::

::: {.proof}
The first inequality is $\abs{\int_X f\overline g\dmu}\leq\int_X\abs{f\overline g}\dmu$.
For the second, if $\norm{f}_2 = 0$ or $\norm{g}_2 = 0$ then $fg = 0$ almost everywhere and both sides vanish.
Otherwise, applying $ab\leq\frac12(a^2+b^2)$ for $a,b\geq 0$ to $a = \abs{f(x)}/\norm{f}_2$ and $b = \abs{g(x)}/\norm{g}_2$ and integrating gives $\int_X\abs{fg}\dmu\leq\norm{f}_2\norm{g}_2$.

For the equality case, if $f = \lambda g$ or $g = \lambda f$ for some $\lambda\in\CC$, then both sides equal $\abs{\lambda}\norm{g}_2^2$ or $\abs{\lambda}\norm{f}_2^2$.
Conversely, suppose $\abs{\inner{f}{g}} = \norm{f}_2\norm{g}_2$.
If $\norm{g}_2 = 0$ then $g = 0$ in $L^2(\mu)$ and $f, g$ are dependent.
Otherwise put $\lambda\coloneqq\inner{f}{g}/\norm{g}_2^2$; expanding gives
$$
\norm{f-\lambda g}_2^2 = \norm{f}_2^2 - \frac{\abs{\inner{f}{g}}^2}{\norm{g}_2^2} = 0,
$$
so $f = \lambda g$ in $L^2(\mu)$.
:::
