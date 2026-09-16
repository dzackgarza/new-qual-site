---
schema: qual/card@1
id: P-AZOFF-A05
kind: problem
title: Uniform differentiability is equivalent to continuity of $f'$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash emits a control character where the prime in $f'$ occurs in the final sentence; the correction is determined by the displayed uniform-differentiability definition and the stated equivalence.
---

::: problem
Let $f$ be differentiable on $[a,b]$.
Say that $f$ is *uniformly differentiable* if for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
\left|\frac{f(x)-f(y)}{x-y}-f'(y)\right|<\varepsilon
\]
whenever $x,y\in[a,b]$, $x\ne y$, and $|x-y|<\delta$.

Prove that $f$ is uniformly differentiable on $[a,b]$ if and only if $f'$ is continuous on $[a,b]$.
:::
