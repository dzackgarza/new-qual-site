---
schema: qual/card@1
id: P-TRIV-CA21
kind: problem
title: $\int_0^\infty \frac{x^p}{x^2+1}\,dx$ for $0<p<1$ by a keyhole contour
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source prints $dz$ at the end of the real integral $I_2$; this source/extraction discrepancy is retained rather than silently changed to $dx$.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the setup of exercise 20 and the Figure 3 contour and removed extraction residue, against Complex Analysis Problems 20-21 on page 15 of the source PDF.
---

::: problem
Repeat exercise 20 this time with $I_1 = \int_C \frac{z^p}{z^2+1}\,\mathrm{d}z$ and $I_2 = \int_0^\infty \frac{x^p}{x^2+1}\,\mathrm{d}x$ with $0 < p < 1$; the contour is the same as before.

Exercise 20 of the source reads:
(a) Compute the integral $I_1 = \int_C \frac{\mathrm{d}z}{(z+i)\sqrt{z}}$, where the contour $C$ is shown in figure 3, $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$, and we send the radius of $\gamma_\epsilon$ to zero and the radius of $C_R$ to infinity.
Note that, because of the square root, $z = 0$ is a branch point.
We choose to have a branch cut on the positive real axis.
(b) Find a relation between the integral $I_1$ and $I_2 = \int_0^\infty \frac{1}{(x+i)\sqrt{x}}\,\mathrm{d}x$, then use the result from the previous point to find the value of $I_2$.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
:::
