---
schema: qual/card@1
id: E-QVH6Y
kind: problem
title: Metrizable spaces with metrizable compactifications
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metrizability
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

Under what conditions does a metrizable space have a metrizable compactification?
:::

::: {.solution}
A metrizable space \(X\) has a metrizable compactification if and only if it is second countable. For metrizable spaces this is equivalent to separability.

Suppose first that \(X\) is dense in a compact metrizable space \(Y\). Every compact metrizable space is second countable, and every subspace of a second-countable space is second countable. Hence \(X\) is second countable.

Conversely, suppose \(X\) is metrizable and second countable. A metrizable space is regular, so by the Urysohn metrization/embedding theorem in its standard embedding form, a second-countable regular space admits a topological embedding
\[
e:X\hookrightarrow [0,1]^{\mathbb Z_+}.
\]
The Hilbert cube \([0,1]^{\mathbb Z_+}\) is compact metrizable. Therefore
\[
Y=\overline{e(X)}
\]
is a closed subspace of a compact metrizable space, hence is itself compact metrizable, and \(e(X)\) is dense in \(Y\). Thus \(Y\) is a metrizable compactification of \(X\).

Hence
\[
\boxed{X\text{ metrizable has a metrizable compactification}\iff X\text{ is second countable}.}
\]
:::
