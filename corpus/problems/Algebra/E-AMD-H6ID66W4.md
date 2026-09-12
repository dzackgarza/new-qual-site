---
schema: qual/card@1
id: E-AMD-H6ID66W4
kind: problem
title: $\ff(R[t])=\ff(R)(t)$
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Polynomials
  - Integral Domains
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
Show that $\operatorname{Frac}(R[t]) \cong \operatorname{Frac}(R)(t)$ for any integral domain $R$.
:::

::: {.solution}
Let
\[
K=\operatorname{Frac}(R).
\]
Since $R[t]\subseteq K[t]$, there is an inclusion
\[
\operatorname{Frac}(R[t])\subseteq K(t).
\]

Conversely, let $P/Q\in K(t)$ with $P,Q\in K[t]$ and $Q\ne0$. Choose a nonzero $d\in R$ clearing all denominators of the coefficients of both $P$ and $Q$. Then
\[
dP,dQ\in R[t],\qquad dQ\ne0,
\]
and
\[
\frac{P}{Q}=\frac{dP}{dQ}\in\operatorname{Frac}(R[t]).
\]
Hence
\[
\boxed{\operatorname{Frac}(R[t])=K(t)=\operatorname{Frac}(R)(t).}
\]
:::
