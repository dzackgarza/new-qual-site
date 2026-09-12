---
schema: qual/card@1
id: P-CASP08E
kind: problem
title: "Evaluation of the integral of x sin(x)/(x^2+a^2) via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
For $a \in \mathbb{R}$ compute the integral $$\int_0^{\infty} \frac{x\sin x}{x^2 + a^2}\,dx.$$ Be sure to show all your work and justify any limits.
:::

::: solution
The integral is even after extending the integrand as
\[
\frac{x\sin x}{x^2+a^2},
\]
so it is half the real-line integral. Assume first $a\ne0$ and put
$b=|a|>0$. Consider
\[
F(z)=\frac{ze^{iz}}{z^2+b^2}
\]
on an upper semicircle. Jordan's lemma (or a direct split-arc estimate) makes
the semicircular contribution tend to zero. The only pole in the upper
half-plane is $z=ib$, with residue
\[
\operatorname{Res}_{z=ib}F(z)
=\frac{ib\,e^{-b}}{2ib}
=\frac12e^{-b}.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{xe^{ix}}{x^2+b^2}\,dx
=\pi i e^{-b}.
\]
Taking imaginary parts gives
\[
\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+b^2}\,dx
=\pi e^{-b}.
\]
Therefore
\[
\boxed{
\int_0^\infty\frac{x\sin x}{x^2+a^2}\,dx
=\frac\pi2 e^{-|a|}.}
\]

For $a=0$ this becomes the Dirichlet integral
\[
\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2,
\]
which agrees with the same formula by continuity in $a$.
:::
