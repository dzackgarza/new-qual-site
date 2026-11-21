---
schema: qual/card@1
id: P-JHUFA01RAB
kind: problem
title: Convolution of functions vanishing at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the two facts the argument uses
    without proof: that a continuous f vanishing at both ends is bounded, which also makes h finite
    everywhere; and that the tail integral of an L^1 function tends to zero, by dominated
    convergence. The split of the convolution integral is now its own step with both pieces bounded
    separately, including the estimate |x - y| >= |x| - |y| > A on the inner range for |x| > A + R.
    The degenerate cases M = 0 and g = 0 almost everywhere are one step rather than parentheses. Not
    checked: the printed exam page, which was not re-read in this pass.
---

::: {.problem}
Let $f,g:\RR\to\RR$ be continuous, suppose
$$
\lim_{\abs{x}\to\infty}f(x)=0,
\qquad
\int_{-\infty}^\infty \abs{g(y)}\,dy<\infty,
$$
and define
$$
h(x)=\int_{-\infty}^\infty f(x-y)g(y)\,dy.
$$
Prove that
$$
\lim_{\abs{x}\to\infty}h(x)=0.
$$
:::

::: {.solution}
This is Problem 2 of the JHU real-analysis qualifying examination of Fall 2001, as printed in the retained compilation (`SRC-JHU-ANALYSIS-EXAMS`). No published solution set is transcribed: the argument is the card's own, and it is the standard convolution estimate.

::: pf

::: {.pf-step #bounded}
$f$ is bounded, with $M=\norm{f}_{\infty}<\infty$, and $h(x)$ is defined and finite for every $x$.

::: pf-proof
A continuous function on $\RR$ that tends to $0$ at both ends is bounded: there is $A_{0}$ with $\abs{f}\leq1$ off $[-A_{0},A_{0}]$, and $\abs{f}$ is bounded on the compact interval. Then $\abs{h(x)}\leq M\int\abs{g}<\infty$ by hypothesis on $g$, so the integral defining $h$ converges absolutely and $h$ is finite everywhere.
:::
:::

::: {.pf-step #tail}
For every $\eta>0$ there is $R>0$ with $\int_{\abs{y}>R}\abs{g(y)}\,dy<\eta$.

::: pf-proof
This is absolute continuity of the integral of an $L^{1}$ function: $\int_{\abs{y}>R}\abs g\to0$ as $R\to\infty$ by dominated convergence applied to $\abs{g}\mathbf{1}_{\abs{y}>R}$, which is dominated by $\abs{g}$ and tends to $0$ pointwise.
:::
:::

::: {.pf-step #smallf}
For every $\eta>0$ there is $A>0$ with $\abs{f(z)}<\eta$ whenever $\abs{z}>A$.

::: pf-proof
This is the hypothesis $\lim_{\abs{x}\to\infty}f(x)=0$.
:::
:::

::: {.pf-step #bound}
If $\norm{g}_{1}>0$ and $M>0$, then $\abs{h(x)}<\varepsilon$ for every $x$ with $\abs{x}>A+R$, where $R$ is chosen for $\varepsilon/(2M)$ and $A$ for $\varepsilon/(2\norm{g}_{1})$.

::: pf-proof
Split the integral over $\abs{y}\leq R$ and $\abs{y}>R$. For $\abs{y}\leq R$ and $\abs{x}>A+R$ one has $\abs{x-y}\geq\abs{x}-\abs{y}>A$, so $\abs{f(x-y)}<\varepsilon/(2\norm{g}_{1})$ and the first piece is at most $\frac{\varepsilon}{2\norm{g}_{1}}\int\abs{g}\leq\varepsilon/2$. The second piece is at most $M\int_{\abs{y}>R}\abs{g(y)}\,dy<\varepsilon/2$ by the choice of $R$ and the bound $\abs{f}\leq M$. Adding gives $\abs{h(x)}<\varepsilon$.
:::
:::

::: {.pf-step #degenerate}
If $M=0$ or $g=0$ almost everywhere, then $h\equiv0$.

::: pf-proof
$M=0$ means $f\equiv0$ by continuity, and then $h\equiv0$; if $g=0$ almost everywhere then $h(x)=0$ for every $x$, the integrand vanishing almost everywhere for each fixed $x$.
:::
:::

::: {.pf-step #conclusion}
$\lim_{\abs{x}\to\infty}h(x)=0$.

::: pf-proof
Given $\varepsilon>0$, either step [](#degenerate){.pf-ref} applies and the conclusion is immediate, or steps [](#tail){.pf-ref} and [](#smallf){.pf-ref} supply $R$ and $A$, and step [](#bound){.pf-ref} gives $\abs{h(x)}<\varepsilon$ for $\abs{x}>A+R$. As $\varepsilon$ was arbitrary, $h$ tends to $0$ at infinity.
:::
:::
:::

:::
