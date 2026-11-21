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

No retained solution set covers this exercise: part (a) is proved here rather than referred to another exam question, with the approximation, the uniform-continuity step and the conclusion as separate steps; part (b) applies (a) to the truncation $\chi_{W_{N}}$, which is in $L^{2}$.

::: pf

::: {.pf-step #translations}
(a) For $f\in L^{2}(\RR)$ and $h\in\RR$, $\norm{f(\cdot+h)-f}_{2}\to0$ as $h\to0$.

::: pf-proof
Given $\varepsilon>0$, choose $g$ continuous with compact support and $\norm{f-g}_{2}<\varepsilon/3$, which is possible because such $g$ are dense in $L^{2}(\RR)$. Choose $A\ge1$ with $g$ vanishing off $[-A,A]$; $g$ is uniformly continuous, so there is $\delta>0$ with $\abs{g(x+h)-g(x)}<\varepsilon/(3\sqrt{2A+2})$ whenever $\abs{h}<\delta$ and $x\in\RR$. If $\abs{h}\le1$ then $g(\cdot+h)-g$ vanishes off $[-A-1,A+1]$, a set of measure $2A+2$, so $\norm{g(\cdot+h)-g}_{2}\le\varepsilon/3$ for $\abs{h}<\min\theset{\delta,1}$. Also $\norm{f(\cdot+h)-g(\cdot+h)}_{2}=\norm{f-g}_{2}<\varepsilon/3$, by invariance of Lebesgue measure under translation. Hence $\norm{f(\cdot+h)-f}_{2}<\varepsilon$ for $\abs{h}<\min\theset{\delta,1}$.
:::

:::

::: {.pf-step #apply}
(a) In particular $f_{n}\to f$ in $L^{2}$ for $f_{n}(x)=f(x+x_{n})$ when $x_{n}\to0$.

::: pf-proof
$\norm{f_{n}-f}_{2}=\norm{f(\cdot+x_{n})-f}_{2}\to0$ by step [](#translations){.pf-ref}, since $x_{n}\to0$ and eventually $\abs{x_{n}}<\min\theset{\delta,1}$.
:::

:::

::: {.pf-step #truncate}
(b) For $N$ large the set $W_{N}=W\cap[-N,N]$ has positive finite measure, so $\chi_{W_{N}}\in L^{2}(\RR)$.

::: pf-proof
$W_{N}$ is measurable, bounded and increasing in $N$ with $\bigcup_{N}W_{N}=W$, so $m(W_{N})\to m(W)>0$; choose $N$ with $m(W_{N})>0$. Then $m(W_{N})\le2N<\infty$ and $\int\abs{\chi_{W_{N}}}^{2}=m(W_{N})<\infty$.
:::

:::

::: {.pf-step #norm}
(b) With $f=\chi_{W_{N}}$ and $f_{y}(x)=\chi_{W_{N}}(x+y)$ one has $\norm{f-f_{y}}_{2}^{2}=2m(W_{N})-2\int\chi_{W_{N}}(x)\chi_{W_{N}}(x+y)\,dx$.

::: pf-proof
$(\chi_{W_{N}}(x)-\chi_{W_{N}}(x+y))^{2}=\chi_{W_{N}}(x)+\chi_{W_{N}}(x+y)-2\chi_{W_{N}}(x)\chi_{W_{N}}(x+y)$ pointwise, and $\int\chi_{W_{N}}(x+y)dx=m(W_{N})$ by translation invariance.
:::

:::

::: {.pf-step #small}
For all sufficiently small $y$ the set $W_{N}\cap(W_{N}-y)$ is nonempty.

::: pf-proof
By step [](#norm){.pf-ref} and part (a) — legitimate because $\chi_{W_{N}}\in L^{2}$ by step [](#truncate){.pf-ref} — the function $y\mapsto\norm{f-f_{y}}_{2}^{2}$ is continuous at $0$ and vanishes there, so for $\abs{y}$ small, $2m(W_{N})-2\int\chi_{W_{N}}\chi_{W_{N}}(\cdot+y)<m(W_{N})$, that is $\int\chi_{W_{N}}(x)\chi_{W_{N}}(x+y)dx>m(W_{N})/2>0$. The integrand is a $0$–$1$ function, so its integral is positive exactly when it is positive on a set of positive measure; in particular there is $x$ with $\chi_{W_{N}}(x)\chi_{W_{N}}(x+y)=1$, that is $x\in W_{N}$ and $x+y\in W_{N}$. Then $y=(x+y)-x\in W_{N}-W_{N}$.
:::

:::

::: {.pf-qed}
Part (a) is steps [](#translations){.pf-ref} and [](#apply){.pf-ref}. For part (b): steps [](#truncate){.pf-ref}, [](#norm){.pf-ref} and [](#small){.pf-ref} show that $y\in W_{N}-W_{N}$ for all sufficiently small $y$, and $W_{N}-W_{N}\subseteq W-W$ because $W_{N}\subseteq W$. So $W-W$ contains an interval about the origin, an open neighbourhood of it.
:::

:::

:::
