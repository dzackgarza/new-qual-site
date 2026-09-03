---
schema: qual/card@1
id: E-GPCW2
kind: problem
title: $1/(x-a)\sqrt{1-x^2}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

:::{.exercise}
\[
I \da \int_{-1}^1 {1\over (x-a) \sqrt{1-x^2} }\dx = {\pi \over \sqrt{a^2-1}}
.\]

:::

:::{.solution}
Note the simple pole at $x=a$ and the branch points $x=\pm 1$, coming from factoring $\sqrt{1-z^2} = \sqrt{(1-z)(1+z)}$.^[T-bone.]
The standard dog bone contour will work, but will involve a residue at $z=a$ and at $z=\infty$.
Instead of taking the usual branch cut $[-1, 1]$, take instead $(-\infty, -1] \union [1, \infty)$ and the following T-bone contour (noting that it is oriented *negatively*):

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-28_02-47-45.png)

Note that in the limit, the two vertical pieces cancel since there is no phase introduced in $f$ when taking a path from $Q_1$ to $Q_2$, and the two upper horizontal segment limit to $\gamma_1\da \ts{t+i\eps \st t\in[-1, 1]}$.
Also note that $\int_{\gamma_1}f(z)\dz \to I$.

Let $\gamma_2$ be the bottom horizontal segment.
As in the arguments for the standard bone contour, 
\[
\int_{\gamma_2}f(z)\dz = -\int_{\gamma_1} -f(z)\dz = I
,\]
so 
\[
\qty{\int_{\gamma_1} + \int_{\gamma_2} }f \to 2I
.\]

The contribution from the residue:
\[
2\pi i \Res_{z=a} {1\over (z-a) \sqrt{1-z^2} } 
= {2\pi i \over \sqrt{1-a^2}} 
= {2\pi \over \sqrt{a^2-1}}
,\]
so
\[
{2\pi \over \sqrt{a^2-1}} = 2I \implies I = {\pi \over \sqrt{a^2-1}}
.\]

:::

