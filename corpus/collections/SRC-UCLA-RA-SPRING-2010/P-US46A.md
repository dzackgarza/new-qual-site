---
schema: qual/card@1
id: P-US46A
kind: problem
title: $L^2$ continuity of translations, and $W-W$ contains a neighbourhood of $0$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Measure Theory
  - Continuity
relations: []
review: draft
---

::: {.problem}
a. For $f\in L^2(\RR)$ and a sequence $\{x_n\}\subseteq\RR$ which converges to zero, define $f_n(x):=f(x+x_n)$.
Show that $\{f_n\}$ converges to $f$ in $L^2$.

b. Let $W\subseteq\RR$ be a Lebesgue measurable set of positive Lebesgue measure.
Show that the set of differences $W-W = \{x-y: x,y\in W\}$ contains an open neighborhood of the origin.
:::

::: {.solution}

No retained solution set covers this exercise: part (a) is proved here rather than referred to another exam question, with the approximation, the uniform-continuity step and the conclusion as separate steps; part (b) then uses (a) with $\chi_{W}$.

::: pf

::: {.pf-step #translations}
(a) For $f\in L^{2}(\RR)$ and $h\in\RR$, $\norm{f(\cdot+h)-f}_{2}\to0$ as $h\to0$.

::: pf-proof
Given $\varepsilon>0$, choose $g$ continuous with compact support and $\norm{f-g}_{2}<\varepsilon/3$, which is possible because such $g$ are dense in $L^{2}(\RR)$. Put $K=[-A,A]$ with the support of $g$ inside $K$; $g$ is uniformly continuous, so there is $\delta>0$ with $\abs{g(x+h)-g(x)}<\varepsilon/(3\sqrt{2A+2})$ whenever $\abs{h}<\delta$ and $x\in\RR$. Then $\norm{g(\cdot+h)-g}_{2}\le\varepsilon/3$ for $\abs{h}<\delta$. Also $\norm{f(\cdot+h)-g(\cdot+h)}_{2}=\norm{f-g}_{2}<\varepsilon/3$, by invariance of Lebesgue measure under translation. Hence $\norm{f(\cdot+h)-f}_{2}<\varepsilon$ for $\abs{h}<\delta$.
:::

:::

::: {.pf-step #apply}
(a) In particular $f_{n}\to f$ in $L^{2}$ for $f_{n}(x)=f(x+x_{n})$ when $x_{n}\to0$.

::: pf-proof
$\norm{f_{n}-f}_{2}=\norm{f(\cdot+x_{n})-f}_{2}\to0$ by step [](#translations){.pf-ref}, since $x_{n}\to0$.
:::

:::

::: {.pf-step #norm}
(b) With $f=\chi_{W}$ and $f_{y}(x)=\chi_{W}(x+y)$ one has $\norm{f-f_{y}}_{2}^{2}=2m(W)-2\int\chi_{W}(x)\chi_{W}(x+y)\,dx$.

::: pf-proof
$(\chi_{W}(x)-\chi_{W}(x+y))^{2}=\chi_{W}(x)+\chi_{W}(x+y)-2\chi_{W}(x)\chi_{W}(x+y)$ pointwise, and $\int\chi_{W}(x+y)dx=m(W)$ by translation invariance.
:::

:::

::: {.pf-step #small}
For all sufficiently small $y$ the set $W\cap(W-y)$ is nonempty.

::: pf-proof
By step [](#norm){.pf-ref} and part (a) the function $y\mapsto\norm{f-f_{y}}_{2}^{2}$ is continuous at $0$ and vanishes there, so for $\abs{y}$ small, $2m(W)-2\int\chi_{W}\chi_{W}(\cdot+y)<m(W)$, that is $\int\chi_{W}(x)\chi_{W}(x+y)dx>m(W)/2>0$. The integrand is a $0$–$1$ function, so its integral is positive exactly when it is positive on a set of positive measure; in particular there is $x$ with $\chi_{W}(x)\chi_{W}(x+y)=1$, that is $x\in W$ and $x+y\in W$, so $y=x-(x+y)\in W-W$ with the sign convention $W-W=\theset{u-v}$.
:::

:::

::: {.pf-qed}
Part (a) is steps [](#translations){.pf-ref} and [](#apply){.pf-ref}; part (b) follows from steps [](#norm){.pf-ref} and [](#small){.pf-ref}: $W-W$ contains the interval of all sufficiently small $y$, an open neighbourhood of the origin.
:::

:::

:::
