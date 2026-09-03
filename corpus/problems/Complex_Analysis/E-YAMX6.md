---
schema: qual/card@1
id: E-YAMX6
kind: problem
title: $x^\alpha/(x+1)^2$
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

::: {.exercise}
\[
I \da \int_0^\infty {x^\alpha \over (1+x)^2}\dx,
\qquad 0<\alpha<1.
\]
:::

::: {.solution}
Set
\[
f(z)=\frac{z^\alpha}{(1+z)^2},
\]
using the branch $z^\alpha=e^{\alpha\Log z}$ with $0<\Arg z<2\pi$.
Take a positively oriented keyhole contour around the positive real axis.

![Keyhole contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-24_04-00-31.png)

On the upper bank, $z^\alpha=x^\alpha$; on the lower bank, $z^\alpha=e^{2\pi i\alpha}x^\alpha$, and the lower bank is traversed from $R$ to $\varepsilon$.
Hence the two straight segments contribute
\[
\qty{1-e^{2\pi i\alpha}}
\int_\varepsilon^R\frac{x^\alpha}{(1+x)^2}\,dx.
\]

The small circular contribution is $O(\varepsilon^{\alpha+1})$, while the large circular contribution is $O(R^{\alpha-1})$.
Both tend to zero because $0<\alpha<1$.

The only pole inside the contour is the double pole at $z=-1$.
Since $\Arg(-1)=\pi$ on this branch,
\[
\Res_{z=-1}f(z)
=\left.\dd{}{z}z^\alpha\right|_{z=-1}
=\alpha e^{i\pi(\alpha-1)}
=-\alpha e^{i\pi\alpha}.
\]
Letting $\varepsilon\to0$ and $R\to\infty$ and applying the residue theorem gives
\[
\qty{1-e^{2\pi i\alpha}}I=-2\pi i\alpha e^{i\pi\alpha}.
\]
Since
\[
1-e^{2\pi i\alpha}=-2i e^{i\pi\alpha}\sin(\pi\alpha),
\]
we obtain
\[
I=\pi\alpha\csc(\pi\alpha).
\]
:::
