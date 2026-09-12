---
schema: qual/card@1
id: E-LRJKU
kind: problem
title: Paracompact coverings need not have locally finite subcoverings
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Give an example to show that if $X$ is paracompact, it does not follow that for every open covering $\mathcal{A}$ of $X$, there is a locally finite subcollection of $\mathcal{A}$ that covers $X$.
:::

::: {.solution}
Take \(X=\mathbb R\), which is metrizable and hence paracompact, and consider the open cover
\[
\mathcal U=\{(-n,n):n\in\mathbb Z_+\}.
\]
Any subcollection that covers \(\mathbb R\) must contain intervals with arbitrarily large \(n\), so it must be infinite. But every member of \(\mathcal U\) contains \(0\). Hence any infinite subcollection fails even to be point-finite at \(0\), and therefore cannot be locally finite. Thus this open cover has no locally finite subcover, although \(X\) is paracompact.
:::
