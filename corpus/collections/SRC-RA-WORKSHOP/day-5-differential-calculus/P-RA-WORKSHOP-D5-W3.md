---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-W3
kind: problem
title: A nonzero derivative gives local injectivity
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
([KRD10, Exercise 6.2.B]) If $f:(a,b)\to\mathbb R$ is continuously differentiable and $f'(x_0)\ne0$ for some $x_0\in(a,b)$, then $f$ is injective on some interval $(c,d)$ containing $x_0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There exist $a<c<x_0<d<b$ such that $f'$ has constant strict sign on $(c,d)$.

::: pf-proof

Since $f'(x_0)\ne0$ and $f'$ is continuous at $x_0$, there is $\delta>0$ with $[x_0-\delta,x_0+\delta]\subset(a,b)$ and
\[
|f'(x)-f'(x_0)|<\tfrac12|f'(x_0)|
\quad\text{whenever }|x-x_0|<\delta.
\]
Set $c=x_0-\delta$ and $d=x_0+\delta$. If $f'(x_0)>0$, then $f'(x)>f'(x_0)/2>0$ throughout $(c,d)$. If $f'(x_0)<0$, then $f'(x)<f'(x_0)/2<0$ throughout $(c,d)$.

:::

:::

::: {.pf-step #s2}

The restriction $f|_{(c,d)}$ is strictly monotone.

::: pf-proof

For any $c<u<v<d$, the mean value theorem gives $\xi\in(u,v)$ such that
\[
f(v)-f(u)=f'(\xi)(v-u).
\]
By step [](#s1){.pf-ref}, the right-hand side has the same nonzero sign for every such pair $u<v$. Hence $f$ is strictly increasing when $f'(x_0)>0$ and strictly decreasing when $f'(x_0)<0$.

:::

:::

::: {.pf-step #s3}

The function $f$ is injective on $(c,d)$.

::: pf-proof

If $u,v\in(c,d)$ are distinct, order them so that $u<v$. Strict monotonicity from step [](#s2){.pf-ref} gives $f(u)\ne f(v)$.

:::

:::

::: pf-qed

The interval supplied by step [](#s1){.pf-ref} contains $x_0$, and step [](#s3){.pf-ref} establishes injectivity on it.

:::

:::

:::
