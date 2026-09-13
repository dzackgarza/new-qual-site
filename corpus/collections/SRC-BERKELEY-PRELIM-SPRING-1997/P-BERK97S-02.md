---
schema: qual/card@1
id: P-BERK97S-02
kind: problem
title: Distance to a closed subset is continuous and detects membership
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Let $(M,d)$ be a metric space and let $C\subset M$ be nonempty and closed. Define
\[
f(x)=\inf\{d(x,y):y\in C\}.
\]
Show that $f:M\to\mathbb R$ is continuous and that
\[
f(x)=0\iff x\in C.
\]
:::
