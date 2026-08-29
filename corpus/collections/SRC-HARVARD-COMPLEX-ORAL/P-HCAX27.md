---
schema: qual/card@1
id: P-HCAX27
kind: problem
title: State the Riemann hypothesis
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
State the Riemann hypothesis.
:::

::: {.solution}
<1>1. The Riemann zeta function $\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$ extends meromorphically to $\mathbb{C}$ with a single simple pole at $s = 1$.
Proof: analytic continuation of the zeta function.

<1>2. The "trivial" zeros of $\zeta$ are at the negative even integers $s = -2, -4, -6, \ldots$.
Proof: the functional equation forces $\zeta$ to vanish at these points.

<1>3. **Riemann Hypothesis.** Every nontrivial zero of $\zeta(s)$ (i.e. every zero in the critical strip $0 < \operatorname{Re} s < 1$) lies on the critical line $\operatorname{Re} s = 1/2$.
Proof: statement of the conjecture.

<1>4. Q.E.D.
Proof: <1>3.
:::
