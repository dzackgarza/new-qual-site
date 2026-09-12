---
schema: qual/card@1
id: P-4M6DM
kind: problem
title: The integral of $(1+x^2)^{-n-1}$ over $\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: problem
Show that
\[
\int_{-\infty}^{\infty} \frac{d x}{\left(1+x^{2}\right)^{n+1}}=\frac{1 \cdot 3 \cdot 5 \cdots(2 n-1)}{2 \cdot 4 \cdot 6 \cdots(2 n)} \cdot \pi
.\]
:::

::: solution
By evenness and the substitution $x=\tan\theta$,
\[
I_n:=\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^{n+1}}
=2\int_0^{\pi/2}\cos^{2n}\theta\,d\theta.
\]
Integration by parts gives the Wallis recursion
\[
\int_0^{\pi/2}\cos^{2n}\theta\,d\theta
=\frac{2n-1}{2n}
\int_0^{\pi/2}\cos^{2n-2}\theta\,d\theta.
\]
Since $\int_0^{\pi/2}1\,d\theta=\pi/2$, induction yields
\[
\int_0^{\pi/2}\cos^{2n}\theta\,d\theta
=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\frac\pi2.
\]
Therefore
\[
\boxed{I_n=
\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}\pi.}
\]
:::
