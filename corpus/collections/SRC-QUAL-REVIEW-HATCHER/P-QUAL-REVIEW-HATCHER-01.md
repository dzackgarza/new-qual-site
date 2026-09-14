---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-01
kind: problem
title: Kronecker pairing descends to homology and cohomology
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 1 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Let $R$ be a ring.
If
\[
z=\sum_i r_i\sigma_i
\]
is a $k$-cycle in $C_k(X;R)$ and $\alpha\in C^k(X;R)$, define
\[
\langle z,\alpha\rangle=\sum_i r_i\,\alpha(\sigma_i).
\]
Prove that if $z-z'$ is a boundary, then $\langle z,\alpha\rangle=\langle z',\alpha\rangle$.
Likewise, prove that if $\alpha$ is a coboundary and $z$ is a cycle, then $\langle z,\alpha\rangle=0$.
Deduce that there is a well-defined bilinear pairing
\[
H_k(X;R)\times H^k(X;R)\longrightarrow R.
\]
This pairing is sometimes called the Kronecker product.
:::
