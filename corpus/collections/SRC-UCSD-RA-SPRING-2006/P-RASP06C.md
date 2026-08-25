---
schema: qual/card@1
id: P-RASP06C
kind: problem
title: "Abel summation and convergence of power series at the boundary"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $\{a_k\}$ be a sequence of complex numbers such that $\sum_{k=0}^{\infty} a_k$ is convergent.
Set $S_m^n := \sum_{i=m}^{n} a_i$.

(a) Show that, for $0 \leq x \leq 1$,
$$
\sum_{k=m}^{n} a_k x^k = \sum_{j=m}^{n-1} S_m^j (x^j - x^{j+1}) + S_m^n x^n.
$$

(b) Show that
$$
\lim_{x \to 1^-} \sum_{k=0}^{\infty} a_k x^k = \sum_{k=0}^{\infty} a_k.
$$

Hint: Estimate the left hand side of the formula in (b).
:::
