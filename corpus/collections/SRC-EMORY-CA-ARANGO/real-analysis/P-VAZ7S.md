---
schema: qual/card@1
id: P-VAZ7S
kind: problem
title: $\lim_{p\to\infty}\|f\|_p=\|f\|_\infty$ on a finite measure space
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
---

::: {.problem}
[Reconstructed from solution — no problem statement page was present in this solutions-only document.] Let $f \in L^{\infty}$ on a finite measure space.
Show that $\displaystyle\lim_{p\to\infty} \|f\|_p = \|f\|_{\infty}$.
:::

:::{.solution}
Since $\limsup_{p\to\infty} \|f\|_p \le \|f\|_{\infty}$, it suffices to show $\liminf_{p\to\infty} \|f\|_p \ge \|f\|_{\infty}$.

Let $\varepsilon>0$ be arbitrary and define $A_{\varepsilon} := \{x : f(x) \ge \|f\|_{\infty} - \varepsilon\}$.

Note that $m(A_{\varepsilon})>0$ and $\|f\|_p \ge \left(\int_{A_{\varepsilon}} f(x)\,dx\right)^{1/p} \ge (\|f\|_{\infty}-\varepsilon)\, m(A_{\varepsilon})^{1/p}$.

Since $\lim_{p\to\infty} m(A_{\varepsilon})^{1/p} = 1$ and $\varepsilon>0$ was arbitrary, the result follows.
:::
