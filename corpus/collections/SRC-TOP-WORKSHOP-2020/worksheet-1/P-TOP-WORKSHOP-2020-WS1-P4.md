---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P4
kind: problem
title: Fixed point property is preserved under retraction
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Retracts
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
(May 2016) Suppose that the space $X$ has the fixed point property (that is, for any continuous function $f\colon X\to X$ there is a point $p\in X$ with $f(p)=p$). Suppose also that $A\subset X$ is a subspace admitting a retraction $r\colon X\to A$.
Show that $A$ also has the fixed point property.
:::

::: {.solution}
Let \(f:A\to A\) be continuous, and let \(i:A\hookrightarrow X\) be inclusion. Define
\[
F=i\circ f\circ r:X\longrightarrow X.
\]
Since \(X\) has the fixed point property, there is \(x\in X\) with \(F(x)=x\). But \(F(x)\) lies in \(i(A)=A\), so \(x\in A\). Since \(r\) is a retraction, \(r(x)=x\). Therefore
\[
x=F(x)=i(f(r(x)))=f(x),
\]
where we identify \(i(A)\) with \(A\). Thus \(f\) has a fixed point. Since \(f\) was arbitrary, \(A\) has the fixed point property.
:::
