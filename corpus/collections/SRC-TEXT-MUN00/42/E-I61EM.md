---
schema: qual/card@1
id: E-I61EM
kind: problem
title: Sections of the minimal uncountable well-ordered set are second countable
classification:
  areas:
  - topology
  topics:
  - Order Topology
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

(a) Show that for each $x \in S_\Omega$, the section of $S_\Omega$ by $x$ has a countable basis and hence is metrizable.

(b) Conclude that $S_\Omega$ is not paracompact.
:::

::: {.solution}
(a) Fix \(x\in S_\Omega=[0,\Omega)\). Its section
\[
S_x=\{y:y<x\}
\]
is countable, since every element of \(S_\Omega\) is a countable ordinal. The order topology on \(S_x\) has a basis consisting of open intervals and end intervals with endpoints in \(S_x\). Since \(S_x\) is countable, this basis is countable. An ordered space is regular, so the Urysohn metrization theorem implies that \(S_x\) is metrizable.

In particular, \(S_\Omega\) is locally metrizable: for each \(x<\Omega\), the open initial segment
\[
[0,x+1)=S_{x+1}
\]
is a metrizable neighborhood of \(x\).

(b) Suppose \(S_\Omega\) were paracompact. Since it is locally metrizable, the Smirnov metrization theorem would imply that \(S_\Omega\) is metrizable. But \(S_\Omega\) is countably compact and not compact, whereas every countably compact metrizable space is compact. This contradiction shows that \(S_\Omega\) is not paracompact.
:::
