---
schema: qual/card@1
id: P-R7WPF
kind: problem
title: Examples of local rings
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Valuation Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Do you know an example of a local ring?
Another one?
What about completions?
:::

::: {.solution}
::: pf

::: pf-step
A field $k$ is local with maximal ideal $(0)$.

::: pf-proof
Its only proper ideal is $(0)$.
:::

:::

::: pf-step
For a prime ideal $\mathfrak p$ of a commutative ring $R$, the localization $R_{\mathfrak p}$ is local with maximal ideal $\mathfrak pR_{\mathfrak p}$. For example, $\ZZ_{(p)}$ is local with maximal ideal $p\ZZ_{(p)}$.

::: pf-proof
An element $a/s$ with $a\notin\mathfrak p$ has inverse $s/a$, so every element outside $\mathfrak pR_{\mathfrak p}$ is a unit, and $\mathfrak pR_{\mathfrak p}$ is a proper ideal.
:::

:::

::: pf-step
For a field $k$, the power series ring $k[[x_1,\ldots,x_n]]$ is local with maximal ideal $(x_1,\ldots,x_n)$.

::: pf-proof
A power series $f$ with $f(0)=c\ne0$ is a unit: $f=c(1-g)$ with $g\in(x_1,\ldots,x_n)$, and $\sum_{j\ge0}g^j$ converges formally to $(1-g)^{-1}$. The non-units are exactly the series with zero constant term, which form the ideal $(x_1,\ldots,x_n)$.
:::

:::

::: pf-step
If $(R,\mathfrak m)$ is a local ring, then its $\mathfrak m$-adic completion $\widehat R=\varprojlim R/\mathfrak m^n$ is local with maximal ideal $\ker(\widehat R\to R/\mathfrak m)$. For example, $\ZZ_p=\varprojlim_n\ZZ/p^n\ZZ$, the completion of $\ZZ_{(p)}$, is local with maximal ideal $p\ZZ_p$, and $k[[t]]$ is the completion of $k[t]_{(t)}$.

::: pf-proof
Let $x=(x_n)\in\widehat R$ with $x_1\ne0$ in $R/\mathfrak m$, that is, $x\notin\ker(\widehat R\to R/\mathfrak m)$. Each $x_n$ lies outside $\mathfrak m/\mathfrak m^n$, the unique maximal ideal of the local ring $R/\mathfrak m^n$, so $x_n$ is a unit there. The inverses are compatible under the transition maps, so $x$ is a unit. Hence the non-units form the proper ideal $\ker(\widehat R\to R/\mathfrak m)$.
:::

:::

:::
:::
