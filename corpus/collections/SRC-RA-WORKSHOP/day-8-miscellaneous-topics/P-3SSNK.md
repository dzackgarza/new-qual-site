---
schema: qual/card@1
id: P-3SSNK
kind: problem
title: Riemann–Stieltjes integral against a jump at $0$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 2014 1)Define $\alpha \colon [-1,1] \to \RR$ by $$\alpha(x) \coloneqq \begin{cases} -1 & x \in [-1,0] \\ 1 & x \in (0,1]. \end{cases}$$ Let $f \colon [-1,1] \to \RR$ be a function that is uniformly bounded on $[-1,1]$ and continuous at $x=0$, but not necessarily continuous for $x \neq 0$.
Prove that $f$ is Riemann-Stieltjes integrable with respect to $\alpha$ over $[-1,1]$ and that $$\int_{-1}^1 f(x)d\alpha(x) = 2f(0).$$
:::

::: {.solution}

For a partition $P=(-1=x_0<\cdots<x_m=1)$, let $j$ be the unique index with $x_{j-1}\leq0<x_j$, and write $I_j=[x_{j-1},x_j]$.

::: pf

::: {.pf-step #s2}

$U(f,P,\alpha)=2\sup_{I_j}f$ and $L(f,P,\alpha)=2\inf_{I_j}f$.

::: pf-proof

The function $\alpha$ is increasing. Its values at both endpoints of every subinterval other than $I_j$ agree, whereas $\alpha(x_j)-\alpha(x_{j-1})=1-(-1)=2$. So only $I_j$ contributes to the upper and lower sums. The suprema and infima are finite because $f$ is bounded.

:::

:::

::: {.pf-step #s3}

For every $\varepsilon>0$ there is $\delta>0$ such that every partition $P$ of mesh less than $\delta$ satisfies $2f(0)-\varepsilon\le L(f,P,\alpha)\le U(f,P,\alpha)\le 2f(0)+\varepsilon$.

::: pf-proof

Continuity of $f$ at zero gives $\delta>0$ such that $\abs{f(t)-f(0)}<\varepsilon/2$ whenever $\abs{t}<\delta$. If the mesh is less than $\delta$, then $I_j\subset(-\delta,\delta)$, because $I_j$ contains $0$ and has length less than $\delta$. Therefore $f(0)-\varepsilon/2\le\inf_{I_j}f\le\sup_{I_j}f\le f(0)+\varepsilon/2$, and step [](#s2){.pf-ref} gives the bounds.

:::

:::

::: pf-step

$f$ is Riemann–Stieltjes integrable with respect to $\alpha$ and $\int_{-1}^1 f(x)\,d\alpha(x)=2f(0)$.

::: pf-proof

By step [](#s3){.pf-ref}, for every $\varepsilon>0$ some partition has $U(f,P,\alpha)-L(f,P,\alpha)\le2\varepsilon$, so the Darboux criterion gives integrability. The integral lies between $L(f,P,\alpha)$ and $U(f,P,\alpha)$ for every $P$, so it lies in $[2f(0)-\varepsilon,2f(0)+\varepsilon]$ for every $\varepsilon>0$, hence equals $2f(0)$.

:::

:::

:::

:::
