---
schema: qual/card@1
id: E-AMD-7FMEI2QD
kind: problem
title: A ring is local iff $x$ or $1-x$ is a unit for every $x$
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Maximal Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $R$ is a local ring iff for every $x\in R$, either $x$ or $1-x$ is a unit.
:::

::: {.solution}
Assume \(R\) is a commutative ring with identity.

Suppose first that \(R\) is local with unique maximal ideal \(\mathfrak m\). The nonunits of \(R\) are exactly the elements of \(\mathfrak m\). If both \(x\) and \(1-x\) were nonunits, then both would lie in \(\mathfrak m\), hence
\[
1=x+(1-x)\in\mathfrak m,
\]
a contradiction. Thus for every \(x\), at least one of \(x\) or \(1-x\) is a unit.

Conversely, assume that for every \(x\in R\), either \(x\) or \(1-x\) is a unit. Let \(\mathfrak m,\mathfrak n\) be maximal ideals. If they were distinct, choose \(a\in\mathfrak m\setminus\mathfrak n\). Since \(\mathfrak n\) is maximal and \(a\notin\mathfrak n\), we have \(\mathfrak n+(a)=R\), so
\[
1=b+ra
\]
for some \(b\in\mathfrak n\), \(r\in R\). Put \(x=ra\). Then \(x\in\mathfrak m\), so \(x\) is not a unit, while \(1-x=b\in\mathfrak n\), so \(1-x\) is not a unit. This contradicts the hypothesis.

Hence \(R\) has a unique maximal ideal, so \(R\) is local.
:::
