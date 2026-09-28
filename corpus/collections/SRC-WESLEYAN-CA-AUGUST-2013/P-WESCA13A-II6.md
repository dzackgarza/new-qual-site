---
schema: qual/card@1
id: P-WESCA13A-II6
kind: problem
title: 'Even analytic functions descend through squaring'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash corrupts the radius/center symbols in this line; the evenness and $f(\sqrt z)$ formulation unambiguously identifies the intended descent-through-$z\mapsto z^2$ problem.
---

::: {.problem}
Let $f$ be even and analytic on a disk $B(0,r)$.
Define
\[
g(z)=f(\sqrt z).
\]
Show that $g$ is well-defined and analytic on $B(0,r^2)$, and express $g^{(n)}(0)$ in terms of derivatives of $f$ at $0$.
:::
