---
schema: qual/card@1
id: P-JHUFA01RAA
kind: problem
title: Uniform continuity of continuous functions with limit at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f$ be continuous on $[0,\infty)$ and suppose the finite limit
$$
L=\lim_{x\to\infty}f(x)
$$
exists. Prove that $f$ is uniformly continuous on $[0,\infty)$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the tail, the compact piece and the bookkeeping on $\delta$ as separate steps.

Let $f$ be continuous on $[0,\infty)$ with $\lim_{x\to\infty}f(x)=L$.

::: pf

::: {.pf-step #tail}
For every $\varepsilon>0$ there is $R>0$ such that $\abs{f(x)-f(y)}<\varepsilon$ whenever $x,y\ge R$.

::: pf-proof
Choose $R$ with $\abs{f(x)-L}<\varepsilon/2$ for $x\ge R$, which is possible since $f(x)\to L$. Then for $x,y\ge R$ the triangle inequality gives $\abs{f(x)-f(y)}\le\abs{f(x)-L}+\abs{f(y)-L}<\varepsilon$.
:::

:::

::: {.pf-step #compact}
On $[0,R+1]$ the function $f$ is uniformly continuous.

::: pf-proof
$[0,R+1]$ is compact and $f$ is continuous there, so Heine–Cantor applies: there is $\delta_{0}>0$ such that $\abs{x-y}<\delta_{0}$ with $x,y\in[0,R+1]$ implies $\abs{f(x)-f(y)}<\varepsilon$.
:::

:::

::: {.pf-step #bookkeeping}
With $\delta=\min\theset{1,\delta_{0}}$, any $x,y\ge0$ with $\abs{x-y}<\delta$ satisfy $\abs{f(x)-f(y)}<\varepsilon$.

::: pf-proof
If both $x,y\ge R$ this is the tail estimate of step [](#tail){.pf-ref}. If both $x,y\le R+1$ it is step [](#compact){.pf-ref}. The remaining possibility, say $x<R$ and $y>R+1$, is impossible: then $\abs{x-y}>R+1-R=1\ge\delta$. So one of the two cases always applies.
:::

:::

::: {.pf-qed}
For every $\varepsilon>0$ a $\delta>0$ has been produced that works for all $x,y\ge0$, so $f$ is uniformly continuous on $[0,\infty)$.
:::

:::

:::
