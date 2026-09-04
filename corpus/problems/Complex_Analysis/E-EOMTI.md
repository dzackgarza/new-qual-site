---
schema: qual/card@1
id: E-EOMTI
kind: problem
title: $\log(x) / (1+x^2)^2$
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
Evaluate
\[
I\da \int_0^\infty {\log x\over(1+x^2)^2}\,dx.
\]
:::

::: {.solution}
Use
\[
f(z)=\frac{\Log z}{(1+z^2)^2}
\]
with the branch $-\pi/2<\Arg z<3\pi/2$, and integrate over an upper semicircle indented around $0$.
The large arc is $O((\log R)/R^3)$ and the small arc is $O(\varepsilon|\log\varepsilon|)$, so both vanish in the limit.

The positive real segment contributes $I$.
On the negative real axis, $\Log(-x)=\log x+i\pi$, so the negative segment contributes
\[
I+i\pi A,
\qquad
A\da\int_0^\infty\frac{dx}{(1+x^2)^2}.
\]
The auxiliary integral is $A=\pi/4$: the full real-line integral is $\pi/2$, since
\[
\Res_{z=i}\frac1{(1+z^2)^2}=\frac1{4i},
\]
and the integrand is even.

The only pole of $f$ in the upper half-plane is the double pole at $i$.
Its residue is
\[
\Res_{z=i}f(z)
=\left.\dd{}{z}\frac{\Log z}{(z+i)^2}\right|_{z=i}
=\frac{1}{i(2i)^2}-\frac{2\Log i}{(2i)^3}
=\frac{i}{4}+\frac{\pi}{8}.
\]
Thus the residue theorem gives
\[
2I+i\pi A
=2\pi i\Res_{z=i}f
=-\frac\pi2+\frac{i\pi^2}{4}.
\]
Since $A=\pi/4$, the imaginary terms cancel and
\[
I=-\frac\pi4.
\]
:::
