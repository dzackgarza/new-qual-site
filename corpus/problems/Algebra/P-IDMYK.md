---
schema: qual/card@1
id: P-IDMYK
kind: problem
title: Quotients of quadratic integer rings by nonzero prime ideals
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Number Theory
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $K=\QQ(\sqrt d)$ be a quadratic number field and let $\OO_K$ be its ring of integers.
What can you say about $\OO_K/\mathfrak p$ when $\mathfrak p\subset \OO_K$ is a nonzero prime ideal?
:::

::: {.solution}
The quotient $\OO_K/\mathfrak p$ is a finite field.

<1>1. Every nonzero prime ideal of $\OO_K$ is maximal.
::: {.proof}
The ring $\OO_K$ is a Dedekind domain. In a Dedekind domain every nonzero prime ideal is maximal. Hence $\OO_K/\mathfrak p$ is a field.
:::

<1>2. The field $\OO_K/\mathfrak p$ is finite.
::: {.proof}
Because $\mathfrak p$ is nonzero, choose $0\ne\alpha\in\mathfrak p$. Since $\alpha$ is an algebraic integer, its norm
\[
N_{K/\QQ}(\alpha)\in\ZZ\setminus\{0\}.
\]
The principal ideal $(\alpha)$ has finite index in $\OO_K$, with
\[
|\OO_K/(\alpha)|=|N_{K/\QQ}(\alpha)|.
\]
Since $(\alpha)\subseteq\mathfrak p$, the quotient map
\[
\OO_K/(\alpha)\twoheadrightarrow\OO_K/\mathfrak p
\]
is surjective. Therefore $\OO_K/\mathfrak p$ is finite.
:::

Thus every nonzero prime ideal of a quadratic integer ring has a finite residue field.
:::
