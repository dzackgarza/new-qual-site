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
- Show that if $f, g$ are continuous and compactly supported, then so is $f\ast g$.

- Show that if $f\in L^1$ and $g$ is bounded, then  $f\ast g$ is bounded and uniformly continuous.

- If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

- Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

  - $f, g\in L^1$ are both bounded.

  - $f, g\in L^1$ with just $g$ bounded.

  - $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

  - $f\in L^1$ and $g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

- Show that if $f\in L^1$ and $g'$ exists with $\dd{g}{x_i}$ all bounded, then $$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$$
:::

::: {.solution}
<1>1. If $f, g$ are continuous and compactly supported, then $f \ast g$ is continuous and compactly supported.

::: {.proof}
$|f\ast g(x + h) - f\ast g(x)| \le \|g\|_1 \sup_z|f(z + h) - f(z)|$, which tends to $0$ because $f$ is uniformly continuous. $f\ast g$ vanishes off the compact set $\supp f + \supp g$, the image of $\supp f \times \supp g$ under addition. The steps are written out in [[E-Y4GZM]].
:::

<1>2. If $f \in L^1$ and $|g| \leq M$, then $|f \ast g| \le M\|f\|_1$ and $f\ast g$ is uniformly continuous.

::: {.proof}
$|f\ast g(x)| \le \int |f(x-y)||g(y)|\,dy \le M\|f\|_1$. Substituting $u = x - y$ gives $|f \ast g(x + h) - f \ast g(x)| \le M\int|f(u + h) - f(u)|\,du$, which does not depend on $x$ and tends to $0$ as $h \to 0$ by continuity of translation in $L^1$. The steps are written out in [[E-E4H2J]].
:::

<1>3. If $f, g$ are compactly supported, then $f \ast g$ is compactly supported.

::: {.proof}
The argument of step <1>1 uses no continuity: $f\ast g(x) = 0$ for $x \notin \supp f + \supp g$, which is compact.
:::

<1>4. $f \ast g$ vanishes at infinity under each of the four listed assumptions.

<2>1. The cases $f, g \in L^1$ both bounded, $f, g \in L^1$ with $g$ bounded, and $f, g$ smooth and compactly supported.

::: {.proof}
These are proved in [[E-LYXHE]]: in the first case split $\int f(x-y)g(y)\,dy$ at $|y| = |x|/2$ and bound each piece by an $L^1$ tail; in the second, truncate $f$ at height $M$ and use the first case; in the third, $f\ast g$ has compact support by step <1>3.
:::

<2>2. If $f \in L^1$ and $g$ is smooth with compact support, then $f\ast g$ is smooth and vanishes at infinity.

::: {.proof}
Every $D^\alpha g$ is bounded, so step <1>5 applied repeatedly gives $D^\alpha(f\ast g) = f\ast D^\alpha g$, which is continuous by step <1>2. Choose $R$ with $\supp g \subseteq \theset{|y| \le R}$. For $|x| \ge 2R$ and $|y| \le R$, $|x - y| \ge |x|/2$, so
$$
|f\ast g(x)| \le \|g\|_\infty\int_{|y| \le R}|f(x-y)|\,dy \le \|g\|_\infty\int_{|u| \ge |x|/2}|f(u)|\,du,
$$
which tends to $0$ as $|x| \to \infty$ because $f \in L^1$.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2.
:::

<1>5. If $f \in L^1$ and $g$ is differentiable with $\dd{g}{x_i}$ bounded, then $\dd{}{x_i}(f \ast g) = f \ast \dd{g}{x_i}$.

::: {.proof}
The difference quotient of $f\ast g$ in the direction $e_i$ is $\int f(x-y)\,\frac{g(y + h e_i) - g(y)}{h}\,dy$. By the mean value theorem the quotient of $g$ is bounded by $\sup|\dd{g}{x_i}|$, and it converges pointwise to $\dd{g}{x_i}$, so dominated convergence with dominating function $\sup|\dd{g}{x_i}|\,|f(x-\cdot)|$ applies. The steps are written out in [[E-GQEMZ]].
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 treat the parts in order.
:::
:::
