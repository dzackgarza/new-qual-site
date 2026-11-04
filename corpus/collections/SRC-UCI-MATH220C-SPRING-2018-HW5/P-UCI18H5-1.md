---
schema: qual/card@1
id: P-UCI18H5-1
kind: problem
title: Product of the multipliers at the two fixed points of a Möbius map
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Suppose $f\in\operatorname{Aut}\widehat{\CC}$ is a linear-fractional transformation that has two distinct fixed points $a$ and $b$.
Prove that $f'(a)f'(b)=1$.
:::

::: {.solution}
For a linear-fractional map $f$ and a Möbius chart $\varphi$, the chain rule in the chart gives $f'(p)=\bigl(\varphi^{-1}\bigr)'\bigl(\varphi(p)\bigr)\,F'\bigl(\varphi(p)\bigr)\,\varphi'(p)$ at a point $p$ where $F=\varphi f\varphi^{-1}$.

::: pf

::: {.pf-step #normal-form}
There is a Möbius chart $\varphi$ with $\varphi(a)=0$ and $\varphi(b)=\infty$, and $F=\varphi f\varphi^{-1}$ satisfies $F(w)=\lambda w$ for some $\lambda\in\CC\setminus\{0,1\}$.

::: pf-proof
Take $\varphi(z)=\frac{z-a}{z-b}$ if $a,b$ are finite; if one of them is $\infty$ take $\varphi(z)=z-a$ or $\varphi(z)=\frac{1}{z-b}$.
Such a $\varphi$ maps $a$ to $0$ and $b$ to $\infty$, and $F$ is a Möbius map fixing both, hence $F(w)=\lambda w$: a Möbius map fixing $0$ has the form $w\mapsto\frac{\alpha w}{\gamma w+\delta}$ with $\delta\ne0$, and fixing $\infty$ forces $\gamma=0$, so $F(w)=\frac{\alpha}{\delta}w$.
Here $\lambda\ne0$ because $F$ is bijective, and $\lambda\ne1$ because $\lambda=1$ would make $F$ the identity and $f$ the identity, which does not have two distinct fixed points.
:::

:::

::: {.pf-step #multipliers}
$F'(0)=\lambda$ and $F'(\infty)=\lambda^{-1}$.

::: pf-proof
The first is immediate from $F(w)=\lambda w$.
In the chart $\zeta=1/w$ at $\infty$ the map $F$ becomes $\zeta\mapsto1/(\lambda/\zeta)=\zeta/\lambda$, whose derivative at $\zeta=0$ is $\lambda^{-1}$.
:::

:::

::: {.pf-step #product}
$f'(a)f'(b)=1$.

::: pf-proof
By the chain rule at $a$, where $\varphi(a)=0$,
$$
f'(a)=\bigl(\varphi^{-1}\bigr)'(0)\,\lambda\,\varphi'(a),
$$
and at $b$, where $\varphi(b)=\infty$ and both derivatives are read in the chart at $\infty$,
$$
f'(b)=\bigl(\varphi^{-1}\bigr)'(\infty)\,\lambda^{-1}\,\varphi'(b).
$$
Multiplying and using step [](#multipliers){.pf-ref}, the product is
$$
\bigl[(\varphi^{-1})'(0)\varphi'(a)\bigr]\bigl[(\varphi^{-1})'(\infty)\varphi'(b)\bigr]\cdot\lambda\lambda^{-1},
$$
and each bracket is $1$, being the derivative of $\varphi^{-1}\circ\varphi$ at $a$ and at $b$ respectively.
Hence $f'(a)f'(b)=1$.
:::

:::

:::

:::
