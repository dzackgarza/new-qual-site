---
schema: qual/card@1
id: P-2YFVO
kind: problem
title: Support, uniform continuity, vanishing at infinity, and derivatives of convolutions
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
(a) Show that if $f, g$ are continuous and compactly supported, then so is $f\ast g$.

(b) Show that if $f\in L^1$ and $g$ is bounded, then  $f\ast g$ is bounded and uniformly continuous.

(c) If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

(d) Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

(i) $f, g\in L^1$ are both bounded.

(ii) $f, g\in L^1$ with just $g$ bounded.

(iii) $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

(iv) $f\in L^1$ and $g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

(e) Show that if $f\in L^1$ and $g$ is bounded and differentiable with every $\dd{g}{x_i}$ bounded, then $$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f, g$ are continuous and compactly supported, then $f \ast g$ is continuous and compactly supported.

::: pf-proof

$\abs{f\ast g(x + h) - f\ast g(x)} \le \norm{g}_1 \sup_z\abs{f(z + h) - f(z)}$, which tends to $0$ because $f$ is uniformly continuous. $f\ast g$ vanishes off the compact set $\supp f + \supp g$, the image of $\supp f \times \supp g$ under addition. See [[E-Y4GZM]].

:::

:::

::: {.pf-step #s2}

If $f \in L^1$ and $\abs{g} \leq M$, then $\abs{f \ast g} \le M\norm{f}_1$ and $f\ast g$ is uniformly continuous.

::: pf-proof

$\abs{f\ast g(x)} \le \int \abs{f(x-y)}\abs{g(y)}\,dy \le M\norm{f}_1$. Substituting $u = x - y$ gives $\abs{f \ast g(x + h) - f \ast g(x)} \le M\int\abs{f(u + h) - f(u)}\,du$, which does not depend on $x$ and tends to $0$ as $h \to 0$ by continuity of translation in $L^1$. See [[E-E4H2J]].

:::

:::

::: {.pf-step #s3}

If $f, g$ are compactly supported, then $f \ast g$ is compactly supported.

::: pf-proof

The argument of step [](#s1){.pf-ref} uses no continuity: $f\ast g(x) = 0$ for $x \notin \supp f + \supp g$, which is compact.

:::

:::

::: {.pf-step #s4}

$f \ast g$ vanishes at infinity under each of the four listed assumptions.

::: pf-proof

::: {.pf-step #s4-1}

The cases $f, g \in L^1$ both bounded, $f, g \in L^1$ with $g$ bounded, and $f, g$ smooth and compactly supported.

::: pf-proof

In the first case split $\int f(x-y)g(y)\,dy$ at $\norm{y} = \norm{x}/2$ and bound each piece by an $L^1$ tail; in the second, truncate $f$ at height $M$ and use the first case; in the third, $f\ast g$ has compact support by step [](#s3){.pf-ref}. See [[E-LYXHE]].

:::

:::

::: {.pf-step #s4-2}

If $f \in L^1$ and $g$ is smooth with compact support, then $f\ast g$ is smooth and vanishes at infinity.

::: pf-proof

Every $D^\alpha g$ is bounded, so step [](#s5){.pf-ref} applied repeatedly gives $D^\alpha(f\ast g) = f\ast D^\alpha g$, which is continuous by step [](#s2){.pf-ref}. Choose $R$ with $\supp g \subseteq \theset{\norm{y} \le R}$. For $\norm{x} \ge 2R$ and $\norm{y} \le R$, $\norm{x - y} \ge \norm{x}/2$, so
$$
\abs{f\ast g(x)} \le \norm{g}_\infty\int_{\norm{y} \le R}\abs{f(x-y)}\,dy \le \norm{g}_\infty\int_{\norm{u} \ge \norm{x}/2}\abs{f(u)}\,du,
$$
which tends to $0$ as $\norm{x} \to \infty$ because $f \in L^1$.

:::

:::

:::

:::

::: {.pf-step #s5}

If $f \in L^1$ and $g$ is differentiable with $\dd{g}{x_i}$ bounded, then $\dd{}{x_i}(f \ast g) = f \ast \dd{g}{x_i}$.

::: pf-proof

The difference quotient of $f\ast g$ in the direction $e_i$ is $\int f(x-y)\,\frac{g(y + h e_i) - g(y)}{h}\,dy$. By the mean value theorem the quotient of $g$ is bounded by $\sup\abs{\dd{g}{x_i}}$, and it converges pointwise to $\dd{g}{x_i}$, so dominated convergence with dominating function $\sup\abs{\dd{g}{x_i}}\,\abs{f(x-\cdot)}$ applies. See [[E-GQEMZ]].

:::

:::

:::

:::
