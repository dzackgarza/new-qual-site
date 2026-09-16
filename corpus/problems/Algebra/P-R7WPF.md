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
Standard examples of local rings include:

- any field, with maximal ideal $(0)$;
- a localization $R_{\mathfrak m}$ at a maximal ideal, whose maximal ideal is $\mathfrak mR_{\mathfrak m}$;
- a discrete valuation ring such as $\mathbb Z_{(p)}$ or $k[[t]]$;
- the formal power-series ring $k[[x_1,\dots,x_n]]$, whose maximal ideal is $(x_1,\dots,x_n)$.

If $(R,\mathfrak m)$ is local, its $\mathfrak m$-adic completion
\[
\widehat R=\varprojlim R/\mathfrak m^n
\]
is again local, with maximal ideal the kernel of $\widehat R\to R/\mathfrak m$. For example,
\[
\mathbb Z_p=\varprojlim_n\mathbb Z/p^n\mathbb Z
\]
is the $p$-adic completion of $\mathbb Z_{(p)}$ and is local with maximal ideal $p\mathbb Z_p$.
:::
