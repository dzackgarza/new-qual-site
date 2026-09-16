---
schema: qual/card@1
id: P-TRIV-CA32
kind: problem
title: Integral representation and functional equation of the Riemann zeta function
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The analytic-continuation step explicitly asks for the contour in Figure 5. Flash preserves only the image placeholder/caption, so that figure-dependent contour data remain unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the missing-figure note with a description of Figure 5 and removed glyph residue, against Complex Analysis Problem 32 on pages 17-18 of the source PDF.
---

::: problem
Riemann's zeta function is defined as $\zeta(z) = \sum_{n=1}^\infty n^{-z}$.

- For which values of $z$ does this converge?

- Show that the zeta function admits the integral representation
  $$
  \zeta(z) = \frac{1}{\Gamma(z)} \int_0^\infty \frac{t^{z-1}}{e^t - 1}\,\mathrm{d}t
  $$
  **hint:** the relation $\sum_{m=1}^\infty e^{-mt} = \frac{e^{-t}}{1 - e^{-t}}$ might prove useful.

- Now we take the contour of figure 5.
  Since we want to allow non integer values of $z$, there is a branch cut along the positive real axis.
  What is $\frac{1}{\Gamma(z)} \int_0^\infty \frac{t^{z-1}}{e^t - 1}\,\mathrm{d}t$ along this contour?

- For $z < 0$ we can deform the contour by sending the radius of the circle $D$ to infinity; the price to pay is that, to compute $I$, we have to evaluate an infinite number of poles, but this can be done.
  By comparing this result to what you did in the previous step, you should find that
  $$
  \zeta(z) = \zeta(1-z)\, \frac{e^{3\pi i z/2} - e^{\pi i z/2}}{e^{2\pi i z} - 1}\, \frac{(2\pi)^z}{\Gamma(z)}.
  $$

- Using the formula you just found, show that $\zeta(-1) = -\frac{1}{12}$.
  Notice that this doesn't mean that $1 + 2 + 3 + 4 + \ldots = -\frac{1}{12}$, since that $\zeta(z) = \sum_{n=1}^\infty n^{-z}$ is valid only for $z > 1$.
  On a side note, this is the reason why string theory (without supersymmetry) needs 26 spacetime dimensions.

Figure 5 of the source (contour for problem 32) shows, with the cut line along the positive real axis, a contour that comes in from $+\infty$ along a line $A$ just above the cut, goes counterclockwise around the origin along a small circle $D$ of radius $\varepsilon$, and returns to $+\infty$ along a line $B$ just below the cut.
:::

::: {.remark}
The source uses $I$ in the fourth part without defining it; it presumably denotes the contour integral of the third part.
:::
