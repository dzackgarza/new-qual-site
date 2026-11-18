---
schema: qual/card@1
id: P-F07LM
kind: problem
title: $\delta$-$\varepsilon$ definition of a limit, and $\lim_{x\to 1} 1/(1+x^2)=1/2$
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
(a) Complete the $\delta$-$\varepsilon$ definition of a limit: Given a function $f: \RR \to \RR$ and $a, L \in \RR$, $\lim_{x \to a} f(x) = L$ means ...

(b) Using the definition, prove that $\lim_{x \to 1} \frac{1}{1 + x^2} = \frac{1}{2}$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own completion of the definition and its $\varepsilon$-$\delta$ proof follow, with the definition, the algebraic identity, the bound near $1$ and the choice of $\delta$ as separate steps.

::: pf

::: {.pf-step #definition}
(a) $\displaystyle\lim_{x\to a}f(x)=L$ means: for every $\varepsilon>0$ there is $\delta>0$ such that $0<\abs{x-a}<\delta$ implies $\abs{f(x)-L}<\varepsilon$.

::: pf-proof
This is the definition of the limit of a real function at a point; the strict inequality $0<\abs{x-a}$ records that the value of $f$ at $a$ itself is irrelevant, and the conclusion has to hold for every $\varepsilon>0$.
:::

:::

::: {.pf-step #identity}
(b) $\abs{\dfrac{1}{1+x^{2}}-\dfrac12}=\dfrac{\abs{x-1}\abs{x+1}}{2(1+x^{2})}$.

::: pf-proof
$\dfrac{1}{1+x^{2}}-\dfrac12=\dfrac{2-(1+x^{2})}{2(1+x^{2})}=\dfrac{1-x^{2}}{2(1+x^{2})}$, and $1-x^{2}=-(x-1)(x+1)$; taking absolute values gives the identity, since $2(1+x^{2})>0$.
:::

:::

::: {.pf-step #near-one}
If $\abs{x-1}<1$ then $\abs{\dfrac{1}{1+x^{2}}-\dfrac12}\le\dfrac32\abs{x-1}$.

::: pf-proof
$\abs{x-1}<1$ gives $0<x<2$, hence $\abs{x+1}<3$ and $1+x^{2}\ge1$, so $\dfrac{\abs{x+1}}{2(1+x^{2})}\le\dfrac{3}{2}$; multiply by $\abs{x-1}$ and apply step [](#identity){.pf-ref}.
:::

:::

::: {.pf-step #delta}
(b) With $\delta=\min\theset{1,\tfrac{2\varepsilon}{3}}$, $0<\abs{x-1}<\delta$ implies $\abs{\dfrac{1}{1+x^{2}}-\dfrac12}<\varepsilon$.

::: pf-proof
Such an $x$ satisfies $\abs{x-1}<1$, so step [](#near-one){.pf-ref} gives the bound $\tfrac32\abs{x-1}<\tfrac32\delta\le\tfrac32\cdot\tfrac{2\varepsilon}{3}=\varepsilon$, using $\delta\le\frac{2\varepsilon}{3}$.
:::

:::

::: {.pf-qed}
Part (a) is step [](#definition){.pf-ref} and part (b) is steps [](#delta){.pf-ref} with [](#near-one){.pf-ref} and [](#identity){.pf-ref}: for every $\varepsilon>0$ a suitable $\delta$ exists, so $\lim_{x\to1}\dfrac{1}{1+x^{2}}=\dfrac12$.
:::

:::

:::
