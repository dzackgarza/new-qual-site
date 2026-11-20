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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. The key inequality for cube roots is
    |u^(1/3) - v^(1/3)|^3 <= |u - v|, which holds because (a - b)(a^2 + ab + b^2) = a^3 - b^3 with
    a = u^(1/3), b = v^(1/3) and the second factor at least b^2 >= 0 gives |a - b| |a^2 + ab + b^2|
    = |a^3 - b^3| with |a^2 + ab + b^2| >= |a-b|^2 ... in any case taking delta = eps^3 gives
    |x - a| < delta => |x^(1/3) - a^(1/3)| < eps uniformly on [0,1], with no separate treatment of
    a = 0 needed. Checked that uniformity in a is what makes this a proof of continuity on the whole
    interval rather than at a point.
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
