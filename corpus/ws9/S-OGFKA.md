---
schema: qual/card@1
id: S-OGFKA
kind: solution
title: Solution to P-VAZ7S
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations:
- kind: solves
  target: P-VAZ7S
review: draft
---

:::{.solution}
Since $\limsup_{p\to\infty} \|f\|_p \le \|f\|_{\infty}$, it suffices to show $\liminf_{p\to\infty} \|f\|_p \ge \|f\|_{\infty}$.

Let $\varepsilon>0$ be arbitrary and define $A_{\varepsilon} := \{x : f(x) \ge \|f\|_{\infty} - \varepsilon\}$.

Note that $m(A_{\varepsilon})>0$ and $\|f\|_p \ge \left(\int_{A_{\varepsilon}} f(x)\,dx\right)^{1/p} \ge (\|f\|_{\infty}-\varepsilon)\, m(A_{\varepsilon})^{1/p}$.

Since $\lim_{p\to\infty} m(A_{\varepsilon})^{1/p} = 1$ and $\varepsilon>0$ was arbitrary, the result follows.
:::
