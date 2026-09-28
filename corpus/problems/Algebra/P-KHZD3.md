---
schema: qual/card@1
id: P-KHZD3
kind: problem
title: Whether a formal power series ring is a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Rings
  - Local Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Is a ring of formal power series $R[[x]]$ a unique factorization domain (UFD)?
:::

::: {.solution}
Not in complete generality.

If $R=k$ is a field, then
\[
k[[x]]
\]
is a discrete valuation ring: every nonzero series has a unique form
\[
f=x^m u,
\]
where $u$ is a unit. Hence every ideal is $(x^m)$, so $k[[x]]$ is a PID and therefore a UFD.

Likewise, for a field $k$, each finite-variable formal power series ring
\[
k[[x_1,\dots,x_n]]
\]
is a regular local ring and hence a UFD.

However, the implication
\[
R\text{ UFD}\Longrightarrow R[[x]]\text{ UFD}
\]
is false in general. Samuel constructed UFDs $R$ for which $R[[x]]$ is not a UFD; see P. Samuel, *On unique factorization domains*, Illinois J. Math. **5** (1961), 1--17. Thus the polynomial-ring theorem of Gauss has no unrestricted formal-power-series analogue.

So the answer depends on hypotheses on $R$: over a field the answer is yes, but for a general UFD the answer can be no.
:::
