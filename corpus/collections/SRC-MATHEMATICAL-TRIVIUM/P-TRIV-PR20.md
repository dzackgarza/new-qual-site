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
---

::: problem
Let $\xi _ { 1 } , . . . , \xi _ { n } , \tau$ be independent random variables, $\xi _ { 1 } , . . . , \xi _ { n }$ have the same distribution, τ takes the values $1 , . . . , n$ 1. Consider the sum of a random number of the random variables $S _ { \tau } = \xi _ { 1 } + \ldots + \xi _ { \tau }$ . Show that

(a) $\mathbf { E } S _ { \tau } = \mathbf { E } \tau \cdot \mathbf { E } \xi _ { 1 }$

(b) $\mathbf { E } ( S _ { \tau } | \tau ) = \tau \mathbf { E } \xi _ { 1 }$

(c) The deterministic extraction contains a variance identity here, but its variance/operator symbols are garbled and the exact displayed formula is unresolved.

(d) $\mathbf { D } ( S _ { \tau } | \tau ) = \tau \mathbf { D } \xi _ { 1 }$
:::
