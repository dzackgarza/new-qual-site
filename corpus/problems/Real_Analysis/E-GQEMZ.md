---
schema: qual/card@1
id: E-GQEMZ
kind: problem
title: $\partial_i(f\ast g)=f\ast\partial_i g$ for $f\in L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- $f\in L^1$ and $g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

- Show that if $f\in L^1$ and $g'$ exists with $\dd{g}{x_i}$ all bounded, then $$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$$
:::

::: {.solution}
Let $f \in L^1(\RR^n)$, let $g$ be differentiable with $\dd{g}{x_i}$ bounded, and let $e_i$ be the $i$th standard basis vector.

::: pf

::: {.pf-step #s1}

For $h \neq 0$, $\frac{(f\ast g)(x + h e_i) - (f\ast g)(x)}{h} = \int f(x-y)\, \frac{g(y + h e_i) - g(y)}{h}\,dy$.

::: pf-proof

$(f\ast g)(x+he_i) = \int f(x+he_i-y)g(y)\,dy$; the change of variables $y \mapsto y + h e_i$ turns this into $\int f(x-y)g(y+he_i)\,dy$. Subtract $(f\ast g)(x) = \int f(x-y)g(y)\,dy$ and divide by $h$.

:::

:::

::: {.pf-step #s2}

As $h \to 0$, the integrands in step [](#s1){.pf-ref} converge pointwise to $f(x-y)\,\dd{g}{y_i}(y)$ and are bounded by $|f(x-y)| \sup_z |\dd{g}{z_i}(z)|$, which is integrable in $y$.

::: pf-proof

Pointwise convergence is differentiability of $g$ in the direction $e_i$. The bound on the difference quotient is the mean value theorem applied to $t \mapsto g(y + te_i)$. The dominating function is integrable because $f \in L^1$.

:::

:::

::: {.pf-step #s3}

$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$.

::: pf-proof

By step [](#s2){.pf-ref} the dominated convergence theorem lets $h \to 0$ pass under the integral in step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

If $g$ is smooth and compactly supported, then $f \ast g$ is smooth.

::: pf-proof

Every partial derivative $D^\alpha g$ of a smooth compactly supported $g$ is bounded, so step [](#s3){.pf-ref} applied repeatedly gives $D^\alpha(f\ast g) = f \ast D^\alpha g$ for every multi-index $\alpha$. Each $f \ast D^\alpha g$ is the convolution of an $L^1$ function with a bounded function, hence continuous, so $f \ast g$ has continuous partial derivatives of all orders.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the differentiation formula, and step [](#s4){.pf-ref} is smoothness of $f\ast g$ for smooth compactly supported $g$.

:::

:::

:::
