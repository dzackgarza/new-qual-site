---
schema: qual/card@1
id: FT-NFMJW
kind: theorem
title: Parseval's identity
prompts:
- State Parseval's identity, and say when Bessel's inequality becomes it.
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Fourier Analysis
relations: []
review: draft
---

::: {.theorem}
Let $H$ be a [[D-7QQUO|Hilbert space]] and let $(e_k)_{k\geq1}$ be an [[D-4IXAO|orthonormal]] sequence in $H$.
For every $x\in H$, Bessel's inequality holds:
$$
\sum_{k\geq1} \abs{\inner{x}{e_k}}^2 \le \norm{x}^2 .
$$
If $(e_k)_{k\geq1}$ is a [[D-AQX7W|basis]] of $H$, then equality holds for every $x\in H$:
$$
\sum_{k\geq1} \abs{\inner{x}{e_k}}^2 = \norm{x}^2 .
$$
:::
