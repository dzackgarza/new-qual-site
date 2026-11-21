---
schema: qual/card@1
id: P-CAF13C
kind: problem
title: 'A holomorphic $f$ with $\abs f\leq 1$ on $\partial\DD$ and no fixed point there has exactly one fixed point in $\DD$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that for t < 1 the homotopy tf - z has |tf| <=
    t < 1 = |-z| on the circle so Rouche gives exactly one zero in the disk, that h_1 = f -
    z has a positive minimum modulus delta on the circle by compactness, that on a small
    interval [1 - eps, 1] the perturbed functions keep no boundary zeros and the argument-
    principle integral is continuous and integer-valued hence constant, and therefore that
    the count at t = 1 is 1. Repair: the earlier prose said the count is constant in t by
    the argument principle without handling the endpoint t = 1, where Rouche's strict
    inequality is unavailable; the endpoint is now covered. The argument is the card's own;
    no retained set is cited.
---

::: {.problem}
Let $f$ be holomorphic on a neighborhood of the closed unit disk $\overline{\DD}$.
Suppose $\sup_{z \in \partial\DD} \abs{f(z)} \leq 1$, and that $f$ has no fixed points on the boundary $\partial\DD$ ($f(z) \ne z$ for all $\abs{z} = 1$).
Prove that $f$ has **exactly one fixed point** in the open unit disk $\DD$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. For $0\le t\le1$ put $h_{t}(z)=tf(z)-z$, holomorphic on a neighbourhood of $\overline{\DD}$ because $f$ is.

::: pf

::: {.pf-step #interior}
For $0\le t<1$ and $\abs{z}=1$ one has $\abs{tf(z)}\le t<1=\abs{z}$; hence $h_{t}$ has no zero on $\partial\DD$ and, by Rouché's theorem, exactly one zero in $\DD$ counted with multiplicity.

::: pf-proof
$\abs{f(z)}\le1$ on $\partial\DD$ by hypothesis, so $\abs{tf(z)}\le t<1=\abs{-z}$ for $t<1$. Rouché's theorem then says that $h_{t}=(-z)+tf$ and $-z$ have the same number of zeros in $\DD$ counted with multiplicity, and $-z$ has the single simple zero $z=0$ there. In particular $h_{t}$ has no zero on $\partial\DD$, since $\abs{-z}>\abs{tf(z)}$ there.
:::

:::

::: {.pf-step #boundary}
$h_{1}=f-z$ has no zero on $\partial\DD$, and there is $\delta>0$ with $\abs{h_{1}(z)}\ge\delta$ for $\abs{z}=1$.

::: pf-proof
$h_{1}(z)\ne0$ for $\abs{z}=1$ is the hypothesis that $f$ has no fixed point on the boundary, and $z\mapsto\abs{h_{1}(z)}$ is continuous and positive on the compact circle $\abs{z}=1$, so it attains a positive minimum $\delta$.
:::

:::

::: {.pf-step #near-one}
There is $\varepsilon>0$ such that the number of zeros of $h_{t}$ in $\DD$, counted with multiplicity, is the same for every $t\in[1-\varepsilon,1]$.

::: pf-proof
Let $M=\sup_{\abs{z}=1}\abs{f(z)}\le1$ and let $\varepsilon>0$ satisfy $(1-\varepsilon)M<\delta$ with $\delta$ as in step [](#boundary){.pf-ref}. For $\abs{z}=1$ and $1-\varepsilon\le t\le1$,
$$
\abs{h_{t}(z)}=\abs{h_{1}(z)-(1-t)f(z)}\ge\delta-(1-t)M\ge\delta-(1-\varepsilon)M>0,
$$
so no $h_{t}$ with $t$ in that interval has a zero on $\partial\DD$. The number of zeros in $\DD$ of $h_{t}$, counted with multiplicity, is $\frac{1}{2\pi i}\oint_{\abs{z}=1}\frac{h_{t}'(z)}{h_{t}(z)}dz$ by the argument principle, and this integral is a continuous function of $t$ on the interval, because the integrand is continuous in $(t,z)$ with a denominator bounded away from $0$ there; being integer-valued and continuous, it is constant.
:::

:::

::: {.pf-step #count}
$h_{1}=f-z$ has exactly one zero in $\DD$, counted with multiplicity.

::: pf-proof
By steps [](#interior){.pf-ref} and [](#near-one){.pf-ref}, the count is $1$ for every $t<1$ and is constant on $[1-\varepsilon,1]$, so its value at $t=1$ is that same constant, namely $1$.
:::

:::

::: {.pf-step}
$f$ has exactly one fixed point in $\DD$.

::: pf-proof
A fixed point of $f$ in $\DD$ is a zero of $h_{1}=f-z$ there. Step [](#count){.pf-ref} says there is exactly one such zero counted with multiplicity, that is exactly one zero, and it is simple.
:::

:::

:::
:::
