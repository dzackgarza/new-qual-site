---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W3
kind: problem
title: An epsilon-delta proof for the cube-root function
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Give an $\varepsilon$-$\delta$ proof that $f(x)=x^{1/3}$ is continuous on $[0,1]$.

(You may also wish to try this for $f(x)=\sqrt{x}$ and/or on the interval $[0,\infty)$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $f(x)=x^{1/3}$ is continuous at $0$.

::: pf-proof

Given $\varepsilon>0$, choose $\delta=\varepsilon^3$. For $x\in[0,1]$ with $\abs{x-0}<\delta$, one has
$$
\abs{f(x)-f(0)}=x^{1/3}<\delta^{1/3}=\varepsilon.
$$

:::

:::

::: {.pf-step #s2}

The function $f$ is continuous at each $a\in(0,1]$.

::: pf-proof

Fix $a>0$ and $\varepsilon>0$, and take $\delta=\varepsilon a^{2/3}$. For $x\in[0,1]$, factorization of $x-a$ as a difference of cubes gives
$$
\abs{f(x)-f(a)}
=\frac{\abs{x-a}}{x^{2/3}+x^{1/3}a^{1/3}+a^{2/3}}
\leq\frac{\abs{x-a}}{a^{2/3}}.
$$
The denominator is positive because $a>0$. Whenever $\abs{x-a}<\delta$, the displayed bound is strictly less than $\varepsilon$.

:::

:::

::: pf-qed

Every point of $[0,1]$ is either $0$, covered by step [](#s1){.pf-ref}, or lies in $(0,1]$, covered by step [](#s2){.pf-ref}. Hence $f$ is continuous on $[0,1]$.

:::

:::

:::
