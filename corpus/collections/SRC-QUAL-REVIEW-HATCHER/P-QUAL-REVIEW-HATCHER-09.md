---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-09
kind: problem
title: A unital multiplication on a positive-dimensional sphere forces odd dimension
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 9 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The source omits the explicit hypothesis n>0, but its parenthetical conclusion “n must be 1, 3, or 7” makes the intended positive-dimensional range clear; n=0 would otherwise be a counterexample.
---

::: {.problem}
Let $n>0$ and let $e\in S^n$.
Suppose there is a map
\[
\mu:S^n\times S^n\longrightarrow S^n
\]
such that
\[
\mu(x,e)=x=\mu(e,x)
\]
for every $x\in S^n$.
Prove that $n$ is odd.

(In fact $n$ must be $1$, $3$, or $7$, but this stronger result is considerably harder.)
:::
