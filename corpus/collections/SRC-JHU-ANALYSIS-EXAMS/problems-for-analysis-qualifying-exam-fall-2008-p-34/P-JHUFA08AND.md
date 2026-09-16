---
schema: qual/card@1
id: P-JHUFA08AND
kind: problem
title: '$\int_0^\infty\frac{\log x}{(x^2+4)^2}\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fall 2008 problem 4 with the retained JHU extraction, including the squared denominator, coefficient and required residue method."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked absolute convergence, the logarithm values on both real segments, the double-pole derivative and explicit estimates on both semicircles."
---

::: {.problem}
4) (10 points) Use residues to verify that

$$
\int _ { 0 } ^ { \infty } \frac { \ln x } { ( x ^ { 2 } + 4 ) ^ { 2 } } d x = \frac { \pi } { 3 2 } ( \ln 2 - 1 ) .
$$
:::

::: solution
<1>1. The real integral is absolutely convergent.

::: proof
For $0<x\leq1$, its absolute integrand is at most
$|\log x|/16$, whose integral is finite. For $x\geq1$,
the inequalities $\log x\leq x$ and $(x^2+4)^2\geq x^4$
bound it by $x^{-3}$. Both endpoint integrals therefore
converge absolutely. Denote the requested integral by $I$.
:::

<1>2. An indented upper semicircle determines $2I$ by a double-pole residue.

::: proof
Choose the logarithm with $-\pi/2<\arg z<3\pi/2$ and set
$$
F(z)=\frac{\operatorname{Log}z}{(z^2+4)^2}.
$$
This branch is holomorphic off the nonpositive imaginary
axis. For $0<\varepsilon<1$ and $R>3$, integrate along
$[-R,-\varepsilon]$, the clockwise upper semicircle of
radius $\varepsilon$, $[\varepsilon,R]$, and the
counterclockwise upper semicircle of radius $R$.
The only enclosed pole is $2i$, of order two. With
$L=\operatorname{Log}(2i)=\log2+i\pi/2$, its residue is
$$
\begin{aligned}
\operatorname{Res}_{2i}F
&=\left.\frac{d}{dz}\frac{\operatorname{Log}z}{(z+2i)^2}
\right|_{z=2i}\\
&=\frac{1}{(2i)(4i)^2}-\frac{2L}{(4i)^3}
=\frac{i(1-L)}{32}.
\end{aligned}
$$
The residue theorem gives total contour integral
$\pi(L-1)/16$ [@SS03]. Since
$\operatorname{Log}(-x)=\log x+i\pi$ for $x>0$, the
sum of the two straight segments is
$$
\int_\varepsilon^R\frac{2\log x+i\pi}{(x^2+4)^2}\,dx.
$$
Its real part is twice the corresponding truncated integral.
:::

<1>3. Both arcs vanish and yield the asserted value.

::: proof
On the outer semicircle the integral has modulus at most
$$
\frac{\pi R(\log R+\pi)}{(R^2-4)^2}\longrightarrow0.
$$
On the inner semicircle the analogous bound is
$$
\frac{\pi\varepsilon(|\log\varepsilon|+\pi)}
{(4-\varepsilon^2)^2}\longrightarrow0.
$$
These follow from the arc lengths, $|\arg z|\leq\pi$
on the upper half-plane, and the reverse triangle
inequality for $z^2+4$. Taking real parts in step <1>2
and then letting $\varepsilon\downarrow0$, $R\to\infty$
is justified by these estimates and absolute convergence.
It gives
$$
2I=\frac{\pi}{16}(\log2-1),
\qquad
\boxed{I=\frac{\pi}{32}(\log2-1)}.
$$
:::
:::
