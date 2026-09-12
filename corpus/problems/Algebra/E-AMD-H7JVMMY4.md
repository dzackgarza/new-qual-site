---
schema: qual/card@1
id: E-AMD-H7JVMMY4
kind: problem
title: Algebraicity of $\alpha\pm\beta$ and $\alpha\beta^{\pm 1}$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $\alpha, \beta$ are algebraic over $F$, then $\alpha\pm \beta, \alpha\beta$, and $\alpha\beta^{-1}$ (for $\beta \neq 0$) are all algebraic over $F$.
:::

::: {.solution}
Since $\alpha$ and $\beta$ are algebraic over $F$, the extension
\[
F(\alpha,\beta)/F
\]
is finite. Indeed,
\[
[F(\alpha,\beta):F]
=[F(\alpha,\beta):F(\alpha)]\,[F(\alpha):F]<\infty.
\]
Every element of a finite extension is algebraic over the base field.

Now $F(\alpha,\beta)$ is a field containing
\[
\alpha+\beta,\quad \alpha-\beta,\quad \alpha\beta,
\]
and, when $\beta\ne0$,
\[
\alpha\beta^{-1}.
\]
Hence all these elements are algebraic over $F$.
:::
