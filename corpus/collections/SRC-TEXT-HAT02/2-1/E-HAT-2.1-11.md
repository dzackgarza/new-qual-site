---
schema: qual/card@1
id: E-HAT-2.1-11
kind: problem
title: Retract induces injective map on homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Retractions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the retraction identity r i = id and functoriality of homology.
---

::: {.problem}
Show that if $A$ is a retract of $X$ then the map $H_n(A) \to H_n(X)$ induced by the inclusion $A \subset X$ is injective.
:::

::: {.solution}
Let
\[
i:A\hookrightarrow X
\]
be the inclusion and let
\[
r:X\to A
\]
be a retraction, so $r\circ i=\operatorname{id}_A$.

<1>1. On homology,
\[
r_*\circ i_*=\operatorname{id}_{H_n(A)}.
\]
::: {.proof}
Homology is functorial, hence
\[
r_*i_*=(r\circ i)_*=(\operatorname{id}_A)_*=\operatorname{id}_{H_n(A)}.
\]
:::

<1>2. Therefore
\[
\boxed{i_*:H_n(A)\to H_n(X)\text{ is injective}.}
\]
::: {.proof}
If $i_*(x)=0$, then applying $r_*$ gives
\[
x=r_*i_*(x)=0.
\]
:::
:::
