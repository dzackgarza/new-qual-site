---
schema: qual/card@1
id: P-TRIV-CA34
kind: problem
title: $\int_0^\infty \frac{dx}{1+x^\alpha}$ by contour integration of $\frac{\log z}{1+z^\alpha}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 34, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Described the Figure 3 contour referenced by Complex Analysis Problem 34, from pages 15 and 18 of the source PDF.
---

::: problem
Solve the integral $\displaystyle\int_0^\infty \frac{1}{1 + x^\alpha}\,dx$ for $\alpha \in \mathbb{N}$, $\alpha > 1$ by integrating the function $\frac{\log z}{1 + z^\alpha}$ along the contour of figure 3.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
In the source this contour is used with the branch cut on the positive real axis, the radius of $\gamma_\epsilon$ sent to zero and the radius of $C_R$ sent to infinity.
:::
