---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3B-HW2
kind: problem
title: Deck transformations of universal covers (warm-up)
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
What is a deck transformation?
Describe the deck transformations from one of the universal covers above.
:::

::: {.solution}
A **deck transformation** of a covering \(p:E\to B\) is a homeomorphism
\[
\phi:E\to E
\]
satisfying
\[
p\circ\phi=p.
\]
Thus it permutes each fiber while preserving the covering projection.

For the universal cover
\[
p:\mathbb R\to S^1,
\qquad p(t)=e^{2\pi i t},
\]
every integer translation
\[
T_n(t)=t+n,\qquad n\in\mathbb Z,
\]
is a deck transformation because \(e^{2\pi i(t+n)}=e^{2\pi it}\). Conversely, if \(T\) is a deck transformation, then \(T(0)\in p^{-1}(1)=\mathbb Z\). Uniqueness of lifts of \(p\) implies \(T=T_{T(0)}\). Hence
\[
\operatorname{Deck}(\mathbb R/S^1)\cong\mathbb Z.
\]
:::
