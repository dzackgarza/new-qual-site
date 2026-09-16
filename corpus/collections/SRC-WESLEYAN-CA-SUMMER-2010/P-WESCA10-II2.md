---
schema: qual/card@1
id: P-WESCA10-II2
kind: problem
title: 'Residues of products at simple poles and a weighted residue formula'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
(a) Suppose $f$ has a simple pole at $a$ and $g$ is analytic near $a$.
Prove
\[
\operatorname{Res}(a,fg)=g(a)\operatorname{Res}(a,f).
\]

(b) Let $D$ be a domain, let $f$ be analytic in $D$ except for simple poles $a_1,\dots,a_n$, and let $g$ be analytic in $D$.
Prove that for every piecewise smooth closed path $\gamma$ avoiding the poles and null-homologous in $D$,
\[
\frac1{2\pi i}\int_\gamma f(z)g(z)\,dz
=\sum_{k=1}^n n(\gamma,a_k)g(a_k)\operatorname{Res}(a_k,f).
\]
:::
