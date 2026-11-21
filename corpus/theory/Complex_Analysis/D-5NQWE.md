---
schema: qual/card@1
id: D-5NQWE
kind: definition
title: Rising and falling factorials
prompts:
- What are the rising and falling factorials?
classification:
  areas:
  - complex-analysis
  topics:
  - Factorials
  - Power Series
relations: []
review: draft
---

::: {.definition}
For $n\in\CC$ and $k\in\ZZ_{\geq0}$, the \dfn{rising factorial} is
$$
\rising{n}{k}\coloneqq n(n+1)(n+2)\cdots(n+k-1),
$$
and the \dfn{falling factorial} is
$$
\falling{n}{k}\coloneqq n(n-1)(n-2)\cdots(n-k+1);
$$
each is a product of $k$ factors, and the empty product for $k=0$ is $1$.
:::

::: {.remark}
For $n\in\ZZ_{>0}$ the rising factorial is $\rising{n}{k} = (n+k-1)!/(n-1)!$, and for $0\leq k\leq n$ the falling factorial is $\falling{n}{k} = n!/(n-k)!$.
In terms of the [[D-Q3MYK|Gamma function]] they read $\Gamma(n+k)/\Gamma(n)$ and $\Gamma(n+1)/\Gamma(n-k+1)$.
:::
