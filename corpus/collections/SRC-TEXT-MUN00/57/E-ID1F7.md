---
schema: qual/card@1
id: E-ID1F7
kind: problem
title: The theorem of meteorology
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Prove the following "theorem of meteorology": at any given moment in time, there exists a pair of antipodal points on the surface of the earth at which both the temperature and the barometric pressure are equal.
:::

::: {.solution}
Model the surface of the earth by the sphere \(S^2\). Assume temperature and barometric pressure vary continuously over the surface at the fixed time in question. Define
\[
F:S^2\to\mathbb R^2,
\qquad
F(x)=(T(x),P(x)),
\]
where \(T\) is temperature and \(P\) is pressure. By the Borsuk--Ulam theorem, there exists \(x\in S^2\) such that
\[
F(x)=F(-x).
\]
Equality of the two coordinates gives
\[
T(x)=T(-x),\qquad P(x)=P(-x).
\]
Thus the antipodal points \(x\) and \(-x\) have both the same temperature and the same barometric pressure.
:::
