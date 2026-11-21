---
schema: qual/card@1
id: P-F12FE
kind: problem
title: $f(xy)=xf(y)+yf(x)$ implies $f(1)=0$ and $f(u^n)=n u^{n-1}f(u)$
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose $f: \RR \to \RR$ satisfies $f(xy) = xf(y) + yf(x)$ for all $x, y \in \RR$.
Prove that $f(1) = 0$ and that $f(u^n) = n u^{n-1} f(u)$ for all $n \in \NN$ and $u \in \RR$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the value at $1$ and the induction as separate steps and the identity's two terms named.

::: pf

::: {.pf-step #at-one}
$f(1)=0$.

::: pf-proof
Putting $x=y=1$ in $f(xy)=xf(y)+yf(x)$ gives $f(1)=1\cdot f(1)+1\cdot f(1)=2f(1)$, so $f(1)=0$ in $\RR$.
:::

:::

::: {.pf-step #induction}
$f(u^{n})=nu^{n-1}f(u)$ for every $n\ge1$ and every $u\in\RR$.

:::: {.pf-proof}

::: {.pf-step #base}
The formula holds for $n=1$.

::: pf-proof
$1\cdot u^{0}f(u)=f(u)=f(u^{1})$.
:::

:::

::: {.pf-step #step}
If it holds for $n$, it holds for $n+1$.

::: pf-proof
Apply $f(xy)=xf(y)+yf(x)$ with $x=u^{n}$ and $y=u$: $f(u^{n+1})=u^{n}f(u)+uf(u^{n})$. By the induction hypothesis $uf(u^{n})=u\cdot nu^{n-1}f(u)=nu^{n}f(u)$, so $f(u^{n+1})=(n+1)u^{n}f(u)$.
:::

:::

::::

:::

::: {.pf-qed}
$f(1)=0$ by step [](#at-one){.pf-ref}, and $f(u^{n})=nu^{n-1}f(u)$ for all $n\in\NN$ and $u\in\RR$ by the induction of step [](#induction){.pf-ref}.
:::

:::

:::
