---
schema: qual/card@1
id: E-YFT35
kind: problem
title: $\FF_{p^n}$ is the splitting field of $x^{p^n}-x$ over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the root set as the unique field of p^n elements.
---

::: {.exercise}
Let $p$ be prime and $n\ge1$. Prove that $\FF_{p^n}$ is the splitting field over $\FF_p$ of
$$
x^{p^n}-x.
$$
:::

::: {.solution}
Let $f(x)=x^{p^n}-x\in\FF_p[x]$.

::: pf

::: {.pf-step #separable}
$f$ has $p^n$ distinct roots in an algebraic closure of $\FF_p$.

::: pf-proof
Its derivative is $f'(x)=p^nx^{p^n-1}-1=-1$, which has no common root with $f$, so all roots of the degree-$p^n$ polynomial $f$ are simple.
:::

:::

::: {.pf-step #splits}
$f$ splits completely over $\FF_{p^n}$.

::: pf-proof
Every $a\in\FF_{p^n}$ satisfies $a^{p^n}=a$: for $a\ne0$ this follows from $\abs{\FF_{p^n}^\times}=p^n-1$ and Lagrange's theorem, and it is trivial for $a=0$.
Thus the $p^n$ elements of $\FF_{p^n}$ are $p^n$ roots of $f$, which by step [](#separable){.pf-ref} are all its roots.
:::

:::

::: pf-step
$\FF_{p^n}$ is the splitting field of $f$ over $\FF_p$.

::: pf-proof
By step [](#splits){.pf-ref}, $f$ splits over $\FF_{p^n}$, and its roots are all elements of $\FF_{p^n}$, so they generate $\FF_{p^n}$ over $\FF_p$.
:::

:::

:::

:::
