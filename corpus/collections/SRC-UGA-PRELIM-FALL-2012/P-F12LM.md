---
schema: qual/card@1
id: P-F12LM
kind: problem
title: $\varepsilon$-$\delta$ proof that $\lim_{x\to 2} 1/(x^2+1)=1/5$
classification:
  areas:
  - prelim
  topics:
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give an $\varepsilon$-$\delta$ proof that $\lim_{x \to 2} \frac{1}{x^2 + 1} = \frac{1}{5}$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own $\varepsilon$-$\delta$ estimate follows, with the algebraic identity, the boundedness on a restricted range and the choice of $\delta$ as separate steps.

::: pf

::: {.pf-step #identity}
$\abs{\dfrac{1}{x^{2}+1}-\dfrac{1}{5}}=\dfrac{\abs{x-2}\,\abs{x+2}}{5(x^{2}+1)}$.

::: pf-proof
Combining the fractions, $\dfrac{1}{x^{2}+1}-\dfrac15=\dfrac{5-(x^{2}+1)}{5(x^{2}+1)}=\dfrac{4-x^{2}}{5(x^{2}+1)}$, and $4-x^{2}=-(x-2)(x+2)$, so the absolute value is $\dfrac{\abs{x-2}\abs{x+2}}{5(x^{2}+1)}$ since $x^{2}+1>0$.
:::

:::

::: {.pf-step #near-two}
If $\abs{x-2}<1$ then $1<x<3$, hence $\abs{x+2}<5$, $x^{2}+1>2$, and $\abs{\dfrac{1}{x^{2}+1}-\dfrac15}<\dfrac12\abs{x-2}$.

::: pf-proof
$\abs{x-2}<1$ gives $1<x<3$; then $3<x+2<5$ so $\abs{x+2}<5$, and $x^{2}+1>1+1=2$ so $\dfrac{1}{5(x^{2}+1)}<\dfrac{1}{10}$. Multiplying the two bounds, the expression of step [](#identity){.pf-ref} is less than $\abs{x-2}\cdot\dfrac{5}{10}=\dfrac12\abs{x-2}$.
:::

:::

::: {.pf-step #delta}
For $\varepsilon>0$ put $\delta=\min\theset{1,2\varepsilon}$; then $0<\abs{x-2}<\delta$ implies $\abs{\dfrac{1}{x^{2}+1}-\dfrac15}<\varepsilon$.

::: pf-proof
Such an $x$ satisfies $\abs{x-2}<1$, so step [](#near-two){.pf-ref} applies and gives the error $<\tfrac12\abs{x-2}<\tfrac12\delta\le\tfrac12\cdot2\varepsilon=\varepsilon$.
:::

:::

::: {.pf-qed}
For every $\varepsilon>0$ a $\delta>0$ has been produced with the required property, so $\lim_{x\to2}\dfrac{1}{x^{2}+1}=\dfrac15$.
:::

:::

:::
