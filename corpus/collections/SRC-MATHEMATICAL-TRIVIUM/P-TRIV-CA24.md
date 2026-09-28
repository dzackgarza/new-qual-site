---
schema: qual/card@1
id: P-TRIV-CA24
kind: problem
title: $\int_0^\infty \frac{\log^2 x}{1+x^2}\,dx$ by contour integration
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Quoted problems 23 and 34 and described the Figure 3 contour referenced by the hint, against Complex Analysis pages 15-18 of the source PDF.
---

::: {.problem}
Compute $\displaystyle\int_0^\infty \frac{\log^2 x}{1 + x^2}\,\mathrm{d}x$ (**hint:** solve problem 23 first.
Use the function $\frac{\log^3 x}{1 + x^2}$ integrated over some smart choice of contour);

Problem 23 of the source reads: Compute $\int_0^\infty \frac{\log x}{1 + x^\alpha}\,\mathrm{d}x$ for $\alpha \in \mathbb{N}$, $\alpha > 1$ (hint: solve problem 34 first. Now, as a contour, use a circular wegde of the complex plane that makes a $2\pi/\alpha$ angle with the positive real axis).

Problem 34 of the source reads: Solve the integral $\int_0^\infty \frac{1}{1 + x^\alpha}\,dx$ for $\alpha \in \mathbb{N}$, $\alpha > 1$ by integrating the function $\frac{\log z}{1 + z^\alpha}$ along the contour of figure 3.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
:::
