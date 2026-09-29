---
schema: qual/card@1
id: P-YBT6I
kind: problem
title: 'Convolutions of $L^2$ functions and convolution operators on $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
7. Let

$$
f \ast g ( x ) : = \int _ { - \infty } ^ { + \infty } f ( y ) g ( x - y ) d y
$$

denote the convolution of f and $g .$

(a) Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ be two square-integrable functions on R (with the usual Lebesgue measure).
Show that the convolution $f * g$ bounded continuous function on R.

(b) Instead let $h \in L ^ { 1 } ( \mathbb { R } )$ be fixed.
Show that $A ( f ) = f * h$ is a bounded operator $L ^ { 1 } ( \mathbb { R } ) \to L ^ { 1 } ( \mathbb { R } )$
:::

::: {.solution}
Write $\tau_hg(y)\da g(y-h)$ and $\norm\cdot_p$ for the $L^p(\RR)$ norm.

::: pf

::: {.pf-step #convolution-bounded}
(a) For $f,g\in L^2$, $\abs{(f\ast g)(x)}\le\norm f_2\norm g_2$ for every $x$.

::: pf-proof
By the Cauchy--Schwarz inequality, $\abs{\int f(y)g(x-y)\,dy}\le\norm f_2\norm{g(x-\cdot)}_2=\norm f_2\norm g_2$.
:::

:::

::: {.pf-step #convolution-continuous}
(a) $f\ast g$ is continuous.

::: pf-proof
By the Cauchy--Schwarz inequality, $\abs{(f\ast g)(x+h)-(f\ast g)(x)}\le\norm f_2\norm{\tau_{-h}g-g}_2$, which tends to $0$ as $h\to0$ by continuity of translation in $L^2$ [@Fol13].
:::

:::

::: {.pf-step #convolution-operator-bounded}
(b) For $f,h\in L^1$, $\norm{f\ast h}_1\le\norm f_1\norm h_1$, so $A$ is a bounded operator on $L^1$ with $\norm A\le\norm h_1$.

::: pf-proof
By Tonelli's theorem, $\int\abs{(f\ast h)(x)}\,dx\le\iint\abs{f(y)}\abs{h(x-y)}\,dy\,dx=\norm f_1\norm h_1$. The map $A$ is linear, so this bound makes it bounded.
:::

:::

::: pf-qed
Steps [](#convolution-bounded){.pf-ref} and [](#convolution-continuous){.pf-ref} prove part (a), and step [](#convolution-operator-bounded){.pf-ref} proves part (b).
:::

:::
:::
