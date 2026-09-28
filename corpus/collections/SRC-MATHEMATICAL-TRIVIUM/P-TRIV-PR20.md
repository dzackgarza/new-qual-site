---
schema: qual/card@1
id: P-TRIV-PR20
kind: problem
title: Wald's identities for a random sum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Part (c)'s variance/operator symbols are damaged in the deterministic extraction, so the missing identity is recorded as an explicit gap rather than reconstructed.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the unresolved variance identity in part (c) and removed a stray digit against Probability Problem 20 on page 30 of the source PDF.
---

::: {.problem}
Let $\xi_1, \ldots, \xi_n, \tau$ be independent random variables, $\xi_1, \ldots, \xi_n$ have the same distribution, $\tau$ takes the values $1, \ldots, n$.
Consider the sum of a random number of the random variables $S_\tau = \xi_1 + \ldots + \xi_\tau$.
Show that

(a) $\mathbf{E} S_\tau = \mathbf{E}\tau \cdot \mathbf{E}\xi_1$,

(b) $\mathbf{E}(S_\tau | \tau) = \tau \mathbf{E}\xi_1$,

(c) $\mathbf{D} S_\tau = \mathbf{E}\tau \cdot \mathbf{D}\xi_1 + \mathbf{D}\tau \cdot (\mathbf{E}\xi_1)^2$,

(d) $\mathbf{D}(S_\tau | \tau) = \tau \mathbf{D}\xi_1$.
:::
