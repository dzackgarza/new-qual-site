---
schema: qual/card@1
id: P-BKF18-2A
kind: problem
title: A differential inequality with $f(0)=0$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose $f:\RR\to\RR$ is differentiable and satisfies $f'(x)>f(x)$ for all real $x$.
Show that if $f(0)=0$, then $f(x)>0$ for all $x>0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is $t>0$ such that $f>0$ on $(0,t)$.

::: pf-proof

$f'(0)>f(0)=0$. Since $f(x)/x\to f'(0)>0$ as $x\to0^+$, there is $t>0$ with $f(x)/x>0$ for $0<x<t$.

:::

:::

::: {.pf-step #s2}

$f(x)>0$ for all $x>0$.

::: pf-proof

Suppose the set $Z=\{x>0: f(x)\le0\}$ is not empty, and let $x_0=\inf Z$. By step [](#s1){.pf-ref}, $x_0\ge t>0$. Points of $Z$ approach $x_0$ and $f$ is continuous, so $f(x_0)\le0$. By the definition of $x_0$, $f>0$ on $(0,x_0)$. Then $f'>f>0$ on $(0,x_0)$. By the mean value theorem, $f(x_0)-f(0)=x_0f'(\xi)$ for some $\xi\in(0,x_0)$, so $f(x_0)>0$. This is a contradiction.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} is the claim.

:::

:::

:::
