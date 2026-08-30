---
schema: qual/card@1
id: P-3DTFZ
kind: problem
title: A map $S^2\to S^2$ of degree 2013
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Does there exist a map of degree 2013 from $S^2 \to S^2$.
:::

::: {.solution}
<1>1. Yes, degree $2013$ maps $S^2\to S^2$ exist.
Proof: $z\mapsto z^{2013}$ on $S^2\cong\C_\infty$ has degree $2013$ (suspension of degree $2013$ on $S^1$).

<1>2. Alternatively $f(z)=z^{2013}$ on $\C$ extends to $S^2$ with $f(\infty)=\infty$.
Proof: <1>1.

<1>3. Q.E.D.
Proof: <1>1.
:::
